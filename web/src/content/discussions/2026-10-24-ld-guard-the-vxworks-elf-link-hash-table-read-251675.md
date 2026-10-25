---
project: binutils
subsystem: ld
patch_id: null
tags:
- security
- vxworks
- linker
- elf
- vulnerability
discussion_id: 20261024152218.2649262-3-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 2/2] ld: guard the vxworks ELF link hash table read'
headline: 'ld: guard the vxworks ELF link hash table read'
tldr: Fixes a heap-buffer-overflow in the VxWorks emulation by ensuring the link hash
  table is an ELF type before accessing its members.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes a heap-buffer-overflow vulnerability.
- Adds a necessary check for the specific type of link hash table.
- Improves the robustness of the VxWorks linker emulation.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes to add a check for `is_elf_hash_table` before accessing `dynamic_sections_created`
    in the VxWorks emulation to prevent heap-buffer-overflows.
  quote: 'An ELF output format does not imply an ELF link hash table: a linker script
    can select an ELF flavour backed by a generic hash table. Testing the flavour
    is not enough.'
primer_expert: This patch addresses a specific vulnerability in the VxWorks linker
  emulation. The `vxworks_after_open` function incorrectly assumes that if the output
  format is ELF, the underlying link hash table structure is `elf_link_hash_table`.
  However, a linker script can specify a generic ELF output format (`OUTPUT_FORMAT("elf32-little")`),
  which results in a generic `bfd_link_hash_table` being used. Accessing `dynamic_sections_created`
  (a member of `elf_link_hash_table`) on this generic structure leads to an out-of-bounds
  read.
primer_glossary:
- term: VxWorks
  definition: A real-time operating system (RTOS) commonly used in embedded systems.
- term: link hash table
  definition: A data structure used by the linker to efficiently manage symbols and
    sections during the linking process.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: heap-buffer-overflow
  definition: A security vulnerability where data is written beyond the boundaries
    of an allocated buffer on the heap, potentially corrupting adjacent memory.
series_id: 'binutils:ld: guard the vxworks elf link hash table read'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024152218.2649262-3-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This patch prevents a heap-buffer-overflow in the VxWorks emulation by adding a check to ensure the link hash table is specifically an ELF hash table before accessing the `dynamic_sections_created` member. Currently, a linker script can select a generic ELF flavor, which uses a generic `bfd_link_hash_table` instead of an `elf_link_hash_table`. Accessing `dynamic_sections_created` on a generic table results in an out-of-bounds read.
