---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- compiler
- tree-optimization
commit_hash: 37846b229e14a54d74bcf77ee8bbfceb6e0b9bbe
source_type: github
author: Richard Biener
headline: Fix ICE with SLP discovery dumping when trapping_stmt is NULL
tldr: Resolves an Internal Compiler Error (ICE) when dumping SLP discovery information
  with a null trapping statement.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fixes PR tree-optimization/127468 by correcting the print statement
  in `vect_build_slp_tree_3` within `tree-vect-slp.cc`. Previously, attempting to
  print a NULL `trapping_stmt` using `%G` caused an ICE. The fix ensures a valid statement
  is printed, preventing the crash.
primer_glossary:
- term: ICE (Internal Compiler Error)
  definition: An unrecoverable error encountered by the compiler during the compilation
    process, indicating a bug within the compiler itself.
- term: SLP discovery
  definition: The phase within the SLP optimization where the compiler identifies
    potential parallelizable instruction patterns.
- term: trapping_stmt
  definition: A statement associated with an operation that might trap or throw an
    exception, used for debugging or error handling.
- term: tree-vect-slp.cc
  definition: The GCC source file containing implementations for SLP vectorization.
- term: PR tree-optimization/127468
  definition: A bug report filed against the GCC tree-optimization component, specifically
    related to an ICE during SLP discovery dumping.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/37846b229e14a54d74bcf77ee8bbfceb6e0b9bbe
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

This commit fixes an Integer Compiler Error (ICE) that occurred during SLP discovery dumping when the `trapping_stmt` was NULL. The issue was caused by attempting to print a NULL pointer using the `%G` format specifier. The fix involves printing the correct `trapping_stmt` in `tree-vect-slp.cc` to resolve this diagnostic issue.
