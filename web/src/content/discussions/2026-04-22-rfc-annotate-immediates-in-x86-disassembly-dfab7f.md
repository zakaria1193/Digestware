---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- disassembler
- x86
- annotation
- symbols
discussion_id: 87fr4njrlb.fsf@redhat.com
source_type: public_inbox
title: 'RFC: Annotate immediates in x86 disassembly'
headline: 'RFC: Annotate immediates in x86 disassembly'
tldr: Nick Clifton proposes a new option to annotate immediate operands in x86 disassembly
  with their corresponding symbol names.
proposer: Nick Clifton
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Performance impact of symbol lookup during disassembly, especially for large binaries.
- Potential for name collisions if multiple symbols have the same address.
- Increased complexity of the disassembler code.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Proposes a new disassembler option to annotate immediate operands with
    symbol names.
  quote: 'Attached is a small potential patch that adds a new target specific

    option to the x86 and x86_64 disassemblers: "-M annotate-immediates".

    If enabled immediate operands which match a symbol''s value will have

    the name of that symbol displayed alongside them.'
- author: H.J. Lu
  role: other
  position: Suggests handling shared libraries.
  quote: '+      || (ins->info->section->owner->flags & EXEC_P) == 0)


    Should it also handle shared libraries?'
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Generally positive regarding the patch.
  quote: 'Hi Nick,


    yes, looks like an extremely useful addition! Thanks!'
- author: Michael Matz <matz@suse.de>
  role: other
  position: Requests a bikeshed regarding the option name.
  quote: 'I think it''s helpful, but may I use the bike-shed and suggest -M annotate-addresses
    or -M annotate-symbols instead?


    annotate-immediates sounds so specific (which it isn''t really), the others more
    general to use -- but perhaps that gets over the top:)'
- author: '"Jiang, Haochen" <haochen.jiang@intel.com>'
  role: other
  position: Inquires about performance impact, concerns about the instruction.
  quote: It's a good feature. Just wondering how it works, does it need to find the
    symbol table every time when disassembling? If so, I am concerning the performance
    impact when disassembling a large binary.
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Agrees with H.J. Lu's suggestion to handle shared libraries.
  quote: 'Yes, yes it should. :-)


    I will fix this in the v2 patch.'
primer_expert: This patch adds a feature to the x86 disassembler in binutils to annotate
  immediate operands with symbol names. This functionality is useful for reverse engineering
  and debugging, as it clarifies the purpose of immediate values that represent addresses.
  The implementation involves looking up symbols based on their addresses during disassembly.
primer_general: The GNU binutils are a collection of tools used for working with binary
  files, including assemblers, linkers, and disassemblers. A disassembler translates
  machine code back into human-readable assembly code, which is helpful for understanding
  how a program works.  Immediate operands are constant values used directly within
  assembly instructions. This proposal aims to enhance the disassembler by showing
  the symbolic name of a function or variable when its address is used as an immediate
  value, improving code readability.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87fr4njrlb.fsf@redhat.com
bugzilla_url: null
date: '2026-04-22'
---

Nick Clifton proposes a new target-specific option, `-M annotate-immediates`, for the x86 and x86_64 disassemblers in binutils. When enabled, immediate operands matching a symbol's value will have the symbol name displayed alongside the immediate. This helps when analyzing code that loads function addresses into registers.
