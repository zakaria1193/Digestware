---
project: binutils
subsystem: bpf
patch_id: null
tags:
- bpf
- gas
- instruction-set
discussion_id: 20260929183603.687571-1-vineet.gupta@linux.dev
source_type: public_inbox
title: '[PATCH] bpf: add the addr_space_cast instruction'
headline: 'bpf: add the addr_space_cast instruction'
tldr: Adds the addr_space_cast BPF instruction to gas for supporting BPF arenas.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Spelling out instruction variants to avoid opcode conflicts simplifies implementation
  but might be less DRY than a more generalized approach.
- The patch prioritizes simplicity by directly implementing the two required combinations.
exchanges:
- author: Vineet Gupta <vineet.gupta@linux.dev>
  role: proposer
  position: Adds the addr_space_cast instruction to gas, which is required for BPF
    arena support.
  quote: 'gas doesn''t support bpf arenas as it is missing addr_space_cast BPF

    instruction. It is essentially a `mov'' with a distinguised offset and

    the two address spaces supported (0: generic, 1: arena) ecoded in the

    immediate.'
- author: Jose E. Marchesi <jemarch@gnu.org>
  role: reviewer
  position: Acknowledges the patch and its purpose, indicating it has been received
    for review.
  quote: Hi Vineet, thanks for the patch.
primer_expert: Adds the `addr_space_cast` instruction to gas for BPF. This instruction
  is analogous to a `mov` but encodes the address space (0 for generic, 1 for arena)
  in its immediate field. The patch implements this by spelling out the two specific
  combinations to avoid conflicts with the `mov` opcode's mask.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260929183603.687571-1-vineet.gupta@linux.dev
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch introduces the addr_space_cast BPF instruction to the GNU Assembler (gas). This instruction is necessary for supporting BPF arenas, as it allows for distinct address spaces (generic and arena) to be encoded within an immediate value. To simplify implementation, the two combinations are spelled out as literal template text, preceding the 'mov' instruction to avoid opcode conflicts.
