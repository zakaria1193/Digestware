---
project: gcc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- build
- warning
- compiler
commit_hash: dbdb8dab6ff70fd56b89dbacc576e3d71340ab81
source_type: github
author: Jakub Jelinek
headline: 'aarch64: Remove spurious semicolons triggering pedantic warnings'
tldr: Removes several unnecessary semicolons from AArch64 backend code that caused
  pedantic warnings.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Multiple files within the AArch64 backend (`aarch64-elf-metadata.cc`,
  `aarch64-sve-builtins-shapes.cc`, `neoversev2.h`) contained redundant semicolons.
  These were flagged by `-Wpedantic` checks, particularly with older GCC versions
  (e.g., GCC 8) building the GCC compiler itself. This commit removes these extraneous
  semicolons to ensure clean builds with strict warning levels.
primer_glossary:
- term: aarch64
  definition: A 64-bit ARM architecture, commonly used in mobile devices, servers,
    and embedded systems.
- term: SVE
  definition: Scalable Vector Extension, an optional extension to the Armv8-A architecture
    providing a flexible vector-processing capability.
- term: pedantic
  definition: Compiler flags that enable stricter checking of code against the C or
    C++ standards, often flagging constructs that are technically allowed but discouraged
    or non-portable.
- term: builtin
  definition: A function or operation that is built into the compiler and often intrinsically
    linked to specific hardware instructions, providing performance benefits.
- term: tuning model
  definition: Configuration data or code that helps the compiler optimize performance
    for specific hardware microarchitectures or target devices.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dbdb8dab6ff70fd56b89dbacc576e3d71340ab81
date: '2026-07-01'
is_stub: true
stub_reason: low_score
---

This commit cleans up the AArch64 backend code by removing several spurious semicolons that were causing pedantic warnings during compilation. These warnings were triggered by `-Wpedantic` flags in files related to AArch64 metadata, SVE builtins, and tuning models. The removed semicolons were syntactically unnecessary and did not affect the code's functionality, ensuring cleaner compilation output.
