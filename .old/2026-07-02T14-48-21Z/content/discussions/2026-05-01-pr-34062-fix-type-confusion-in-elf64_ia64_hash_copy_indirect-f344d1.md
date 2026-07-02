---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- bfd
- elf
- type confusion
discussion_id: afShEkDOzdDFVRZI@squeak.grove.modra.org
source_type: public_inbox
title: PR 34062 type confusion in elf64_ia64_hash_copy_indirect
headline: 'PR 34062: Fix type confusion in elf64_ia64_hash_copy_indirect'
tldr: The output BFD should determine the linker hash table and symbol entry types,
  fixing a type confusion issue.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The patch corrects a type confusion, potentially improving linker stability and
  correctness.
- There are no apparent downsides to this fix.
exchanges: []
primer_expert: BFD is the Binary File Descriptor library, providing a uniform interface
  to different object file formats. The linker uses BFD to read and write object files.
  This patch addresses a type confusion in the ELF backend, specifically related to
  symbol merging and hash table manipulation.
primer_general: The Binary File Descriptor (BFD) library provides a generic interface
  for working with different object file formats, such as ELF. The linker uses this
  library to manipulate object files during the linking process. This patch fixes
  a bug in how the linker handles symbols, ensuring that the correct data types are
  used when merging symbols from different object files. This can prevent crashes
  or incorrect linking behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afShEkDOzdDFVRZI@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-01'
---

Alan Modra proposes a patch to fix a type confusion issue in the linker. The patch ensures that the output BFD (Binary File Descriptor) determines the linker hash table type and symbol entry type, and that output BFD functions are used when manipulating hash table symbols. This avoids using potentially incorrect types from the input BFD.
