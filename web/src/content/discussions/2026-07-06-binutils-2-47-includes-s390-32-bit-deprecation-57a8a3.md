---
project: binutils
subsystem: binutils
patch_id: null
tags:
- s390
- deprecation
- release
discussion_id: 3c1688c2-fe6c-41ac-b55d-d36f7be83f44@linux.ibm.com
source_type: public_inbox
title: 'Re: Upcoming 2.47 branch and release dates'
headline: Binutils 2.47 includes s390 32-bit deprecation
tldr: Jens Remus informs that the deprecation of s390 32-bit targets has been committed
  for Binutils 2.47.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Notifies that the s390 32-bit deprecation has been committed for Binutils
    2.47.
  quote: 'Nick, just FYI, that I finally committed the Binutils and GDB

    s390 32-bit deprecation to mainline for Binutils 2.47:


    748bc6a7febf ("s390: Deprecate s390 32-bit target "s390-*")'
primer_expert: The s390 target in Binutils has had its 32-bit variant deprecated.
  This is a maintenance change for the release branch, and doesn't impact ongoing
  development on mainline.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/3c1688c2-fe6c-41ac-b55d-d36f7be83f44@linux.ibm.com
bugzilla_url: null
date: '2026-07-06'
is_stub: false
stub_reason: ''
---

Jens Remus provides an update on the upcoming Binutils 2.47 release, noting that the deprecation of s390 32-bit targets has been committed. This change will be included in the 2.47 release, which is scheduled to branch on July 11th and release on July 25th.
