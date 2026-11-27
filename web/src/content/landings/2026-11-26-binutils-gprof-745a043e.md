---
project: binutils
subsystem: binutils/gprof
patch_id: null
tags:
- binutils
- gprof
- debugging
- dwarf
commit_hash: 745a043e6a52760b28d92340eeb804d455b80bc4
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Gprof enables decompression before checking separate debug files
tldr: Gprof now enables decompression for separate debug files earlier, fixing source
  line reporting for compressed DWARF sections.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The binutils/gprof subsystem initializes BFD (Binary File Descriptor)
  to read symbol information from executables and core dumps. This commit adjusts
  the order of operations when opening separate debug files. It ensures that the BFD_DECOMPRESS
  flag is set on the debug BFD *before* bfd_check_format() is called, mirroring the
  behavior for the main executable in core_init(). This resolves a bug where compressed
  DWARF sections in separate debug files were not being correctly decompressed, leading
  to incorrect source line reporting.
primer_glossary:
- term: gprof
  definition: A performance analysis tool that profiles a program's execution and
    provides information about the time spent in different functions.
- term: BFD
  definition: Binary File Descriptor library, a C library used by binutils and GDB
    to provide a common interface for reading and writing various executable file
    formats.
- term: DWARF
  definition: A debugging data format used by many compilers and linkers. It stores
    information about variables, types, and source code locations.
- term: compressed DWARF
  definition: A version of DWARF debugging information that has been compressed to
    reduce file size. This requires decompression before the information can be used.
- term: separate debug files
  definition: A mechanism where debugging information (like DWARF) is stored in a
    separate file from the executable itself. This can help reduce the size of the
    main executable.
- term: BFD_DECOMPRESS
  definition: A flag within the BFD library that indicates whether decompression should
    be applied to section data when reading files.
- term: bfd_check_format
  definition: A BFD library function that checks and identifies the file format of
    a given BFD object.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261126121946.A209142AFE4E@sourceware.org
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

This change modifies gprof to enable decompression for separate debug files before checking their format. Previously, this occurred after format checking, causing issues with compressed DWARF sections. By enabling decompression earlier, gprof now correctly reports source lines for files like tst-gmon-gprof-l2, which previously showed unknown locations.
