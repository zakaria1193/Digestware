---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- type system
- optimization
discussion_id: CAFiYyc2OeQMg23k72G791ec3i56uQa=tkHPbeHCFKwOWDWMQxg@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Remove double-int.'
headline: Remove double-int.
tldr: Discusses removing double-int in favor of wide-int, considering potential efficiency
  losses.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Removal of `double-int` simplifies code but may impact performance.
- Adoption of `fixed_wide_int` avoids heap allocations but needs performance validation.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: proposer
  position: Supports removing `double-int` in favor of `wide_int` but emphasizes the
    need to examine potential efficiency losses in size and speed.
  quote: 'In general I''d support dropping double_int uses in favor

    of wide_int, but we have to look out for the loss of

    efficiency (in size/speed?)'
- author: Kael Andrew Franco via Gcc
  role: contributor
  position: Notes that `double-int` operates on 128-bit integers and `wide-int.h`
    has `fixed_wide_int` which doesn't use the heap, potentially simplifying functions
    and enabling the removal of `double_int_to_tree`.
  quote: 'double-int currently operates in 128 bit integers according to double-int.h.

    wide-int.h has fixed_wide_int, which does not use heap.

    This helps PR126622, simplifying build_int_cst-like functions,

    including the removal

    of double_int_to_tree.'
primer_expert: This discussion concerns the potential removal of the `double_int`
  type from GCC, which represents 128-bit integers. The proposal suggests replacing
  it with `fixed_wide_int`, a more modern implementation that avoids heap allocations.
  The primary concern is the potential performance impact, as `double_int` might be
  more efficient in certain code paths.
primer_glossary:
- term: double-int
  definition: A GCC internal type representing 128-bit integers, potentially implemented
    using multiple machine words.
- term: wide-int
  definition: A more general type in GCC for representing arbitrary-width integers,
    with `fixed_wide_int` being a variant that uses a fixed-size buffer instead of
    heap allocation.
- term: PR126622
  definition: A bug report or feature request within the GCC bug tracking system,
    relevant to the simplification of `build_int_cst`-like functions.
- term: double_int_to_tree
  definition: A GCC internal function that converts a `double_int` type to a GENERIC
    tree representation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc2OeQMg23k72G791ec3i56uQa=tkHPbeHCFKwOWDWMQxg@mail.gmail.com
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This discussion revolves around removing the `double-int` C++ type in favor of `fixed_wide_int`. The proposer supports the removal, contingent on a thorough evaluation of potential performance degradations in terms of size and speed. The potential impact on various compiler components is also noted.
