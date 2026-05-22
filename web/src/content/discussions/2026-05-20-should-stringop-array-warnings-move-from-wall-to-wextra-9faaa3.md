---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- warnings
- -Wall
- -Wextra
- stringop
discussion_id: 43f957da6e2d189b4b98d79b93d1a8f21f4230d5.camel@gwdg.de
source_type: public_inbox
title: 'Re: Is it time to take the middle-end stringop/array warnings out of -Wall?'
headline: Should stringop/array warnings move from -Wall to -Wextra?
tldr: Debate continues on whether certain GCC warnings about string and array operations
  should be moved from `-Wall` to `-Wextra` due to high false-positive rates.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Under Review
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Reducing false positives in `-Wall` by moving less reliable warnings to `-Wextra`.
- Potentially hiding real issues from developers who rely solely on `-Wall`.
- Maintaining a balance between comprehensive warnings and a clean build process.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: proposer
  position: Suggests moving string and array operation warnings to -Wextra as a reasonable
    intermediate step.
  quote: It seems to be a reasonable, if intermediate step.
- author: Martin Uecker <muecker@gwdg.de>
  role: other
  position: Prefers keeping the warnings at least in -Wextra, noting their usefulness
    in C and the stricter nature of modern languages.
  quote: 'I sometimes find them useful (in C, C++ might be affected differently).


    I also observe that people invent entirely new languages which are much

    stricter and which fail hard for things which would be considered

    false positives, so keeping them at least in -Wextra would seem

    appropriate to me.'
primer_expert: GCC's `-Wall` flag enables a set of commonly useful warnings.  Some
  middle-end warnings (e.g., those emitted during IPA or tree-SSA passes related to
  string and array operations) have a high false positive rate. Moving them to `-Wextra`
  would still allow developers to enable them, but avoid the noise for those expecting
  `-Wall` to be relatively quiet.  The discussion hinges on which warning flags are
  'essential'.
primer_general: Compilers can be configured to emit warnings about potentially problematic
  code. GCC uses flags like `-Wall` to enable groups of warnings. Some warnings related
  to how strings and arrays are handled can be overly sensitive, flagging code that
  is actually safe. This discussion is about whether these more noisy warnings should
  be moved to a different flag (`-Wextra`) so that new projects are not burdened with
  them by default. This creates a trade-off between catching potential errors and
  overwhelming developers with false alarms.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/EA5F2DB8-4712-46E7-8D65-5FEEB9613D3A@gmail.com
bugzilla_url: null
date: '2026-05-20'
is_stub: false
---

The ongoing discussion centers on moving certain middle-end string and array operation warnings from the `-Wall` flag to `-Wextra` in GCC.  The rationale is that these warnings, while sometimes useful, generate a high number of false positives, causing more annoyance than help for developers. Moving them to `-Wextra` would keep them available for those who want them, while reducing noise for the average user. The suggestion is seen as a reasonable intermediate step.
