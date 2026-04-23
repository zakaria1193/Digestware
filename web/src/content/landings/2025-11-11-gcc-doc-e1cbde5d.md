---
project: gcc
subsystem: gcc/doc
patch_id: null
tags:
- documentation
- grammar
- optimization
commit_hash: e1cbde5d13a4332ef3b31b03c4fcd1f7c2345ee8
source_type: github
author: Sam James
headline: 'Doc: Grammar fix for -ffunction-cse'
tldr: Adds a missing period to the documentation for the `-ffunction-cse` flag.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit corrects a grammar issue in the documentation file `doc/invoke.texi`
  related to the `-ffunction-cse` flag. While minor, maintaining grammatical accuracy
  contributes to the overall quality of the GCC documentation.
primer_general: This commit improves the documentation for GCC's `-ffunction-cse`
  flag by fixing a grammatical error. The `-ffunction-cse` flag controls a specific
  optimization in the compiler that attempts to eliminate redundant calculations within
  functions. Correcting the documentation helps users better understand the flag and
  its effects.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e1cbde5d13a4332ef3b31b03c4fcd1f7c2345ee8
date: '2025-11-11'
---

This commit adds a missing full stop to the documentation for the `-ffunction-cse` flag in `doc/invoke.texi`. This improves the grammar and readability of the documentation.
