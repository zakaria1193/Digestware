---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- isa
- extensions
discussion_id: 20261120134246.3804996-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[committed] RISC-V: Add Zbc implies Zbkc and Zvknhb implies Zvknha'
headline: 'RISC-V: Add Zbc implies Zbkc and Zvknhb implies Zvknha'
tldr: Updates RISC-V assembler to reflect new ISA manual definitions for Zbc and Zvknhb.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Ensures compliance with the latest RISC-V ISA specifications.
- Maintains correct assembler behavior for complex extension combinations.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Adds new implicit subset relationships for Zbc and Zvknhb based on the
    updated RISC-V ISA manual.
  quote: ''
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks for clarification on having multiple entries with the same string
    as the first field in the implicit subsets table.
  quote: "Is it correct to have multiple entries with the same string as the\nfirst\
    \ field? There's\n\n  {\"zvknhb\", \"+zve32x\", check_implicit_always},\n\na few\
    \ lines down."
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Confirms that multiple entries with the same string are intentional and
    necessary for defining different implicit relationships.
  quote: ''
primer_expert: This patch modifies `bfd/elfxx-riscv.c` and `gas/testsuite/gas/riscv/imply.d`
  to update the RISC-V assembler's understanding of instruction set extension implications.
  Specifically, it incorporates the latest definitions from the RISC-V ISA manual
  where `Zbkc` is now a subset of `Zbc`, and `Zvknhb` implies `Zvknha`. This ensures
  the assembler correctly handles implied extensions when parsing `-march` or similar
  options.
primer_glossary:
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: Zbc
  definition: A RISC-V standard extension for bit manipulation instructions.
- term: Zbkc
  definition: A RISC-V standard extension that is a subset of Zbc.
- term: Zvknhb
  definition: A RISC-V standard extension for vector cryptography instructions.
- term: Zvknha
  definition: A RISC-V standard extension for vector cryptography instructions, which
    Zvknhb is a superset of.
- term: implicit subset
  definition: In the context of RISC-V extensions, when one extension implies another
    (e.g., if you enable extension A, extension B is automatically enabled because
    it's a subset or otherwise prerequisite).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120134246.3804996-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This commit updates binutils to reflect the latest RISC-V ISA manual, where Zbkc is now defined as a subset of Zbc, and Zvknhb is a superset of Zvknha. This change ensures the assembler correctly interprets these instruction set extensions.
