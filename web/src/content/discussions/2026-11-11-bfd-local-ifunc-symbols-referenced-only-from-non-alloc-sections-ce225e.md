---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- IFUNC
- ELF
- BFD
- bugfix
discussion_id: 20261111110350.3761956-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/7] bfd: local IFUNC symbols referenced only from non-alloc sections'
headline: 'bfd: local IFUNC symbols referenced only from non-alloc sections'
tldr: Fixes binutils linker to correctly handle local IFUNC symbols referenced only
  from non-alloc sections across multiple architectures.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds a new helper function to BFD, increasing library complexity but improving code
  reuse.
- Applies a consistent logic across architectures, potentially masking subtle architecture-specific
  behaviors if not carefully implemented.
- Introduces new test cases for various scenarios, expanding the test suite.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes a series of patches to fix the binutils linker's handling of
    local IFUNC symbols referenced only from non-alloc sections, by introducing a
    common helper function and applying it to multiple architectures.
  quote: A local STT_GNU_IFUNC symbol gets its hash entry (on s390, its PLT slot)
    from the relocation scan, which skips non-SEC_ALLOC sections. When only such a
    section refers to the symbol, relocate_section aborts on i386, x86-64, AArch64,
    RISC-V, SPARC and LoongArch, and s390 fails the link with no diagnostic or uses
    an unallocated PLT slot. A global symbol in the same place links. "gcc -g -O2"
    hits thi…
primer_expert: This series tackles a linker bug (PR ld/34988) where local IFUNC symbols
  are not linked correctly if their sole references reside in non-allocatable sections
  (e.g., debug info). The linker's standard relocation scan omits these sections,
  causing a lack of necessary symbol information. The solution involves creating a
  unified BFD helper (`_bfd_elf_ifunc_nonalloc_reloc`) to manage these IFUNCs, then
  applying this logic to specific architectures like x86 and AArch64. This brings
  their behavior in line with global IFUNCs, ensuring either successful linking, a
  skipped relocation, or a diagnostic e…
primer_glossary:
- term: STT_GNU_IFUNC
  definition: A symbol type in the ELF format that represents an indirect function.
    The linker and dynamic loader resolve this symbol to a specific function pointer
    at runtime, allowing for architecture-specific or version-specific function implementations.
- term: non-alloc section
  definition: An ELF section that is not loaded into memory when the program is executed.
    These sections are often used for debugging information, notes, or other metadata.
- term: relocation scan
  definition: The process by which the linker identifies and resolves references between
    different parts of an executable or library. This involves examining relocation
    entries in object files.
- term: hash entry
  definition: A data structure within an ELF file that helps speed up symbol lookups,
    particularly for dynamic linking. For IFUNC symbols, a hash entry is important
    for runtime resolution.
- term: IFUNC
  definition: Indirect Function. Similar to STT_GNU_IFUNC, it's a mechanism to select
    a function implementation at runtime based on certain criteria.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers. It stores
    information about variables, types, and source code locations.
series_id: 'binutils:bfd: local ifunc symbols referenced only from non-alloc sections'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261111110350.3761956-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

This patch series addresses a bug in the binutils linker (PR ld/34988) where local STT_GNU_IFUNC symbols fail to link when their only references come from non-allocatable sections. The linker's relocation scan intentionally skips these sections, preventing the necessary hash entry creation. The series introduces a common BFD helper function for handling these cases and then applies this logic to x86, AArch64, RISC-V, and SPARC. This ensures consistent behavior, mirroring how global IFUNC symbols are handled, and provides appropriate error messages when resolution is not possible.
