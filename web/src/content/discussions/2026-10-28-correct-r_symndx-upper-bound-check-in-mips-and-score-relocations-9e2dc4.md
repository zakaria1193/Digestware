---
project: binutils
subsystem: binutils
patch_id: null
tags:
- elf
- relocations
- mips
- score
- bugfix
discussion_id: auJ2pT-SInvbwe9a@squeak.grove.modra.org
source_type: public_inbox
title: mips and score check_relocs r_symndx upper bound
headline: Correct r_symndx upper bound check in MIPS and Score relocations
tldr: Fixes an incorrect upper bound check for `r_symndx` in MIPS and Score ELF relocation
  processing.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- The author notes that this check will be removed entirely in a subsequent patch.
exchanges: []
primer_expert: The `check_relocs` function in BFD's ELF backends verifies relocation
  entries. For MIPS and Score, the check for the upper bound of `r_symndx` was flawed.
  The `sym_hashes` array is indexed by `r_symndx - extsymoff` and has a size related
  to `NUM_SHDR_ENTRIES`. The patch corrects the check from `r_symndx >= extsymoff
  + NUM_SHDR_ENTRIES` to `r_symndx >= NUM_SHDR_ENTRIES`, aligning it with how `sym_hashes`
  is indexed and sized, and preventing out-of-bounds access or incorrect validation.
primer_glossary:
- term: r_symndx
  definition: The symbol table index field within an ELF relocation entry.
- term: MIPS
  definition: A Reduced Instruction Set Computing (RISC) architecture, commonly used
    in embedded systems and historically in workstations.
- term: Score
  definition: A 32-bit RISC processor architecture.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: BFD
  definition: Binary File Descriptor library, a low-level interface used by binutils
    for manipulating object files.
- term: relocation entry
  definition: Data within an object file that specifies how to modify addresses in
    code or data when the object is linked, especially for position-independent code.
- term: extsymoff
  definition: An offset related to the external symbol table in ELF files, used for
    indexing.
- term: NUM_SHDR_ENTRIES
  definition: A macro likely representing the number of section header entries in
    an ELF file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ2pT-SInvbwe9a@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch corrects an off-by-one error in the `check_relocs` functions for MIPS and Score ELF targets. The `r_symndx` field in relocation entries should not exceed the number of symbols available in the symbol table. The previous check incorrectly included an `extsymoff` offset that was not relevant for calculating the upper bound, leading to potential misinterpretation of symbol indices. A later patch will remove these checks entirely.
