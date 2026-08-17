---
project: binutils
subsystem: avr/ld
patch_id: null
tags:
- avr
- ld
- linker
- optimization
- relaxation
discussion_id: 119dbbc3-90ac-4bba-9e16-de0c9d084a8e@gjlay.de
source_type: public_inbox
title: '[patch] AVR: Let -mrelax elide global RJMP .+0'
headline: 'AVR: Elide global RJMP .+0 with -mrelax'
tldr: Patch allows the AVR linker, with -mrelax, to elide RJMP instructions with a
  zero offset targeting global symbols.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Eliding instructions might make debugging slightly more complex if the original
  instruction's presence was significant for analysis.
- The `--no-elide-rjmp0` option adds complexity to the linker's command-line interface.
exchanges:
- author: Georg-Johann Lay
  role: proposer
  position: Submits a patch to allow the AVR linker to elide specific RJMP instructions
    when relaxation is enabled.
  quote: This patch extends the avr-specific linker relaxation machine to elide trivial
    RJMP instructions. These are RJMP instructions with a jump offset of 0 that are
    targeting a global symbol.
primer_expert: This patch modifies the AVR backend of the GNU linker (`ld`) to introduce
  a new relaxation optimization. When the `-mrelax` option is used, the linker will
  now elide `RJMP .+0` instructions if they target a global symbol. This is specifically
  for cases like tail calls where the called function immediately follows the caller,
  and the `RJMP` is effectively a no-op. A new option, `--no-elide-rjmp0`, is added
  to disable this behavior.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology).
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or another object file.
- term: Relaxation
  definition: A linker optimization process where instructions with relative offsets
    are adjusted after the initial linking phase to accommodate final code placement,
    potentially allowing for shorter or more efficient instruction forms.
- term: RJMP
  definition: Relative Jump, an instruction on AVR microcontrollers that jumps to
    a target address relative to the current program counter.
- term: Elide
  definition: To omit or suppress; in this context, to remove an instruction that
    has no functional effect.
- term: Global symbol
  definition: A symbol (like a function or variable name) that is visible and accessible
    across different object files or modules.
- term: Tail call
  definition: A function call that is the very last operation in a function before
    it returns. Tail call optimization can replace the call with a jump, avoiding
    stack growth.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/119dbbc3-90ac-4bba-9e16-de0c9d084a8e@gjlay.de
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Georg-Johann Lay proposes a patch to extend the AVR linker's relaxation capabilities to elide zero-offset RJMP instructions that target global symbols. This optimization is intended for cases where a function tail-calls another function located immediately after it. The new feature can be disabled using the `--no-elide-rjmp0` linker option.
