---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- extension
discussion_id: CA+yXCZCnHyKj2EGpkjHEJdybyUGuShw6_qF40i6S7PRbkjRU3A@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add Zama16b extension support'
headline: 'RISC-V: Add Zama16b extension support'
tldr: 'Patch committed: RISC-V Zama16b extension support added to binutils.'
proposer: Wang Yaduo <wangyaduo@linux.alibaba.com>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds support for a new RISC-V extension, improving compatibility with GCC, at the
  cost of increasing the assembler's complexity.
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: other
  position: Confirms that the patch adding RISC-V Zama16b extension support has been
    committed.
  quote: committed :)
- author: Nelson Chu <nelson.chu1990@gmail.com>
  role: reviewer
  position: Approved the patch for binutils to support the Zama16b extension, noting
    that GCC already supported it.
  quote: Okay, if Gcc already supported it then we should at least recognize it in
    Binutils.  Please commit, thanks.
- author: Wang Yaduo <wangyaduo@linux.alibaba.com>
  role: proposer
  position: Submitted a patch to add support for the RISC-V Zama16b extension to binutils,
    noting that GCC supported it and binutils was causing errors.
  quote: 'I noticed that using -march with zama16b on current trunk triggers an

    assembler error(https://godbolt.org/z/ed1EdfaKr). GCC has supported the

    extension but it seems that the binutils misses it.'
primer_expert: This commit adds support for the RISC-V Zama16b extension to the GNU
  Assembler (gas) and BFD library within binutils. Zama16b is a standard RISC-V extension.
  The changes update the internal lists of supported RISC-V extensions and documentation,
  resolving an issue where binutils would error on this extension.
primer_glossary:
- term: Zama16b
  definition: A RISC-V extension related to atomic operations, specifically for 16-bit
    values.
- term: BFD
  definition: Binary File Descriptor library, used by GNU Binutils and GDB to provide
    a common interface to various object file formats.
- term: gas
  definition: The GNU Assembler, responsible for translating assembly language code
    into machine code.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) based on RISC principles.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZCnHyKj2EGpkjHEJdybyUGuShw6_qF40i6S7PRbkjRU3A@mail.gmail.com
bugzilla_url: null
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This confirms that a patch adding support for the RISC-V Zama16b extension to binutils has been committed. The change was made to BFD and gas, updating supported extensions and NEWS entries. This addresses an issue where binutils did not recognize the Zama16b extension, causing assembler errors.
