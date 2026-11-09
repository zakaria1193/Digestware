---
project: binutils
subsystem: binutils/mips
patch_id: null
tags:
- binutils
- mips
- embedded
commit_hash: b13db0254577b781ee0a95682d42239cf72d9a95
source_type: public_inbox
author: '"Maciej W. Rozycki" <macro@sourceware.org>'
headline: 'MIPS: Add support for Octeon machine types in BFD and gold.'
tldr: Binutils now correctly identifies and handles MIPS Octeon processor types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch integrates MIPS Octeon machine types, including `AFL_EXT_OCTEON3`,
  into BFD's a.out handling and gold's processor classification. The `bfd_mach_mips_octeon*`
  variants are now correctly mapped in `bfd/aoutx.h`, and `bfd/elfxx-mips.c` is updated
  to translate `AFL_EXT_OCTEON3` to `bfd_mach_mips_octeon3`. Gold's `mips.cc` also
  gains support for these types, complementing prior work on Octeon 3 support.
primer_glossary:
- term: BFD
  definition: The Binary File Descriptor library, a GNU project that provides a common
    interface for reading and writing various object file formats, including ELF and
    a.out.
- term: a.out
  definition: A legacy executable file format, originating from Unix, that binutils
    and other tools need to support for older systems or specific use cases.
- term: gold
  definition: The GNU gold linker, a faster replacement for the traditional GNU ld
    linker, which supports ELF, Mach-O, and other object file formats.
- term: MIPS
  definition: A family of reduced instruction set computer (RISC) architectures widely
    used in embedded systems and networking equipment.
- term: Octeon
  definition: A family of highly integrated network processors developed by Cavium
    (now Marvell), based on the MIPS architecture and featuring multiple CPU cores.
- term: machine type
  definition: A specific identifier within an architecture (like MIPS) that denotes
    a particular processor core or configuration, influencing instruction set extensions
    and behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261108184442.B4E344BA2E2E@sourceware.org
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This commit adds missing support for MIPS Octeon processor types within binutils. It updates BFD's a.out handling and gold's MIPS machine type conversion to recognize `AFL_EXT_OCTEON3` and other Octeon variants, ensuring correct processing of binaries targeting these embedded systems.
