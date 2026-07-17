---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- testsuite
- bugfix
commit_hash: f8eeddb64139a05a3ba250350394159e3ecbd285
source_type: github
author: Craig Blackmore
headline: Typed test-suite fix for RISC-V assembler
tldr: Fixes a typo in a RISC-V test case, allowing the assembly hard register test
  to run correctly.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gcc.dg/asm-hard-reg-4.c` testcase's target selector contained
  a typo, preventing it from being run on RISC-V. This commit corrects that typo.
primer_glossary:
- term: RISC-V
  definition: An open-standard Instruction Set Architecture (ISA) based on Reduced
    Instruction Set computing principles.
- term: gcc.dg
  definition: The directory within the GCC testsuite that contains regression tests
    for various language frontends and optimization passes.
- term: asm-hard-reg
  definition: Refers to assembly code that specifically uses hard registers (physical
    machine registers) rather than symbolic or virtual ones.
- term: target selector
  definition: A mechanism within the GCC testsuite used to specify which target architectures
    or configurations a particular test case should be compiled and run on.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f8eeddb64139a05a3ba250350394159e3ecbd285
date: '2026-07-13'
is_stub: true
stub_reason: low_score
---

A typo in the target selector of the `gcc.dg/asm-hard-reg-4.c` test file prevented it from being run for the RISC-V architecture. This commit corrects the typo, ensuring the test suite correctly applies this specific assembly hard register test to RISC-V targets.
