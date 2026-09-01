---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- relocation
- ifunc
- dynamic linking
discussion_id: 20260901023318.3503991-4-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 03/11] alpha: allocate R_ALPHA_IRELATIVE'
headline: 'alpha: allocate R_ALPHA_IRELATIVE'
tldr: Define the R_ALPHA_IRELATIVE relocation type for the Alpha architecture.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces a new relocation type necessary for IFUNC support.
- Requires synchronization with the corresponding glibc definition.
exchanges: []
primer_expert: This patch allocates and defines the `R_ALPHA_IRELATIVE` relocation
  type for the Alpha ELF target. This relocation is specifically designed for IFUNCs
  (Indirect Functions), enabling the dynamic linker or C library startup code to resolve
  the IFUNC's target address at runtime and update a 64-bit field with it. The patch
  assigns it the next available relocation number (42) and integrates it into the
  BFD relocation mapping, aligning with similar definitions in other targets and a
  corresponding glibc change.
primer_glossary:
- term: R_ALPHA_IRELATIVE
  definition: An Alpha ELF relocation type used in dynamic linking to calculate the
    final address of a symbol by adding the load address of the shared object to the
    symbol's addend. For IFUNCs, it stores the address returned by the resolver.
- term: IFUNC
  definition: Indirect Function. A mechanism allowing a symbol to resolve to different
    function implementations at runtime, typically chosen by a resolver function.
    Similar to a function pointer but resolved at link or load time.
- term: dynamic linking
  definition: The process where the operating system or a dynamic linker resolves
    external references and loads shared libraries at runtime.
- term: static executable
  definition: An executable file that contains all necessary library code within itself,
    not requiring separate shared libraries to run.
- term: BFD
  definition: Binary File Descriptor. A library used by GNU Binutils to provide a
    generic interface to various executable file formats.
series_id: 'binutils:alpha: allocate r_alpha_irelative'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-4-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch introduces the R_ALPHA_IRELATIVE relocation type for the Alpha architecture, assigning it the value 42. This relocation is crucial for dynamic linking and static executables, as it allows the dynamic linker or C library startup code to execute an IFUNC's resolver and store the returned address. The patch also adds the necessary entry to the BFD relocation map and defines the relocation's class, preparing for linker support that will generate this relocation.
