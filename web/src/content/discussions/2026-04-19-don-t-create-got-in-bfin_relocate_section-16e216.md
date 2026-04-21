---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- elf
- blackfin
- relocation
- got
discussion_id: aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
source_type: public_inbox
title: Don't create got in bfin_relocate_section
headline: Don't create got in bfin_relocate_section
tldr: Removes the creation of a .got section in `bfin_relocate_section` to prevent
  a segmentation fault during linking of incompatible object files.
stakes: This patch prevents a potential crash during the linking process, improving
  the stability of the toolchain.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes code that attempts to create a .got section during relocation.
- May expose errors earlier in the linking process when a .got section is required
  but is missing.
- Prevents potential segfaults during linking of incompatible object files.
exchanges: []
primer_expert: The Blackfin architecture's ELF ABI requires a Global Offset Table
  (GOT) for position-independent code.  The GOT provides a mechanism for accessing
  global data at runtime. This patch reverts commit 7a84e3daf81a which created .got
  in relocate_section, and instead flags an error if the section is missing. Relevant
  code is in `bfd/elf32-bfin.c`.
primer_general: When linking object files into an executable, the linker resolves
  references between different parts of the code.  For position-independent code (PIC),
  the Global Offset Table (GOT) is used to store the addresses of global variables.
  This patch fixes a bug in the binutils linker for the Blackfin architecture where
  the GOT was being created too late in the linking process, potentially leading to
  a crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch removes the creation of the `.got` (Global Offset Table) section within the `bfin_relocate_section` function in `bfd/elf32-bfin.c`. Creating the `.got` section in `relocate_section` is considered too late in the linking process.  The correct behavior is to report an unresolvable relocation error if the `.got` section has not already been created.
