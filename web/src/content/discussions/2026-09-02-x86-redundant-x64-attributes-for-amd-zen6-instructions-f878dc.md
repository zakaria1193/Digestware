---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- amd
- instructions
- clean-up
- linker
discussion_id: b76eb9a5-f72c-42e1-a5a4-9dd7685ec91d@suse.com
source_type: public_inbox
title: 'Re: [PATCH] x86: support further AMD Zen6 instructions'
headline: 'x86: Redundant ''x64'' attributes for AMD Zen6 instructions'
tldr: Removes redundant 'x64' attributes from new AMD Zen6 instructions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Minor code cleanup, improving maintainability and accuracy.
- No functional change, purely a correctness improvement in the definition files.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Identifies redundant 'x64' attributes in new AMD Zen6 instruction definitions.
  quote: 'Since you have implied x64 here ...


    ... I believe we do not need the x64 here. They are redundant.'
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Confirms the redundancy and states intent to submit a corrective patch.
  quote: Indeed. The same applies to RMPREAD - I'll make a patch to remove the ex
primer_expert: This discussion concerns the x86 instruction definitions within binutils.
  Specifically, it addresses the addition of new AMD Zen6 instructions (RMPDIRTY,
  RMPOPT) and identifies that the 'x64' architecture attribute in their opcode table
  definitions is redundant, as the context implies 64-bit operation. The maintainer
  agrees and plans to submit a fix.
primer_glossary:
- term: x64
  definition: Refers to the 64-bit extension of the x86 instruction set architecture,
    commonly used in modern desktop and server processors.
- term: AMD Zen6
  definition: The codename for a future microarchitecture from AMD, implying new instructions
    or enhancements.
- term: opcodes table
  definition: A data structure, often a C array, used by assemblers and disassemblers
    to map instruction mnemonics and their encodings.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/b76eb9a5-f72c-42e1-a5a4-9dd7685ec91d@suse.com
bugzilla_url: null
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

Jan Beulich points out that the 'x64' attributes added for new AMD Zen6 instructions (RMPDIRTY, RMPOPT) are redundant because the context already implies a 64-bit architecture. He notes this is similar to the RMPREAD instruction and indicates he will provide a patch to correct this. This clean-up improves the accuracy and conciseness of the instruction definitions.
