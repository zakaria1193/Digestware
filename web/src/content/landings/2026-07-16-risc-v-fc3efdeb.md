---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- test
- vector
commit_hash: fc3efdeb72acb145a5a4772d88a2367eef535edf
source_type: github
author: Pan Li
headline: 'RISC-V: Add tests for vfcvt.x.f.v register group overlap.'
tldr: New RISC-V tests cover register group overlap for vfcvt.x.f.v.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds tests for register group overlap in RISC-V vector
  conversion instructions, specifically `vfwcvt.x.f.v`. Similar to the `vszext.vf8`
  instruction, this change allows for destination register groups to overlap with
  source register groups. The tests cover various floating-point to integer widths
  (f16, f32) and vector lengths (m1, m2, m4, mf2, mf4) to ensure correct compiler
  behavior when managing register reuse and preventing data corruption during these
  operations.
primer_glossary:
- term: vfwcvt.x.f.v
  definition: A RISC-V vector instruction that converts floating-point values to signed
    integer values within a vector register.
- term: Register group overlap
  definition: A situation in vector processing where the destination registers for
    an instruction may partially or fully overlap with the source registers, requiring
    careful management to avoid corrupting data before it's used.
- term: RVV
  definition: The RISC-V Vector Extension, a set of instructions designed to perform
    parallel operations on multiple data elements simultaneously.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fc3efdeb72acb145a5a4772d88a2367eef535edf
date: '2026-07-16'
is_stub: true
stub_reason: low_score
---

This commit introduces a series of new test cases for the RISC-V vector instruction `vfwcvt.x.f.v`. These tests focus on scenarios involving register group overlap, where destination registers might coincide with source registers. The tests cover various data types including f16 and f32, and different vector lengths, ensuring the compiler correctly handles these potentially complex register allocation situations.
