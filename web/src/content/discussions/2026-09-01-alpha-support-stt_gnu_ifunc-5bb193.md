---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- ifunc
- relocation
- elf
discussion_id: 20260901023318.3503991-1-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 00/11] alpha: support STT_GNU_IFUNC'
headline: 'alpha: support STT_GNU_IFUNC'
tldr: Adds support for GNU_IFUNC symbol type to the Alpha linker, enabling indirect
  function resolution.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enables support for a more advanced function resolution mechanism.
- Relies on future dynamic linker and C library support for full runtime functionality.
exchanges: []
primer_expert: This patch series enables the Alpha linker to fully support `STT_GNU_IFUNC`
  symbols. It introduces the necessary `R_ALPHA_IRELATIVE` relocation type (patch
  3) and modifies relocation handling for both PIC (patch 5) and non-PIC (patch 7)
  links to correctly capture the address returned by an IFUNC's resolver. The series
  also includes general code cleanup and preparation for IFUNC support. The immediate
  impact is minimal as dynamic linker and C library support are still developing,
  but it lays the groundwork for future IFUNC usage on Alpha.
primer_glossary:
- term: STT_GNU_IFUNC
  definition: A symbol type in the ELF format that represents an Indirect Function.
    An IFUNC symbol's resolved address is determined at runtime by a resolver function,
    allowing for platform-specific or optimized function implementations.
- term: IFUNC
  definition: Indirect Function. A mechanism allowing a symbol to resolve to different
    function implementations at runtime, typically chosen by a resolver function.
    Similar to a function pointer but resolved at link or load time.
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and run at any memory
    address without modification. Essential for shared libraries and modern executable
    security.
- term: R_ALPHA_IRELATIVE
  definition: An Alpha ELF relocation type used in dynamic linking to calculate the
    final address of a symbol by adding the load address of the shared object to the
    symbol's addend. For IFUNCs, it stores the address returned by the resolver.
- term: resolver
  definition: A function that determines the actual address of an IFUNC at runtime,
    often based on system characteristics.
series_id: 'binutils:alpha: support stt_gnu_ifunc'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-1-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This series of patches introduces support for `STT_GNU_IFUNC` (Indirect Functions) to the Alpha linker. This enables the linker to correctly handle IFUNCs, which allow a symbol to resolve to different function implementations at runtime based on a resolver. The changes include allocating the `R_ALPHA_IRELATIVE` relocation type, handling IFUNC references in PIC and non-PIC links, and ensuring compatibility with glibc. Until dynamic linker or C library support is widespread, existing binaries will continue to use the resolver's address, preventing regressions.
