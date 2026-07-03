---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GCC
- floating-point
- exceptions
- compilation
discussion_id: a3e960ff-0bc8-a13f-19ad-f0d0bd551746@redhat.com
source_type: public_inbox
title: 'Re: [RFC] Turning off trapping-math for C and C++ front-ends by default'
headline: Turning off trapping-math for C and C++ front-ends by default
tldr: GCC proposal to disable floating-point exception trapping by default for C/C++
  to simplify exception handling.
proposer: Richard Biener <rguenther@suse.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 6
technical_tradeoffs:
- Disabling FPU traps by default simplifies compiler optimizations but may require
  explicit enabling for code that relies on trap behavior.
- Standardizing FPU exception control via flags like `-ffp-exceptions` aims for clarity
  but requires careful definition of each level.
exchanges:
- author: Richard Biener <rguenther@suse.de>
  role: proposer
  position: Suggests disabling floating-point trapping by default for C/C++ to simplify
    exception handling and asks for alternative suggestions if the proposed option
    is not suitable.
  quote: null
- author: Joseph Myers <josmyers@redhat.com>
  role: reviewer
  position: Expresses concern that grouping 'ieee' and 'ieee-alternate' might be too
    broad, as they imply different levels of transformation restrictions.
  quote: null
primer_expert: This RFC proposes to change the default behavior of floating-point
  exception handling in GCC's C and C++ front-ends. Currently, the compiler might
  enable trapping mechanisms for floating-point operations, which can complicate optimization
  passes by introducing complex control flow for exception handling. The proposal
  aims to disable this trapping by default, aligning with a simpler exception model,
  and queries the best way to control specific floating-point exception behaviors
  via compiler flags.
primer_glossary:
- term: trapping-math
  definition: A floating-point behavior where exceptions (like division by zero, overflow,
    underflow) trigger a trap or interrupt, halting normal execution to handle the
    exception.
- term: floating-point exceptions
  definition: Events that occur during floating-point arithmetic operations, such
    as Invalid Operation, Division by Zero, Overflow, Underflow, and Inexact Result.
- term: exception handling
  definition: The mechanisms by which a program responds to runtime errors or exceptional
    conditions, such as floating-point exceptions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/E9DC9440-8EAD-416D-9C8C-6C460F5B6F4B@suse.de
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

Richard Biener proposes disabling floating-point exception trapping by default in GCC's C and C++ front-ends. The goal is to simplify exception handling, as trapping can complicate transformations. Joseph Myers questions the grouping of 'ieee' and 'ieee-alternate' under a single option, suggesting they encompass a wide range of restrictions. Biener seeks an alternative suggestion that isolates trap-based exceptions.
