---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- relocations
- ELF
discussion_id: 20261109-fix-livepatch-v1-1-746e33313147@scaleway.com
source_type: public_inbox
title: '[PATCH 1/2] bfd: Fix writing of secondary reloc sections'
headline: 'bfd: Fix writing of secondary reloc sections'
tldr: Fixes a typo in secondary relocation writing logic, correcting internal relocation
  lookups.
proposer: Antoine Damhet <adamhet@scaleway.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Antoine Damhet <adamhet@scaleway.com>
  role: proposer
  position: Submits a patch to fix a typo in BFD's secondary relocation handling,
    which was causing incorrect internal relocation lookups.
  quote: 'Commit eb92a17c47ea ("bfd: move sec_info from ELF to general section struct")
    introduced a typo in ''_bfd_elf_write_secondary_reloc_section'' that made the
    internal relocations of secondary reloc sections incorrectly looked up.'
primer_expert: This patch addresses a regression in the BFD library's ELF backend,
  specifically within the `_bfd_elf_write_secondary_reloc_section` function. A previous
  change moved `sec_info` from an ELF-specific structure to the general section structure.
  This patch corrects a typo introduced during that refactoring, where `sec->sec_info`
  was incorrectly used instead of `relsec->sec_info`, leading to incorrect relocation
  data being written.
primer_glossary:
- term: sec_info
  definition: Likely a structure or pointer within a BFD section that holds information
    specific to relocations within that section.
- term: secondary reloc sections
  definition: Sections in an object file that contain relocation information, possibly
    for a secondary linking or patching stage.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: bfd
  definition: The Binary File Descriptor library, a core component of GNU Binutils
    that provides a device-independent interface to a variety of object file formats.
series_id: 'binutils:bfd: fix writing of secondary reloc sections'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261109-fix-livepatch-v1-1-746e33313147@scaleway.com
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This patch corrects a typo introduced in commit eb92a17c47ea that affected the `_bfd_elf_write_secondary_reloc_section` function. The typo caused internal relocations of secondary reloc sections to be incorrectly looked up, leading to corrupted data.
