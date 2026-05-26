---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- ARC-V APEX
- custom instructions
discussion_id: 20260525133052.1885254-2-luiss@synopsys.com
source_type: public_inbox
title: '[PATCH 1/2] RISC-V: Add ARC-V APEX assembler support'
headline: 'RISC-V: Add support for ARC-V APEX assembler'
tldr: This patch adds support for the ARC-V APEX extension, allowing dynamic custom
  instruction definition in the RISC-V assembler.
proposer: Luis Silva <Luis.Silva1@synopsys.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The implementation requires adding a new directive, `.extInstruction`, which may
  introduce compatibility issues with existing assembly code.
- Emitting metadata into a COMDAT ELF section increases the size of the object file.
exchanges:
- author: Luis Silva
  role: proposer
  position: Proposes adding ARC-V APEX assembler support, which allows users to define
    custom instructions dynamically.
  quote: 'Add support for ARC-V APEX (ARC Processor EXtension), which allows users
    to

    dynamically define custom instructions that use the Custom-0 encoding space.'
primer_expert: This patch adds support for ARC-V APEX to the RISC-V assembler. APEX
  allows users to dynamically define custom instructions that use the Custom-0 encoding
  space. The implementation involves adding a new directive, `.extInstruction`, and
  emitting metadata records into a COMDAT ELF section. This allows instruction definitions
  to be preserved in the linked object.
primer_general: The GNU Assembler (GAS) translates assembly code into machine code.  This
  patch adds support for the ARC-V APEX extension to the RISC-V assembler.  APEX allows
  developers to create their own custom instructions, extending the base RISC-V instruction
  set. This patch introduces a new directive called `.extInstruction` that allows
  developers to define these custom instructions within their assembly code.
series_id: 'binutils:risc-v: add arc-v apex assembler support'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260525133052.1885254-2-luiss@synopsys.com
bugzilla_url: null
date: '2026-05-25'
is_stub: false
---

This patch introduces support for ARC-V APEX (ARC Processor EXtension) to the RISC-V assembler.  APEX enables users to dynamically define custom instructions using the Custom-0 encoding space. The patch implements the `.extInstruction` directive for registering new instructions, which emit metadata into a COMDAT ELF section. This allows instruction definitions to be preserved in the linked object.
