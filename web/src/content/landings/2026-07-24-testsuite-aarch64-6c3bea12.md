---
project: gcc
subsystem: testsuite/aarch64
patch_id: null
tags:
- testsuite
- aarch64
- sve
commit_hash: 6c3bea12470afd607fe7a56da18c312a6784ec4c
source_type: github
author: Andrea Pinski
headline: Update test for aarch64 SVE register usage.
tldr: Fixes a failing aarch64 test by updating expected register usage in `bitint-args.c`.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The AArch64 test `bitint-args.c` failed because the expected output
  for the `sbfx` instruction in `f19` was using the `x` register form, while the compiler
  now prefers the `w` register form for this operation. This commit corrects the test's
  expected output to match the compiler's current register allocation strategy, ensuring
  test stability.
primer_glossary:
- term: aarch64
  definition: The 64-bit ARM architecture, commonly used in mobile devices and servers.
- term: SVE
  definition: Scalable Vector Extension, an optional extension for ARM processors
    that allows vector registers to have a variable length, adapting to the hardware.
- term: w vs x reg usage
  definition: Refers to the use of 32-bit (w) versus 64-bit (x) general-purpose registers
    in the AArch64 architecture. The compiler may have preferences for one over the
    other in certain contexts.
- term: sbfx
  definition: The signed byte extract (sbfx) instruction in ARM assembly, which extracts
    a specified number of bits from a source register into a destination register,
    preserving the sign.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6c3bea12470afd607fe7a56da18c312a6784ec4c
date: '2026-07-24'
is_stub: true
stub_reason: low_score
---

The `bitint-args.c` test for AArch64 was failing due to incorrect expectations about register usage. This commit updates the test case to reflect the compiler's preference for using the `w` form of registers over the `x` form for the `f19` instruction. This alignment ensures the test suite accurately reflects the compiler's generated code.
