---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- extension
discussion_id: CA+yXCZDuaXG_ExSFSoxgToYtRr61zYrD=o0HA5Ykmc-n1WkNLw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add support for ziccamoc extension.'
headline: 'RISC-V: Add support for ziccamoc extension.'
tldr: 'Patch committed: RISC-V Ziccamoc extension (v1.0) support added to binutils.'
proposer: Dongyan Chen <chendongyan@isrc.iscas.ac.cn>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures binutils supports the Ziccamoc extension, aligning with GCC support, but
  adds complexity to the assembler's knowledge of RISC-V features.
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: other
  position: Confirms that the patch adding RISC-V Ziccamoc extension support has been
    committed.
  quote: committed :)
- author: Dongyan Chen <chendongyan@isrc.iscas.ac.cn>
  role: proposer
  position: Submitted a patch to add minimal support for the RISC-V Ziccamoc extension,
    version 1.0, to binutils.
  quote: "This patch adds minimal support for the RISC-V Ziccamoc extension, version\
    \ 1.0[1].\n\n[1] https://github.com/riscv/riscv-isa-manual/blob/main/src/unpriv/ziccamoc.adoc\n\
    \nbfd/ChangeLog:\n\n        * elfxx-riscv.c: Add ziccamoc extension.\n\ngas/ChangeLog:\n\
    \n        * NEWS: Add ziccamoc extension.\n        * testsuite/gas/riscv/march-help.l:\
    \ Ditto."
primer_expert: This commit integrates support for the RISC-V Ziccamoc extension into
  the GNU Assembler (gas) and BFD library within binutils. Ziccamoc is a draft extension
  related to atomic memory operations. The changes update the internal lists of supported
  RISC-V extensions and documentation.
primer_glossary:
- term: Ziccamoc
  definition: A draft RISC-V extension related to atomic memory operations, providing
    specialized instructions for complex atomic manipulations.
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
url: https://inbox.sourceware.org/binutils/CA+yXCZDuaXG_ExSFSoxgToYtRr61zYrD=o0HA5Ykmc-n1WkNLw@mail.gmail.com
bugzilla_url: null
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This discussion confirms the commitment of a patch that adds support for the RISC-V Ziccamoc extension, version 1.0, to the binutils. The changes were made to BFD and gas, including updating the list of supported extensions and NEWS files. This addition aligns binutils with GCC's support for the extension.
