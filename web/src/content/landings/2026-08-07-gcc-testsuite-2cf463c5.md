---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- x86
- floating-point
commit_hash: 2cf463c555a85b39f645173703c75bd4e38c8fef
source_type: github
author: Eikansh Gupta
headline: Fix copysign tests on ilp32 x86
tldr: Tests for copysign on ilp32 x86 now use SSE2 and SSE floating-point math.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The testsuite needed adjustments for ilp32 x86 builds to correctly
  test `copysign` behavior. The fix involves adding compiler flags `-msse2` and `-mfpmath=sse`
  to the relevant test cases (`pr109843.c` and `pr112472.c`). This ensures that the
  floating-point operations are handled using the SSE instruction set, aligning with
  the expected behavior for these tests.
primer_glossary:
- term: ilp32
  definition: A data model where pointers and integers are 32 bits wide. This contrasts
    with lp64, where pointers are 64 bits and integers are 32 bits.
- term: x86
  definition: A family of instruction set architectures descended from the Intel 8086
    microprocessor. It is the dominant architecture for desktop and laptop computers.
- term: SSE2
  definition: Streaming SIMD Extensions 2, a set of SIMD (Single Instruction, Multiple
    Data) instructions for x86 processors introduced by Intel. It enhances floating-point
    and integer operations.
- term: copysign
  definition: A function that returns a value with the magnitude of the first argument
    and the sign of the second argument.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2cf463c555a85b39f645173703c75bd4e38c8fef
date: '2026-08-07'
is_stub: true
stub_reason: low_score
---

Tests for the copysign function on the ilp32 x86 architecture have been fixed. The tests now explicitly enable SSE2 and SSE floating-point math, which are necessary for correct operation in this specific configuration. These changes address issues reported in PR109843 and PR112472.
