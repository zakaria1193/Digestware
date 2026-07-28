---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- bfd
- elf
- security
- fuzzing
discussion_id: amb5fXXwmsjGAiy2@squeak.grove.modra.org
source_type: public_inbox
title: Use ufile_ptr for file position
headline: Use ufile_ptr for file position
tldr: Changes `file_ptr` to `ufile_ptr` in `elf.c` to safely handle file offsets and
  removecasts.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes a potential integer overflow vulnerability related to large file handling.
- Improves the safety and correctness of file offset calculations.
- Removes unnecessary type casts.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to change `file_ptr` to `ufile_ptr` for file positions
    in `bfd/elf.c`, resolving an overflow issue found by fuzzing `objcopy` and simplifying
    type casting.
  quote: 'This is in response to a fuzzed objcopy test that overflows file_ptr

    addition.  It makes sense to use an unsigned value for current file

    offset, and allows a couple of casts to be removed.'
primer_expert: This patch targets the BFD library's ELF backend, specifically within
  `bfd/elf.c`. It refactors the handling of file positions and offsets, changing the
  type used for these calculations from `file_ptr` (a signed integer type likely aliased
  to `long` or `off_t`) to `ufile_ptr` (an unsigned integer type, possibly `Elf64_Addr`
  or `uint64_t`). This change is motivated by a fuzzing-discovered overflow vulnerability
  when performing arithmetic on `file_ptr` related to large file offsets. Using an
  unsigned type ensures that operations on file positions, especially for very large
  files, are handled co…
primer_glossary:
- term: ufile_ptr
  definition: An unsigned integer type used to represent file offsets or positions,
    likely chosen for its ability to handle larger file sizes accurately and safely
    compared to signed types.
- term: file_ptr
  definition: A data type used to represent file offsets or positions, potentially
    a signed type that can lead to overflow issues with large files.
- term: bfd/elf.c
  definition: The C source file within the Binary File Descriptor library that handles
    ELF (Executable and Linkable Format) specific operations.
- term: objcopy
  definition: A GNU binary file manipulation utility that copies and translates object
    files from one format to another. It can also modify sections and symbols.
- term: fuzz test
  definition: A software testing technique that involves providing invalid, unexpected,
    or random data as input to a program to discover bugs or security vulnerabilities.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries on Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/amb5fXXwmsjGAiy2@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch replaces the `file_ptr` type with `ufile_ptr` for tracking file offsets within `bfd/elf.c`. This change directly addresses an issue where `file_ptr` addition could overflow, as discovered by an `objcopy` fuzz test. Using an unsigned type (`ufile_ptr`) for current file offsets provides greater safety and accuracy, allowing for the removal of unnecessary type casts and preventing potential bugs related to large file sizes.
