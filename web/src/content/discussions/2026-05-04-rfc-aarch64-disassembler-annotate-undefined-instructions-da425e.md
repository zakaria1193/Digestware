---
project: binutils
subsystem: binutils
patch_id: null
tags:
- disassembler
- AArch64
- annotation
- undefined instructions
discussion_id: 20ba1c89-62e7-481e-b512-6db305b32094@redhat.com
source_type: public_inbox
title: 'Re: RFC: AArch64 Disassembler: Annotate undefined instructions'
headline: 'RFC: AArch64 Disassembler: Annotate undefined instructions'
tldr: Nick Clifton clarifies that the RFC to annotate undefined AArch64 instructions
  is driven by a desire for more informative disassembler output, not a specific u…
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The change would add complexity to the disassembler's logic.
- There's a risk of false positives, where valid instructions are incorrectly identified
  as undefined.
- The benefit is improved readability and understanding of disassembled code.
exchanges:
- author: Nick Clifton
  role: proposer
  position: Proposes annotating undefined AArch64 instructions in the disassembler
    to provide more informative output. Responds to questions about 32-bit instructions
    and the use of labels with `.inst` directives.
  quote: No, it is just me, trying to make the disassembler output slightly more informative.
primer_expert: The disassembler translates machine code back into assembly language.  This
  RFC proposes to annotate instructions that are undefined in the AArch64 architecture.
  The discussion touches on the `.inst` directive which is used to insert raw machine
  code words into the assembly.
primer_general: A disassembler is a tool that converts machine code (the binary instructions
  that a computer executes) into a human-readable assembly language representation.
  Assembly language is a low-level programming language that corresponds directly
  to the machine code instructions. This discussion concerns a proposal to improve
  the output of the AArch64 disassembler by adding annotations to undefined instructions.
  Undefined instructions are sequences of bytes that don't correspond to valid AArch64
  operations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20ba1c89-62e7-481e-b512-6db305b32094@redhat.com
bugzilla_url: null
date: '2026-05-04'
---

Nick Clifton clarifies that his RFC to annotate undefined AArch64 instructions in the disassembler isn't driven by a specific user-reported case, but rather by a desire to improve the disassembler's output. He also acknowledges a mistake regarding the size of AArch64 instructions and agrees that creating a test case to trigger unintended annotation of `.inst` values is difficult.
