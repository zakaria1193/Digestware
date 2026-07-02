---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- release
- backport
- bug fixes
discussion_id: agQ8EH3YIJ6C2dUs@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: Planned binutils-2.46.1 release'
headline: Planned binutils-2.46.1 release
tldr: Discussion about backporting fixes to the binutils-2.46 branch for an upcoming
  point release.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: other
  position: Offers opinion on backporting fuzzing and memory leak fixes, recommending
    against it unless it simplifies backporting other desired fixes.
  quote: 'As a general principle I don''t recommend backporting fuzzing fixes or

    "not freed before exit" type memory leak fixes, unless backporting

    them makes it a lot easier to backport some other wanted fix.'
primer_expert: This thread concerns the stabilization of binutils 2.46 via a point
  release (2.46.1). The discussion centers around which bug fixes should be backported
  from the development branch to the 2.46 branch.  sframe is a debugging data structure.
  The fixes address const correctness issues introduced by C23 and glibc 2.43.
primer_general: Binutils is a suite of tools for working with binary files, including
  the assembler, linker, and other utilities. A point release is a minor update to
  a software project that includes bug fixes and small improvements. Backporting involves
  applying changes from a newer version of software to an older, stable version.  This
  discussion is about deciding which bug fixes are important enough to include in
  a maintenance release of binutils.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/agQ8EH3YIJ6C2dUs@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-13'
is_stub: false
---

Sam James is planning a binutils-2.46.1 point release motivated by C23/glibc-2.43 fixes. The thread discusses backporting additional fixes, including one related to sframe version checking.  Alan Modra advises against backporting fuzzing fixes or memory leak fixes unless they significantly aid in backporting other desired fixes.
