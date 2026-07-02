---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- warnings
- memory-safety
- false positives
discussion_id: 06843749fe753b34a5161dd71d7436615944d135.camel@gwdg.de
source_type: public_inbox
title: 'Re: Is it time to take the middle-end stringop/array warnings out of -Wall?'
headline: Is it time to take middle-end stringop/array warnings out of -Wall?
tldr: Martin suggests new warning categories for memory-safety issues with aggressive
  warnings for potential safety problems.
proposer: Martin Uecker <muecker@gwdg.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- More aggressive warnings may lead to more false positives, requiring developers
  to spend time investigating non-issues.
- Adding new warning categories requires development effort and may increase the complexity
  of GCC's warning system.
exchanges:
- author: Martin Uecker <muecker@gwdg.de>
  role: proposer
  position: Suggests creating new warning categories related to memory-safety issues
    with more aggressive warnings.
  quote: 'Some alternative could be to have new warning categories related

    to memory-safety issues where the expectation is that the warnings

    are aggressive and even potential safety issues see a warning.'
primer_expert: GCC's middle-end performs optimizations and transformations on the
  intermediate representation (IR) of code.  Stringop/array warnings detect potential
  buffer overflows or out-of-bounds accesses during this phase.
primer_general: Compilers use a multi-stage process to translate human-readable code
  into machine instructions. After parsing and initial conversion, the "middle-end"
  stage optimizes the code. This stage can detect potential errors, such as writing
  beyond the boundaries of an array.  These warnings can be controlled by flags such
  as `-Wall` (all warnings) and `-Wextra` (extra warnings).
series_id: 6C8E18B9-B946-4358-94A3-2979A435417C@gmail.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/06843749fe753b34a5161dd71d7436615944d135.camel@gwdg.de
bugzilla_url: null
date: '2026-05-21'
is_stub: false
---

Martin Uecker suggests creating new warning categories related to memory-safety issues. These categories would have aggressive warnings, even for potential safety problems. This could include warnings about unsafe casts or pointer arithmetic. He acknowledges the desire to reduce false positives.
