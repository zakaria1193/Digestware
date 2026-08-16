---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- optimization
- GOT
- security
discussion_id: 20260814202538.1039846-1-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH] alpha: reallocate .got contents when relaxation grows a subsection'
headline: 'alpha: reallocate .got contents when relaxation grows a subsection'
tldr: Fixes a bug where alpha GOT subsections can grow during relaxation, causing
  buffer overflows and crashes when not reallocated.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Ensuring memory safety and preventing crashes by reallocating GOT buffers vs. potential
  performance overhead of reallocation and assertions during relaxation.
- Correctly handling optimization flags like -O1 which enable relaxation by default.
exchanges:
- author: Matt Turner
  role: proposer
  position: Identified and proposed a fix for a bug in the Alpha linker where growing
    GOT subsections during relaxation cause buffer overflows, leading to crashes or
    corrupted output.
  quote: 'When a subsection grows, elf64_alpha_relocate_section writes GOT slots past

    the end of the allocated buffer, corrupting whatever objalloc placed after

    it.  Linking a large C++ shared library with -Bsymbolic or

    -Bsymbolic-functions aborts ld with a glibc "free(): invalid next size", or

    produces a library whose .rela.dyn is corrupt and which faults at run time

    with a GOT slot holding an unrelated p…'
primer_expert: This patch for the Alpha target in binutils' ld fixes a flaw in how
  the GOT (Global Offset Table) subsections are handled during relaxation. Specifically,
  `elf64_alpha_early_size_sections` allocates buffers for GOT subsections, but a subsequent
  call to `elf64_alpha_size_got_sections` during relaxation (with `may_merge` enabled)
  can recompute subsection sizes, potentially increasing them. If a subsection grows
  beyond its allocated buffer, `elf64_alpha_relocate_section` writes past the buffer
  boundary. This patch introduces reallocation of the buffer in `elf64_alpha_relax_section`
  if growth is…
primer_glossary:
- term: GOT
  definition: Global Offset Table, a data structure used in position-independent code
    (PIC) to hold addresses of external functions and global variables, allowing them
    to be resolved at runtime.
- term: relaxation
  definition: A linker optimization technique where relocations are resolved at link-time
    rather than runtime, potentially allowing for more compact or efficient code,
    especially in architectures like Alpha.
- term: subsections
  definition: Within a section like .got, subsections are used to group related entries,
    allowing for more granular management and optimization.
- term: buffer overflow
  definition: A condition where a program writes data beyond the allocated boundary
    of a buffer, potentially corrupting adjacent memory and causing crashes or security
    vulnerabilities.
- term: Alpha
  definition: A Reduced Instruction Set Computing (RISC) microprocessor architecture
    developed by Digital Equipment Corporation (DEC), known for its high performance
    in its era.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260814202538.1039846-1-mattst88@gmail.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch addresses a critical bug in the Alpha linker where Global Offset Table (GOT) subsections can grow during relaxation, exceeding their initially allocated buffer size. This leads to buffer overflows, data corruption, and crashes, particularly when linking large C++ shared libraries with optimization flags. The fix involves reallocating the GOT subsection buffer if its recomputed size exceeds the allocated space during relaxation, and adding an assertion to detect and report overflows during relocation.
