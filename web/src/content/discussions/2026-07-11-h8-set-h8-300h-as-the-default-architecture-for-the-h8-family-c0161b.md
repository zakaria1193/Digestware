---
project: binutils
subsystem: h8
patch_id: null
tags:
- H8
- microcontroller
- default architecture
- binutils
- embedded
discussion_id: 20260711005357.744443-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH v3 1/2] H8: Set H8/300H as the default architecture for the H8 family'
headline: 'H8: Set H8/300H as the default architecture for the H8 family'
tldr: Sets H8/300H as the default architecture for the H8 family in binutils.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Simplifies toolchain configuration for H8/300H users by making it the default.
- Might require users targeting the older H8/300 to explicitly specify it, potentially
  breaking older build scripts if not updated.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Proposes setting H8/300H as the default architecture for the H8 family
    across BFD, gas, and ld, updating configuration and NEWS files accordingly. This
    is presented as a follow-up to a previous discussion.
  quote: "This patch sets H8/300H as the default architecture for the H8 family. More\n\
    info in the previous thread.\n\nbfd/ChangeLog:\n\n\t* cpu-h8300.c: Set H8/300H\
    \ as the default architecture\n\tfor the H8 family.\n\ngas/ChangeLog:\n\n\t* config/tc-h8300.c:\
    \ Set H8/300H as the default architecture\n\tfor the H8 family.\n\t* NEWS: Added\
    \ info about the above change.\n\nld/ChangeLog:\n\n\t* configure.tgt: Set H8/300H\
    \ as the defau…"
primer_expert: This patch series updates the binutils toolchain for the Renesas H8
  microcontroller family. Specifically, it changes the default architecture from H8/300
  to H8/300H. This impacts how the assembler, linker, and BFD library configure themselves
  when targeting H8 platforms. The H8/300H variant offers more advanced features,
  including a 32-bit address space in its default advanced mode, compared to the H8/300's
  16-bit default. The change also necessitates updates to test suites.
primer_glossary:
- term: H8/300H
  definition: A specific microcontroller variant in the Renesas H8 family, characterized
    by its 32-bit internal architecture and addressing capabilities, often used in
    embedded systems.
- term: H8/300
  definition: An earlier and simpler variant of the Renesas H8 microcontroller family,
    typically operating with a 16-bit address space in its default configuration.
- term: binutils
  definition: A collection of programming tools, including the assembler (as), linker
    (ld), and binary file descriptor library (BFD), used for handling object files
    and executable code.
- term: BFD (Binary File Descriptor)
  definition: A library within binutils that provides a consistent interface for reading,
    writing, and manipulating various object file formats (e.g., ELF, COFF).
- term: gas
  definition: The GNU Assembler, part of binutils. It translates assembly language
    into machine code.
- term: ld
  definition: The GNU linker, part of binutils. It combines object files and libraries
    into an executable or library.
- term: configure.tgt
  definition: A configuration file used by the linker to define target-specific settings
    and architectures.
- term: NEWS file
  definition: A file in many projects that summarizes user-visible changes and new
    features in each release.
series_id: 'binutils:h8: set h8/300h as the default architecture for the h8 family'
series_role: reply
series_parts:
- title: 'H8: Set H8/300H as the default architecture for the H8 family'
  url: https://inbox.sourceware.org/binutils/48480d9c-958a-4985-8ccd-1b389cdd8571@o2.pl
  n: 1
  total: 2
- title: 'H8: Set H8/300H as the default architecture for the H8 family'
  url: https://inbox.sourceware.org/binutils/alF-KqRJviBRU6px@squeak.grove.modra.org
  n: 1
  total: 2
- title: 'H8: Set H8/300H as the default architecture for the H8 family'
  url: https://inbox.sourceware.org/binutils/20260710145551.744408-1-jdx@o2.pl
  n: 1
  total: 2
url: https://inbox.sourceware.org/binutils/20260711005357.744443-1-jdx@o2.pl
bugzilla_url: null
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

This patch changes the default architecture for the H8 family of processors within the binutils toolchain to H8/300H. The change affects binutils' BFD, gas, and ld components, updating their respective configuration and documentation files to reflect the new default. The aim is to streamline the build process for users targeting H8/300H by making it the out-of-the-box setting.
