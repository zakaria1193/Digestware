---
project: gcc
subsystem: match
patch_id: null
tags:
- optimization
- compiler
commit_hash: bb5d3acc84c001f9ae7564874996560c191d2a79
source_type: github
author: Kael Andrew Alonzo Franco
headline: 'match: Remove one build_minus_one_cst (type) in r15-6257.'
tldr: GCC match patterns simplified by removing a redundant function call for the
  constant -1.
impact_score: 2
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In `match.pd`, a pattern previously using `build_minus_one_cst (type)`
  was updated to use `integer_minus_onep@1`. This change is safe because all operands
  in the relevant patterns have the same type, allowing the direct use of the `integer_minus_onep`
  predicate to check for the value -1 without needing to explicitly construct the
  constant.
primer_glossary:
- term: match.pd
  definition: A file containing pattern definitions used by GCC's pattern matching
    system, likely for optimizing or generating code.
- term: build_minus_one_cst
  definition: A function likely used to construct a constant integer value of -1.
- term: integer_minus_onep
  definition: A predicate or function that checks if an operand represents the integer
    value -1.
- term: r15-6257
  definition: A reference, possibly to an internal bug report or code review identifier.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bb5d3acc84c001f9ae7564874996560c191d2a79
date: '2026-07-12'
is_stub: true
stub_reason: low_score
---

A redundant function call to `build_minus_one_cst` has been removed from GCC's pattern matching definitions in `match.pd`. Since all operands share the same type, the `integer_minus_onep@1` predicate can now be used directly to represent the constant value -1, simplifying the pattern.
