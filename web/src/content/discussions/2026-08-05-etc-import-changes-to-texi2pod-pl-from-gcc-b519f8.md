---
project: binutils
subsystem: etc
patch_id: null
tags:
- documentation
- build
- scripting
- texinfo
- perl
discussion_id: 87v79olsxh.fsf@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] etc: import changes to texi2pod.pl from gcc'
headline: 'etc: import changes to texi2pod.pl from gcc'
tldr: Sync binutils' texi2pod.pl script with GCC's, adding @option and @table @option
  support.
proposer: Andrew Burgess <aburgess@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Importing GCC's script risks introducing GCC-specific behaviors or dependencies
  into binutils.
- Reverting GCC commit 386c402747d2bc6bad3e1bc2f9383d4d669576e0 might mask an underlying
  issue in GCC's texi2pod.pl that could surface later.
exchanges:
- author: Andrew Burgess <aburgess@redhat.com>
  role: proposer
  position: Proposes syncing binutils' texi2pod.pl with GCC's version to fix @option
    and @table @option formatting issues, incorporating local modifications.
  quote: 'I was looking at making some cleanup in the GDB documentation and I ran
    into a limitation of the texi2pod.pl script, it is not able to correctly format:
    ''@option{--text}'' or ''@table @option''.


    Patching our copy of texi2pod.pl is easy enough, but it is probably better to
    just sync with gcc''s version of the script, which already has some @option support
    in place.


    I took the version from gcc commit…'
primer_expert: This patch updates binutils' local copy of texi2pod.pl, a script used
  to convert Texinfo documentation to POD format for man pages. It imports changes
  from GCC's version to improve support for @option and @table within man pages, addressing
  specific formatting issues encountered in GDB documentation. Local adjustments were
  necessary to maintain compatibility with binutils' existing features and past commits.
primer_glossary:
- term: texi2pod.pl
  definition: A Perl script that converts Texinfo markup (used for documentation in
    GNU projects) into POD (Plain Old Documentation) format, commonly used for man
    pages.
- term: '@option'
  definition: A Texinfo command used to denote command-line options within documentation.
- term: '@table @option'
  definition: A Texinfo construct used to create a list of options, where each item
    is introduced by the @option command.
- term: man pages
  definition: Manual pages, the traditional documentation system on Unix-like operating
    systems, providing reference information about commands and utilities.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87v79olsxh.fsf@redhat.com
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

Andrew Burgess proposes syncing binutils' texi2pod.pl script with the version from GCC. This addresses limitations in formatting 
@option{--text} and @table @option, which were affecting GDB documentation cleanup. The imported GCC version required local adjustments to support --no-split, TARGET as a man page section, and to revert a GCC change that affected list formatting. Burgess also added trivial support for @table @option, which has been submitted to the GCC mailing list.
