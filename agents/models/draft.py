"""Lenient twins of the strict output models, for structured LLM output.

WHY THIS EXISTS
---------------
The lesson agent used to ask its models for "one JSON object, raw JSON, no
markdown fences" and parse the reply by hand. That makes correct JSON
*encoding* the model's job, and the lesson dossier is the worst possible
payload for that: verbatim C source and a raw diff, full of backslashes and
quotes that have to survive re-escaping into a JSON string. Every lesson on
disk as of 2026-09-14 is a stub, and two of them died exactly there —
``Invalid \\escape`` and ``Expecting ',' delimiter``, thousands of characters
into the dossier, after every tool call in the run had already been paid for.

Handing the model a structured ``output_type`` moves encoding to the provider:
the dossier arrives as a tool-call argument the API itself serialises, so a
backslash in a diff is no longer a chance to lose the week's article.

WHY NOT POINT ``output_type`` AT THE STRICT MODEL
-------------------------------------------------
Two reasons, both of which would trade the parse failure for a different one:

1. **Length caps are repairs, not requirements.** ``SourceExcerpt.code`` caps
   at 6000 characters while ``read_file`` hands back up to 8192, so a model
   that copies an excerpt verbatim *exactly as instructed* overruns the cap.
   Today ``_clamp_to_schema`` trims it and the run continues. Put those caps in
   the schema and the overrun becomes a validation failure that costs another
   full round-trip — or the article.
2. **Nulls mean "nothing to report".** Models routinely answer
   ``"external_context": null`` rather than ``[]``; that is the other two stubs
   on disk. The draft accepts null on every optional field and the caller drops
   it with ``exclude_none=True``, letting the strict model's own default apply.

So the draft is the same shape with the constraints taken off: generate it,
clamp it, then validate it against the strict model, which stays the single
definition of what a valid dossier or article is.

Derived rather than hand-written, because a hand-written twin is a second copy
of the schema that silently drifts from the first.
"""

from __future__ import annotations

from types import NoneType, UnionType
from typing import Any, Union, cast, get_args, get_origin

from pydantic import BaseModel, create_model, model_validator

_EMPTY_FOR: dict[Any, Any] = {str: "", int: 0, float: 0.0, bool: False}


def _denull(annotation: Any) -> Any:
    """Drop ``None`` out of a union.

    Nullability is expressed in the schema as ``anyOf: [{...}, {"type":
    "null"}]``, and Gemini's function-calling dialect does not handle that —
    nor ``$ref``. We reach Gemini through OpenRouter's *OpenAI-compatible*
    endpoint, so pydantic-ai applies its OpenAI schema transformer rather than
    its Google one and the union goes out untouched. Tolerating a null is
    still worth having, so ``_drop_nulls`` below does it in the validator
    instead, where no schema has to describe it.
    """
    origin = get_origin(annotation)
    if origin in (Union, UnionType):
        args = tuple(a for a in get_args(annotation) if a is not NoneType)
        if not args:
            return annotation
        return args[0] if len(args) == 1 else Union[args]
    return annotation


def _empty_default(annotation: Any) -> Any:
    """A concrete stand-in for an omitted optional field."""
    origin = get_origin(annotation) or annotation
    if origin in (list, set, tuple):
        return []
    if origin is dict:
        return {}
    return _EMPTY_FOR.get(origin, "")


def _relax(annotation: Any, seen: dict) -> Any:
    """Return *annotation* with every nested model swapped for its draft twin.

    Stripping caps off the top-level fields is not enough: ``excerpts`` is a
    ``list[SourceExcerpt]``, and the cap that actually bites (``code``) lives
    inside ``SourceExcerpt``. So the substitution recurses through containers
    and unions rather than stopping at the first layer.
    """
    if isinstance(annotation, type) and issubclass(annotation, BaseModel):
        return draft_model(annotation, seen=seen)

    origin = get_origin(annotation)
    if origin is None:
        return annotation

    args = tuple(_relax(arg, seen) for arg in get_args(annotation))
    if origin in (Union, UnionType):
        return Union[args]
    return origin[args]


@model_validator(mode="before")
@classmethod
def _drop_nulls(cls, data: object) -> object:
    """Remove explicit ``null``s so the field's default applies instead.

    The schema no longer offers null (see ``_denull``), but a model can still
    send one, and models routinely answer ``"external_context": null`` for "I
    found nothing". Dropping the key turns that into the empty default rather
    than a validation error — which, at this stage, costs the week's lesson.
    """
    if not isinstance(data, dict):
        return data
    return {key: value for key, value in data.items() if value is not None}


def draft_model(
    model: type[BaseModel],
    *,
    name: str | None = None,
    exclude: frozenset[str] = frozenset(),
    require: frozenset[str] = frozenset(),
    override: dict[str, Any] | None = None,
    seen: dict | None = None,
) -> type[BaseModel]:
    """Build a lenient twin of *model* to use as an agent's ``output_type``.

    The twin keeps every field's name and type but drops its length caps, makes
    each optional field nullable, and recurses into nested models. Fields named
    in *exclude* are left out entirely — use it for values the pipeline injects
    from the subject afterwards (identity, dates), which the model should not be
    asked to echo and cannot get right anyway.

    ``require`` is the counterweight, and it is not optional care. A schema
    where every field may be null tells the model that returning the two
    identity fields and nothing else is a complete answer — and on 2026-09-14
    that is exactly what happened: the explorer called the output tool after
    one tool call and 53 tokens, the dossier came back empty, and the writer
    spent $0.08 of Opus honestly explaining that it had no evidence to teach
    from. Under ``output_type=str`` the prompt alone carried that obligation;
    with a schema, the schema carries it. So a field the caller cannot use the
    result without is listed here and becomes required in the twin, even where
    the strict model gives it a default for other reasons.

    ``override`` replaces a field's type outright. It exists for the case where
    the pipeline, not the model, is the better source for a field's *content*:
    the dossier's excerpts are named by the model but read out of git, so the
    twin asks for ``list[ExcerptRequest]`` where the strict model holds
    ``list[SourceExcerpt]``. The field keeps its name, so hydration stays a
    one-to-one mapping.

    Args:
        model: the strict model to mirror.
        name: class name for the twin; defaults to ``<Model>Draft``.
        exclude: field names to omit.
        require: fields to make required even if the strict model defaults them.
        override: field name -> replacement annotation.
        seen: internal cache so a model reached twice yields one twin.
    """
    seen = {} if seen is None else seen
    override = override or {}
    key = (model, exclude, require, tuple(sorted(override)))
    cached = seen.get(key)
    if cached is not None:
        return cached

    fields: dict[str, Any] = {}
    for field_name, field in model.model_fields.items():
        if field_name in exclude:
            continue
        # `field.annotation` is already the bare type — pydantic keeps the
        # `Field(max_length=...)` constraints in `field.metadata`, which we
        # simply don't carry over.
        if field_name in override:
            annotation = override[field_name]
        else:
            annotation = _relax(field.annotation, seen)
        annotation = _denull(annotation)
        if field.is_required() or field_name in require:
            fields[field_name] = (annotation, ...)
        else:
            fields[field_name] = (annotation, _empty_default(annotation))

    draft = create_model(
        name or f"{model.__name__}Draft",
        # `create_model` types `__validators__` as plain callables; a
        # `@model_validator` is a descriptor proxy, which is what it actually
        # wants here. Runtime is correct — see the null-handling tests.
        __validators__=cast(Any, {"_drop_nulls": _drop_nulls}),
        **fields,
    )
    draft.__doc__ = (
        f"Lenient twin of {model.__name__} — see agents/models/draft.py."
    )
    seen[key] = draft
    return draft
