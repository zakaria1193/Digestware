---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- binutils
- opcodes
- template
- assembly
discussion_id: a04ec8d3-c40d-45a6-ab94-3f460fad4ca7@suse.com
source_type: public_inbox
title: '[PATCH] x86: introduce <hl> template'
headline: 'x86: introduce <hl> template'
tldr: A new template `<hl>` is introduced in the x86 opcode table to simplify the
  definition of instructions involving high and low byte operations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies opcode table maintenance by abstracting common instruction patterns.
- May slightly increase the complexity of understanding the opcode table for those
  unfamiliar with the new template.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Introduces a new opcode template `<hl>` for x86 instructions to simplify
    the definition of operations involving high and low parts, citing VPINTERLEAVE
    as a similar pattern.
  quote: <hl:mov:fp:int:mul:shuf, h:4:1:8:e5:f3, l:0:0:0:d5:f2>
primer_expert: The patch modifies `opcodes/i386-opc.tbl` to add a new template `<hl>`.
  This template is designed to abstract the common patterns found in x86 instructions
  that involve high (`h`) and low (`l`) byte/word operations, particularly for multiply
  instructions like `pmulhw` and `pmullw`. It consolidates the encoding logic, reducing
  verbosity and potential errors in the opcode table.
primer_glossary:
- term: opcode table
  definition: A data structure used by assemblers and disassemblers to map mnemonic
    instructions to their binary machine code representations.
- term: template
  definition: In this context, a reusable pattern or macro within the opcode table
    definition to represent common instruction formats.
- term: x86
  definition: A family of instruction set architectures developed by Intel, widely
    used in personal computers and servers.
- term: VPINTERLEAVE
  definition: AVX-512 instructions that interleave data elements from two sources
    into a destination.
- term: PMULHW
  definition: Packed Multiply High Word, an MMX or SSE instruction that multiplies
    the high words of packed integers.
- term: PMULLW
  definition: Packed Multiply Low Word, an MMX or SSE instruction that multiplies
    the low words of packed integers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/a04ec8d3-c40d-45a6-ab94-3f460fad4ca7@suse.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch introduces a new template named `<hl>` into the x86 opcode table in binutils. This template aims to reduce redundancy in defining instructions that operate on high and low parts of registers or memory, similar to existing patterns for VPINTERLEAVE instructions. It simplifies the encoding of instructions like PMULHW/PMULLW.
