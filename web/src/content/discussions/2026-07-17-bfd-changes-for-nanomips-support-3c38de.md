---
project: binutils
subsystem: elf
patch_id: null
tags:
- BFD
- ELF
- nanomips
- build system
discussion_id: 20260717103858.199743-3-lei.wang@oss.cipunited.com
source_type: public_inbox
title: '[PATCH 2/6] BFD changes for nanoMIPS support.'
headline: BFD changes for nanoMIPS support.
tldr: Adds nanoMIPS architecture support to the BFD library.
proposer: Tsing <lei.wang@oss.cipunited.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Adds nanoMIPS support to the BFD library, enabling it to read and write
  nanoMIPS object files. This involves updating BFD's build system and configuration
  to recognize nanoMIPS targets (e.g., nanomips32-elf, nanomips64-elf), defining nanoMIPS-specific
  ELF structures and relocations, and creating new C source files for nanoMIPS ELF
  handling.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    to provide a consistent interface for reading and writing various object file
    formats.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps.
- term: relocation
  definition: Information in an object file that describes how to modify certain symbols
    (like addresses) when linking it with other object files or loading it into memory.
- term: EM_NANOMIPS
  definition: The ELF machine type identifier for the nanoMIPS architecture.
series_id: binutils:bfd changes for nanomips support
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260717103858.199743-3-lei.wang@oss.cipunited.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch integrates nanoMIPS architecture support into the Binary File Descriptor (BFD) library. It updates build system files (Makefile.am, configure.ac), adds new BFD-specific files for nanoMIPS (elfnn-nanomips.c, elfxx-nanomips.c), and defines nanoMIPS relocations. The changes enable BFD to handle nanoMIPS ELF object files.
