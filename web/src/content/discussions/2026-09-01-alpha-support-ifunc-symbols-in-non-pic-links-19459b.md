---
project: binutils
subsystem: alpha
patch_id: null
tags:
- binutils
- alpha
- linker
- IFUNC
- PIC
discussion_id: 20260901023318.3503991-8-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 07/11] alpha: support IFUNC symbols in non-PIC links'
headline: 'alpha: support IFUNC symbols in non-PIC links'
tldr: Enables IFUNC symbol support in non-Position-Independent Code (PIC) links on
  Alpha.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables IFUNC support in a wider range of link scenarios.
- Introduces a new section (`.rela.iplt`) and associated processing logic.
exchanges: []
primer_expert: This patch enables IFUNC symbol support in non-PIC links for Alpha
  by introducing the `.rela.iplt` section. In PIC links, `R_ALPHA_IRELATIVE` relocations
  are used, but non-PIC links did not have a corresponding mechanism. This change
  ensures that IFUNC references in non-PIC executables are placed in `.rela.iplt`,
  which is processed by `ld.so` or libc startup. It also refines the sizing of `.rela.iplt`
  to be exact and handles the marking of GOT entries during relaxation, ensuring correct
  IFUNC resolution in static executables.
primer_glossary:
- term: IFUNC
  definition: Indirect Function. A mechanism allowing functions to be resolved at
    runtime, often used for performance optimization or selecting architecture-specific
    implementations.
- term: non-PIC links
  definition: Linker operations that produce Position-Dependent Code, where addresses
    are fixed relative to the program's base.
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and run at any memory
    address without modification.
- term: dynamic relocation
  definition: A relocation entry that is processed by the dynamic linker at runtime
    to resolve symbols or fix addresses in shared libraries or dynamically linked
    executables.
- term: .rela.iplt
  definition: A section in an ELF object file that holds relocation entries for the
    Indirect Procedure Linkage Table, used for resolving IFUNCs.
- term: GOT
  definition: Global Offset Table. A table used in position-independent code to store
    addresses of functions and global variables, enabling indirect access.
series_id: 'binutils:alpha: support ifunc symbols in non-pic links'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-8-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch enables support for indirect function (IFUNC) symbols in non-PIC (Position-Independent Code) links on the Alpha architecture. Previously, non-PIC links lacked a mechanism to reserve dynamic relocations for IFUNCs, leading to failures. This change introduces a new `.rela.iplt` section to store these relocations, ensuring they are correctly processed by the dynamic linker (`ld.so`) or the C library's startup code, thereby allowing IFUNCs to function in static executables.
