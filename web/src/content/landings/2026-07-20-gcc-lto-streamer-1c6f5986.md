---
project: gcc
subsystem: gcc/lto-streamer
patch_id: null
tags:
- lto
- cleanup
commit_hash: 1c6f598668e5b85d24e35cf97bd55da2898df502
source_type: github
author: Filip Kastl
headline: Remove unused field from lto_location_cache
tldr: LTO stream representation class removes an unused field.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Removes the `stream_linemap_order` field from `lto_location_cache`
  in `lto-streamer.h`. This field tracks the ordering of linemaps within the LTO stream
  but is not utilized by the current streaming logic.
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compilation technique where optimization is
    performed not just on individual source files, but also across object files during
    the linking phase, potentially enabling more aggressive optimizations.
- term: lto-streamer
  definition: A component within GCC responsible for serializing and deserializing
    intermediate representation (IR) data for Link-Time Optimization.
- term: lto_location_cache
  definition: A data structure used by the LTO streamer to cache location information,
    likely related to debugging or source mapping.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1c6f598668e5b85d24e35cf97bd55da2898df502
date: '2026-07-20'
is_stub: true
stub_reason: low_score
---

The `lto_location_cache` class within the LTO streamer component has had its `stream_linemap_order` field removed, as it was not being used.
