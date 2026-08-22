---
project: gcc
subsystem: gimple-fold
patch_id: null
tags:
- optimization
- performance
- stdio
commit_hash: dc6b71d23465f237165050bc30c4e038c602a2d7
source_type: github
author: Kyrylo Tkachov
headline: Fold fwrite of a single byte to fputc for performance.
tldr: Optimizes single-byte `fwrite` calls to `fputc`, improving performance in applications
  like `jq`.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `gimple-fold` pass optimizes GIMPLE (GCC's intermediate representation)
  by replacing certain built-in functions with more efficient equivalents. This change
  adds a folder for `BUILT_IN_FWRITE` and `BUILT_IN_FWRITE_UNLOCKED` when they transfer
  exactly one byte. This mirrors existing logic that folds one-character `fputs` into
  `fputc` and assumes unlocked entry points can be folded similarly. The performance
  gains are seen in applications like `jq` that emit output character by character.
primer_glossary:
- term: GIMPLE
  definition: GCC's internal three-address intermediate representation, used for many
    optimization passes.
- term: fputc
  definition: A C standard library function that writes a single character to an output
    stream.
- term: fwrite
  definition: A C standard library function that writes a block of data to an output
    stream.
- term: gimple-fold
  definition: A GCC optimization pass that simplifies or replaces GIMPLE expressions
    with equivalent but more efficient ones.
- term: jq
  definition: A lightweight and flexible command-line JSON processor.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dc6b71d23465f237165050bc30c4e038c602a2d7
date: '2026-08-15'
is_stub: false
stub_reason: ''
---

This commit introduces a new GIMPLE pass to fold `fwrite(p, 1, 1, f)` calls into `fputc(*p, f)`. This optimization is beneficial because `fputc` writes directly to the stream, bypassing `fwrite`'s buffered-write path. Benchmarks with `jq` show significant reductions in instructions and cycles, particularly when processing large datasets.
