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
discussion_id: CAH6eHdRfEVsGjbJ__kU5AR9BfVdLQZ_iGGDZa=yQnT4fgG2P6w@mail.gmail.com
source_type: public_inbox
title: Is it time to take the middle-end stringop/array warnings out of -Wall?
headline: Is it time to take the middle-end stringop/array warnings out of -Wall?
tldr: Jonathan Wakely argues for removing middle-end stringop/array warnings from
  -Wall due to high false positive rates and lack of actionable information.
proposer: Jonathan Wakely <jwakely.gcc@gmail.com>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Moving the warnings to -Wextra might cause them to be ignored, leading to bitrot.
- Removing the warnings entirely might eliminate the incentive to improve the compiler's
  optimization capabilities.
- Keeping the warnings in -Wall can lead to user frustration due to false positives.
exchanges:
- author: Jonathan Wakely <jwakely.gcc@gmail.com>
  role: proposer
  position: Argues for removing the warnings from -Wall due to high false positive
    rates and the warnings not being actionable.
  quote: The warnings **are not actionable**. They are usually the result of complex
    transformations and reordering by the optimizers, but the warning gives no indication
    of that. It just says "overflow on this line", without explaining that the compiler
    is assuming some sequence of conditions which have to hold before the "bug" could
    happen.
- author: Rene Kita <mail@rkta.de>
  role: other
  position: Agrees with Jonathan Wakely, quoting his message in full.
  quote: null
- author: Sam James <sam@gentoo.org>
  role: other
  position: Agrees with Jonathan Wakely that the warnings should not lie to users.
  quote: null
- author: Richard Biener <richard.guenther@gmail.com>
  role: other
  position: Suggests moving the diagnostics earlier or removing them altogether if
    they are no longer in -Wall and become unmaintained.
  quote: null
- author: Joseph Myers <josmyers@redhat.com>
  role: other
  position: Suggests putting the warnings in -Wextra if they are removed from -Wall.
  quote: null
- author: Jonathan Wakely <jwakely.gcc@gmail.com>
  role: other
  position: Quotes Joseph Myers about the intended purpose of -Wall.
  quote: null
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
url: https://inbox.sourceware.org/gcc/CAH6eHdRfEVsGjbJ__kU5AR9BfVdLQZ_iGGDZa=yQnT4fgG2P6w@mail.gmail.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

Jonathan Wakely argues that the false positive rate for middle-end stringop/array warnings in GCC has been unacceptably high for years. He claims the warnings often lie, are not actionable, and make GCC look bad.  He suggests that using these warnings as a proxy for finding missed optimization opportunities is a terrible policy.
