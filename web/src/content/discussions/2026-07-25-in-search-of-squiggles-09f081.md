---
project: gcc
subsystem: gcc
patch_id: null
tags:
- diagnostics
- compiler
- debugging
- source location
discussion_id: CAA_5UQ7_bu97+pLbmqftjKtzfBY-YEw=w5pcD4GfTHB3Y785FQ@mail.gmail.com
source_type: public_inbox
title: 'Re: in search of squiggles'
headline: in search of squiggles
tldr: Compiler diagnostic location information explained with references to libcpp
  header and example file.
proposer: Lewis Hyatt <lhyatt@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Encoding range information directly in `location_t` saves space but is limited to
  simple cases.
- Using ad-hoc locations with a lookup table allows for arbitrary ranges but adds
  a layer of indirection and memory overhead.
exchanges:
- author: Lewis Hyatt <lhyatt@gmail.com>
  role: proposer
  position: Provided pointers to existing documentation for understanding diagnostic
    location information and squiggle generation.
  quote: 'There''s a good amount of explanation in the comments at the top of

    libcpp/include/line-map.h and also in the example file

    libcpp/location-example.txt.'
primer_expert: This exchange clarifies the mechanism for generating source code squiggles
  in GCC diagnostics. The core data structure is `location_t`, which stores positional
  information. The discussion focuses on how `location_t` encodes both line/column
  details and, for simple cases, the end of the highlighted range. More complex ranges
  use external tables, indicated by a flag in `location_t`.
primer_glossary:
- term: libcpp
  definition: The C preprocessor library used by GCC. It handles preprocessor directives,
    macro expansion, and source file inclusion.
- term: location_t
  definition: A data type used by GCC to represent source code locations, including
    file, line, column, and potentially range information for diagnostics.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAA_5UQ7_bu97+pLbmqftjKtzfBY-YEw=w5pcD4GfTHB3Y785FQ@mail.gmail.com
bugzilla_url: null
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

Responding to a question about how the GCC diagnostic system highlights errors, a participant pointed to documentation within libcpp/include/line-map.h and libcpp/location-example.txt. These resources explain how location_t values encode range information, either directly in their lower bits for simple ranges or via an external lookup table for more complex ones, determining the extent of compiler-generated squiggles.
