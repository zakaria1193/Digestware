---
project: gcc
subsystem: gcc/vectorization
patch_id: null
tags:
- gcc
- vectorization
- x86
- testing
commit_hash: cc1ca3c60f20621565dffa6c64a5105c10e8b894
source_type: github
author: Richard Biener
headline: Adjust x86 strided vectorization tests for cost comparison.
tldr: Strided vectorization tests in GCC are updated with explicit cost comparison
  flags and adjusted code generation expectations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses the impact of cost comparison on strided vectorization
  in x86. When cost comparison is enabled and MMX-with-SSE vector width is available,
  the vectorizer now prefers V2SImode over V4SImode with shuffles.  The original tests
  are modified to disable vector cost comparison, while new `-?b.c` variants are created
  to enable it.  This change highlights the interaction between `ix86_vector_costs`,
  target-specific vector widths, and shuffle costs.
primer_general: Strided vectorization optimizes memory accesses with non-unit strides.  GCC's
  vectorizer employs cost models to evaluate different vectorization strategies.  This
  commit updates tests to account for the impact of cost comparison on the choice
  of vector modes (V2SI vs V4SI) in strided vectorization scenarios on x86, using
  MMX and SSE instruction sets.  The cost model helps the compiler decide which approach
  yields better performance.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cc1ca3c60f20621565dffa6c64a5105c10e8b894
date: '2026-04-28'
---

The `gcc.target/i386/vect-strided-?.c` tests have been modified with explicit cost comparison settings. Variants with cost comparison disabled are retained, while new variants (`-?b.c`) enable cost comparison and adjust expected code generation accordingly. This allows for testing the vectorizer's behavior when cost comparison influences the choice between V2SImode and V4SImode with shuffles.
