---
project: binutils
subsystem: binutils
patch_id: null
tags:
- build
- warnings
- cleanup
discussion_id: 20261019193231.1708375-1-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH 00/18] Fix bfd/opcodes/binutils/sim/ld warnings with clang 23'
headline: Fix bfd/opcodes/binutils/sim/ld warnings with clang 23
tldr: Series of patches to fix compiler warnings in binutils, particularly for clang
  23.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves build robustness by eliminating warnings.
- Addresses compiler changes that require code adjustments.
exchanges: []
primer_expert: This is the cover letter for a series of patches aimed at resolving
  build-time warnings, specifically those introduced by newer versions of clang (e.g.,
  clang 23) that now enforce stricter checks for unused variables and other potential
  issues. The series touches multiple parts of the binutils project, including the
  Binary File Descriptor (BFD) library, the opcodes disassembly engine, the simulator
  (sim), and the linker (ld).
primer_glossary:
- term: BFD
  definition: Binary File Descriptor. A library within binutils that provides a common
    interface for reading and writing various binary object file formats.
- term: opcodes
  definition: The part of binutils responsible for disassembling machine code into
    human-readable assembly instructions.
- term: sim
  definition: Simulator. A component of binutils that simulates the execution of code
    for various processor architectures.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or library.
- term: unused-but-set-variable
  definition: A compiler warning indicating a variable that has been assigned a value
    but is never subsequently read. This often suggests dead code.
- term: strchr
  definition: A C standard library function that searches for the first occurrence
    of a character within a string.
series_id: binutils:fix bfd/opcodes/binutils/sim/ld warnings with clang 23
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261019193231.1708375-1-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This patch series addresses compiler warnings, primarily from clang 23, that have surfaced due to its increased strictness with unused variables. It includes fixes for various components like BFD, opcodes, sim, and ld, removing unused variables and correcting type issues. One patch also includes a fix for a glibc 2.43 change affecting `strchr`'s signature.
