---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- elf
- performance
- cleanup
commit_hash: f2fa1a5ec2e1a7ae206ed3790e9b2ff975b88aec
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Remove duplicate symbol lookups in ELF backends
tldr: Eliminates redundant local symbol lookups in the `check_relocs` function across
  several ELF backends.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Several ELF backends in BFD were performing a local symbol lookup (e.g.,
  via `bfd_sym_lookup` or similar) within their `check_relocs` function, even when
  the result was not used or was redundant. This commit consolidates these lookups
  by performing the lookup once and reusing the result, or removing the lookup entirely
  if unnecessary. It also trims an old comment in some files.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to parse and manipulate various object file formats.
- term: ELF
  definition: Executable and Linkable Format. A common standard for object file formats
    on Unix-like systems.
- term: relocation
  definition: The process of updating symbolic references (like function or variable
    addresses) in relocatable object files to their final addresses when linked into
    an executable or shared library.
- term: backend
  definition: In the context of a compiler or linker, a backend refers to the part
    of the toolchain that handles a specific target architecture or object file format.
- term: symbol lookup
  definition: The process of searching for information about a symbol (e.g., a function
    or variable name) within an object file or executable.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261028223705.BF1EA4BA23CB@sourceware.org
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit addresses a performance and code duplication issue by removing redundant local symbol lookups within the `check_relocs` function in multiple ELF backends. The affected backends include csky, i386, s390, x86-64, aarch64, kvx, and riscv. This change simplifies the code and avoids repeated lookups.
