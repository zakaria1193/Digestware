---
project: binutils
subsystem: binutils/readelf
patch_id: null
tags:
- binutils
- readelf
- elf
- debugging
- diagnostics
commit_hash: ced7bfccaa63502f0765783dd513d174d415ef9e
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Clarify STAPDT vs STAPSDT note handling in readelf
tldr: Corrects error messages and internal labels in readelf when processing STAPSDT
  notes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `binutils/readelf.c`, the `print_stapsdt_note` function's internal
  error handling was unified under a single `too_small` label, previously `stapdt_note_too_small`.
  This change corrects the error reporting for malformed `Elf_Internal_Note` structures
  when they are too small to contain the expected STAPSDT data, aligning the diagnostic
  with the specific note type being processed.
primer_glossary:
- term: readelf
  definition: A command-line utility that displays information about ELF (Executable
    and Linkable Format) files. It can show sections, symbols, relocation entries,
    and other details.
- term: STAPSDT
  definition: SystemTap dynamic tracing. A facility that allows users to dynamically
    instrument running Linux kernel or userspace programs to gather detailed performance
    and operational data.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: note
  definition: A section type in ELF files that contains arbitrary metadata. Tools
    like readelf can parse specific note types, such as those used for debugging or
    tracing information.
discussion_id_link: public_inbox:binutils#34419
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261011071404.402884BA23C1@sourceware.org
date: '2026-10-11'
is_stub: false
stub_reason: ''
---

The `readelf` utility previously confused 'stapdt' and 'stapsdt' sections, leading to misleading error messages for malformed notes. This commit clarifies the distinction by renaming an internal label and correcting the error message to accurately reflect that the note is too small for STAPSDT processing. This resolves PR 34419.
