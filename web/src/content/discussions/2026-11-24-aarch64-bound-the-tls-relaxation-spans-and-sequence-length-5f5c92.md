---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- tls
- security
- elf
- binutils
discussion_id: 20261124073127.3003048-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 2/2] aarch64: bound the TLS relaxation spans and sequence length'
headline: 'aarch64: bound the TLS relaxation spans and sequence length'
tldr: Binutils AArch64 TLS relaxation now validates spans and sequence lengths to
  prevent out-of-bounds access.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enhances security by preventing out-of-bounds memory access during TLS relaxation.
- Adds runtime checks for TLS relaxation, which might have a minor performance impact.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes bounding TLS relaxation spans and sequence lengths in AArch64
    ELF.
  quote: 'elfNN_aarch64_tls_relax rewrites a fixed instruction sequence at the

    relocation offset.  The sequence is up to 20 octets, wider than the

    howto size, and the GD and TLSDESC transitions read the following one

    or two relocations.  A crafted object could place such a relocation

    near the end of a short section, or leave the sequence truncated, and

    the linker wrote past the section contents or read pas…'
primer_expert: This is the second patch in a series for binutils' AArch64 ELF backend,
  focusing on Thread-Local Storage (TLS) relaxation. The `elfNN_aarch64_tls_relax`
  function rewrites instruction sequences which can be larger than the standard relocation
  size. This patch adds crucial bounds checking to ensure that the rewritten sequence,
  and the subsequent relocations it might need to read, do not extend beyond the section's
  boundaries. This prevents memory corruption on malformed inputs, improving robustness
  and security. It replaces a weak `BFD_ASSERT` with a proper error return.
primer_glossary:
- term: TLS
  definition: Thread-Local Storage, a mechanism allowing each thread in a process
    to have its own private copy of a variable.
- term: relaxation
  definition: An optimization process where the linker adjusts code or data references,
    often to create position-independent code or to enable specific features like
    TLS.
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries.
- term: relocation
  definition: A placeholder in object code that specifies how to modify an address
    or symbol reference when linking.
- term: howto
  definition: Describes how a relocation should be applied, including the size of
    the field being modified.
- term: GD
  definition: General Dynamic, a TLS model providing access to thread-local variables
    via a GOT.
- term: TLSDESC
  definition: TLS Descriptor, a mechanism used in some ABIs for accessing thread-local
    variables, often involving an indirection through a descriptor structure.
- term: BFD_ASSERT
  definition: A macro used in the BFD library for internal assertions; if it fails,
    it typically terminates the program.
series_id: 'binutils:aarch64: bound the tls relaxation spans and sequence length'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261124073127.3003048-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch enhances binutils' AArch64 ELF support by adding checks for Thread-Local Storage (TLS) relaxation. It validates that the written span does not exceed section limits and that required relocation sequences are present, preventing out-of-bounds writes and reads caused by crafted objects.
