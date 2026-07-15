---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- arm
- linking
- MVE
commit_hash: d74edc4c7929be882daf9cd960ad875d820773b1
source_type: github
author: Torbjörn SVENSSON
headline: Add MVE link test for ARM to ensure target compatibility
tldr: New ARM test verifies that MVE-enabled code can link successfully.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `arm_v8_1m_mve_ok` target is used to check if MVE is enabled. This
  new `arm_v8_1m_mve_link` target follows the same approach but adds a crucial linkage
  step. It uses the `arm_v8_1m_mve_link` in `lib/target-supports.exp` and applies
  it to relevant test cases like `gcc.target/arm/pr110268-1.c`. This helps catch issues
  where MVE instructions might be generated correctly but fail to link due to ABI
  or linker script conflicts, especially with bundled test code like `testglue.c`.
primer_glossary:
- term: MVE
  definition: M-Profile Vector Extension, a SIMD (Single Instruction, Multiple Data)
    instruction set extension for ARM Cortex-M processors, designed to enhance performance
    for DSP and machine learning workloads.
- term: Linker flags
  definition: Options passed to the linker (usually `ld`) that control how object
    files are combined into an executable or shared library. Examples include specifying
    library paths, entry points, or memory layout.
- term: ARM
  definition: A family of reduced instruction set computing (RISC) architectures for
    computer processors. Widely used in mobile devices, embedded systems, and increasingly
    in servers due to its energy efficiency and performance.
- term: dejagnu
  definition: A testing framework developed by Cygnus Solutions, widely used in the
    GCC project for writing and running tests. It provides infrastructure for test
    case selection, execution, and result reporting.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d74edc4c7929be882daf9cd960ad875d820773b1
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

This commit introduces a new linking test target, `arm_v8_1m_mve_link`, for the ARM architecture. It aims to confirm that code compiled with options enabling the MVE (M-Profile Vector Extension) can link correctly. This is important because board-specific linker flags might sometimes be incompatible with the linkage requirements of certain test cases, ensuring overall build stability.
