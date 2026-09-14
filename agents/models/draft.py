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

from types import UnionType
from typing import Any, Union, get_args, get_origin

from pydantic import BaseModel, create_model


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


def draft_model(
    model: type[BaseModel],
    *,
    name: str | None = None,
    exclude: frozenset[str] = frozenset(),
    seen: dict | None = None,
) -> type[BaseModel]:
    """Build a lenient twin of *model* to use as an agent's ``output_type``.

    The twin keeps every field's name and type but drops its length caps, makes
    each optional field nullable, and recurses into nested models. Fields named
    in *exclude* are left out entirely — use it for values the pipeline injects
    from the subject afterwards (identity, dates), which the model should not be
    asked to echo and cannot get right anyway.

    Args:
        model: the strict model to mirror.
        name: class name for the twin; defaults to ``<Model>Draft``.
        exclude: field names to omit.
        seen: internal cache so a model reached twice yields one twin.
    """
    seen = {} if seen is None else seen
    key = (model, exclude)
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
        annotation = _relax(field.annotation, seen)
        if field.is_required():
            fields[field_name] = (annotation, ...)
        else:
            fields[field_name] = (Union[annotation, None], None)

    draft = create_model(name or f"{model.__name__}Draft", **fields)
    draft.__doc__ = (
        f"Lenient twin of {model.__name__} — see agents/models/draft.py."
    )
    seen[key] = draft
    return draft
