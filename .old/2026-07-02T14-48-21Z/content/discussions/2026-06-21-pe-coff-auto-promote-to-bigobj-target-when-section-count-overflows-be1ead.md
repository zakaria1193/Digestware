---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- PE/COFF
- bigobj
- assembler
- linker
- bfd
discussion_id: 20260621174919.1150-3-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] PE/COFF: auto-promote to bigobj target when section count overflows'
headline: 'PE/COFF: auto-promote to bigobj target when section count overflows'
tldr: Binutils now automatically promotes PE/COFF object files to the 'bigobj' format
  when the section count exceeds the 16-bit limit, preventing silent truncation a…
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased object file size for files that are automatically promoted to bigobj,
  even if only slightly over the 16-bit section limit.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Proposes to automatically promote PE/COFF object files to the 'bigobj'
    format when the section count exceeds 65535, preventing silent corruption and
    linker errors.
  quote: Fix this by automatically switching the xvec to the matching bigobj target
    before any headers or symbols are finalized, so the object is written out using
    the extended COFF format which supports 32-bit section numbers.
primer_expert: This patch targets the Binutils `bfd` library, specifically the PE/COFF
  object file format (`coffcode.h`). Standard PE/COFF uses 16-bit integers for section
  numbers in the symbol table, limiting an object file to 65535 sections. When `coff_compute_section_file_positions`
  detects an overflow (`target_index >= bfd_coff_max_nscns`), the patch checks for
  `COFF_WITH_PE_BIGOBJ` and, if available, reassigns `abfd->xvec` to `&TARGET_SYM_BIG`.
  This change promotes the object to the extended COFF 'bigobj' format, which accommodates
  32-bit section numbers, thus avoiding silent truncation and subsequent…
primer_general: This discussion is about an improvement to Binutils, a set of programming
  tools for working with compiled computer programs. Specifically, it concerns how
  Binutils handles a type of file format called PE/COFF, often used on Windows. Older
  versions of this format had a limit on how many different sections a program could
  have. If a program exceeded this limit, the tools would silently create corrupted
  files, leading to confusing errors during the linking phase (when different parts
  of a program are put together). This patch automatically detects when this limit
  is exceeded and switches to a newer, extended version of the PE/COFF format called
  'bigobj', which supports more sections. This makes the tools more robust and prevents
  difficult-to-diagnose errors for developers working on very large programs.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260621174919.1150-3-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-06-21'
is_stub: false
---

This patch for Binutils addresses a problem with the PE/COFF object file format where exceeding the 16-bit section count limit could lead to silently corrupted object files and misleading linker errors. The proposed solution automatically switches the object file format to 'bigobj' when the section count overflows, allowing for 32-bit section numbers. This change improves the reliability of the assembler by preventing corrupted output and clarifying linker diagnostics for large projects.
