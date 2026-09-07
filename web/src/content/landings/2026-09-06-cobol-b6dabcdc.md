---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- optimization
- performance
commit_hash: b6dabcdc335a9d1a942d489725e5a0fadcb5b55f
source_type: github
author: Robert Dubner
headline: 'cobol: Improve INSPECT performance with specialized routines.'
tldr: Optimizes COBOL INSPECT performance by separating single-byte and multi-byte
  operations and using task-specific search routines.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `libgcobol` INSPECT implementation has been optimized by splitting
  routines into single-byte character (SBC) and multi-byte character variants. This
  allows for faster processing when dealing with SBC operations, particularly in routines
  like `the_alpha_and_omega_sbc` and newly introduced ones for pattern matching and
  bounds setting. New routines like `__gg__inspect_format_2_sbc` and `__gg__inspect_format_4_sbc`
  are also introduced to handle specific INSPECT formats more efficiently.
primer_glossary:
- term: INSPECT statement
  definition: A COBOL statement used for examining data items and performing replacements
    based on character content.
- term: single-byte character (SBC)
  definition: A character encoding where each character is represented by a single
    byte, commonly used for ASCII or basic Latin alphabets.
- term: multi-byte character
  definition: A character encoding where characters can be represented by one or more
    bytes, used for broader character sets like UTF-8.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b6dabcdc335a9d1a942d489725e5a0fadcb5b55f
date: '2026-09-06'
is_stub: false
stub_reason: ''
---

This commit enhances the performance of the COBOL INSPECT statement by refactoring its library routines. It now differentiates between single-byte and multi-byte character processing, applying specialized, faster routines for each. Additionally, new task-specific routines are introduced for efficient string searching within memory.
