---
project: binutils
subsystem: gprof
patch_id: null
tags:
- gprof
- binutils
- dwarf
- debugging
- performance
discussion_id: awgkHhgam5vpfOBc@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] gprof: Enable decompression before checking separate debug files'
headline: 'gprof: Enable decompression before checking separate debug files'
tldr: Fixes gprof's output when DWARF debug info is compressed and in a separate file.
proposer: Alan Modra <amodra@gmail.com>
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Modifies the initialization order in BFD to set BFD_DECOMPRESS before `bfd_check_format`
  for separate debug files.
- Addresses a specific issue related to compressed DWARF in separate files, potentially
  improving accuracy for users employing this configuration.
- Relies on the existing DWARF compression and BFD infrastructure.
exchanges:
- author: Li Guan
  role: proposer
  position: Submitted a patch to resolve `gprof`'s incorrect source line reporting
    with compressed DWARF in separate debug files by enabling decompression earlier
    in the process.
  quote: 'With compressed DWARF enabled by default, tst-gmon-gprof-l2 reports

    <unknown>:0 for f1, f2 and f3 instead of the expected source lines.


    BFD initializes compressed section sizes while checking the object

    format. Set BFD_DECOMPRESS before bfd_check_format(), as core_init() already does
    for the main executable, so the separate debug file is opened with the same section
    decompression behavior.'
- author: Alan Modra
  role: maintainer
  position: Accepted the patch, indicating it has been applied.
  quote: Thank you, applied.
primer_expert: This patch for `gprof` corrects the display of source line numbers
  when DWARF debug information is both compressed and located in a separate debug
  file. Previously, `bfd_check_format` would be called before BFD's internal decompression
  mechanisms were fully initialized for these external files, leading to section sizes
  being reported incorrectly. This resulted in `gprof` failing to map execution samples
  to their correct source lines, showing `<unknown>:0`. The fix ensures that BFD_DECOMPRESS
  is set before `bfd_check_format` is invoked for separate debug files, aligning its
  behavior with the p…
primer_glossary:
- term: gprof
  definition: A performance analysis tool that collects and displays call graph and
    timing information.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about program variables, functions, and types.
- term: compressed DWARF
  definition: DWARF debug information that has been compressed to reduce file size.
- term: separate debug files
  definition: Object files that contain only DWARF debug information, separate from
    the executable binary. This allows the executable to be smaller and the debug
    information to be managed independently.
- term: BFD
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface to various object file formats.
- term: section decompression
  definition: The process of uncompressing data that has been compressed within a
    specific section of an object file.
- term: bfd_check_format
  definition: A function within the BFD library used to determine and validate the
    format of a binary file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/awgkHhgam5vpfOBc@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where `gprof` would output `<unknown>:0` for source file lines when using compressed DWARF debug information stored in separate files. The problem stemmed from BFD not initializing the decompression for these separate debug sections early enough. By enabling decompression before `bfd_check_format`, similar to how it's handled for the main executable, the separate debug file is opened with the correct decompression behavior, resolving the incorrect source line reporting.
