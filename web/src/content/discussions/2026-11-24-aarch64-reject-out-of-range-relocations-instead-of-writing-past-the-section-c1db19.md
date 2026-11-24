---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- security
- relocation
- elf
- binutils
discussion_id: 20261124073127.3003048-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/2] aarch64: reject out-of-range relocations instead of writing past
  the section'
headline: 'aarch64: reject out-of-range relocations instead of writing past the section'
tldr: Binutils AArch64 ELF support now rejects relocations with fields outside section
  bounds and validates TLS relaxation spans.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: ready
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Addresses critical security vulnerabilities related to out-of-bounds memory access
  in AArch64 ELF processing.
- Implements a per-backend solution, which is more targeted but less generic than
  a wholly-backend-agnostic approach.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes a series of patches to reject out-of-range relocations and validate
    TLS relaxation spans in AArch64 ELF.
  quote: 'elfNN_aarch64_relocate_section and elfNN_aarch64_tls_relax write into

    the section contents at the relocation offset without checking that the

    field, or the relaxed instruction sequence, lies inside the section.

    A crafted object can make ld read and write past the section.'
primer_expert: This cover letter introduces a two-patch series for binutils' AArch64
  ELF backend, addressing security concerns related to out-of-bounds memory access.
  The patches implement per-backend checks similar to those in x86 ELF backends. Patch
  1 adds a check to `elfNN_aarch64_relocate_section` to ensure relocation fields,
  considering their actual write size, are within section bounds, preventing heap
  overflows. Patch 2 focuses on TLS relaxation, adding checks to `elfNN_aarch64_tls_relax`
  to ensure that the rewritten instruction sequences and subsequent relocation reads
  do not go out of bounds. This…
primer_glossary:
- term: AddressSanitizer
  definition: A memory error detector for C/C++ that finds use-after-free, buffer
    overflows, and other memory safety issues.
- term: relocation
  definition: A placeholder in object code that specifies how to modify an address
    or symbol reference when linking.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: TLS
  definition: Thread-Local Storage, a mechanism allowing each thread in a process
    to have its own private copy of a variable.
- term: relaxation
  definition: An optimization process where the linker adjusts code or data references,
    often to create position-independent code or to enable specific features like
    TLS.
- term: heap-buffer-overflow
  definition: A type of buffer overflow where the overflow occurs in dynamically allocated
    memory (the heap).
- term: R_AARCH64_TLS_DTPREL
  definition: An AArch64 relocation type used for Thread-Local Storage (TLS) data
    access.
series_id: 'binutils:aarch64: reject out-of-range relocations instead of writing past
  the section'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261124073127.3003048-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This series addresses security vulnerabilities in binutils' AArch64 ELF handling by adding bounds checks for relocations and TLS relaxation. The first patch rejects relocations whose fields lie outside section boundaries, and the second patch validates TLS relaxation spans and sequence lengths. These changes prevent out-of-bounds reads and writes on crafted objects.
