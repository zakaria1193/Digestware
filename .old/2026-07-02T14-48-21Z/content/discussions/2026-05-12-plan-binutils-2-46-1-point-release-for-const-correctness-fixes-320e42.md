---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- release
- const correctness
- c23
- glibc
discussion_id: 87o6ilgdrj.fsf@gentoo.org
source_type: public_inbox
title: Planned binutils-2.46.1 release
headline: Plan binutils-2.46.1 point release for const-correctness fixes.
tldr: Sam James plans a binutils-2.46.1 release to address C23/glibc-2.43 const correctness
  issues and asks for other fixes to backport.
proposer: Sam James <sam@gentoo.org>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Backporting fixes carries the risk of introducing regressions.
- Failing to backport necessary fixes can lead to build failures with newer toolchains.
exchanges:
- author: Sam James <sam@gentoo.org>
  role: proposer
  position: Proposes a point release for binutils-2.46 to address const correctness
    issues and asks for other fixes to be backported.
  quote: I plan to make a point release for binutils-2.46 in a few days, motivated
    by the C23/glibc-2.43 fixes for const correctness, as the 2.46 release fails to
    build w/ -Werror enabled by default
primer_expert: Binutils is a collection of binary tools like the linker and assembler.  Point
  releases address bug fixes and minor issues.  C23 and glibc-2.43 introduce changes
  to const correctness that can cause build failures if not addressed in binutils.
primer_general: Binutils provides essential tools for working with binary files, including
  the linker (which combines compiled code into executables) and the assembler (which
  translates assembly language into machine code). This discussion concerns a minor
  update to address compatibility issues with newer versions of the C language and
  the standard C library (glibc).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87o6ilgdrj.fsf@gentoo.org
bugzilla_url: null
date: '2026-05-12'
is_stub: false
---

Sam James announces plans for a binutils-2.46.1 point release to address build failures with -Werror due to C23/glibc-2.43 const correctness changes.  The release will include fixes for PR34028, PR34088, and PR34125, and solicits input on other fixes to backport.
