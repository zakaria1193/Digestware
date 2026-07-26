---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- binutils
- bfd
- risc-v
- compiler
- extensions
discussion_id: 93e2c76e-edd5-4293-9d99-04d6bf30b1f4@suse.com
source_type: public_inbox
title: '[PATCH v4 02/12] bfd/RISC-V: Zve{32,64}f don''t need to explicitly imply Zvl{32,64}b'
headline: 'BFD/RISC-V: Zve{32,64}f do not need to explicitly imply Zvl{32,64}b'
tldr: Removes redundant RISC-V CPU extension implications in BFD to avoid excess processing.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Reduces complexity in the BFD RISC-V extension handling.
- Leverages existing implications to avoid redundant definitions.
exchanges: []
primer_expert: In binutils' BFD library, this patch refines the RISC-V CPU extension
  handling logic within `elfxx-riscv.c`. It modifies the `riscv_implicit_subset_map`
  to remove redundant explicit dependencies of `zve64f` on `zvl64b` and `zve32f` on
  `zvl32b`. Since `zve64x` and `zve32x` already imply `zvl64b` and `zvl32b` respectively,
  these specific subsets no longer need to be explicitly listed under `zve64f` and
  `zve32f`.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level interface for manipulating
    object files and archives. It supports various object file formats like ELF and
    a.out.
- term: RISC-V
  definition: An open-standard Instruction Set Architecture (ISA) based on reduced
    instruction set computing principles. It is known for its modularity and extensibility.
- term: Zve{32,64}f
  definition: RISC-V extension for single-precision (32-bit) and double-precision
    (64-bit) floating-point operations.
- term: Zvl{32,64}b
  definition: RISC-V extension for 32-bit and 64-bit vector operations.
- term: Zve{32,64}x
  definition: RISC-V extension for 32-bit and 64-bit vector-integer operations.
- term: Instruction Set Architecture (ISA)
  definition: The part of the processor architecture visible to the programmer or
    compiler. It defines the set of instructions a CPU can execute.
- term: Implication
  definition: In the context of CPU extensions, an implication means that enabling
    one extension automatically enables others that depend on it.
series_id: 'binutils:bfd/risc-v: zve{32,64}f don''t need to explicitly imply zvl{32,64}b'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/93e2c76e-edd5-4293-9d99-04d6bf30b1f4@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch simplifies RISC-V CPU extension handling in binutils' BFD library. It removes explicit implications for Zvl{32,64}b when Zve{32,64}f extensions are present. The existing Zve{32,64}x implications already cover the necessary dependencies, making the explicit Zvl settings redundant and subject to excess processing.
