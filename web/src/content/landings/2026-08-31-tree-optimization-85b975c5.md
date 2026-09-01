---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- bugfix
commit_hash: 85b975c5795c11cf9cb0db357c4e16f961c7adba
source_type: github
author: Richard Biener
headline: Fixes typo in vectorizer mask conversion pattern recognition.
tldr: Corrects a type typo in vectorizer's mask conversion pattern to fix PR127116.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vect_recog_mask_conversion_pattern` function in `tree-vect-patterns.cc`
  incorrectly passed `rhs1_type` as the scalar type argument to `build_mask_conversion`.
  This commit corrects it to pass the appropriate scalar type, resolving PR127116.
  Additionally, mask precision dumps were added to `vect_init_pattern_stmt` and `append_pattern_def_seq`
  for improved debugging.
primer_glossary:
- term: vectorizer
  definition: A compiler component that automatically transforms loops and other code
    constructs to use SIMD (Single Instruction, Multiple Data) instructions, which
    can operate on multiple data elements simultaneously for improved performance.
- term: mask conversion
  definition: In vectorization, this refers to operations that convert or create bitmasks,
    often used for selecting or manipulating elements within vector registers.
- term: scalar type
  definition: The fundamental data type of a single element, as opposed to a vector
    type which holds multiple elements.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/85b975c5795c11cf9cb0db357c4e16f961c7adba
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit corrects a typo in the GCC vectorizer's pattern recognition for mask conversions. Specifically, `rhs1_type` was passed incorrectly to `build_mask_conversion` in `vect_recog_mask_conversion_pattern`. The change ensures the correct scalar type is used, fixing PR127116. Debugging dumps for mask precision have also been added to relevant functions.
