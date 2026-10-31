---
project: binutils
subsystem: x86/apx
patch_id: null
tags:
- x86
- assembler
- optimization
- code size
discussion_id: 91815583-ea03-4d4f-a013-5586b060a10b@suse.com
source_type: public_inbox
title: '[PATCH 4/5] x86/APX: optimize {nf} forms of AND with small negative immediates'
headline: 'x86/APX: optimize {nf} forms of AND with small negative immediates'
tldr: Optimizes AND instructions in gas for x86 APX with small negative immediates
  to use smaller forms for size reduction.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reduces code size for specific instructions by using shorter encodings, potentially
  at the cost of slightly increased instruction decoding complexity or a very minor
  performance difference in some edge cases (e.g., partial register stalls).
- The optimization is restricted to 'non-fused' forms and only when optimizing for
  size.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes an optimization for `AND` instructions with small negative immediates
    in the x86 APX gas assembler. The change transforms instructions into smaller
    byte/word forms to reduce code size when optimizing for space.
  quote: 'These can be expressed with byte or word forms, leveraging that non-

    EVEX.ND byte/word operations leave the upper bits unaltered. Since

    - word forms incur length-changing-prefix effects,

    - byte and word forms can incur partial register stalls,

    restrict transforming those to merely size optimization.'
primer_expert: This patch targets the x86 instruction emitter in gas, specifically
  for the APX (Advanced Performance Extensions) instruction set. It optimizes the
  encoding of non-fused (nf) forms of the `AND` instruction when a small, negative
  immediate operand is used. The optimization leverages the fact that byte and word
  operations on registers (e.g., `ANDb`, `ANDw`) only affect the lower bits, and any
  upper bits in the destination register are zeroed or preserved depending on the
  instruction's mode. This allows larger immediates (up to 16-bit, represented as
  negative values) to be encoded using their 8-…
primer_glossary:
- term: x86/APX
  definition: Refers to the x86 instruction set architecture with Advanced Performance
    Extensions, a set of newer instructions for Intel processors designed to improve
    performance.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    converting assembly code into machine code.
- term: AND
  definition: A bitwise logical operation that sets a bit to 1 only if it is set to
    1 in both operands.
- term: immediate
  definition: A constant value embedded directly within an instruction, rather than
    being stored in a register or memory location.
- term: EVEX.ND
  definition: Encoding for advanced vector extensions (AVX-512 and later) in x86.
    'ND' likely refers to 'not-downconverted' or a similar encoding detail relevant
    to operation size and masking.
- term: -Os
  definition: A compiler optimization flag that instructs the compiler to optimize
    for code size.
series_id: 'binutils:x86/apx: optimize {nf} forms of and with small negative immediates'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/91815583-ea03-4d4f-a013-5586b060a10b@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch optimizes the assembly of `AND` instructions in the gas assembler for x86 APX targets when used with small, negative immediates. It leverages the behavior of non-EVEX.ND byte/word operations, which leave upper bits unaltered. The optimization transforms larger forms of these instructions into their smaller byte or word equivalents, aiming to reduce code size, particularly when optimizing for space (`-Os`).
