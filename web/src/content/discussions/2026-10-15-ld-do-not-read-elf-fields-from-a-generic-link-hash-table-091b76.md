---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- ELF
- security
- heap overflow
discussion_id: 20261015093017.3106937-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 2/2] ld: do not read ELF fields from a generic link hash table'
headline: 'ld: do not read ELF fields from a generic link hash table'
tldr: The linker now checks if the link hash table is an ELF table before accessing
  ELF-specific fields, preventing heap buffer overflows.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adding a check increases code complexity slightly but significantly improves security.
- Ensures correct behavior across different ELF output formats and generic hash table
  usage.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes a fix to prevent out-of-bounds reads in the linker by checking
    for ELF hash table type before accessing ELF-specific fields.
  quote: 'ldelf_after_open_output assumes that an ELF output BFD implies an ELF

    link hash table.  A linker script can select an ELF flavour that uses

    the generic hash table, for example OUTPUT_FORMAT("elf64-nfp").  The

    hook then reads hash_table_id, which is past the end of the generic

    table (AddressSanitizer: heap-buffer-overflow).


    Check is_elf_hash_table before reading the table, as most other uses

    of l…'
primer_expert: This patch addresses a heap buffer overflow in the `ldelf_after_open_output`
  function within the GNU linker (`ld`). The issue arises when a linker script specifies
  an ELF output format that utilizes a generic link hash table instead of an ELF-specific
  one (e.g., `OUTPUT_FORMAT("elf64-nfp")`). In such cases, the function incorrectly
  assumes an ELF hash table and attempts to read ELF-specific fields like `hash_table_id`,
  leading to an out-of-bounds read. The fix introduces a check `is_elf_hash_table`
  to ensure the hash table is of the expected ELF type before accessing these fields.
  This is par…
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: link hash table
  definition: A data structure used by the linker to efficiently store and retrieve
    information about symbols and object files during the linking process.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executable files, shared libraries, and core dumps on Unix-like systems.
- term: generic link hash table
  definition: A non-ELF specific version of the link hash table used by the linker,
    which might be employed when targeting non-ELF output formats or specific ELF
    configurations.
- term: heap-buffer-overflow
  definition: A type of security vulnerability that occurs when a program writes data
    beyond the allocated buffer on the heap, potentially corrupting adjacent memory
    or control structures.
series_id: 'binutils:ld: do not read elf fields from a generic link hash table'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261015093017.3106937-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This patch addresses an out-of-bounds read vulnerability in the linker (ld). When a linker script specifies an ELF flavor that uses a generic link hash table (e.g., OUTPUT_FORMAT("elf64-nfp")), the `ldelf_after_open_output` hook incorrectly attempts to read ELF-specific fields like `hash_table_id`. This patch adds a check for `is_elf_hash_table` to ensure that these fields are only accessed when the hash table is indeed an ELF type, thereby preventing heap buffer overflows. A related test case is also extended.
