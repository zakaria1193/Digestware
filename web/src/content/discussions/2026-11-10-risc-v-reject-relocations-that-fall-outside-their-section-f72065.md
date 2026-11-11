---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- ld
- risc-v
- relocation
- security
discussion_id: 20261110201522.2149977-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/5] RISC-V: reject relocations that fall outside their section (PR
  34987)'
headline: 'RISC-V: reject relocations that fall outside their section'
tldr: binutils ld now rejects RISC-V relocations that point outside their section,
  preventing crashes and silent errors.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds runtime checks for relocations, potentially introducing a small performance
  overhead during the linking process.
- Fixes a security vulnerability and improves overall linker robustness.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes a series of patches to add range checks for RISC-V relocations
    within `ld`, preventing out-of-bounds memory access and associated issues like
    double frees or heap-buffer-overflows.
  quote: The RISC-V relocate loop and the relaxation helpers access section contents
    at rel->r_offset without checking that the field lies inside the section. A crafted
    object can make ld write out of bounds (PR ld/34987)
primer_expert: The binutils `ld` linker has been updated to validate relocation offsets
  against section boundaries for RISC-V targets. Previously, crafted object files
  could exploit invalid relocation entries (e.g., R_RISCV_SUB_ULEB128 or R_RISCV_TLSDESC_CALL)
  that extended past the end of a section, leading to out-of-bounds writes in `perform_relocation`
  or `riscv_resolve_tlsdesc_lo_relocs`. This series adds checks to reject such malformed
  relocations, fixing PR ld/34987 and improving linker robustness.
primer_glossary:
- term: relocation
  definition: Information in an object file that tells the linker how to modify certain
    instructions or data references to correctly link code or data from different
    sections or other object files.
- term: ld
  definition: The GNU linker, part of the binutils package. It combines object files
    and libraries into an executable or shared library.
- term: section
  definition: A segment of an object file or executable that contains related data,
    such as code (.text), initialized data (.data), or uninitialized data (.bss).
- term: out-of-bounds write
  definition: Writing data to a memory location that is outside the allocated buffer
    or memory region, leading to data corruption or crashes.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles,
    increasingly used in embedded systems and high-performance computing.
series_id: 'binutils:risc-v: reject relocations that fall outside their section (pr
  34987)'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261110201522.2149977-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This series of patches addresses a bug in binutils' linker (ld) where it would process RISC-V relocations that extended beyond the bounds of their section. This could lead to out-of-bounds writes, resulting in crashes or silent data corruption. The changes introduce explicit checks to reject such invalid relocations, improving robustness and preventing security vulnerabilities.
