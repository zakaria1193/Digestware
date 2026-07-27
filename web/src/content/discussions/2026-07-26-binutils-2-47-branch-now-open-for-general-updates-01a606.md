---
project: binutils
subsystem: binutils
patch_id: null
tags:
- release management
- workflow
- binutils
- contribution
discussion_id: 87ldaxy5by.fsf@redhat.com
source_type: public_inbox
title: The 2_47 branch is open for updating as normal
headline: Binutils 2.47 branch now open for general updates
tldr: The binutils-2_47 branch is now open for patching, allowing non-bugfix updates
  and routine changes.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Allows for more agile development and inclusion of improvements on the release branch.
- Potential for less review on non-bugfix changes compared to a main development branch.
- Decision on what gets included in point releases remains with maintainers.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: maintainer
  position: Announces that the `binutils-2_47` branch is open for general patching,
    removing the need for pre-approval and allowing non-bugfix updates.
  quote: 'The binutils-2_47-branch is now open for patching as normal.


    Ie, there is no more need to run patches by me first, and

    updates that are not bug fixes are allowed, although of

    course they may not reach the public unless there is a 2.47.1

    point release.'
primer_expert: This communication informs developers that the `2_47` release branch
  for Binutils is now open for contributions beyond just critical bug fixes. Developers
  can now push updates, including new features or improvements, directly to this branch
  without explicit pre-approval from the maintainer. However, the message clarifies
  that the integration of these non-bugfix changes into future public point releases
  is at the discretion of the release managers, implying that only significant or
  necessary updates will be backported.
primer_glossary:
- term: release branch
  definition: A stable branch in a version control system (like Git) that contains
    the code for a specific released version of software. Updates to release branches
    are typically restricted to bug fixes.
- term: patch
  definition: A set of changes to a software file intended to update or fix the program.
    In software development, patches are often submitted for review and inclusion
    into the main codebase.
- term: point release
  definition: A minor update to a software release, usually indicated by a change
    in the last digit of the version number (e.g., 2.47.1). Point releases are typically
    used to deliver bug fixes and security patches.
- term: binutils-2_47-branch
  definition: The specific Git branch used for the development and maintenance of
    Binutils version 2.47.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87ldaxy5by.fsf@redhat.com
bugzilla_url: null
date: '2026-07-26'
is_stub: false
stub_reason: ''
---

This message announces that the `binutils-2_47` branch is now open for standard updates. Developers no longer need to seek prior approval for patches, and updates that are not strictly bug fixes are permitted. However, it's noted that such non-bugfix changes might not be included in public releases unless a point release (e.g., 2.47.1) is made.
