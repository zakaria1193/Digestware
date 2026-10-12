"""build_model's tool-choice handling for models that reject forced tool use."""

from agents._openrouter import (
    DEFAULT_LESSON_RESEARCH_MODEL,
    DEFAULT_LESSON_WRITER_MODEL,
    NO_FORCED_TOOL_CHOICE,
    build_model,
)


def test_lesson_models_do_not_force_tool_choice(monkeypatch):
    # Both lesson stages use a structured output_type, so PydanticAI would send
    # tool_choice="required" — which no endpoint of these models accepts.
    monkeypatch.setenv("OPENROUTER_API_KEY", "test")
    for slug in (DEFAULT_LESSON_RESEARCH_MODEL, DEFAULT_LESSON_WRITER_MODEL):
        assert slug in NO_FORCED_TOOL_CHOICE
        assert build_model(slug).profile.get("supports_forced_tool_choice") is False


def test_other_models_keep_forced_tool_choice(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test")
    assert build_model("google/gemini-2.5-flash-lite").profile.get("supports_forced_tool_choice") is True
