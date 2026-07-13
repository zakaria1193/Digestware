---
project: binutils
subsystem: binutils
patch_id: null
tags:
- release
- binutils
- release-management
- bugfix
discussion_id: 8733xoedw1.fsf@redhat.com
source_type: public_inbox
title: The 2.47 release branch has been created
headline: The 2.47 release branch has been created
tldr: The binutils 2.47 release branch is now open for bug fixes and translations,
  aiming for a July 26th release.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs: []
exchanges:
- author: Nick Clifton
  role: proposer
  position: Announces the creation of the binutils 2.47 release branch, defines criteria
    for accepted patches (bug fixes, translations, documentation), and sets a target
    release date. Requires patch review.
  quote: "The 2.47 branch has now been created:\n\n     git clone git://sourceware.org/git/binutils-gdb.git\
    \ -b binutils-2_47-branch\n\n   A snapshot of the sources is also available here:\n\
    \n     https://sourceware.org/pub/binutils/snapshots/binutils-2.46.90.tar.xz\n\
    \n   Please could all patches for the branch be run by me.\n   The rules for the\
    \ branch are:\n\n     * No new features.\n     * Target specific bug fixes…"
- author: H.J. Lu
  role: reviewer
  position: Acknowledges the announcement and notes the rule that new features are
    not accepted, then quotes the proposer's text.
  quote: 'On Sun, Jul 12, 2026 at 5:50 PM Nick Clifton <nickc@redhat.com> wrote:


    > Hi Everyone,

    >

    > The 2.47 branch has now been created:

    >

    > git clone git://sourceware.org/git/binutils-gdb.git -b binutils-2_47-branch

    >

    > A snapshot of the sources is also available here:

    >

    > https://sourceware.org/pub/binutils/snapshots/binutils-2.46.90.tar.xz

    >

    > Please could all patches for the branch be run by me.

    > Th…'
primer_expert: Announcement of the creation of the `binutils-2_47-branch` for the
  upcoming Binutils 2.47 release. This branch is for critical bug fixes, documentation
  updates, and translations only; no new features are allowed. The release is targeted
  for July 26th, and all patches must be reviewed by Nick Clifton. The GOLD linker
  is not part of this release.
primer_glossary:
- term: Release branch
  definition: A specific version of source code maintained for releasing a stable
    version of software, typically receiving only bug fixes and critical updates.
- term: GOLD
  definition: An alternative linker to GNU ld, developed by the Android/Google team,
    known for its performance. It is not included in this particular binutils release.
- term: Snapshot
  definition: A version of the source code at a specific point in time, often provided
    as a tarball for easier download and use.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8733xoedw1.fsf@redhat.com
bugzilla_url: null
date: '2026-07-12'
is_stub: false
stub_reason: ''
---

Nick Clifton announces the creation of the binutils 2.47 release branch, providing git clone instructions and a link to the source snapshot. He outlines the rules for accepting patches (bug fixes, documentation, translations) and sets a target release date of July 26th. All patches require his review. The GOLD assembler is not included in this release.
