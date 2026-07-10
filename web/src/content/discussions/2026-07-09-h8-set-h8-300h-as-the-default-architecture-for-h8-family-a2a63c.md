---
project: binutils
subsystem: h8
patch_id: null
tags:
- h8
- default architecture
- linker
- assembler
- gcc
discussion_id: 20260709210449.744366-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] H8: Set H8/300H as the default architecture for H8 family'
headline: 'H8: Set H8/300H as the default architecture for H8 family'
tldr: Changes the default H8 architecture in binutils from H8/300 to H8/300H to match
  GCC's default.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 9
technical_tradeoffs:
- Aligns binutils with GCC's default architecture, improving toolchain consistency.
- Resolves test case failures caused by architecture mismatches.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Proposes to set H8/300H as the default architecture for the H8 family
    in binutils to match GCC's default, resolving test case failures.
  quote: 'Binutils, in particular ld and gas, use H8/300 as the default architecture.
    On the other hand, support for H8/300 has been removed from gcc since July 2020
    (AFAIR) and H8/300H is the default there. This situation causes that about 30
    test cases fail in the following way:'
- author: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
  role: reviewer
  position: Agrees with the change, stating that it makes sense given GCC's removal
    of H8/300 support.
  quote: I'm a lot less involved in binutils than I have been in the past, but this
    makes sense to me. As Jan mentions, we dropped old H8/300 support in GCC a while
    back and default to
primer_expert: This change standardizes the default toolchain architecture for the
  H8 family. Binutils' `ld` and `gas` previously defaulted to H8/300, while GCC has
  since switched to H8/300H as its default. This patch synchronizes binutils to match
  GCC, resolving linker/assembler incompatibilities with modern H8/300H compilation
  targets and unblocking a number of test suite failures.
primer_glossary:
- term: H8/300
  definition: An older variant of the H8 microcontroller architecture.
- term: H8/300H
  definition: An enhanced variant of the H8 microcontroller architecture, often used
    as a default in modern toolchains.
- term: gcc
  definition: The GNU Compiler Collection, a widely used suite of compilers.
- term: binutils
  definition: A collection of programming tools, including the assembler (gas) and
    the linker (ld), for manipulating object code.
- term: linker (ld)
  definition: A program that takes one or more object files and combines them into
    a single executable file or library.
- term: assembler (gas)
  definition: A program that translates assembly language code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260709210449.744366-1-jdx@o2.pl
bugzilla_url: null
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

This patch updates binutils' default architecture for the H8 family from H8/300 to H8/300H. This change aligns binutils with GCC, which removed support for H8/300 and now defaults to H8/300H. The discrepancy caused approximately 30 test cases to fail due to incompatible architectures between the compiler output and the linker/assembler defaults. The change affects `bfd/cpu-h8300.c`, `gas/config/tc-h8300.c`, and `ld/configure.tgt`.
