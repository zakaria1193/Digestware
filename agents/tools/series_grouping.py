"""Batch items without splitting a series of related items.

A "series" is a set of items that share the same non-None key returned by a
caller-supplied *series_key* function.  Typical examples:

- A ``[PATCH 1/3]`` / ``[PATCH 2/3]`` / ``[PATCH 3/3]`` email series on a
  mailing list — all three patches share the same normalised subject key.
- An email thread identified by a common root Message-ID from the
  ``References`` / ``In-Reply-To`` headers.

Use ``series_aware_batches`` instead of plain ``range(0, len(items), N)``
slicing whenever items may form series that must not be split across LLM calls.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def series_aware_batches(
    items: list[T],
    batch_size: int,
    series_key: Callable[[T], str | None],
) -> list[list[T]]:
    """Pack *items* into batches without splitting a series.

    Items that share the same non-None *series_key* value are always placed in
    the same batch.  If a single series is larger than *batch_size* it forms
    its own oversized batch rather than being split.  Items whose *series_key*
    returns ``None`` are treated as independent singletons.

    Series appear in first-seen order; relative order within a series is
    preserved.

    Args:
        items: Flat list of items to partition into batches.
        batch_size: Target maximum items per batch.
        series_key: Callable that returns a series identifier string for an
            item, or ``None`` if the item belongs to no series.

    Returns:
        List of batches (each batch is a list of items).  Returns ``[]`` when
        *items* is empty.
    """
    if not items:
        return []

    # --- Pass 1: collect groups in first-seen order ----------------------
    groups: dict[str, list[T]] = {}
    key_order: list[str] = []

    for idx, item in enumerate(items):
        key = series_key(item)
        # Use a sentinel-prefixed index string so singletons never collide
        # with a real series key that happens to look like an integer.
        group_key: str = key if key is not None else f"\x00{idx}"
        if group_key not in groups:
            groups[group_key] = []
            key_order.append(group_key)
        groups[group_key].append(item)

    # --- Pass 2: greedy packing — never break a group across batches -----
    batches: list[list[T]] = []
    current: list[T] = []

    for gk in key_order:
        group = groups[gk]
        if current and len(current) + len(group) > batch_size:
            batches.append(current)
            current = list(group)
        else:
            current.extend(group)

    if current:
        batches.append(current)

    return batches
