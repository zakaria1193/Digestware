---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- ld
- hppa
- hpux
- testsuite
discussion_id: ahNbZYyU-pwmC6oe@mx3210.local
source_type: public_inbox
title: '[COMMITTED] hppa*64*-*-hpux*: Create dummy milli.a archive for binutils and
  ld tests'
headline: 'hppa*64*-*-hpux*: Create dummy milli.a archive for binutils and ld tests'
tldr: A dummy milli.a archive is created for hppa*64*-*-hpux* to fix test failures
  due to missing or undefined symbols.
proposer: John David Anglin <dave.anglin@bell.net>
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The change to objcopy.exp causes the "objcopy executable (pr25662)" test to fail,
  but this test did not execute successfully previously due to the missing archive.
exchanges:
- author: John David Anglin <dave.anglin@bell.net>
  role: proposer
  position: Committed a change to create a dummy milli.a archive for hppa*64*-*-hpux*
    to fix test failures.
  quote: null
primer_expert: This commit modifies the binutils and ld testsuites to create a dummy
  ``milli.a`` archive for the ``hppa*64*-*-hpux*`` target. This fixes test failures
  related to the missing or undefined symbols in the HP's ``milli.a`` archive. The
  changes involve modifications to ``objcopy.exp`` and ``default.exp`` to include
  LDFLAGS and create the dummy archive.
primer_general: The binutils and ld are essential tools for compiling and linking
  programs.  Their testsuites ensure correct functionality across different platforms.
  This commit addresses test failures on the HP-UX platform by creating a placeholder
  archive, ensuring the testsuite can run without relying on a specific system library.
  This improves the portability and reliability of the toolchain build process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahNbZYyU-pwmC6oe@mx3210.local
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This commit introduces a dummy ``milli.a`` archive for the ``hppa*64*-*-hpux*`` target in binutils and ld testsuites. This resolves test failures that occurred during cross-building due to the archive not being found.  It also addresses undefined symbol errors on ``hppa*64*-*-hpux*`` systems. The change modifies the ``objcopy.exp`` test to include LDFLAGS for the new archive.
