---
project: gcc
subsystem: rtems/aarch64
patch_id: null
tags:
- RTEMS
- AArch64
- multilibs
- deprecation
commit_hash: ba0efd525470ffa9e2b7a50c52796b6c9f5bc885
source_type: github
author: Thomas Schwinge
headline: 'RTEMS/AArch64: Disable ILP32 multilibs build.'
tldr: Prevents the build of ILP32 multilibs for RTEMS on AArch64 due to deprecation
  and subsequent build failures.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The RTEMS AArch64 target configuration (`gcc/config/aarch64/t-aarch64-rtems`)
  previously enabled ILP32 multilibs. Due to upstream changes deprecating and removing
  ILP32 support, and the use of `-Werror`, a build failure occurs in `libstdc++` related
  to DTPREL relocations. This patch modifies the target configuration to disable ILP32
  multilibs, aligning with the upstream decision to drop ILP32.
primer_glossary:
- term: ILP32
  definition: A data model where integers and pointers are 32 bits wide. This is in
    contrast to LP64, where integers are 32 bits and pointers are 64 bits.
- term: multilibs
  definition: A mechanism in GCC to produce libraries and executables for multiple
    target configurations (e.g., different ABIs, architectures, or floating-point
    modes) from a single compiler build.
- term: DTPREL relocation
  definition: A type of relocation used in ELF object files for Dynamic Thread-Local
    Storage (DTLS). It's used to access data that is local to each thread.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ba0efd525470ffa9e2b7a50c52796b6c9f5bc885
date: '2026-11-07'
is_stub: false
stub_reason: ''
---

This change disables the build of ILP32 multilibs for the RTEMS operating system on AArch64 targets. Following the deprecation and removal of ILP32 from default multilibs, recent GCC versions with '-Werror' cause build failures in the standard libraries. This commit prevents these build issues by omitting the ILP32 multilibs.
