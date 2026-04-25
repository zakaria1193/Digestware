---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GCC 16
- release
- branch
- frozen
discussion_id: aejhdeMRLLBGea1Y@tucnak
source_type: public_inbox
title: GCC 16.0.1 Status Report (2026-04-22), branch frozen for release
headline: GCC 16.0.1 branch is frozen for release
tldr: The GCC 16 branch is now frozen for release, requiring release manager approval
  for all changes.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Announces that the GCC 16 branch is frozen for release and that all changes
    require release manager approval.
  quote: 'We have branched for the GCC 16 release.  All changes on the releases/gcc-16

    branch require release manager approval now.'
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: other
  position: Asks if some bug fixes pushed to master after the branching are ok for
    the branch now, or if she needs to wait until after the release.
  quote: 'I pushed some bug fixes to master just after the branch.  There are 7 commits

    in total; two bug fixes, one testsuite fix, and four miscellaneous

    improvements.  Are they ok for the branch now, or do I need to wait until after

    the release?'
- author: Jakub Jelinek <jakub@redhat.com>
  role: other
  position: Requests Alice Carlotti to ask the release managers.
  quote: null
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: other
  position: States that she will do that.
  quote: null
primer_expert: This status report indicates that the GCC 16 release branch is frozen,
  meaning only approved changes can be merged. The report also includes bug count
  statistics, categorized by priority. This is standard procedure before a major release.
primer_general: This message indicates that the development of GCC version 16 has
  reached a stage where it is nearing release. The "branch frozen" status means that
  only critical bug fixes will be applied to this version. This is done to ensure
  stability and predictability for the upcoming release. After this point, any further
  changes need special approval.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aejhdeMRLLBGea1Y@tucnak
bugzilla_url: null
date: '2026-04-22'
---

Jakub Jelinek reports that the GCC 16 branch is now frozen for release. All changes to the releases/gcc-16 branch require release manager approval. The status report details the number of open bugs of various priorities.
