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
discussion_id: 20261124073127.3003048-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/2] aarch64: reject a relocation whose field lies outside the section'
headline: 'aarch64: reject a relocation whose field lies outside the section'
tldr: Binutils AArch64 ELF support now rejects relocations with fields outside section
  bounds.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enhances security by preventing out-of-bounds memory access.
- Adds a check at the beginning of the relocation loop, potentially impacting performance
  slightly for valid inputs.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes adding checks to reject relocations whose fields lie outside
    section boundaries in AArch64 ELF.
  quote: 'elfNN_aarch64_relocate_section applied each relocation without checking

    that the relocated field lies inside the section, so a crafted object

    with a bad r_offset made the linker read and write past the section

    contents.  elf64-x86-64.c and elf32-i386.c already range-check.'
primer_expert: This is the first patch in a series addressing security issues in binutils'
  AArch64 ELF processing. It introduces a bounds check at the start of the relocation
  loop in `elfNN_aarch64_relocate_section`. This check ensures that the memory location
  targeted by a relocation, considering its potentially wider write size (e.g., for
  64-bit writes like `R_AARCH64_TLS_DTPREL`), is fully within the section's limits.
  This prevents heap overflows and other memory corruption when processing malformed
  object files, aligning with checks in other backends like x86. The patch also adds
  tests to verify this be…
primer_glossary:
- term: relocation
  definition: A placeholder in object code that specifies how to modify an address
    or symbol reference when linking.
- term: r_offset
  definition: The offset within the section where the relocation is to be applied.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: heap-buffer-overflow
  definition: A type of buffer overflow where the overflow occurs in dynamically allocated
    memory (the heap).
- term: R_AARCH64_TLS_DTPREL
  definition: An AArch64 relocation type used for Thread-Local Storage (TLS) data
    access.
- term: bfd_put_64
  definition: A BFD library function to write a 64-bit value to a file.
- term: R_AARCH64_NONE
  definition: An AArch64 relocation type that indicates no operation is needed.
series_id: 'binutils:aarch64: reject a relocation whose field lies outside the section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261124073127.3003048-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch modifies binutils' AArch64 ELF handling to reject relocations where the accessed field falls outside the section boundaries. This prevents crafted objects from causing the linker to read or write past section contents, addressing a security vulnerability.
