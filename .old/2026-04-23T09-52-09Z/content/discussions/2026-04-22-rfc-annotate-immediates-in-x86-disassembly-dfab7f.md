---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- disassembler
- objdump
- x86
- annotation
discussion_id: 87fr4njrlb.fsf@redhat.com
source_type: public_inbox
title: 'RFC: Annotate immediates in x86 disassembly'
headline: 'RFC: Annotate immediates in x86 disassembly'
tldr: Proposes adding an option to the x86 disassembler to display symbol names alongside
  immediate operands.
stakes: Improves readability and understanding of disassembled x86 code, especially
  when dealing with function addresses.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The discussion shows general agreement and positive feedback,
  with suggestions for improvement.  This indicates strong support for the feature.
technical_tradeoffs:
- Adds complexity to the disassembler.
- Improves readability of disassembled code.
- The feature could potentially slow down disassembly, although this is unlikely to
  be significant.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Proposes adding a new option to the x86 disassembler to annotate immediate
    operands with symbol names.
  quote: "Attached is a small potential patch that adds a new target specific\n  \
    \ option to the x86 and x86_64 disassemblers: \"-M annotate-immediates\".\n  \
    \ If enabled immediate operands which match a symbol's value will have\n   the\
    \ name of that symbol displayed alongside them."
- author: H.J. Lu <hjl.tools@gmail.com>
  role: reviewer
  position: Positive feedback to the addition of the new feature.
  quote: null
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Positive feedback to the addition of the new feature.
  quote: null
- author: Michael Matz <matz@suse.de>
  role: reviewer
  position: Supports the change but suggests renaming the option.
  quote: 'I think it''s helpful, but may I use the bike-shed and suggest to

    rename the -M thing, to use the traditional -m[no-]symbol-annotate?'
- author: Jiang, Haochen <haochen.jiang@intel.com>
  role: reviewer
  position: Sounds like a useful addition.
  quote: null
primer_expert: The `objdump` utility disassembles machine code into assembly. On x86,
  immediate operands are constant values embedded directly in the instruction.  This
  patch adds an annotation pass to `objdump` to look up symbols matching the immediate's
  value, so that the disassembly output shows the symbolic name as a hint. This is
  particularly useful when reverse engineering code that uses function pointers or
  constant offsets.
primer_general: When you convert a compiled program back into human-readable assembly
  code (a process called disassembly), it can be difficult to understand what certain
  numbers in the code represent. This patch proposes a change to the disassembler
  tool to make it easier to understand these numbers. Specifically, if a number in
  the assembly code corresponds to the address of a named function or variable, the
  disassembler will now show that name next to the number. This makes the disassembled
  code much easier to read and understand.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87fr4njrlb.fsf@redhat.com
bugzilla_url: null
date: '2026-04-22'
---

This RFC proposes a new target-specific option, `-M annotate-immediates`, for the x86 and x86_64 disassemblers. When enabled, immediate operands that match a symbol's value will have the symbol's name displayed alongside them in the disassembly output. This is intended to aid in understanding code that loads function addresses into registers.
