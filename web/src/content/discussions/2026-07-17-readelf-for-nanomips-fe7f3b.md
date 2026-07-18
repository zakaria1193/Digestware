---
project: binutils
subsystem: binutils
patch_id: null
tags:
- readelf
- ELF
- nanomips
discussion_id: 20260717103858.199743-5-lei.wang@oss.cipunited.com
source_type: public_inbox
title: '[PATCH 4/6] Readelf for nanoMIPS.'
headline: Readelf for nanoMIPS.
tldr: Adds nanoMIPS support to the readelf utility.
proposer: Tsing <lei.wang@oss.cipunited.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Enables readelf to parse nanoMIPS executables. This involves updating
  ELF identification logic (EM_NANOMIPS) and relocation handling within readelf.c
  to correctly interpret nanoMIPS-specific machine types and relocation entries.
primer_glossary:
- term: readelf
  definition: A command-line utility that displays information about ELF (Executable
    and Linkable Format) files.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps.
- term: relocation
  definition: Information in an object file that describes how to modify certain symbols
    (like addresses) when linking it with other object files or loading it into memory.
- term: EM_NANOMIPS
  definition: The ELF machine type identifier for the nanoMIPS architecture.
series_id: binutils:readelf for nanomips
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260717103858.199743-5-lei.wang@oss.cipunited.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch updates the readelf utility to recognize and process the nanoMIPS architecture. It adds support for EM_NANOMIPS in various functions like guess_is_rela, get_machine_name, dump_relocations, and get_machine_flags. Additionally, it incorporates specific checks for nanoMIPS relocation types (R_NANOMIPS_32, R_NANOMIPS_PC32, etc.).
