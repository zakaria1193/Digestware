---
project: binutils
subsystem: xtensa
patch_id: null
tags:
- binutils
- gas
- xtensa
- assembler
- optimization
discussion_id: 7cdc8d664a39bd2ce3e70f0d0c6d9e233e5eb1f4.camel@espressif.com
source_type: public_inbox
title: '[PATCH] xtensa: fix MAX_ISTACK for loopgtz L32R widening'
headline: 'xtensa: fix MAX_ISTACK for loopgtz L32R widening'
tldr: Increase MAX_ISTACK in Xtensa gas to 16 to accommodate loopgtz relaxation.
proposer: Alexey Lapshin <alexey.lapshin@espressif.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases memory usage slightly by enlarging the instruction stack.
- Fixes a bug that could lead to assembler crashes or incorrect code generation for
  out-of-range loops.
exchanges:
- author: Alexey Lapshin
  role: proposer
  position: Submits a patch to increase `MAX_ISTACK` to 16 for Xtensa gas, fixing
    instruction stack overflows during `loopgtz` relaxation.
  quote: 'The loopgtz variant of that sequence needs 13 istack entries, but

    MAX_ISTACK remained 12, so relaxation of an out-of-range loopgtz

    overflowed the instruction stack. Increase MAX_ISTACK and report

    overflow with as_fatal that names MAX_ISTACK. Add a test.'
primer_expert: This patch addresses an overflow issue in the Xtensa assembler's instruction
  stack (`istack`) during loop relaxation. A recent change (commit 403b0b61f6d4) replaced
  loop widening with an L32R-based sequence. The `loopgtz` variant of this new sequence
  requires 13 entries on the instruction stack, but `MAX_ISTACK` was previously set
  to 12. This discrepancy caused the stack to overflow when relaxing out-of-range
  `loopgtz` instructions. The patch increases `MAX_ISTACK` to 16, provides more informative
  error messages for stack overflows, and adds a dedicated test case (`loopgtz-relax.d`
  and `.s`)…
primer_glossary:
- term: Xtensa
  definition: A configurable processor architecture used in many embedded systems.
    Binutils provides support for generating code for Xtensa processors.
- term: MAX_ISTACK
  definition: A macro defining the maximum size of the instruction stack used by the
    Xtensa assembler during relaxation and code generation.
- term: loopgtz
  definition: A conditional branch instruction that jumps if a given value is greater
    than zero.
- term: L32R
  definition: Load 32-bit Register. A type of instruction used in some architectures,
    including Xtensa, for loading 32-bit values into registers. It can be part of
    a sequence for handling wider immediate values.
- term: relaxation
  definition: A process in assemblers and compilers where short, potentially fixed-position
    instructions are replaced with longer, more flexible ones (or vice-versa) to handle
    code that might be placed at different addresses in memory. This is common for
    optimizing branches and calls.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project. It translates assembly
    language code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/7cdc8d664a39bd2ce3e70f0d0c6d9e233e5eb1f4.camel@espressif.com
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Alexey Lapshin proposes increasing `MAX_ISTACK` in the Xtensa assembler configuration from 12 to 16. This is necessary because the `loopgtz` relaxation sequence, which uses L32R widening, requires 13 instruction stack entries, causing overflows with the current limit. The patch also enhances overflow reporting and adds a new test case.
