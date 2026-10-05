---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- coff
- xcoff
- security
discussion_id: CAOX--DQV9Xa_t_KTx-UaxHwAiErvLTC_+hGmNCYGK5o0QJS1zg@mail.gmail.com
source_type: public_inbox
title: '[PATCH] bfd: validate COFF and XCOFF symbol tables before the linker walks
  them'
headline: 'bfd: validate COFF and XCOFF symbol tables before linker walks them'
tldr: Patch validates COFF and XCOFF symbol tables to prevent heap writes caused by
  out-of-bounds access.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adding validation checks to prevent buffer overflows versus the potential minor
  performance overhead of these checks.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes validating COFF and XCOFF symbol tables to prevent heap writes
    caused by incorrect auxiliary entry counts. The patch addresses specific unvalidated
    paths in XCOFF linking and strengthens generic COFF linker paths.
  quote: null
primer_expert: This patch in binutils/bfd (specifically affecting `cofflink.c` and
  `xcofflink.c`) addresses potential heap buffer overflows. The issue arises when
  processing COFF and XCOFF symbol tables, where `n_numaux` can cause out-of-bounds
  reads/writes into state arrays like `sym_hashes` and `sym_indices` if not properly
  validated. The patch aims to rectify this by adding explicit checks before the linker
  walks these tables, building on previous hardening efforts.
primer_glossary:
- term: bfd
  definition: The Binary File Descriptor library, a low-level library used by binutils
    to parse and manipulate object files and executables.
- term: COFF
  definition: Common Object File Format, a file format for executables, object code,
    and shared libraries on Unix-like systems, and older versions of Windows.
- term: XCOFF
  definition: An extended version of COFF, primarily used on IBM's AIX operating system.
    It includes additional information for debugging and linking.
- term: symbol table
  definition: A data structure used by linkers and debuggers to store information
    about symbols (variables, functions, etc.) defined in an object file.
- term: n_numaux
  definition: A field in a COFF symbol entry that specifies the number of auxiliary
    entries following the main symbol entry. These auxiliary entries provide additional
    information about the symbol.
- term: heap writes
  definition: Writing data to the heap, a region of memory used for dynamic memory
    allocation. Out-of-bounds writes can corrupt other data or lead to crashes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAOX--DQV9Xa_t_KTx-UaxHwAiErvLTC_+hGmNCYGK5o0QJS1zg@mail.gmail.com
bugzilla_url: null
date: '2026-10-04'
is_stub: false
stub_reason: ''
---

This patch addresses heap buffer overflows in binutils' COFF and XCOFF linkers by validating symbol tables before they are processed. Specifically, it corrects issues where a symbol's auxiliary entries could point beyond the allocated buffer, leading to out-of-bounds writes, and aims to harden unvalidated paths present in generic COFF and XCOFF linking.
