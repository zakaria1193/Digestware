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
discussion_id: 20261124080017.3387430-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/2] arm: reject out-of-range relocations instead of reading and writing
  past the section'
headline: 'arm: reject out-of-range relocations instead of reading and writing past
  the section'
tldr: Binutils ARM ELF support now rejects relocations with fields outside section
  bounds and checks indirectly read instructions.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: ready
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Addresses critical security vulnerabilities related to out-of-bounds memory access
  in ARM ELF processing.
- Implements a per-backend solution, which is more targeted but less generic than
  a wholly-backend-agnostic approach.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes a series of patches to reject out-of-range relocations and validate
    indirectly read instructions in ARM ELF.
  quote: 'elf32_arm_relocate_section applies relocations at contents + r_offset

    without checking that the field lies inside the section, and three

    other paths read an instruction away from the field without checking

    it either.  A crafted object can make ld read and write past the

    section.'
primer_expert: This cover letter introduces a two-patch series for binutils' ARM ELF
  backend, aiming to mitigate security risks identified by AddressSanitizer. The core
  issue is that the linker, when processing ARM object files, would sometimes read
  or write past the defined section boundaries due to crafted relocation offsets or
  indirectly accessed instructions. Patch 1 implements a general bounds check for
  the relocation field itself, mirroring existing checks in other backends. Patch
  2 specifically addresses indirect reads of instructions by certain TLS and interworking
  relocations, ensuring those instru…
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
- term: ARM
  definition: A family of reduced instruction set computing (RISC) architectures for
    processors, widely used in mobile and embedded systems.
- term: heap-buffer-overflow
  definition: A type of buffer overflow where the overflow occurs in dynamically allocated
    memory (the heap).
- term: R_ARM_TLS_GOTDESC
  definition: An ARM relocation type related to Thread-Local Storage (TLS) GOT (Global
    Offset Table) descriptor entries.
- term: R_ARM_V4BX
  definition: An ARM relocation type associated with the BX (Branch and Exchange)
    instruction, used for interworking between ARM and Thumb states.
- term: R_ARM_THM_TLS_DESCSEQ
  definition: An ARM relocation type for Thumb instructions related to TLS descriptor
    sequences.
series_id: 'binutils:arm: reject out-of-range relocations instead of reading and writing
  past the section'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261124080017.3387430-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This series introduces bounds checking for ARM relocations in binutils to prevent out-of-bounds reads and writes. The first patch rejects relocations whose fields lie outside the section, and the second patch ensures that instructions indirectly read by specific relocations are also within section bounds. This addresses security vulnerabilities found via AddressSanitizer.
