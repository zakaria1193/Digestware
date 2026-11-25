---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- disassembler
- optimization
- instruction decoding
discussion_id: 20261125025135.3126887-1-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH] x86: Short circuit ACE outer product table pass'
headline: 'x86: Short circuit ACE outer product table pass'
tldr: Optimizes x86 instruction decoding by introducing a new table for ACE outer
  product instructions.
proposer: Haochen Jiang <haochen.jiang@intel.com>
consensus: Under Review
outcome: under_review
impact_score: 4
sentiment_score: 7
technical_tradeoffs:
- Introduces a new table, potentially increasing code size slightly, but offering
  performance gains during instruction decoding.
exchanges:
- author: Haochen Jiang <haochen.jiang@intel.com>
  role: proposer
  position: Proposes to introduce a new table (`USE_X86_64_EVEX_PFX_ACE_TABLE`) to
    streamline the decoding of x86 ACE outer product instructions, noting that these
    instructions share common attributes.
  quote: 'All the ACE outer product instruction shares the same pattern (or you can
    say attributes): 64-bit, EVEX512, modrm.mod == 3 and W0. As Jan said, it gave
    us a chance to short circuit the table pass.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions the inclusion of the 'W0' attribute for all ACE outer product
    instructions, suggesting it might not apply to all cases like TOP1PD.
  quote: The W0 part doesn't quite fit TOP1PD, so may want leaving out.
primer_expert: This patch introduces `USE_X86_64_EVEX_PFX_ACE_TABLE` into `opcodes/i386-dis.c`
  and related headers. It leverages the observation that ACE outer product instructions
  share common EVEX prefix attributes. By grouping these into a dedicated table, the
  disassembler can short-circuit the lookup process, avoiding redundant checks. This
  is an optimization for instruction decoding, specifically targeting the handling
  of these specialized x86 instructions.
primer_glossary:
- term: ACE
  definition: Advanced Cryptography Extensions, a set of instructions for accelerating
    cryptographic operations.
- term: EVEX
  definition: An instruction encoding scheme used in x86 processors (AVX-512 and later)
    that extends the existing VEX prefix, allowing for more advanced features and
    wider vector registers.
- term: modrm.mod
  definition: A byte in x86 instruction encoding that specifies the addressing mode.
    'mod' bits indicate whether the operand is a register or memory, and how the memory
    address is formed.
- term: W0
  definition: A bit within the EVEX prefix that, in some contexts, indicates the operand
    size (e.g., 64-bit for registers).
- term: TOP1PD
  definition: A specific x86 instruction (e.g., 'Multiply Packed Single-Precision
    Floating-Point Values').
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261125025135.3126887-1-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch introduces a new table, `USE_X86_64_EVEX_PFX_ACE_TABLE`, to optimize the decoding of x86 ACE outer product instructions. These instructions share common attributes (64-bit, EVEX512, modrm.mod == 3, W0), allowing the disassembler to short-circuit the table lookup process for improved performance. The change removes redundant table entries and simplifies the decoding logic.
