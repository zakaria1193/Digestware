---
project: binutils
subsystem: binutils/aarch64
patch_id: null
tags:
- binutils
- aarch64
- cygwin
- cross-compilation
- target support
discussion_id: 20261029202614.37089-1-evgeny.karpov@arm.com
source_type: public_inbox
title: 'aarch64: Introduce aarch64-pc-cygwin target'
headline: 'aarch64: Introduce aarch64-pc-cygwin target'
tldr: Adds support for the aarch64-pc-cygwin target in binutils, enabling cross-compilation
  for AArch64 on Cygwin.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Increases the complexity of the build system configuration by adding a new target
  triplet. However, it is necessary to enable support for this platform.
exchanges:
- author: Evgeny Karpov
  role: proposer
  position: Proposes adding aarch64-pc-cygwin target support to binutils by updating
    configuration files.
  quote: 'The patch adds support for aarch64-pc-cygwin target.


    Co-authored-by: Radek Barton <radek.barton@microsoft.com>'
- author: Christophe Lyon
  role: reviewer
  position: Notes that the GDB-related changes require approval from GDB maintainers
    and suggests CCing gdb-patches.
  quote: 'I think the GDB parts need approval from GDB maintainers (thus cc''ing

    gdb-patches).


    Thanks'
primer_expert: This patch expands binutils' target support by adding the `aarch64-pc-cygwin`
  triplet. It modifies various configuration scripts (`configure.ac`, `config.bfd`,
  `ld/configure.tgt`, etc.) and linker emulation parameters to correctly identify
  and configure build systems for this target, which likely targets AArch64 processors
  running on the Cygwin POSIX compatibility layer on Windows.
primer_glossary:
- term: aarch64
  definition: The 64-bit ARM architecture. It is a popular instruction set for mobile
    devices and is increasingly used in servers and desktops.
- term: Cygwin
  definition: A POSIX-compatible environment that runs on Microsoft Windows. It provides
    a Unix-like API and command-line interface.
- term: BFD
  definition: Binary File Descriptor library. A library used by binutils to provide
    a common interface for handling various object file formats, including ELF.
- term: Cross-compilation
  definition: The process of compiling code on one system (the host) for execution
    on a different system (the target). This is common when developing for embedded
    systems or different architectures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029202614.37089-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch introduces support for the `aarch64-pc-cygwin` target within the binutils project. It modifies configuration files across BFD, binutils, gas, and ld to recognize and handle this new target, facilitating cross-compilation for AArch64 architecture on the Cygwin environment.
