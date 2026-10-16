---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- x86
- ELF
- security
- heap overflow
discussion_id: 20261015093017.3106937-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/2] bfd: elfxx-x86: reject non-x86 target ids in elf_x86_hash_table'
headline: 'bfd: elfxx-x86: reject non-x86 target ids in elf_x86_hash_table'
tldr: The x86 ELF backend now rejects non-x86 target IDs, preventing heap buffer overflows
  when linker scripts retarget output BFDs.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Strictly enforcing target IDs prevents certain retargeting scenarios but significantly
  enhances security.
- Adding checks and early returns makes the code more robust against misconfigurations.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes to reject non-x86 target IDs in the x86 ELF hash table function
    to prevent heap buffer overflows caused by retargeting linker scripts.
  quote: 'A linker script can retarget the output BFD, for example with

    OUTPUT_FORMAT("elf64-bpfle").  The x86 emulation still calls

    bfd_elf_linker_x86_set_options.  That function takes the target id

    from the output BFD.  The id and the hash table both belong to the

    foreign backend, so the target id check passes.  The write to

    htab->params then overflows the heap block (AddressSanitizer:

    heap-buffer-overfl…'
primer_expert: This patch addresses a heap buffer overflow in the x86 ELF backend
  of binutils. The vulnerability occurs when a linker script uses `OUTPUT_FORMAT`
  to specify a non-x86 target (e.g., `elf64-bpfle`). The x86 emulation code, specifically
  `bfd_elf_linker_x86_set_options`, is still invoked. It retrieves the target ID from
  the output BFD, which belongs to the foreign backend, and uses it to access the
  `elf_x86_hash_table`. This leads to an out-of-bounds write because the hash table
  is not actually an x86 one. The fix ensures that `elf_x86_hash_table` returns NULL
  for non-x86 IDs and that `bfd_elf_l…
primer_glossary:
- term: bfd
  definition: Binary Description Format, a library within GNU Binutils that provides
    a common interface to various object file formats.
- term: elfxx-x86
  definition: The specific backend within binutils that handles ELF object files for
    the x86 architecture.
- term: OUTPUT_FORMAT
  definition: A linker script command used to specify the output file format.
- term: heap-buffer-overflow
  definition: A type of security vulnerability that occurs when a program writes data
    beyond the allocated buffer on the heap, potentially corrupting adjacent memory
    or control structures.
- term: target ID
  definition: An identifier that specifies the target architecture and ABI for which
    an object file is being produced.
series_id: 'binutils:bfd: elfxx-x86: reject non-x86 target ids in elf_x86_hash_table'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261015093017.3106937-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This patch fixes a heap buffer overflow in the x86 ELF backend of binutils. When a linker script retargets the output BFD to a non-x86 format (e.g., `OUTPUT_FORMAT("elf64-bpfle")`), the x86 emulation hook still runs. The function `bfd_elf_linker_x86_set_options` incorrectly uses the foreign target ID to access the hash table parameters, leading to an out-of-bounds write. This patch modifies `elf_x86_hash_table` to return NULL for non-x86 target IDs and adds an early return in `bfd_elf_linker_x86_set_options` to prevent this overflow. A test case is also added.
