---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- extensions
- hardware
discussion_id: 20260708024729.54397-1-garthlei@linux.alibaba.com
source_type: public_inbox
title: '[PATCH] RISC-V: Add support for XXTVarith and XXTVcoder extensions'
headline: 'RISC-V: Add support for XXTVarith and XXTVcoder extensions'
tldr: Adds support for XuanTie vendor-specific XXTVarith and XXTVcoder RISC-V extensions
  to binutils.
proposer: Bohan Lei <garthlei@linux.alibaba.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adding vendor-specific extensions increases toolchain complexity but enables support
  for new hardware features.
- Maintaining compatibility with evolving RISC-V specifications and toolchain conventions
  is crucial.
exchanges:
- author: Bohan Lei <garthlei@linux.alibaba.com>
  role: proposer
  position: Submits a patch to add support for XuanTie vendor-specific RISC-V extensions
    XXTVarith and XXTVcoder, detailing their functionalities and the vendor prefix
    used.
  quote: 'This patch adds support for XuanTie vendor-specific XXTVarith [1] and

    XXTVcoder [2] extensions.


    XXTVarith contains arithmetic instructions like vector interleave,

    Galois-field multiply-xor, and fast CRC folding operations.  XXTVcoder

    contains similar instructions to those in Zvabd.


    The vendor prefix used in XXTVarith and XXTVcoder is "xt." [3].'
primer_expert: This patch series adds support for XuanTie's custom RISC-V extensions,
  XXTVarith and XXTVcoder, to binutils. These extensions augment the RISC-V vector
  (V) and bit-manipulation (B) standard extensions with specialized arithmetic and
  CRC operations. The changes involve updating the BFD backend for ELF extension subset
  identification and the GAS assembler for new opcodes and test cases, using the 'xt.'
  vendor prefix as per RISC-V toolchain conventions.
primer_glossary:
- term: XXTVarith
  definition: A XuanTie vendor-specific RISC-V extension providing advanced arithmetic
    operations, including vector interleave, Galois-field multiply-xor, and CRC folding.
- term: XXTVcoder
  definition: A XuanTie vendor-specific RISC-V extension, similar to Zvabd, likely
    for vector-based coding or processing operations.
- term: binutils
  definition: A collection of programming tools for creating and managing executable
    programs, including the GNU Assembler (gas) and the GNU Binary File Descriptor
    library (BFD).
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computing principles.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface to various object file formats, including ELF.
- term: GAS
  definition: The GNU Assembler, part of binutils, responsible for translating assembly
    language code into machine code.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260707174719.1883721-1-garthlei@linux.alibaba.com
bugzilla_url: null
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This patch introduces support for the XuanTie vendor-specific RISC-V extensions, XXTVarith and XXTVcoder, within the binutils project. The changes include updates to BFD for ELF subset handling, GAS for new test cases and opcode definitions, and inclusion of the 'xt.' vendor prefix.
