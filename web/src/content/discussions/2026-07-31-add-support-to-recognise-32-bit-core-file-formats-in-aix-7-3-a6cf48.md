---
project: binutils
subsystem: binutils
patch_id: null
tags:
- core dump
- AIX
- bugfix
discussion_id: 20260731071926.86917-2-akamath996@gmail.com
source_type: public_inbox
title: Add support to recognise 32 bit core file formats in AIX 7.3
headline: Add support to recognise 32 bit core file formats in AIX 7.3
tldr: Enables binutils to recognize 32-bit core dump file formats on AIX 7.3.
proposer: Aditya Vidyadhar Kamath <akamath996@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: 'This patch addresses an issue where the binutils BFD library fails
  to recognize 32-bit core dump files generated on AIX 7.3. The problem manifests
  as GDB reporting the core file as ''not a core dump: file format not recognized.''
  The change likely involves updating BFD''s format detection logic for AIX core dumps
  to accommodate a new or previously unsupported format on AIX 7.3.'
primer_glossary:
- term: core file
  definition: A file that contains a snapshot of a process's memory and state at the
    time of a crash.
- term: BFD
  definition: Binary File Descriptor library, a backend API for accessing object file
    formats.
- term: AIX
  definition: Advanced Interactive eXecutive, a Unix operating system developed by
    IBM.
- term: 32-bit core file format
  definition: A specific structure and encoding used for core dump files generated
    by 32-bit applications or operating system versions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260731071926.86917-2-akamath996@gmail.com
bugzilla_url: null
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

This patch adds support to the binutils BFD library for recognizing 32-bit core dump file formats on AIX 7.3. Previously, GDB would report these files as unrecognized, preventing analysis. The patch ensures that BFD can correctly identify these formats, allowing tools like GDB to process them.
