---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- release
- branch
- frozen
discussion_id: aejhdeMRLLBGea1Y@tucnak
source_type: public_inbox
title: GCC 16.0.1 Status Report (2026-04-22), branch frozen for release
headline: Gcc 16.0.1 Status Report (2026-04-22), Branch Frozen
tldr: The GCC 16 branch is frozen for release, requiring release manager approval
  for all changes.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jakub Jelinek
  role: proposer
  position: Announces that the GCC 16 branch is frozen for release, requiring release
    manager approval for all changes.
  quote: 'We have branched for the GCC 16 release.  All changes on the releases/gcc-16

    branch require release manager approval now.'
- author: Alice Carlotti
  role: other
  position: Asks whether some bug fixes and improvements pushed to master after the
    branch are OK for the branch now.
  quote: 'I pushed some bug fixes to master just after the branch.  There are 7 commits

    in total; two bug fixes, one testsuite fix, and four miscellaneous

    improvements.  Are they ok for the branch now, or do I need to wait until after

    the release?'
- author: Jakub Jelinek
  role: other
  position: States that the changes should be OK, but asks Alice to check with the
    release managers.
  quote: null
- author: Alice Carlotti
  role: other
  position: Confirms that she will check with the release managers.
  quote: null
primer_expert: GCC releases are managed using branches. Once a release branch is created,
  it is frozen to stabilize the code for release. Changes to the branch require approval
  from the release manager. The "master" branch is where active development happens
  for future releases.
primer_general: GCC, the GNU Compiler Collection, has a major version released each
  year. Once a release branch is created (like `releases/gcc-16`), it is frozen. This
  means that any changes to the code must be approved by the release manager. This
  process ensures the stability of the release.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aejhdeMRLLBGea1Y@tucnak
bugzilla_url: null
date: '2026-04-22'
---

Jakub Jelinek reports that the GCC 16 branch is frozen for release. All changes on the releases/gcc-16 branch now require release manager approval. Alice Carlotti asks if some bug fixes and improvements pushed to master after the branch are OK for the branch now.
