---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- release candidate
- bootstrap
- ia64
discussion_id: aeoJkja2vKycbMMh@tucnak
source_type: public_inbox
title: 'Re: GCC 16.1 Release Candidate available from gcc.gnu.org'
headline: Gcc 16.1 RC bootstraps fine on ia64-linux.
tldr: Frank Scheiner reports that GCC 16.1 Release Candidate bootstrapped successfully
  on ia64-linux, with test suite runs scheduled.
proposer: Frank Scheiner <frank.scheiner@web.de>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Balancing testing coverage across different architectures with limited resources.
- Prioritizing testing on more common architectures vs. less common ones.
exchanges:
- author: Frank Scheiner <frank.scheiner@web.de>
  role: proposer
  position: Reports that the GCC 16.1 release candidate bootstrapped successfully
    on ia64-linux and that testsuite runs are scheduled.
  quote: 'Also bootstraps fine for c and c++ on ia64-linux. Testsuite run

    scheduled for tomorrow.'
- author: Frank Scheiner <frank.scheiner@web.de>
  role: other
  position: Acknowledges original poster's email.
  quote: 'On 24.04.26 23:08, Frank Scheiner wrote:

    > On 23.04.26 13:59, Jakub Jelinek via Gcc wrote:

    >> The first release candidate for GCC 15.1 is available from'
primer_expert: A GCC bootstrap involves building the compiler with itself.  Successful
  bootstrap on ia64-linux is one data point indicating the release candidate is stable.
  IA-64 is less commonly tested than x86_64.
primer_general: GCC is the GNU Compiler Collection.  A release candidate (RC) is a
  version of software that is nearly ready for release. Bootstrapping means compiling
  the compiler with itself, verifying core functionality.  ia64-linux is a less common
  architecture, so testing there is valuable.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/28d19d74-1081-4da5-bf89-69ea660506e6@web.de
bugzilla_url: null
date: '2026-04-24'
---

Frank Scheiner reports that the GCC 16.1 Release Candidate bootstrapped successfully for C and C++ on ia64-linux.  Testsuite runs were scheduled to follow.  This provides early feedback on the release candidate and broadens the set of tested platforms.
