---
project: binutils
subsystem: bfd/epiphany
patch_id: null
tags:
- bfd
- epiphany
- cleanup
- compiler-warning
commit_hash: da76bc467dcfaf1df603b3e2bf9e50c6a3ceae2c
source_type: public_inbox
author: Simon Marchi <simark@sourceware.org>
headline: Unused variable removed from epiphany BFD ELF handling
tldr: The unused `epiphany_relaxed` variable has been removed from BFD's Epiphany
  ELF object file handling.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `epiphany_relaxed` global variable in `bfd/elf32-epiphany.c` was
  intended to track whether relaxation was enabled for Epiphany ELF objects. However,
  it was set but never read, leading to an unused-variable warning with `-Werror`.
  This commit removes the variable entirely, simplifying the code for the Epiphany
  backend within BFD.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by binutils
    to parse and manipulate various executable file formats.
- term: Epiphany
  definition: A microcontroller architecture developed by Imagination Technologies.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries on many Unix-like systems.
- term: relaxation
  definition: A linker optimization technique where symbolic addresses are replaced
    with actual addresses during the linking process, potentially adjusting instruction
    offsets for shorter encodings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261110194731.0D22D4BA2E0D@sourceware.org
date: '2026-11-10'
is_stub: true
stub_reason: low_score
---

This commit removes the `epiphany_relaxed` global variable from BFD's ELF handling for the Epiphany architecture. The variable was declared but never used since its introduction in 2011. Its removal cleans up the code and resolves a compiler warning about unused variables when using recent Clang versions.
