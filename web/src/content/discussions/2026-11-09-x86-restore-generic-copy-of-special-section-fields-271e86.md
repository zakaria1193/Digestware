---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- bfd
- x86
- relocations
- ELF
discussion_id: 20261109-fix-livepatch-v1-2-746e33313147@scaleway.com
source_type: public_inbox
title: '[PATCH 2/2] x86: Restore generic copy of special section fields'
headline: 'x86: Restore generic copy of special section fields'
tldr: Restores generic section field copying for non-Solaris binaries, fixing secondary
  reloc issues.
proposer: Antoine Damhet <adamhet@scaleway.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Antoine Damhet <adamhet@scaleway.com>
  role: proposer
  position: Submits a patch to restore generic section field copying, resolving issues
    with secondary relocations on non-Solaris binaries.
  quote: 'Commit f5c3ce3687f7 ("x86: Add _bfd_elf_x86_copy_special_section_fields")
    short-circuited the generic handling for non-Solaris binaries. Restore the generic
    handling for these inputs to avoid ''SHT_SECONDARY_RELOC'' with zeroed ''sh_link/sh_info''.'
primer_expert: This patch modifies the `_bfd_elf_x86_copy_special_section_fields`
  function in the x86 ELF backend. It reverts a change that made this function return
  `false` for non-Solaris binaries, which inadvertently bypassed the generic `_bfd_elf_copy_special_section_fields`
  function. This generic function is necessary for correctly handling fields like
  `sh_link` and `sh_info` for sections like `SHT_SECONDARY_RELOC`, preventing corruption.
primer_glossary:
- term: sh_link
  definition: A field in an ELF section header that provides a reference to another
    section, typically a symbol table.
- term: sh_info
  definition: A field in an ELF section header that contains additional information
    about the section, its meaning depending on the section type.
- term: SHT_SECONDARY_RELOC
  definition: A section type in the ELF file format that indicates secondary relocation
    information, often used in specific linking or patching scenarios.
- term: Solaris
  definition: An operating system, formerly developed by Sun Microsystems and now
    by Oracle, based on UNIX.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
series_id: 'binutils:x86: restore generic copy of special section fields'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109-fix-livepatch-v1-2-746e33313147@scaleway.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch restores the generic handling of special section fields for non-Solaris binaries. A previous commit had short-circuited this generic handling, leading to incorrect zeroing of the 'sh_link' and 'sh_info' fields for 'SHT_SECONDARY_RELOC' sections, which is now corrected.
