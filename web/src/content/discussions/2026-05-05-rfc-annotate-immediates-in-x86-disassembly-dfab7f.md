---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- disassembly
- x86
- comments
- immediate values
discussion_id: 87fr4njrlb.fsf@redhat.com
source_type: public_inbox
title: 'Re: RFC: Annotate immediates in x86 disassembly'
headline: 'RFC: Annotate immediates in x86 disassembly'
tldr: Maintainer Nick Clifton is unsure how to handle multiple comments in x86 disassembly
  and suggests an x86 maintainer take over.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Need to handle multiple comments for a single instruction.
- Comments need to be displayed according to the chosen assembly syntax (AT&T vs Intel).
- Requires expertise in x86 disassembly.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Admits uncertainty about handling multiple comments in x86 disassembly
    and suggests an x86 maintainer take over.
  quote: Ah, OK, this is beyond my x86 expertise.  Maybe a real x86 maintainer would
    like to take over ?
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Raises the issue of how to handle multiple comments for different operands,
    particularly in AT&T vs Intel syntax.
  quote: 'Surely we want to switch the present

    %rip-relative operand printing to the new cappend_*() model.

    Hence both

    that and an immediate may want to have a comment added.  Presumably those

    would want to appear in the same order as the operands, which are

    printed in different order for AT&T vs Intel syntax.'
- author: Andreas Jaeger <aj@suse.com>
  role: other
  position: Acknowledges that he hasn't been active as a maintainer for a long time
    and should be removed from the maintainer list.
  quote: 'If there''s a document that lists me still as maintainer in binutils: Please
    remove me as I don''t expect to contr'
primer_expert: The discussion revolves around annotating immediate values in x86 disassembly
  with comments, specifically within the binutils disassembler.  The challenge lies
  in managing multiple annotations for a single instruction (e.g., RIP-relative addressing
  and immediate values) and ensuring that the comments appear in the correct order
  regardless of the disassembly syntax (AT&T vs. Intel). `cappend_*()` likely refers
  to a family of functions used to append strings/comments to the disassembly output.
primer_general: Disassembly is the process of converting machine code back into human-readable
  assembly language. Binutils provides tools for disassembly, among many other things.  When
  disassembling x86 code, it can be helpful to add comments to explain the purpose
  of certain instructions or operands. Immediates are constant values embedded directly
  in the instruction. RIP-relative addressing is a way to access memory locations
  relative to the instruction pointer (RIP) register. The challenge is that one instruction
  might have multiple parts that all need annotations, and these annotations should
  appear in a consistent order depending on the chosen assembly syntax.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/0b3d0cb8-eb76-445c-8b49-7276a2382862@redhat.com
bugzilla_url: null
date: '2026-05-05'
---

This is a follow-up to a previous RFC about annotating immediates in x86 disassembly. The discussion raises the issue of how to handle multiple comments, specifically when both a RIP-relative operand and an immediate value need annotations.  Nick Clifton, the current maintainer, admits a lack of x86 expertise and suggests that a dedicated x86 maintainer might be better suited to take over the work.
