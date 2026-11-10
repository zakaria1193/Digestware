---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- XCOFF
- security
- fuzzing
discussion_id: avJOpG2W-DddrcZi@squeak.grove.modra.org
source_type: public_inbox
title: xcoff armap traversal
headline: xcoff armap traversal
tldr: Fixes an out-of-bounds read vulnerability in XCOFF armap symbol processing.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Corrects loop bounds to prevent out-of-bounds memory access, enhancing security
  and stability.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submitted a patch to fix an out-of-bounds read in XCOFF armap handling.
  quote: "oss-fuzz found a bug in code matching armap symbol names against bfds.\n\
    It's possible to run off the end of the armap, resulting in an\nunitialised read\
    \ or if you're really lucky, a read buffer overflow.\n\n\t* coff-rs6000.c (xcoff_write_armap_big):\
    \ Move armap count test\n\tto correct loop."
primer_expert: This patch addresses a security vulnerability found by oss-fuzz in
  the XCOFF (`coff-rs6000.c`) implementation related to `armap` symbol processing.
  The incorrect loop conditions in `xcoff_write_armap_big` could allow `i` to exceed
  `orl_count`, leading to reads from uninitialized memory or buffer overflows when
  processing archives. The fix correctly integrates the count check into the loop
  conditions.
primer_glossary:
- term: XCOFF
  definition: eXtended Common Object File Format. An object file format used on IBM
    RS/6000 and other PowerPC systems.
- term: armap
  definition: Likely refers to an archive map or a similar data structure used within
    archive processing.
- term: oss-fuzz
  definition: A free, open-source fuzzing service provided by Google that helps projects
    like Binutils find bugs.
- term: buffer overflow
  definition: A condition where a program attempts to write data beyond the allocated
    buffer, potentially corrupting adjacent memory.
- term: uninitialized read
  definition: Accessing memory that has not been assigned a value, leading to unpredictable
    program behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/avJOpG2W-DddrcZi@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

An oss-fuzz report revealed a bug in the XCOFF armap symbol name matching logic within binutils. The issue could lead to an uninitialized read or a buffer overflow if the armap traversal went past its intended bounds. The patch corrects the loop condition to prevent this.
