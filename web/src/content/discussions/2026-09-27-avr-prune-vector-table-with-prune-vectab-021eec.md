---
project: binutils
subsystem: avr
patch_id: null
tags:
- linker
- avr
- optimization
- embedded
discussion_id: 0763b1cc-1a98-43dd-bb4b-72fed08ec5b3@gjlay.de
source_type: public_inbox
title: '[patch] AVR: Prune vector table with --prune-vectab PR ld/34679'
headline: 'AVR: Prune vector table with --prune-vectab'
tldr: Adds a new ld option --prune-vectab for AVR targets to remove unused vector
  table entries and simplify relaxation.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reduces code size by pruning unused vector table entries.
- Simplifies relaxation process, potentially improving link times.
- Adds a new option to the linker, increasing its complexity.
exchanges: []
primer_expert: This patch introduces a linker option, `--prune-vectab`, for the AVR
  architecture. It targets the vector table, which often contains many unused entries
  pointing to `__bad_interrupt`. The option prunes these entries before the standard
  relaxation pass, which typically converts `JMP` to `RJMP+NOP`. This pre-pruning
  simplifies the relaxation process. Additionally, it allows the removal of the final
  NOP in a sequence of `RJMP+NOP` entries. Tests were conducted on ATmega128 and ATmega8,
  comparing behavior with and without `-mrelax --prune-vectab`.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers manufactured by Atmel (now Microchip Technology).
    Common in embedded systems.
- term: vector table
  definition: A table in memory that contains the addresses of interrupt service routines.
    When an interrupt occurs, the processor uses this table to find the appropriate
    handler.
- term: __bad_interrupt
  definition: A placeholder or default interrupt handler function that is typically
    called when an unassigned interrupt vector is triggered.
- term: relaxation
  definition: A linker optimization process that adjusts instruction addresses and
    sizes to use shorter, more efficient opcodes where possible, often converting
    longer jumps to shorter ones.
- term: RJMP
  definition: A relative jump instruction in AVR assembly language. It has a shorter
    encoding than a traditional absolute jump.
- term: NOP
  definition: No Operation; an instruction that does nothing but consume clock cycles.
    Often used as padding or to align code.
- term: CLH
  definition: Possibly 'Clear Halt' or a similar low-level instruction, mentioned
    in the context of AVR-SD and AVR-LibC.
- term: AVR-SD
  definition: Likely refers to a specific AVR development toolchain or configuration,
    possibly related to debug or simulation.
- term: AVR-LibC
  definition: A standard C library implementation for the AVR microcontroller family.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/0763b1cc-1a98-43dd-bb4b-72fed08ec5b3@gjlay.de
bugzilla_url: null
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

This patch introduces the --prune-vectab option for the AVR target in GNU ld. This new option prunes the vector table by removing unused entries that point to __bad_interrupt, simplifying subsequent relaxation steps. It also allows the removal of trailing NOPs in RJMP+NOP sequences within the vector table. The changes have been tested and pass the avr-gcc testsuite.
