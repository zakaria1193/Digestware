---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- arm
- pch
commit_hash: 4eff3a846fd13ade32b34209d6e3306a4d7b729b
source_type: github
author: Christophe Lyon
headline: ARM testsuite avoids forcing --save-temps for PCH comparison.
tldr: ARM testsuite no longer forces --save-temps, enabling correct PCH compilation
  tests.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/testsuite/lib/target-supports.exp`, the ARM effective targets
  `arm_v8_1m_mve*` were incorrectly configured to always include `-save-temps`. This
  flag causes intermediate compilation outputs, including assembly files, to be removed
  by default cleanup routines. This behavior broke PCH tests in `dg-pch.exp` because
  the assembly comparison required assembly output to be present. The fix removes
  `-save-temps` from these effective targets and selectively adds it via `dg-options`
  or `DEFAULT_CFLAGS` in relevant test suites like `mve.exp` and `simd.exp`.
primer_glossary:
- term: PCH
  definition: Precompiled Header, a compilation technique where header files are precompiled
    into a binary format to speed up subsequent compilations.
- term: --save-temps
  definition: A compiler flag that instructs the compiler to keep intermediate files
    (like preprocessed source, assembly, and object files) after compilation.
- term: effective-targets
  definition: In GCC's testsuite, a mechanism to define sets of compiler flags or
    target-specific options that are applied to a group of tests.
- term: scan-assembler
  definition: A testsuite utility that checks the generated assembly code for specific
    patterns or correctness.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4eff3a846fd13ade32b34209d6e3306a4d7b729b
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

The ARM testsuite's `arm_v8_1m_mve*` effective targets unconditionally added `--save-temps`, which interfered with Precompiled Header (PCH) tests. The assembly output was removed before PCH checks could be performed, despite `-keep-output`. This commit removes `--save-temps` from these effective targets and adds it only where needed for scan-assembler tests or as a default CFLAG, allowing PCH tests to function correctly.
