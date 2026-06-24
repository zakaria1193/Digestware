---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- binutils
- pe-coff
- bigobj
- linker
- windows
discussion_id: 20260623213900.2000-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH v2] PE/COFF: auto-promote oversized objects to bigobj'
headline: Binutils auto-promotes oversized PE/COFF objects to bigobj format
tldr: This patch enables Binutils to automatically convert oversized PE/COFF object
  files to the `bigobj` format when the 16-bit section limit is exceeded.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Automatic promotion to `bigobj` resolves section limit issues but might implicitly
  increase object file size or introduce compatibility concerns with older toolchains
  that do not fully support `bigobj`.
exchanges:
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: proposer
  position: Proposes to auto-promote oversized PE/COFF object files to the `bigobj`
    format when the 16-bit section limit is reached, making the process transparent
    for supported toolchains.
  quote: Teach coff_compute_section_file_positions to switch PE/COFF output to the
    corresponding bigobj target when the normal section-number limit is exceeded.
    This preserves the existing hard error for targets without bigobj support, but
    lets supported PE targets transparently emit a valid bigobj object instead of
    requiring manual selection.
primer_expert: PE/COFF (Portable Executable/Common Object File Format) is the standard
  object file and executable format for Windows. A limitation of the traditional PE/COFF
  format is its use of 16-bit section numbers, which caps the number of sections a
  single object file can have. For modern C++ projects using aggressive optimization
  (like `/Gw` or `-ffunction-sections`) or extensive template metaprogramming, this
  limit is easily exceeded, leading to compilation failures. Microsoft introduced
  the `bigobj` format to address this, extending section numbers to 32 bits. This
  patch modifies `bfd/coffcode.h` wi…
primer_general: When you write a program, the compiler breaks your code into different
  parts called "sections" (e.g., one section for code, another for data). The output
  of this compilation is an "object file." For programs compiled for Windows, these
  object files use a format called PE/COFF. A problem with the standard PE/COFF format
  is that it can only handle a limited number of these sections. If you write a very
  large program, or use certain advanced C++ features, you might exceed this limit,
  causing the compiler or linker to fail with an error like "too many sections." To
  solve this, Microsoft introduced a special version called `bigobj`, which allows
  for many more sections. This proposal updates the GNU Binutils (a set of tools for
  creating and managing program binaries) to automatically use the `bigobj` format
  whenever a PE/COFF object file gets too large. This means developers won't have
  to manually tell the tools to use `bigobj`, making the compilation process smoother
  and preventing unexpec…
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260623213900.2000-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-06-23'
is_stub: false
---

This patch (v2) for Binutils introduces automatic promotion of oversized PE/COFF object files to the `bigobj` format. Standard PE/COFF files are limited to 16-bit section numbers, leading to "too many sections" errors for large projects. While BFD already supports `bigobj`, users currently have to explicitly select it. This change modifies `coff_compute_section_file_positions` to transparently switch to `bigobj` when the section limit is hit, preventing errors and providing a seamless experience for supported backends.
