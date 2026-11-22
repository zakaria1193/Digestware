---
project: binutils
subsystem: ia64
patch_id: null
tags:
- ia64
- linker
- relocation
- assertion
- musl
discussion_id: 2b362474-918e-440f-8fe6-d7306c3072ca@web.de
source_type: public_inbox
title: '[PATCH] ia64: Fix .rela.got sizing for __ehdr_start during relaxation'
headline: 'ia64: Fix .rela.got sizing for __ehdr_start during relaxation'
tldr: Fixes a BFD assertion failure in the IA-64 backend when linking musl libc due
  to incorrect .rela.got section sizing.
proposer: Frank Scheiner <frank.scheiner@web.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Aims to fix a specific assertion failure with minimal code change.
- Potential for unintended side effects on other linking scenarios if the state management
  fix is not comprehensive.
exchanges: []
primer_expert: The IA-64 ELF backend in binutils' BFD library experiences an assertion
  failure (`elfnn-ia64.c:3238`) during the linking of dynamic libraries, specifically
  when handling the linker-defined symbol `__ehdr_start`. This is caused by an undersized
  `.rela.got` section due to a discrepancy in how symbol states are managed across
  different sizing passes within the relaxation process. The patch aims to synchronize
  these states to ensure correct `.rela.got` section sizing.
primer_glossary:
- term: IA-64
  definition: Intel's 64-bit instruction set architecture, also known as Itanium.
- term: .rela.got
  definition: A section in an ELF object file that contains relocation entries for
    the Global Offset Table (GOT), used for dynamic linking.
- term: __ehdr_start
  definition: A linker-defined symbol that typically points to the beginning of the
    ELF header in an executable or shared library.
- term: Relaxation
  definition: A linking process where the linker adjusts addresses and offsets of
    instructions and data after initial assembly, often to support position-independent
    code or specific architectural features.
- term: BFD
  definition: Binary File Descriptor library, used by GNU Binutils.
- term: musl libc
  definition: A lightweight C standard library designed for embedded systems and high-performance
    computing.
- term: Assertion failure
  definition: A condition detected during program execution that violates a logical
    assertion, often indicating a bug.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2b362474-918e-440f-8fe6-d7306c3072ca@web.de
bugzilla_url: null
date: '2026-11-21'
is_stub: false
stub_reason: ''
---

This patch addresses a BFD assertion failure in the IA-64 backend related to the sizing of the `.rela.got` section when processing the `__ehdr_start` symbol during relaxation. This issue was encountered while porting musl to IA-64. The fix adjusts the symbol state management to resolve a mismatch between different sizing passes, enabling a successful dynamic build of musl for IA-64. The patch was tested on real hardware.
