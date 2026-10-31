---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- vectorization
- autovectorizer
commit_hash: cf3eaa0ee525be8ad51bb4cb2e3eea94e9944932
source_type: github
author: Robin Dapp
headline: 'RISC-V: Add USAD patterns for autovectorization'
tldr: RISC-V autovectorization now includes patterns for USAD (Unsigned Subtract and
  Add) operations, improving vector loop optimization.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This patch introduces new instruction patterns to `gcc/config/riscv/autovec.md`
  for the RISC-V vector extension, specifically targeting the `USAD` (Unsigned Subtract
  and Add) operation. It adds native expansion patterns for `usad<mode>3` where the
  accumulator width is wider than the input (e.g., `qi->hi`, `hi->si`). A synthesized
  `qi->si` variant is also provided, leveraging `vmv.v.i`, `vwabdau`, and `vwadd`
  for accumulation. The `vector-iterators.md` file is updated to refine `VWEXTI_HS`
  into `VWEXTI_H` and `VWEXTI_S`. This work aims to improve the autovectorizer's ability
  to handle loops in…
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: USAD
  definition: Unsigned Subtract and Add. A compound arithmetic operation that performs
    a subtraction and then adds the absolute difference to an accumulator. It's often
    used in multimedia processing and signal processing.
- term: autovectorizer
  definition: A compiler component that automatically transforms scalar code within
    loops into vector code, allowing for SIMD instructions to process multiple data
    elements in parallel.
- term: SIMD
  definition: Single Instruction, Multiple Data. A class of parallel computers in
    Flynn's taxonomy that perform the same operation on multiple data points simultaneously.
- term: patterns
  definition: In compiler construction, 'patterns' refer to descriptions of machine
    instructions or sequences of operations that the compiler can recognize and map
    to specific hardware instructions.
- term: vmv.v.i, vwabdau, vwadd
  definition: Specific RISC-V vector instructions. `vmv.v.i` likely moves an immediate
    value into a vector register, `vwabdau` performs a widening absolute difference
    and add, and `vwadd` performs a widening add.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cf3eaa0ee525be8ad51bb4cb2e3eea94e9944932
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

This commit enhances the RISC-V autovectorizer by adding native patterns for the USAD (Unsigned Subtract and Add) instruction. It introduces patterns for `usad qi->hi`, `usad hi->si`, and a synthesized `usad qi->si` variant. The synthesized variant utilizes instructions like `vmv.v.i`, `vwabdau`, and `vwadd`. This addition is intended to improve the vectorization of loops that perform USAD operations, with an expectation that future patches will allow direct use of native variants by narrowing accumulators for common use cases like x264 loops.
