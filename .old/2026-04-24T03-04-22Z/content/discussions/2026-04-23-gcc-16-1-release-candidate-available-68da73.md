---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- release
- release candidate
discussion_id: aeoJkja2vKycbMMh@tucnak
source_type: public_inbox
title: GCC 16.1 Release Candidate available from gcc.gnu.org
headline: Gcc 16.1 Release Candidate Available
tldr: The first release candidate for GCC 16.1 is available for testing.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jakub Jelinek
  role: proposer
  position: Announces the availability of the first release candidate for GCC 16.1
    and asks for testing.
  quote: "The first release candidate for GCC 15.1 is available from\n\n https://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-202523/\n\
    \ ftp://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-20250423/\n\nand shortly its mirrors.\
    \  It has been generated from git commit\nr16-8809-g9fa782dee8894e01."
- author: Jakub Jelinek
  role: proposer
  position: Corrects typos in the URLs for the release candidate.
  quote: "Sorry for typos in the URLs,\n https://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-20260423/\n\
    \ https://gcc.gnu.org/pub/gcc/snapshots/16.1.0-RC-20260423/"
primer_expert: GCC releases are managed using branches. Once a release branch is created,
  release candidates are cut from that branch. This allows for last-minute fixes to
  be applied to the release without disrupting development on the main trunk.
primer_general: GCC, the GNU Compiler Collection, is a suite of programming language
  compilers.  Before a final release, release candidates are created that can be tested
  by the community.  This helps to identify and fix any remaining bugs before the
  final release.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aeoJkja2vKycbMMh@tucnak
bugzilla_url: null
date: '2026-04-23'
---

The first release candidate for GCC 16.1 is now available for testing.  Jakub Jelinek asks for testing and bug reports in bugzilla. If all goes well, the plan is to release 16.1 on April 30th.
