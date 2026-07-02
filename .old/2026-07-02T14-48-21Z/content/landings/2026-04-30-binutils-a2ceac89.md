---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gprof
- debugging
- debuginfo
commit_hash: a2ceac895716f71daf67eca5b5897bf316500749
source_type: public_inbox
author: Frank Ch. Eigler <fche@sourceware.org>
headline: Gprof supports split debuginfo, tweak.
tldr: gprof now correctly handles binaries stripped with "strip -g" by using debug
  BFD for symbol and line information.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: gprof uses BFD to read symbol information from binaries and separated
  debuginfo files. This commit touches `gprof/corefile.c` to improve handling of split
  debuginfo, which is used when binaries are stripped of debug symbols using `strip
  -g`. The change removes a now-unnecessary conditional setting the `BFD_DECOMPRESS`
  flag.
primer_general: Gprof is a performance analysis tool that profiles the execution of
  programs to determine where they spend their time. Debuginfo is extra data embedded
  in or alongside compiled programs that allows debuggers to correlate machine code
  with source code.  Split debuginfo is a method where debug information is stored
  in separate files, typically used to reduce the size of the main executable. This
  commit enhances gprof's ability to work with split debuginfo, especially in cases
  where binaries have been stripped of their debug symbols.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260430172201.9B455436F7C2@sourceware.org
date: '2026-04-30'
---

This commit removes a conditional that enabled decompression on the debug file in gprof/corefile.c.  The BFD_DECOMPRESS flag is no longer explicitly set on the debug BFD, simplifying the logic for handling split debuginfo.
