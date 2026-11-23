---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- dwarf
- security
- readelf
- vulnerability
discussion_id: loopr.38.ps3uramm4hpc@research.digiscrypt.com
source_type: public_inbox
title: '[PATCH] binutils: validate DW_LNE_define_file filename bounds'
headline: Validate DW_LNE_define_file filename bounds in DWARF line programs
tldr: Patch to prevent heap-buffer-overflow in binutils' readelf by bounding strlen
  for DW_LNE_define_file.
proposer: Alhuda Khan <alhuda@research.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixes a security vulnerability (heap-buffer-overflow).
- Adds bounds checking, which is a standard practice for robust parsing.
exchanges:
- author: Alhuda Khan <alhuda@research.digiscrypt.com>
  role: proposer
  position: Proposes a patch to fix a heap-buffer-overflow in `readelf -wL` by bounding
    the `strlen` call when processing `DW_LNE_define_file`.
  quote: 'The patch is attached. It uses memchr() bounded by op_code_end to find the

    terminator, and if there isn''t one it warns and stops processing that opcode

    instead of walking past the end.'
primer_expert: This patch addresses a security vulnerability in binutils' DWARF line
  information parser, specifically within the `readelf` utility. When processing the
  `.debug_line` section, the `DW_LNE_define_file` opcode (which defines a source file
  path) is vulnerable to a buffer overflow if the provided filename lacks a null terminator
  before the end of the opcode's data. The fix involves bounding the `strlen` operation
  to prevent it from reading past the allocated buffer, thus mitigating a heap overflow.
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to provide
    information about variables, types, and code structure.
- term: line program
  definition: A component of DWARF debugging information that maps compiled code addresses
    back to source code line numbers.
- term: DW_LNE_define_file
  definition: An opcode within DWARF line number information that defines a file name
    to be used in subsequent entries.
- term: readelf
  definition: A utility in the GNU Binutils package that displays information about
    ELF (Executable and Linkable Format) files, including debugging information.
- term: heap-buffer-overflow
  definition: A type of buffer overflow where a program writes data beyond the allocated
    buffer on the heap, potentially corrupting adjacent data or executing malicious
    code.
- term: strlen
  definition: A standard C library function that calculates the length of a null-terminated
    string.
- term: memchr
  definition: A standard C library function that searches for the first occurrence
    of a character within a block of memory.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/loopr.38.ps3uramm4hpc@research.digiscrypt.com
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

A vulnerability has been identified in binutils where `readelf -wL` can cause a heap-buffer-overflow when processing malformed DWARF line programs. The `DW_LNE_define_file` opcode reads the filename using `strlen()` without proper bounds checking against the opcode's payload end. This patch introduces a bounds check using `memchr()` to find the null terminator within the allocated buffer, preventing `strlen()` from reading past the end and causing a crash or potential security issue.
