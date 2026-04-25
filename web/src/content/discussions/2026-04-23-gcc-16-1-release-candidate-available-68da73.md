---
project: gcc
subsystem: gcc
patch_id: null
tags: []
discussion_id: aeoJkja2vKycbMMh@tucnak
source_type: public_inbox
title: GCC 16.1 Release Candidate available from gcc.gnu.org
headline: GCC 16.1 Release Candidate available
tldr: The first release candidate for GCC 16.1 is available for testing.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Announces the availability of the first release candidate for GCC 16.1
    and asks for testing.
  quote: "The first release candidate for GCC 15.1 is available from\n\n https://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-202523/\n\
    \ ftp://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-20250423/\n\nPlease test it and\
    \ report any issues to bugzilla."
- author: Jakub Jelinek <jakub@redhat.com>
  role: other
  position: Corrects typos in the URLs for the release candidate.
  quote: "Sorry for typos in the URLs,\n  https://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-20260423/\n\
    \  ftp://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-20260423/"
- author: Frank Scheiner <frank.scheiner@web.de>
  role: other
  position: Reports that the release candidate bootstraps fine for C and C++.
  quote: Also bootstraps fine for c and c++
primer_expert: GCC 16.1 release candidate. Generated from git commit r16-8809-g9fa782dee8894e01.
primer_general: GCC is a compiler collection.  Release candidates are made available
  for testing before a final release.  This allows users to test upcoming features
  and bug fixes and report any issues.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aeoJkja2vKycbMMh@tucnak
bugzilla_url: null
date: '2026-04-23'
---

The first release candidate for GCC 16.1 is now available. Jakub Jelinek bootstrapped and tested the release candidate on x86_64-linux and asks for testing and bug reports. The anticipated release date is April 30th.
