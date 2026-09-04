---
project: binutils
subsystem: avr
patch_id: null
tags:
- avr
- linker
- optimization
- relaxation
discussion_id: 22920702-1e43-4045-bc1d-45bcdd804cc4@gjlay.de
source_type: public_inbox
title: 'Re: [patch] AVR: Let -mrelax elide global RJMP .+0'
headline: 'AVR: Let -mrelax elide global RJMP .+0'
tldr: Allow the AVR linker's relaxation to elide RJMP instructions targeting global
  symbols.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Potential for increased code size if the elision is incorrect in edge cases, though
  tests passed.
- Adds a new command-line option (--no-elide-rjmp0) for fine-grained control.
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Extends AVR linker relaxation to elide RJMP instructions with zero offset
    targeting global symbols. Passes test suite.
  quote: "This patch extends the avr-specific linker relaxation machine to elide trivial\
    \ RJMP instructions. These are RJMP instructions with a jump offset of 0 that\
    \ are targeting a global symbol.\nThe use case is when a function is tail-calling\
    \ some other function, and the latter happens to be located right after the former,\
    \ like in:\n\n  \t\trjmp\tfunc\t\t  ;; from module A\n  \t\t.global func\t  ;;\
    \ from module B…"
primer_expert: This patch targets the AVR architecture's linker relaxation pass within
  binutils. Specifically, it allows the linker to optimize away redundant RJMP instructions
  (relative jumps) when they target a global symbol and the jump offset is zero. This
  is a micro-optimization for specific code generation patterns.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/22920702-1e43-4045-bc1d-45bcdd804cc4@gjlay.de
bugzilla_url: null
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

This patch extends the AVR linker's relaxation capabilities to elide RJMP instructions that jump to a global symbol with a zero offset. This optimization is useful in scenarios like tail-calling functions where the called function immediately follows the caller. A new option, --no-elide-rjmp0, is introduced to disable this feature. The patch has been tested and approved.
