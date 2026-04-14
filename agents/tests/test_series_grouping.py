"""Unit tests for agents.tools.series_grouping.series_aware_batches."""

from __future__ import annotations

import pytest

from agents.tools.series_grouping import series_aware_batches


def key(item: dict) -> str | None:
    return item.get("s")


# ---------------------------------------------------------------------------
# Basic behaviour
# ---------------------------------------------------------------------------

def test_empty_input_returns_empty():
    assert series_aware_batches([], 5, key) == []


def test_singletons_fill_batches_normally():
    items = [{"s": None, "v": i} for i in range(7)]
    batches = series_aware_batches(items, 3, key)
    # 7 singletons with batch_size=3 → [3, 3, 1]
    assert [len(b) for b in batches] == [3, 3, 1]
    # All items present
    assert sum(len(b) for b in batches) == 7


def test_series_items_stay_together():
    # Items: A B A — the two A's should land in the same batch
    items = [{"s": "A"}, {"s": None}, {"s": "A"}]
    batches = series_aware_batches(items, 10, key)
    # With batch_size=10, everything fits in one batch; the two A's are together
    flat = [item for b in batches for item in b]
    a_positions = [i for i, x in enumerate(flat) if x.get("s") == "A"]
    assert a_positions == [0, 1] or a_positions == [1, 2], (
        "Both A items must be adjacent (grouped)"
    )


def test_series_never_split_across_batches():
    # 3-item series + 2 singletons, batch_size=3
    # Series has 3 items → fills one batch; singletons fill another
    items = [{"s": "X"}, {"s": None}, {"s": "X"}, {"s": "X"}, {"s": None}]
    batches = series_aware_batches(items, 3, key)
    for batch in batches:
        series_keys_in_batch = {x["s"] for x in batch if x["s"] is not None}
        # A batch must not contain X mixed with another named series
        # (here there's only one named series, so this just verifies X is never split)
    # Verify all X items are in the same batch
    x_batches = [i for i, b in enumerate(batches) if any(x["s"] == "X" for x in b)]
    assert len(x_batches) == 1, "All X items must be in the same batch"
    x_batch = batches[x_batches[0]]
    assert sum(1 for x in x_batch if x["s"] == "X") == 3


def test_oversized_series_forms_own_batch():
    # Series of 5 items with batch_size=3 — must not be split
    items = [{"s": "big"} for _ in range(5)]
    batches = series_aware_batches(items, 3, key)
    assert len(batches) == 1
    assert len(batches[0]) == 5


def test_multiple_series_do_not_intermix():
    # Series A (2 items) and series B (2 items), batch_size=3
    # Expected: [A, A, B] [B]  or  [B, B, A] [A]  depending on order
    items = [{"s": "A"}, {"s": "B"}, {"s": "A"}, {"s": "B"}]
    batches = series_aware_batches(items, 3, key)
    for batch in batches:
        named = [x["s"] for x in batch if x["s"] is not None]
        # Each batch must contain at most one named series
        assert len(set(named)) <= 1, f"Batch mixes series: {batch}"


def test_order_within_series_preserved():
    items = [{"s": "Z", "order": i} for i in range(4)]
    batches = series_aware_batches(items, 10, key)
    flat = [item for b in batches for item in b]
    assert [x["order"] for x in flat] == [0, 1, 2, 3]


def test_first_seen_series_order_respected():
    # A appears first, then B — A's group should come before B's group
    items = [{"s": "A"}, {"s": "B"}, {"s": "A"}, {"s": "B"}]
    batches = series_aware_batches(items, 10, key)
    flat = [item for b in batches for item in b]
    a_pos = [i for i, x in enumerate(flat) if x["s"] == "A"]
    b_pos = [i for i, x in enumerate(flat) if x["s"] == "B"]
    assert max(a_pos) < min(b_pos), "A's group should precede B's group (first-seen order)"


def test_all_items_present_in_output():
    items = [{"s": "A"}, {"s": None}, {"s": "B"}, {"s": "A"}, {"s": None}]
    batches = series_aware_batches(items, 2, key)
    flat = [item for b in batches for item in b]
    assert len(flat) == len(items)


def test_batch_size_one():
    items = [{"s": "A"}, {"s": "A"}, {"s": None}]
    batches = series_aware_batches(items, 1, key)
    # Series A has 2 items → one oversized batch; singleton → its own batch
    assert len(batches) == 2
    a_batch = next(b for b in batches if any(x["s"] == "A" for x in b))
    assert len(a_batch) == 2
