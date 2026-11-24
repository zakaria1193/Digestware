---
project: binutils
subsystem: arm
patch_id: null
tags:
- arm
- security
- relocation
- elf
- binutils
discussion_id: 20261124080017.3387430-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/2] arm: reject a relocation whose field lies outside the section'
headline: 'arm: reject a relocation whose field lies outside the section'
tldr: Binutils ARM ELF support now rejects relocations with fields outside section
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
    section boundaries.
  quote: 'elf32_arm_relocate_section applied each relocation without checking that

    the relocated field lies inside the section, so a crafted object with a

    bad r_offset made the linker read and write past the section contents.

    elf64-x86-64.c and elf32-i386.c already range-check.'
primer_expert: This is the first patch in a series addressing security issues in binutils'
  ARM ELF processing. It introduces a critical bounds check at the beginning of the
  relocation loop within `elf32_arm_relocate_section`. This ensures that the memory
  range accessed by a relocation (considering potentially wider fields than the basic
  howto size for certain Thumb and ARM instructions) is fully contained within the
  section. This prevents heap-buffer-overflows and other memory corruption when processing
  malformed object files, aligning with checks already present in x86 ELF backends.
primer_glossary:
- term: relocation
  definition: A placeholder in object code that specifies how to modify an address
    or symbol reference when linking.
- term: r_offset
  definition: The offset within the section where the relocation is to be applied.
- term: position-independent code
  definition: Code that can be loaded and executed at any memory address without modification.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library, used by binutils to handle various object
    file formats.
- term: howto
  definition: Describes how a relocation should be applied, including the size of
    the field being modified.
- term: R_ARM_THM_BF16
  definition: An ARM relocation type for Thumb instructions, potentially affecting
    16 bits.
- term: R_ARM_LDR_PC_G0
  definition: An ARM relocation type for load instructions relative to the program
    counter.
- term: R_ARM_NONE
  definition: A relocation type that indicates no operation is needed.
series_id: 'binutils:arm: reject a relocation whose field lies outside the section'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261124080017.3387430-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch modifies binutils' ARM ELF handling to reject relocations where the accessed field falls outside the section boundaries. This prevents crafted objects from causing the linker to read or write past section contents, addressing a security vulnerability.
