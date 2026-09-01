---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- xtensa
- assembler
- optimization
discussion_id: CAMo8BfJkN2jh5VLuEr0US2Ed+Hsv0PcD_nd_G7u6Ti_SfEL7+g@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] gas: fix MAX_ISTACK for loopgtz L32R widening'
headline: 'gas: fix MAX_ISTACK for loopgtz L32R widening'
tldr: Increase MAX_ISTACK in gas for Xtensa to accommodate loopgtz relaxation.
proposer: Max Filippov <jcmvbkbc@gmail.com>
consensus: Committed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increases memory usage for the instruction stack.
- Fixes a crash/overflow issue, improving robustness.
exchanges: []
primer_expert: This patch increases MAX_ISTACK in `gas/config/xtensa-istack.h` from
  12 to 16 to accommodate the instruction stack requirements of the `loopgtz` relaxation
  sequence, which now uses L32R instructions. It also modifies `istack_push` and `istack_push_space`
  in `gas/config/tc-xtensa.c` to report overflows using `as_fatal`. A new test case
  `gas/testsuite/gas/xtensa/loopgtz-relax.s` is added.
primer_glossary:
- term: MAX_ISTACK
  definition: The maximum number of entries allowed on the instruction stack within
    the gas assembler for Xtensa targets.
- term: loopgtz
  definition: A conditional branch instruction that continues looping as long as a
    counter is greater than zero.
- term: L32R
  definition: A specific instruction encoding or type used in Xtensa architectures,
    likely related to 32-bit register loads.
- term: relaxation
  definition: An optimization process performed by the assembler or linker to adjust
    instruction encodings or addresses for better code density or performance, often
    involving a temporary buffer (instruction stack).
- term: instruction stack
  definition: A temporary buffer used by the assembler during instruction relaxation
    to store information about instructions and their potential modifications.
- term: as_fatal
  definition: A function within the assembler (gas) used to report a fatal error and
    terminate the assembly process.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMo8BfJkN2jh5VLuEr0US2Ed+Hsv0PcD_nd_G7u6Ti_SfEL7+g@mail.gmail.com
bugzilla_url: null
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

A recent change in gas for Xtensa replaced loop widening with an L32R-based sequence. The loopgtz variant of this sequence requires 13 istack entries, exceeding the previous MAX_ISTACK limit of 12. This patch increases MAX_ISTACK to 16, documents the requirement, and improves overflow reporting. A new test case is included.
