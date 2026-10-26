---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- disassembler
- patch
- review
discussion_id: cc7f9b1c-d817-4186-9ce6-100ad06e5b98@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: add an "arch=" disassembler option'
headline: 'RISC-V: add an "arch=" disassembler option'
tldr: Reviewer Jiawei expresses concern about handling invalid ISA strings in the
  RISC-V disassembler's new 'arch=' option and suggests adding a test case.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding an "arch=" option provides flexibility but requires careful validation of
  ISA strings to maintain disassembler integrity.
- Balancing the default ISA inference with user-provided overrides, ensuring precedence
  rules are clear and consistently applied.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Raises concerns about the handling of invalid ISA strings and suggests
    preserving the previous state on parsing failure, along with adding a test case.
  quote: The 'riscv_dis_set_arch' updates 'default_arch' unconditionally, while 'riscv_dis_parse_subset'
    releases the existing subset list without checking whether 'riscv_parse_subset
    succeeds'. An invalid value could therefore leave the disassembler with a partially
    updated architecture state.
- author: Farid Khaidari <khaidari.fg@gmail.com>
  role: proposer
  position: Submitted a patch to add an 'arch=' option to the RISC-V disassembler
    to override the ISA, especially for core files.
  quote: null
primer_expert: This discussion concerns a patch to binutils' RISC-V disassembler,
  introducing an `"arch="` option. This option allows overriding the default ISA string
  used for disassembly, which is typically inferred from the object file's architecture
  attribute or defaults to `rv64gc`. The motivation stems from scenarios like analyzing
  core files where the executable's ISA is unknown. The reviewer's feedback focuses
  on robust error handling for invalid ISA strings and ensuring architectural state
  consistency within the disassembler.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer (RISC) principles.
- term: disassembler
  definition: A program that translates machine code (binary) back into assembly language.
- term: ISA
  definition: Instruction Set Architecture. Defines the set of instructions that a
    processor can execute.
- term: core file
  definition: A file that contains a snapshot of a program's memory and state at the
    time it crashed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/cc7f9b1c-d817-4186-9ce6-100ad06e5b98@iscas.ac.cn
bugzilla_url: null
date: '2026-10-26'
is_stub: false
stub_reason: ''
---

A patch introduces an 'arch=' option to the RISC-V disassembler to override the default ISA, particularly useful for core files. A reviewer raises concerns about the unconditional update of the default architecture and the lack of error checking during subset parsing, which could leave the disassembler in an inconsistent state. The reviewer suggests preserving the previous valid state on parsing failure and adding a test case.
