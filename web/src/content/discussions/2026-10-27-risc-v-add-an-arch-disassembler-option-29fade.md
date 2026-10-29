---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- disassembler
- option
- committed
discussion_id: CA+yXCZA_-iBj8so2AU-AkNQRSqE-MTmHiPvuczt30Y-D5QXoJw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] RISC-V: add an "arch=" disassembler option'
headline: 'RISC-V: add an "arch=" disassembler option'
tldr: The patch adding an `arch=` option to the RISC-V disassembler has been committed
  after a minor nitpick.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- A minor code cleanup was performed by the committer, removing redundant pointer
  nullification.
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: maintainer
  position: Confirms the commit of the RISC-V disassembler patch, mentioning a minor
    fix applied.
  quote: 'Thanks for this patch, committed to trunk with a minor nit fix, and

    it''s minor enough so I just fix that and push, hope you don''t mind :)


    nit: pd will free later so we don''t need to reset those two pointers to NULL.'
primer_expert: The patch introduces a new command-line option, `arch=`, to binutils'
  RISC-V disassembler. This allows users to explicitly specify the target RISC-V architecture
  (e.g., RV32I, RV64GC) when disassembling code, ensuring that the disassembler interprets
  instructions correctly according to the specified ISA extension. The commit message
  indicates a minor cleanup related to freeing memory in `disassemble_free_riscv`.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles,
    designed for simplicity and modularity.
- term: disassembler
  definition: A program that translates machine code (binary instructions) back into
    a human-readable assembly language format.
- term: ISA
  definition: Instruction Set Architecture. The vocabulary of commands understood
    by a CPU.
- term: RV32I, RV64GC
  definition: Specific profiles of the RISC-V ISA. RV32I is the base integer instruction
    set for 32-bit, while RV64GC includes the base integer set, multiplication/division,
    atomics, floating-point, and compressed instructions for 64-bit.
- term: trunk
  definition: The main development branch in a version control system, typically containing
    the latest committed code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZA_-iBj8so2AU-AkNQRSqE-MTmHiPvuczt30Y-D5QXoJw@mail.gmail.com
bugzilla_url: null
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This discussion confirms the commitment of a patch that adds an `arch=` option to the RISC-V disassembler. The committer, Kito Cheng, notes that a minor fix was applied before merging, specifically regarding the reset of two null pointers (`arch_option` and `default_arch`) within the `disassemble_free_riscv` function. This reset was deemed unnecessary as the memory would be freed later anyway. The patch is now in trunk.
