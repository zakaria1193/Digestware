---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- blackfin
- got
- relocation
- linker
discussion_id: aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
source_type: public_inbox
title: Don't create got in bfin_relocate_section
headline: Don't create got in bfin_relocate_section
tldr: This patch prevents the creation of the .got section in relocate_section for
  the Blackfin architecture, reverting a previous change that could lead to a segfau…
stakes: Fixes a potential segfault when linking Blackfin binaries, improving the stability
  of the toolchain.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes the creation of the .got section in relocate_section.
- May expose the original crash if --no-warn-mismatch is used and incompatible ABI
  objects are linked.
- Prevents segfaults due to late section creation.
exchanges: []
primer_expert: This patch reverts commit 7a84e3daf81a, which created the `.got` section
  in `bfin_relocate_section` in `bfd/elf32-bfin.c`. The patch now reports an unresolvable
  relocation error if the `.got` section does not exist, avoiding the late creation
  of sections in relocate_section. The `.got` (Global Offset Table) is used for position-independent
  code (PIC) and position-independent data (PID). The Blackfin architecture is a family
  of embedded processors.
primer_general: The `.got` (Global Offset Table) is a data section used in dynamically
  linked executables and shared libraries to hold the addresses of global variables
  and functions. This allows code to be loaded at different memory addresses without
  needing to be recompiled. This patch addresses a problem in the binutils linker
  for the Blackfin architecture, where the `.got` section was being created too late
  in the linking process, potentially leading to errors or crashes. The patch ensures
  that an error is reported if the `.got` section is missing, rather than attempting
  to create it at a late stage.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch reverts a change that created the `.got` section within `bfin_relocate_section`. Creating sections this late in the linking process is problematic. The original change was intended to prevent crashes when linking incompatible object files, but this patch handles this issue by reporting an unresolvable relocation error if `.got` has not already been created.
