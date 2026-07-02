---
project: gcc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- cleanup
- warning
commit_hash: dbdb8dab6ff70fd56b89dbacc576e3d71340ab81
source_type: github
author: Jakub Jelinek
headline: 'aarch64: Remove multiple spurious semicolons.'
tldr: Cleans up several redundant semicolons across aarch64 configuration files, resolving
  pedantic warnings.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Multiple spurious semicolons have been removed from aarch64-specific
  files (`aarch64-elf-metadata.cc`, `aarch64-sve-builtins-shapes.cc`, `neoversev2.h`)
  that were triggering ``-Wpedantic`` warnings when building with GCC 8. The specific
  locations include function definitions and shape definitions for SVE built-ins and
  tuning models. These are purely cosmetic and warning-suppressing changes.
primer_general: This commit performs minor code cleanup for the GCC compiler's support
  of the aarch64 processor architecture. Similar to a previous commit, it removes
  several instances of extra semicolons that are not syntactically required by the
  C++ language but can cause the compiler to issue warnings if it's configured to
  be very strict. The changes affect files related to aarch64's SVE (Scalable Vector
  Extension) features and performance tuning models. Removing these semicolons resolves
  the warnings without changing how the code operates.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dbdb8dab6ff70fd56b89dbacc576e3d71340ab81
date: '2026-07-01'
is_stub: true
stub_reason: low_score
---

This commit removes several spurious semicolons found in various configuration and header files related to the aarch64 architecture's GCC support. These extra semicolons were triggering pedantic warnings during compilation, particularly with GCC 8. The changes involve code cleanup in files like `aarch64-elf-metadata.cc`, `aarch64-sve-builtins-shapes.cc`, and `neoversev2.h`. Removing these semicolons resolves the warnings without altering the code's behavior.
