---
project: gcc
subsystem: gimple-fold.h
patch_id: null
tags:
- documentation
- gimple
commit_hash: 4dee18cade51d955d9cd6dc86f4399be133a2821
source_type: github
author: Filip Kastl
headline: 'gimple-fold.h: Update a comment'
tldr: Corrects a comment in gimple-fold.h about the location of gimple_simplify definitions.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The comment in `gimple-fold.h` has been updated to reflect the correct
  location of `gimple_simplify` function definitions, which are now in `gimple-match-exports.cc`
  rather than the non-existent `gimple-match.cc`. This is a minor documentation fix.
primer_glossary:
- term: GIMPLE
  definition: GCC's internal representation (IR) used for optimization passes. It's
    a three-address, statically-scheduled intermediate language.
- term: gimple_simplify
  definition: A function used within GCC's GIMPLE infrastructure to simplify GIMPLE
    statements.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4dee18cade51d955d9cd6dc86f4399be133a2821
date: '2026-10-26'
is_stub: true
stub_reason: low_score
---

This commit corrects a comment in `gimple-fold.h` that incorrectly stated that `gimple_simplify` definitions are located in `gimple-match.cc`. The definitions are actually in `gimple-match-exports.cc`, and `gimple-match.cc` does not exist. This change improves code maintainability by ensuring accurate documentation.
