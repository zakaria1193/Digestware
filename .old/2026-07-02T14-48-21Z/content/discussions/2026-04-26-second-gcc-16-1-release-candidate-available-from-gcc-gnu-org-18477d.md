---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- release candidate
- ia64
- bootstrap
discussion_id: 83201887-7a15-4234-8bce-a5aa0c21c383@web.de
source_type: public_inbox
title: 'Re: Second GCC 16.1 Release Candidate available from gcc.gnu.org'
headline: Second GCC 16.1 Release Candidate available from gcc.gnu.org
tldr: Frank Scheiner reports that the second GCC 16.1 release candidate bootstrapped
  fine on ia64-linux.
proposer: Frank Scheiner <frank.scheiner@web.de>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Testing release candidates on different platforms helps identify and fix platform-specific
  issues before the final release.
- The bootstrap process is a critical test of the compiler's ability to compile itself
  correctly.
exchanges:
- author: Frank Scheiner <frank.scheiner@web.de>
  role: proposer
  position: Reports a successful bootstrap of GCC 16.1 RC2 on ia64-linux for C and
    C++.
  quote: 'Also bootstraps fine for c and c++ on ia64-linux. Testsuite run

    hhopefully tomorrow.'
primer_expert: GCC 16.1 is the next planned minor release of the GCC 16 series.  Bootstrapping
  involves compiling the compiler with itself and its support libraries, checking
  for regressions.
primer_general: GCC is the GNU Compiler Collection, which compiles source code into
  machine code.  A release candidate (RC) is a pre-release version offered for testing
  before the final release. Bootstrapping is the process of compiling the compiler
  using itself, testing its own ability to produce working code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/83201887-7a15-4234-8bce-a5aa0c21c383@web.de
bugzilla_url: null
date: '2026-04-26'
is_stub: true
---

Frank Scheiner reports that the second release candidate for GCC 16.1 bootstrapped successfully for C and C++ on ia64-linux. He planned to run the test suite the next day. Release candidates are important milestones on the path to a stable release, and testing on various platforms helps ensure quality.
