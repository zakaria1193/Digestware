---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- sse
- abi
commit_hash: e5d0ea3ffd72398ffb410cd646814fadc48c2625
source_type: github
author: Jakub Jelinek
headline: Fix tree-ssa/forwprop tests with SSE ABI warnings
tldr: Test suite adjustments prevent failures due to SSE ABI warnings on specific
  architectures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The tests `gcc.dg/tree-ssa/forwprop-45.c` and `gcc.dg/tree-ssa/forwprop-46.c`
  failed on i686-linux due to warnings about SSE vector usage changing the ABI (`-Wpsabi`).
  For `forwprop-46.c`, simply adding `-Wno-psabi` to `dg-options` resolves the issue.
  For `forwprop-45.c`, which requires 16-byte vector support, the patch adds `-Wno-psabi`
  and `-msse2` to `dg-additional-options` for ia32 targets. The `scan-tree-dump` checks
  are also guarded with a list of targets that are known to pass, making the test
  suite more resilient to platform-specific ABI behaviors.
primer_glossary:
- term: tree-ssa
  definition: Static Single Assignment form. An intermediate representation used by
    the compiler that makes data flow analysis easier, particularly for optimizations.
- term: forwprop
  definition: Forward propagation. A compiler optimization that replaces variables
    with their constant values when they are known.
- term: SSE
  definition: Streaming SIMD Extensions. A set of CPU instructions for multimedia
    and data processing tasks, often involving vector operations.
- term: ABI
  definition: Application Binary Interface. Defines how low-level code is structured,
    including function calling conventions, data type representations, and memory
    layout.
- term: -Wpsabi
  definition: A GCC warning flag that checks for potential violations of the SSE ABI
    when using vector types, especially in function signatures.
- term: scan-tree-dump
  definition: A GCC testsuite mechanism used to verify the compiler's internal tree
    representation at various optimization stages.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e5d0ea3ffd72398ffb410cd646814fadc48c2625
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This commit addresses test failures in GCC's `tree-ssa/forwprop-{45,46}.c` tests, which were triggered by SSE ABI warnings on the i686-linux target. The fix involves adding `-Wno-psabi` to suppress these warnings and, for `forwprop-45.c`, also adding `-msse2` to ensure the test environment correctly handles SSE vector types. Additionally, scan-tree-dump checks are guarded with a list of known good targets to improve test robustness.
