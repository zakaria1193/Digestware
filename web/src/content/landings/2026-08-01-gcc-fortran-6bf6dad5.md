---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- gfortran
- warning
commit_hash: 6bf6dad534766300376dec6d093d49b89a452ea1
source_type: github
author: Thomas Koenig
headline: Fix undefined variable warning in ASSOCIATE constructs.
tldr: Associating variables in Fortran ASSOCIATE constructs now correctly warns about
  undefined variables.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The gfortran frontend's resolution pass now correctly tracks variable
  usage within ASSOCIATE constructs. A new parameter in `gfc_resolve` allows `mark_assoc_used`
  to update `value_used` and `value_set` for associate names, preventing false positives
  for undefined variables, particularly after code resolution.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6bf6dad534766300376dec6d093d49b89a452ea1
date: '2026-08-01'
is_stub: true
stub_reason: low_score
---

This patch addresses an undefined variable warning in Fortran's ASSOCIATE constructs. It ensures that the `value_used` and `value_set` attributes are correctly updated for the associate names after code resolution. This change requires an extra argument to `gfc_resolve` to access the association list and includes a new test case to verify the fix.
