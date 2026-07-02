---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- disassembler
- x86
- comments
- immediate values
discussion_id: 64c8b84c-ab9c-4bc2-9289-b4f165e85b72@suse.com
source_type: public_inbox
title: 'Re: RFC: Annotate immediates in x86 disassembly'
headline: 'RFC: Annotate immediates in x86 disassembly'
tldr: Jan Beulich raises concerns about handling multiple comments in x86 disassembly
  with the proposed immediate annotation patch.
proposer: Nick Clifton
consensus: Under Review
outcome: under_review
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adding annotations improves readability but increases code complexity.
- Handling multiple comments requires careful design to avoid confusion.
- The order of comments may need to be adjusted based on the assembly syntax (AT&T
  vs. Intel).
exchanges:
- author: Nick Clifton
  role: proposer
  position: Proposes a patch to annotate immediates in x86 disassembly, displaying
    the annotation as a comment at the end of the line.
  quote: "Attached is a v2 of the proposed patch.  It adds:\n\n * The annotation is\
    \ displayed as a comment at the end of the line.\n * The symbol name is displayed\
    \ in dis_style_symbol rather than dis_style_address.\n * Shared object files (type\
    \ ET_DYN) can also benefit from the new feature."
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Questions how the patch handles multiple comments and suggests aligning
    the comment order with the operand order in different syntaxes.
  quote: 'How''s handling of

    multiple comments going to work? Surely we want to switch the present

    %rip-relative operand printing to the new cappend_*() model. Hence both

    that and an immediate may want to have a comment added.'
primer_expert: This discussion concerns a proposed enhancement to the x86 disassembler
  in binutils. The goal is to annotate immediate values with symbolic information
  to improve readability. A key challenge is handling potential conflicts with existing
  commenting schemes, such as those used for RIP-relative addressing.
primer_general: This discussion focuses on improving the output of the disassembler
  tool in binutils when working with x86 assembly code.  The disassembler translates
  machine code back into human-readable assembly.  The proposal is to add comments
  to the disassembled code that explain the meaning of immediate values (constants),
  but the discussion highlights the need to handle cases where multiple comments might
  be needed on the same line.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/64c8b84c-ab9c-4bc2-9289-b4f165e85b72@suse.com
bugzilla_url: null
date: '2026-05-03'
---

Jan Beulich responds to an RFC for annotating immediates in x86 disassembly. He raises a question about how the patch will handle multiple comments, especially considering the existing `%rip`-relative operand printing already adds comments. He suggests ensuring that the order of comments matches the order of operands in both AT&T and Intel syntax.
