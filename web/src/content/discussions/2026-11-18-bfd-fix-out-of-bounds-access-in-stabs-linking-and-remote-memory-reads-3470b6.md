---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- security
- vulnerability
- stabs
- elf
discussion_id: CAO9RCZUT=3VECw6t8aMQVct_66-S4iyZJAZOgZXxdkHFQ8QvEg@mail.gmail.com
source_type: public_inbox
title: '[PATCH] bfd: fix out-of-bounds access in stabs linking and remote memory reads'
headline: 'BFD: Fix out-of-bounds access in stabs linking and remote memory reads'
tldr: Patches BFD to prevent out-of-bounds memory access during stabs processing and
  remote memory reads by adding necessary bounds checks.
proposer: mustafa <mustafa@medios.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Enhances security and robustness by preventing memory corruption vulnerabilities.
- Introduces additional checks that may have a minor performance impact during parsing
  of stabs and remote memory operations.
exchanges:
- author: mustafa
  role: proposer
  position: Submits a patch to fix out-of-bounds memory access in BFD related to stabs
    linking and remote memory reads.
  quote: 'Two places in bfd trust offsets from the input without checking them.


    _bfd_link_section_stabs, when it looks ahead after an N_BINCL, builds

    a pointer from stabstrbuf, the running string offset and the n_strx of

    the N_BINCL entry and reads it up to a NUL.  The check that is done

    for the entries in the main loop is missing here, so a large n_strx

    makes ld read far outside the .stabstr buffer and c…'
primer_expert: This patch addresses two distinct vulnerabilities in BFD. The first,
  in `bfd/stabs.c`, concerns `_bfd_link_section_stabs` where the look-ahead for `N_BINCL`
  entries doesn't validate the `n_strx` against the `.stabstr` table size, leading
  to potential reads beyond the buffer. The second, in `bfd/elfcode.h`, affects `bfd_from_remote_memory`
  by performing unchecked 64-bit arithmetic on ELF header fields (`p_offset + p_filesz`,
  `e_shoff + e_shnum * e_shentsize`) and segment end calculations, which can result
  in integer overflow and incorrect memory region validation. The fixes add necessary
  bound…
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a part of GNU Binutils providing a common
    API for various object file formats.
- term: stabs
  definition: A debugging information format used in older Unix systems and still
    supported by some compilers and tools. It stores symbolic information in a structured
    text format within object files.
- term: N_BINCL
  definition: A stab entry type that signifies the beginning of a file inclusion,
    similar to a preprocessor `#include` directive.
- term: .stabstr
  definition: The string table associated with stab debugging information, containing
    the textual representation of stab entries.
- term: out-of-bounds access
  definition: An error condition where a program attempts to read or write memory
    outside the allocated buffer or array boundaries.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps used on many Unix-like systems.
- term: segment
  definition: In ELF, a program segment (defined by a Program Header) that is loadable
    into memory.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAO9RCZUT=3VECw6t8aMQVct_66-S4iyZJAZOgZXxdkHFQ8QvEg@mail.gmail.com
bugzilla_url: null
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This patch addresses two distinct out-of-bounds memory access vulnerabilities in the BFD library. The first, in `stabs.c`, allows a malformed `.stabstr` table with an invalid string index after an `N_BINCL` entry to cause `ld` to read past the buffer. The second, in `elfcode.h`'s `bfd_from_remote_memory`, involves unchecked 64-bit additions for segment and section header ends, which can lead to wrapped values and subsequent buffer overflows. The fixes introduce crucial bounds checks for string indices and arithmetic operations to prevent these issues.
