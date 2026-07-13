---
project: binutils
subsystem: arm
patch_id: null
tags:
- arm
- binutils
- bfd
- bugfix
- warning
discussion_id: alOPx1A3Abg0my_B@squeak.grove.modra.org
source_type: public_inbox
title: 'arm: remove stray backslash in warning message'
headline: 'arm: remove stray backslash in warning message'
tldr: Fixes a stray backslash in an ARM build warning message in binutils.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Fixes a syntax error in a printf-style format string used for a warning
  message in bfd/elf32-arm.c. The stray backslash likely affected message formatting
  or localization. This corrects an issue introduced by an older commit.
primer_glossary:
- term: binutils
  definition: A set of programming tools for manipulating binary files, including
    the GNU Assembler (gas), GNU linker (ld), and the Binary File Descriptor library
    (BFD).
- term: BFD
  definition: The Binary File Descriptor library, a crucial component of GNU Binutils
    that provides a common interface for reading and writing various object file formats.
- term: arm
  definition: A family of reduced instruction set computing (RISC) architectures for
    computer processors, widely used in mobile devices and embedded systems.
- term: backslash
  definition: A typographical character (\) often used in computing to escape special
    characters or denote directory separators.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alOPx1A3Abg0my_B@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-12'
is_stub: false
stub_reason: ''
---

This patch corrects a stray backslash in an ARM-specific warning message within binutils' BFD library. The error was introduced in 2004 and could potentially affect how warning messages are displayed or parsed. The fix is a minor correction to the error formatting string.
