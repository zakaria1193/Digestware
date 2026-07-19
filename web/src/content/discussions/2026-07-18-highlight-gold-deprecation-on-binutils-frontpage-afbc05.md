---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- website
- documentation
- linker
- gold
discussion_id: B919DAA9-6853-4962-B785-177EBD3C50FA@itkaufmann.at
source_type: public_inbox
title: Highlight gold deprecation on binutils frontpage
headline: Highlight gold deprecation on binutils frontpage
tldr: Suggest updating the binutils website to reflect gold linker's deprecation.
proposer: Mindy Batek <m.batek+all-hail-stallman@itkaufmann.at>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Mindy Batek <m.batek+all-hail-stallman@itkaufmann.at>
  role: proposer
  position: Requests that the Binutils website be updated to accurately represent
    the status of the gold linker, noting its deprecation and removal from releases.
  quote: null
primer_expert: The GNU Binutils project maintains a website that historically promoted
  its 'gold' linker as a modern alternative. This discussion concerns updating that
  public-facing information to be accurate, as 'gold' is no longer actively maintained
  or included in recent versions of the Binutils suite.
primer_glossary:
- term: GNU Binutils
  definition: A collection of programming tools for manipulating binary and object
    files, including the assembler (as), linker (ld), and binary file manipulator
    (objdump).
- term: gold linker
  definition: A high-performance linker developed by the GNU toolchain project, intended
    as a replacement for the traditional (bfd) linker.
- term: deprecated
  definition: Software or a feature that is no longer recommended for use, often indicating
    that it will be removed in future versions. Support may be limited or non-existent.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/B919DAA9-6853-4962-B785-177EBD3C50FA@itkaufmann.at
bugzilla_url: null
date: '2026-07-18'
is_stub: false
stub_reason: ''
---

Mindy Batek points out that the GNU Binutils webpage still advertises 'gold' as a new, faster linker, despite it being deprecated and excluded from many releases. This is misleading for users who might still consider using it.
