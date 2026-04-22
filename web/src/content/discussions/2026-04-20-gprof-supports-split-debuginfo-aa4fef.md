---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gprof
- debuginfo
- profiling
- strip
- BFD
discussion_id: 20260206190747.GA5540@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: Gprof supports split debuginfo
tldr: gprof can now find symbols and line numbers in split debuginfo files (stripped
  binaries).
stakes: Allows profiling of stripped binaries, which is important for performance
  analysis in production environments.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in gprof to handle split debuginfo.
- Potential performance overhead when searching for debuginfo in separate files.
- Reliance on debug BFD for accessing debug information.
exchanges:
- author: fche@redhat.com
  role: proposer
  position: Proposes adding gprof support for split debuginfo, allowing it to work
    with stripped binaries by utilizing debug BFD to locate necessary information
    from separate debuginfo files.
  quote: Use debug BFD for symbol and line information when a separated debuginfo
    file is found, enabling gprof to work correctly with binaries stripped with "strip
    -g".  Baby steps toward possible future debuginfod/dwz support.
- author: Alan Modra
  role: reviewer
  position: Agrees with the patch but suggests removing a conditional statement.
  quote: The patch is OK with the conditional removed here.
primer_expert: gprof relies on debug information (DWARF) to map execution samples
  back to source code lines.  When binaries are stripped using `strip -g`, this information
  is moved to a separate debuginfo file. This patch modifies gprof to use the debug
  BFD (Binary File Descriptor library) to locate and access this split debuginfo.  The
  patch touches `bfd` and interacts with the ELF file format.  The ultimate goal is
  debuginfod integration.
primer_general: gprof is a tool for profiling programs, showing how much time is spent
  in each function. To do this, it needs debug information that maps machine code
  to source code.  The debug information is typically stored in the binary itself
  or in a separate file if the binary has been stripped. This patch enhances gprof
  to find debug information even when it's separated from the main binary file.  This
  separation is often done to reduce the size of the deployed binary while still allowing
  for debugging and profiling when needed. BFD is a library within binutils for abstracting
  access to different object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/877bq13a6w.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This patch enables gprof to work with binaries that have been stripped of debug information using "strip -g". It uses the debug BFD to locate symbol and line number information from separate debuginfo files. This is a step towards supporting debuginfod/dwz.
