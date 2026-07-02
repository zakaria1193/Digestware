---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- disassembler
- AArch64
- undefined instructions
- annotation
discussion_id: 4d960fb5-bcb9-4066-a2e3-8c669fefd73b@arm.com
source_type: public_inbox
title: 'Re: RFC: AArch64 Disassembler: Annotate undefined instructions'
headline: 'RFC: AArch64 Disassembler: Annotate undefined instructions'
tldr: The disassembler would annotate disassembly of `.word` directives to indicate
  that they might be addresses, but there are concerns about the narrow use case.
proposer: '"Richard Earnshaw (foss)" <Richard.Earnshaw@arm.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Increased complexity in the disassembler.
- Potential for false positives (incorrectly identifying data as code or vice versa).
- Impact on disassembler performance (negligible, but measurable).
- Benefit of providing more informative disassembly output in specific cases.
exchanges:
- author: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
  role: proposer
  position: Questions the practical need for annotating undefined instructions in
    the disassembler, particularly in cases where it requires specific conditions
    to trigger, such as using the `.inst` directive with a label, which is invalid.
  quote: So to even trigger this case you have to contort your sources in ways I really
    can't see users trying to do. Is there some user reported case driving this?
primer_expert: The binutils disassembler aims to translate machine code back into
  assembly instructions. This typically involves mapping memory addresses to instruction
  opcodes. The proposal concerns cases where the disassembler encounters an undefined
  instruction (i.e., a sequence of bytes that doesn't correspond to a valid instruction)
  and attempts to determine if it's actually data.  The discussion hinges on the accuracy
  and relevance of such annotations, particularly for AArch64.
primer_general: A disassembler is a tool that translates machine code (binary instructions)
  back into a human-readable assembly language form. This is the reverse of what a
  compiler does. When a disassembler encounters bytes that don't form a valid instruction,
  it needs to decide how to represent them. This proposal deals with how the AArch64
  disassembler handles these 'undefined instructions'. The core question is whether
  to interpret these undefined instructions as data (like an address or a constant)
  and annotate them accordingly, giving developers more context when debugging or
  reverse-engineering.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/4d960fb5-bcb9-4066-a2e3-8c669fefd73b@arm.com
bugzilla_url: null
date: '2026-04-30'
---

Nick Clifton proposed a change to the AArch64 disassembler to annotate undefined instructions, specifically when they appear to be data rather than code. The disassembler would check if the closest preceding mapping symbol is `$d` and annotate accordingly. Richard Earnshaw questions the necessity and practicality of this approach, suggesting that it might only be triggered in contrived scenarios, and asks whether annotating `.word` directives that contain addresses is a real-world use case.
