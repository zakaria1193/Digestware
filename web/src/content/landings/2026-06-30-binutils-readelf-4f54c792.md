---
project: binutils
subsystem: binutils/readelf
patch_id: null
tags:
- binutils
- readelf
- bugfix
commit_hash: 4f54c792679f49250301c5a5bc3d8cfd0f5127cd
source_type: public_inbox
author: H.J. Lu
headline: 'readelf: Also set do_got_section_contents to false'
tldr: readelf now correctly disables GOT section content processing when section headers
  fail to load.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `binutils/readelf.c` to set `do_got_section_contents`
  to false within the `process_object` function, specifically when `process_section_headers`
  returns false. This addresses PR binutils/34323, ensuring that GOT section processing
  is correctly skipped if section headers cannot be loaded.
primer_general: '`readelf` is a command-line utility used to display information about
  object files. This commit fixes a bug where `readelf` might incorrectly attempt
  to process or display information about the Global Offset Table (GOT) even if it
  failed to load the essential section headers of the file. Now, if section headers
  cannot be processed, `readelf` will also refrain from attempting to display GOT
  section contents, leading to more robust error handling.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260630073027.163AA4BA23C8@sourceware.org
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This change modifies the `readelf` utility to ensure that processing of Global Offset Table (GOT) section contents is also disabled if the program fails to load its section headers. This prevents potential errors or incorrect output when the object file is malformed or incomplete.
