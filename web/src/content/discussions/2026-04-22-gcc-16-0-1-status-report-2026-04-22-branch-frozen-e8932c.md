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
tldr: The GCC 16 branch is frozen for release; changes require release manager approval.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Announces that the GCC 16 branch is frozen for release and all changes
    require release manager approval.
  quote: 'We have branched for the GCC 16 release.  All changes on the releases/gcc-16

    branch require release manager approval now.'
- author: Alice Carlotti
  role: other
  position: Asks whether recently pushed bug fixes and improvements to master are
    suitable for backport to the branch.
  quote: 'I pushed some bug fixes to master just after the branch.  There are 7 commits

    in total; two bug fixes, one testsuite fix, and four miscellaneous

    improvements.  Are they ok for the branch now, or do I need to wait until after

    the release?'
- author: Jakub Jelinek
  role: other
  position: Suggests creating a separate thread to discuss backporting the commits.
  quote: let's discuss those on a separate thread please.
- author: Alice Carlotti
  role: other
  position: Acknowledges and will create a separate thread.
  quote: '> let''s discuss those on a separate thread please.


    Ok, I''ll do that.'
primer_expert: Branch freezing indicates that the development branch for GCC 16 is
  now in the final stages of preparation for release. Only critical bug fixes are
  allowed, and they require approval from the release manager. This ensures stability
  for the upcoming release.
primer_general: This report indicates that the upcoming release of GCC 16 is nearing
  completion. The 'branch' is a specific version of the code being prepared for release.
  'Freezing' the branch means that only essential bug fixes will be applied, ensuring
  a stable release. Any further changes require approval from the release manager.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aejhdeMRLLBGea1Y@tucnak
bugzilla_url: null
date: '2026-04-22'
---

Jakub Jelinek reports that the GCC 16 branch has been frozen for release. All changes to the releases/gcc-16 branch now require release manager approval. Bug fixes are still being addressed.
