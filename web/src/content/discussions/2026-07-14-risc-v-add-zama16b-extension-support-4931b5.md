---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- extension
- gcc
discussion_id: 20260714082601.45789-1-wangyaduo@linux.alibaba.com
source_type: public_inbox
title: 'RISC-V: Add Zama16b extension support'
headline: 'RISC-V: Add Zama16b extension support'
tldr: Adds support for the RISC-V Zama16b extension to binutils, fixing an assembler
  error.
proposer: Wang Yaduo <wangyaduo@linux.alibaba.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 7
technical_tradeoffs:
- Keeping up with new and draft instruction set extensions ensures toolchain compatibility
  with emerging hardware features.
- Maintaining a comprehensive list of supported extensions requires regular updates
  to the assembler and linker.
exchanges:
- author: Wang Yaduo <wangyaduo@linux.alibaba.com>
  role: proposer
  position: Submits a patch to add RISC-V Zama16b extension support to binutils, addressing
    an assembler error.
  quote: 'I noticed that using -march with zama16b on current trunk triggers an

    assembler error(https://godbolt.org/z/ed1EdfaKr). GCC has supported the

    extension but it seems that the binutils misses it.'
primer_expert: This patch adds support for the RISC-V 'Zama16b' extension, a draft
  feature. The change involves updating the BFD module's list of recognized RISC-V
  extensions and consequently updating the gas assembler's knowledge base and test
  suite. This is necessary for binutils to correctly assemble code targeting this
  new extension, preventing errors that would otherwise occur.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA).
- term: Zama16b
  definition: A draft extension for the RISC-V architecture, likely related to specific
    arithmetic or bit manipulation operations.
- term: binutils
  definition: A collection of programming tools for manipulating binary files, including
    the assembler (gas), linker (ld), and disassembler (objdump).
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU binutils
    to handle various object file formats.
- term: gas
  definition: The GNU Assembler, part of the GNU binutils.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260714082601.45789-1-wangyaduo@linux.alibaba.com
bugzilla_url: null
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

Wang Yaduo proposes adding support for the RISC-V Zama16b extension to binutils. Currently, using `-march` with this extension causes an assembler error, even though GCC supports it. This patch updates `bfd/elfxx-riscv.c` to include `Zama16b` in the list of supported extensions and modifies `gas/NEWS` and `gas/testsuite/gas/riscv/march-help.l` accordingly.
