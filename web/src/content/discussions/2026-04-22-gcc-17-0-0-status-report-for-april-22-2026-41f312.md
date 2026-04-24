---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GCC 17
- GCC 16
- status report
- development
discussion_id: aejiciLTTTAjeO6Q@tucnak
source_type: public_inbox
title: GCC 17.0.0 Status Report (2026-04-22)
headline: GCC 17.0.0 status report for April 22, 2026
tldr: GCC 17 development is open, and GCC 16 branching has occurred.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Reports on the status of GCC 17 development and the branching of GCC 16.
  quote: 'We have reached zero P1 regressions and branched for the GCC 16

    release.  This leaves trunk which is to become GCC 17 next year

    open for general development, Stage 1, again.'
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Acknowledges the status report.
  quote: null
primer_expert: This is a status report on GCC development. GCC development follows
  a branching model, with stable releases branched off from the main development trunk.  Once
  a release branch is created, the trunk is opened for development of the next major
  release. P1 regressions are critical bugs that must be fixed before a release.
primer_general: This report provides an update on the development status of the GCC
  compiler.  The development process involves creating separate branches for stable
  releases and allowing the main development line to move forward.  A "regression"
  refers to a bug that is introduced into the code, and P1 regressions are the most
  critical bugs that must be fixed before a software release.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aejiciLTTTAjeO6Q@tucnak
bugzilla_url: null
date: '2026-04-22'
---

Jakub Jelinek reports that GCC 17 development is now open, with trunk available for general development again. This follows the branching for GCC 16, which had reached zero P1 regressions.  Developers are asked to avoid disruptive changes to git master to allow for last-minute fixes for GCC 16.1.
