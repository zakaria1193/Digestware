---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- gas
- x86
- optimization
- floating-point
discussion_id: 68f081b9-2332-4c98-b2ae-3baf1f404f6f@suse.com
source_type: public_inbox
title: 'Re: [PATCH] x86: support -Ofast'
headline: 'x86: support -Ofast'
tldr: Discussion on the implications of adding -Ofast support to binutils, particularly
  regarding its relaxation of strict commutativity and NaN handling.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Balancing aggressive optimization with strict standards compliance.
- Defining the scope of the -Ofast flag in the assembler.
- Potential impact on program correctness due to relaxed constraints.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes adding -Ofast support to binutils, explaining its analogy to
    GCC's option and its relaxation of NaN-related commutativity constraints.
  quote: With this I was trying to offer a compromise on the earlier discussion regarding
    the XCHG -> MOV optimization. It was certainly my expectation that ...
- author: H. J. Lu
  role: reviewer
  position: Engages in the discussion about -Ofast, its connection to commutativity
    and NaN handling, and the potential renaming of the control variable to encompass
    NOP-like instruction optimizations.
  quote: null
primer_expert: This thread discusses the addition of the `-Ofast` optimization level
  to the GNU Assembler for x86. The discussion draws parallels with GCC's `-Ofast`
  flag, which permits aggressive optimizations that may violate strict standards compliance,
  such as those related to floating-point NaN (Not a Number) handling and instruction
  commutativity. A key point of debate is whether this new assembler option should
  also control optimizations for instructions that are effectively NOPs in certain
  contexts, like the XCHG to MOV transformation.
primer_glossary:
- term: -Ofast
  definition: An optimization level flag for compilers and assemblers that enables
    aggressive optimizations, potentially at the cost of strict adherence to floating-point
    standards or other language specifications. It may relax constraints on instruction
    ordering and commutativity.
- term: NaN
  definition: Not a Number. A special floating-point value used to represent undefined
    or unrepresentable results, such as the result of 0/0.
- term: Commutativity
  definition: A property of an operation where the order of operands does not affect
    the result (e.g., a + b = b + a). Floating-point operations may not be strictly
    commutative due to NaN handling or precision issues.
- term: XCHG
  definition: An x86 assembly instruction that exchanges the contents of two operands
    (e.g., a register and memory).
- term: MOV
  definition: An x86 assembly instruction that copies data from a source operand to
    a destination operand.
- term: NOP
  definition: No Operation. An instruction that does nothing and simply advances the
    instruction pointer. Sometimes, other instructions can be optimized into NOPs
    or replaced by NOPs.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/68f081b9-2332-4c98-b2ae-3baf1f404f6f@suse.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

Jan Beulich discusses the implications of adding -Ofast support to binutils, relating it to GCC's -Ofast option. The conversation touches on how -Ofast relaxes constraints on instruction commutativity, especially concerning NaN handling in floating-point operations. It also explores whether this option should also control optimizations for NOP-like instructions, like the XCHG to MOV transformation.
