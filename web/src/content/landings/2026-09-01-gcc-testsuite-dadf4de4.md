---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- gcc
- testsuite
- x86
- sse
commit_hash: dadf4de4556924e28bb200c6f3d296f2d290ff9f
source_type: github
author: Iain Sandoe
headline: 'x86: Allow for vpord instruction variant in sse2-v1ti-logic-2.c'
tldr: Updates an x86 test case to accommodate newer instructions that include 'vpord'.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC testsuite is used to verify compiler correctness. This commit
  modifies `gcc/testsuite/gcc.target/i386/sse2-v1ti-logic-2.c`. The change is motivated
  by the emergence of new instruction variants, specifically `vpord`, on newer x86
  microarchitectures. The test was too strict in expecting only a subset of instructions,
  causing it to fail when the compiler correctly generated `vpord`. The fix makes
  the test more flexible by optionally matching the 'd' in the instruction mnemonic.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures (ISAs) developed by Intel,
    widely used in desktop, laptop, and server computers.
- term: SSE2
  definition: Streaming SIMD Extensions 2, an instruction set extension for x86 microprocessors
    that enhances multimedia and scientific processing capabilities.
- term: vpord
  definition: A specific x86 instruction, likely related to vector operations (VP)
    and a logical OR operation (ORD), possibly with a 'd' suffix indicating a specific
    variant or operand size/type.
- term: testsuite
  definition: A collection of tests used to verify the correctness of a software project,
    in this case, the GCC compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dadf4de4556924e28bb200c6f3d296f2d290ff9f
date: '2026-09-01'
is_stub: true
stub_reason: low_score
---

A test case in the GCC testsuite for x86 architectures (`sse2-v1ti-logic-2.c`) has been updated to correctly handle code generation on newer CPUs like Cascadelake and Sapphire Rapids. These processors can emit 'vpord' instructions, which were not accounted for by the original test. The fix allows for this optional 'd' suffix in the instruction pattern within the test file.
