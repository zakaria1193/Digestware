---
project: gcc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- NEON
- intrinsics
- floating-point
commit_hash: acefdec15b785b2f186f5d23a4484fd99e9ee4eb
source_type: github
author: Karl Meakin
headline: Port NEON FP min/max intrinsics to pragma framework
tldr: AArch64 NEON floating-point min/max intrinsics are now handled by the pragma-based
  framework.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch integrates NEON floating-point min/max intrinsics (`vmin`,
  `vmax`) for aarch64 into the pragma-based framework. The core issue is that AArch64
  `fmin`/`fmax` instructions differ from GCC's internal `MIN_EXPR`/`MAX_EXPR` semantics,
  requiring expansion to `UNSPEC_FMIN`/`UNSPEC_FMAX`. The commit removes obsolete
  `aarch64_general_gimple_fold_builtin` cases and cleans up associated intrinsic definitions
  from `arm_neon.h`, as well as unused builtin functions.
primer_glossary:
- term: NEON
  definition: ARM's advanced SIMD extension, providing a set of instructions for single
    instruction, multiple data (SIMD) processing.
- term: intrinsic
  definition: A function that the compiler recognizes and translates directly into
    a specific machine instruction or a short sequence of instructions, often used
    to expose low-level hardware features.
- term: pragma-based framework
  definition: A system within GCC that uses pragmas to define and manage intrinsic
    functions, allowing for a more structured and extensible way to handle them compared
    to hardcoding.
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: UNSPEC
  definition: An internal GCC representation for operations that do not have a direct
    mapping to a standard GIMPLE operation, often used for target-specific instructions
    or complex expansions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/acefdec15b785b2f186f5d23a4484fd99e9ee4eb
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This commit ports the NEON floating-point min/max intrinsics (e.g., vmin, vmax) to the pragma-based framework for the aarch64 architecture. Similar to reduction intrinsics, the AArch64 `fmin`/`fmax` instructions have different semantics than GCC's `MIN_EXPR`/`MAX_EXPR`, leading to their expansion via UNSPEC_FMIN and UNSPEC_FMAX. This change consolidates their handling, removes redundant definitions, and cleans up unused builtin functions.
