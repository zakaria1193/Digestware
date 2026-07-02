---
project: binutils
subsystem: binutils
patch_id: null
tags:
- release management
- binutils
- schedule
- bug fixes
- feature freeze
discussion_id: 87h5mvym74.fsf@redhat.com
source_type: public_inbox
title: Upcoming 2.47 branch and release dates
headline: Upcoming 2.47 branch and release dates
tldr: The Binutils 2.47 release is planned for July 25th, with branching on July 11th,
  urging any critical fixes or features to be submitted soon.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 5
technical_tradeoffs:
- Strict release dates can lead to rushed feature integration or delayed bug fixes
  if they are not ready by the deadline.
- Flexibility in release dates offers more time for stabilization but can delay the
  delivery of new features or critical bug fixes to users.
- The trade-off between release stability (fewer changes after branching) and the
  inclusion of last-minute important features/fixes.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Announces the schedule for the Binutils 2.47 release, with the branching
    date on July 11th and the release date on July 25th. He urges developers to get
    any important fixes or features in before these dates, while noting that the dates
    are adjustable if absolutely necessary.
  quote: "The time for the 2.47 release is coming up fast. My current plans are:\n\
    \n Create the branch: Sat 11 July\n Create the release: Sat 25 July\n\nSo now\
    \ is the time to get any important fixes or features in..."
- author: H.J. Lu
  role: reviewer
  position: Requests review of a specific fix for a known bug in light of the approaching
    release deadline, indicating that critical bug fixes are still in progress.
  quote: 'Can you review the fix


    https://sourceware.org/pipermail/binutils/2026-June/149706.html


    for


    https://sourceware.org/bugzilla/show_bug.cgi?id=34184'
primer_expert: Binutils releases, like other large FOSS projects, operate on a time-boxed
  schedule. This means developers synchronize their work around specific branching
  and release dates. The 'branch' refers to creating a stable codebase from the main
  development trunk (often 'HEAD' or 'master') for final stabilization before a release.
  Once branched, only cherry-picked critical bug fixes are usually allowed, as new
  features or disruptive changes are deferred to the next development cycle. This
  process ensures release quality, but also imposes a time pressure for developers
  to land their changes.
primer_general: Binutils is a collection of tools used by programmers to create and
  manage executable programs, libraries, and other software components. This includes
  tools like `as` (the assembler), `ld` (the linker), and `objdump` (for inspecting
  objects). Like many large software projects, Binutils releases new versions periodically
  to add features, fix bugs, and improve performance. This discussion announces the
  schedule for an upcoming release (version 2.47), including when the development
  team will 'branch' the code (create a stable version for final testing) and when
  the official release will happen. This is important for all developers because it
  sets a deadline for any new features or bug fixes they want to include in this specific
  version of Binutils. Missing the deadline means their changes will have to wait
  for a future release.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87h5mvym74.fsf@redhat.com
bugzilla_url: null
date: '2026-06-22'
is_stub: false
---

Nick Clifton announced the upcoming release schedule for Binutils 2.47, with the branch creation slated for July 11th and the official release for July 25th. This tight deadline means developers have a limited window to submit important fixes or new features. H.J. Lu responded by requesting a review of a specific fix for a bug, indicating that development work is still active and urgent given the impending release. The hard deadline for new features and critical fixes means developers must prioritize their current work to ensure inclusion in this release.
