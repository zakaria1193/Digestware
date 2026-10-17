---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- relaxation
- bfd
- elf
- security
discussion_id: 20261016123644.1429854-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 1/8] bfd: add _bfd_elf_relax_delete_range_ok'
headline: 'bfd: add _bfd_elf_relax_delete_range_ok'
tldr: Introduces a shared function to validate ELF relaxation byte deletion ranges.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Introduces a reusable safety check, improving code quality and reducing duplication.
- Directly addresses a heap corruption vulnerability.
- Adds a new error reporting mechanism (`bfd_error_bad_value`).
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Adds `_bfd_elf_relax_delete_range_ok` to `bfd/elf.c` to validate byte
    deletion ranges during ELF relaxation.
  quote: 'Introduce shared helper _bfd_elf_relax_delete_range_ok in bfd/elf.c to

    validate deletion intervals.  The helper takes toaddr and checks

    addr <= toaddr, count <= toaddr - addr, and toaddr <= sec->size.  On

    failure, report a descriptive bfd_error_bad_value error message.'
primer_expert: 'This patch adds a foundational helper function, `_bfd_elf_relax_delete_range_ok`,
  to the BFD library''s common ELF code in `bfd/elf.c`. This function addresses a
  critical vulnerability in linker relaxation: when sections are shrunk by deleting
  bytes, the `memmove` operation''s size calculation (`toaddr - addr - count`) can
  underflow if `count` exceeds `toaddr - addr`. This function enforces `addr <= toaddr`
  and `toaddr <= sec->size` to prevent this underflow and associated heap corruption,
  reporting a specific error on failure.'
primer_glossary:
- term: linker relaxation
  definition: A linker optimization process that adjusts instruction addresses and
    sizes at link time to improve code density or enable features like position-independent
    code. It may involve deleting or replacing instructions.
- term: BFD
  definition: Binary File Descriptor library, a GNU library used by binutils and other
    tools to abstract access to various executable file formats.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: memmove
  definition: A C standard library function that copies a block of memory from a source
    location to a destination location. It handles overlapping memory regions safely.
- term: underflow
  definition: In the context of memory or arithmetic operations, underflow occurs
    when a value becomes smaller than the minimum representable value. For unsigned
    integers, this typically results in wrap-around to a very large positive number.
- term: heap buffer overflow
  definition: A type of security vulnerability where a program writes data beyond
    the allocated buffer boundary on the heap, potentially corrupting adjacent memory
    or control structures.
series_id: 'binutils:bfd: add _bfd_elf_relax_delete_range_ok'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch introduces a new shared helper function, `_bfd_elf_relax_delete_range_ok`, within the BFD library's ELF support (`bfd/elf.c`). This function is designed to validate the parameters (address, count, and target address) for shifting section contents when deleting bytes during linker relaxation. It prevents unsigned subtractions from underflowing to `SIZE_MAX` by checking that the deletion range is within section bounds, thereby avoiding heap buffer overflows and crashes. On failure, it reports a `bfd_error_bad_value` error.
