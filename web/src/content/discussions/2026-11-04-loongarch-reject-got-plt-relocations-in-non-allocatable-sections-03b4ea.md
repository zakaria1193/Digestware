---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- LoongArch
- linker
- relocation
- security
discussion_id: 20261104021434.46062-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Reject GOT/PLT relocations in non-allocatable sections'
headline: 'LoongArch: Reject GOT/PLT relocations in non-allocatable sections'
tldr: Patch rejects GOT/PLT relocations in non-allocatable sections for LoongArch
  to prevent errors.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Prevents potential crashes or assertion failures by rejecting invalid relocations,
  potentially causing link-time errors for programs that incorrectly place these relocations.
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Submits a patch to reject specific relocations in non-allocatable sections
    for the LoongArch architecture to prevent runtime errors.
  quote: null
primer_expert: The LoongArch ELF backend in binutils is being updated to reject certain
  relocations (GOT, TLS GOT, branch) when they are applied to sections marked as non-allocatable
  (`SEC_ALLOC`). The linker's relocation scanning process typically ignores these
  sections, thus not reserving space in the Global Offset Table (GOT) or Procedure
  Linkage Table (PLT). Attempting to resolve such relocations later can lead to invalid
  memory accesses or assertion failures. The patch adds checks to detect and reject
  these cases during the final linking phase, while exempting debug sections (`SEC_DEBUGGING`).
primer_glossary:
- term: LoongArch
  definition: A RISC-ISA (Instruction Set Architecture) developed in China.
- term: GOT
  definition: Global Offset Table. A table used by position-independent code to store
    addresses of global variables and functions.
- term: PLT
  definition: Procedure Linkage Table. A table used in ELF executables to handle calls
    to dynamically linked external functions.
- term: relocation
  definition: A symbol or pointer in an object file that needs to be resolved by the
    linker before the program can be executed. Relocations contain information about
    how to modify addresses or other data.
- term: non-allocatable sections
  definition: Sections in an object file that are not intended to be loaded into memory
    at runtime, such as those containing debugging information or linker-specific
    metadata.
- term: linker
  definition: A program that combines various object files and libraries into a single
    executable file or library.
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261104021434.46062-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch prevents errors in the LoongArch linker by rejecting GOT, TLS GOT, and branch relocations when they occur in non-allocatable sections. Relocation scanning normally skips these sections, meaning GOT or PLT entries are not allocated for them. Processing these relocations later can lead to access misses, assertions, or invalid memory accesses. Debugging sections are still allowed.
