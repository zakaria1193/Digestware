---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- rvv
- vector
- testsuite
- floating-point
commit_hash: ebca3fd0efc881ad033a7a8da6e7f254edfca26c
source_type: github
author: Pan Li
headline: 'RISC-V: Add test cases for vector float conversion register overlap.'
tldr: New tests verify register group overlap handling for RVV's vfwcvt.f.f.v instruction.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: New test cases are added to the RISC-V testsuite to cover register
  group overlap scenarios for the `vfwcvt.f.f.v` instruction. This instruction performs
  a widening float conversion from a half-precision to a single-precision floating-point
  format. The tests specifically target situations where the source and destination
  register groups may overlap, ensuring the GCC backend correctly sequences operations
  and manages register lifetimes to prevent incorrect results or resource conflicts.
primer_glossary:
- term: RISC-V Vector (RVV)
  definition: A set of extensions for the RISC-V instruction set architecture designed
    to accelerate vector and SIMD processing through wide registers and specialized
    instructions.
- term: vfwcvt.f.f.v
  definition: A RISC-V Vector instruction that performs a widening conversion from
    floating-point format X to floating-point format Y. The specific 'f.f' indicates
    a conversion between two floating-point types (e.g., FP16 to FP32).
- term: register group overlap
  definition: A situation in vector processing where consecutive instructions or internal
    operations might refer to overlapping sets of vector registers, requiring careful
    management by the compiler or hardware to ensure data integrity and correct execution
    flow.
- term: vector length
  definition: The number of elements processed by a single vector instruction. In
    RVV, vector length is configurable and dynamic, affecting how registers are utilized.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ebca3fd0efc881ad033a7a8da6e7f254edfca26c
date: '2026-07-19'
is_stub: true
stub_reason: low_score
---

This commit introduces a suite of new test cases for the RISC-V Vector (RVV) extension, specifically focusing on the `vfwcvt.f.f.v` instruction. These tests aim to validate the correct handling of register group overlap, a scenario where instruction operands might share register resources. The addition of these tests ensures the compiler properly manages register allocation and avoids conflicts when generating code for this vector floating-point conversion instruction across various vector lengths and element sizes.
