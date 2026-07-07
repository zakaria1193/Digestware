---
project: binutils
subsystem: binutils/objcopy
patch_id: null
tags:
- binutils
- objcopy
- bugfix
commit_hash: 64ca9aa24218cee8b31c4dc47694369da67b1acd
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Fix objcopy crash when updating SHT_GROUP sections
tldr: objcopy no longer crashes when attempting to update SHT_GROUP sections.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bfd_get_section_by_name` function can return a section that does
  not have a corresponding output section when dealing with SHT_GROUP sections. The
  `objcopy` utility's `--update-section` logic did not account for this, leading to
  a NULL pointer dereference when accessing `pupdate->section->output_section`. This
  commit adds a check for `osec == NULL` to prevent the crash.
primer_glossary:
- term: objcopy
  definition: A utility that copies and translates object files. It can be used to
    modify sections, symbols, and other information within an object file.
- term: SHT_GROUP
  definition: A section type in ELF object files that indicates a group of sections
    that should be treated as a single unit. This is often used for symbol tables
    or other metadata.
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils for reading and writing object file formats.
- term: output_section
  definition: In the BFD library, this refers to the section in the output object
    file that corresponds to an input section.
discussion_id_link: public_inbox:binutils#34353
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260707011301.08C274BA2E19@sourceware.org
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

objcopy previously crashed with a null-pointer dereference when the --update-section option was used on a SHT_GROUP section. This occurred because the output_section was NULL in such cases. This change modifies objcopy to correctly handle this scenario, preventing the crash and improving error reporting.
