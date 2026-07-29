---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- bfd
- core dump
- aix
- gdb
discussion_id: 20260728093632.62791-2-akamath996@gmail.com
source_type: public_inbox
title: '[PATCH v1] Add support to recognise 32 bit core file formats in AIX 7.3'
headline: AIX 7.3 32-bit core file format recognition
tldr: Patch adds support for recognizing 32-bit core file formats on AIX 7.3 in BFD.
proposer: Aditya Vidyadhar Kamath <akamath996@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The Binary File Descriptor (BFD) library, a core component of GNU Binutils
  and GDB, is responsible for handling various object file and core dump formats.
  This patch specifically targets AIX 7.3's 32-bit core dump format, which was not
  previously recognized by BFD. By adding support for this format, GDB and other tools
  relying on BFD can now correctly load and analyze core dumps generated on newer
  AIX versions.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a GNU project library that provides
    a common interface to various object file formats.
- term: core dump
  definition: A file containing the memory image of a process at the time it terminated
    abnormally. Debuggers use core dumps to analyze the state of the program.
- term: AIX
  definition: A proprietary Unix operating system developed by IBM.
- term: file format not recognized
  definition: An error message indicating that a tool cannot understand the structure
    or type of a given file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260728093632.62791-2-akamath996@gmail.com
bugzilla_url: null
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where GDB on AIX 7.3 fails to recognize 32-bit core dump files. The problem stems from the Binary File Descriptor (BFD) library not supporting the specific core file format used in AIX 7.3. Applying this patch enables BFD to correctly identify and process these core files, resolving the GDB error.
