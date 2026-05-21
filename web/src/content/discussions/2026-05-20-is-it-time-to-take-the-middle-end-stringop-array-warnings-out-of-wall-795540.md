---
project: gcc
subsystem: gcc
patch_id: null
tags:
- warnings
- -Wall
- middle-end
- stringop
- array
discussion_id: EA5F2DB8-4712-46E7-8D65-5FEEB9613D3A@gmail.com
source_type: public_inbox
title: 'Re: Is it time to take the middle-end stringop/array warnings out of -Wall?'
headline: Is it time to take the middle-end stringop/array warnings out of -Wall?
tldr: Richard Biener agrees it may be time to move middle-end stringop/array warnings
  out of -Wall.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: proposer
  position: Agrees that moving the warnings out of -Wall seems like a reasonable intermediate
    step.
  quote: It seems to be a reasonable, if intermediate step.
primer_expert: The middle-end of GCC performs optimizations and transformations on
  the program's intermediate representation (IR).  Stringop/array warnings detect
  potential buffer overflows or out-of-bounds accesses during these optimizations.
  The `-Wall` flag enables a set of commonly used warnings.
primer_general: GCC is a compiler that translates human-readable code into machine
  code. During compilation, GCC performs various checks and optimizations.  `-Wall`
  is a compiler flag that enables a set of useful warnings.  This thread discusses
  whether certain warnings related to string and array operations, which may produce
  false positives, should be enabled by default.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/EA5F2DB8-4712-46E7-8D65-5FEEB9613D3A@gmail.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

Martin Uecker finds middle-end stringop/array warnings useful in C, and observes that some new languages are stricter and fail hard for false positives. Richard Biener agrees that moving the warnings out of -Wall seems like a reasonable intermediate step. The discussion considers whether these warnings, which can have a high false positive rate, should remain in the default warning set.
