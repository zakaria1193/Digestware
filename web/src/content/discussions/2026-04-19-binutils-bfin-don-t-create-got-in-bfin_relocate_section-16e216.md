---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- blackfin
- GOT
- segfault
discussion_id: aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
source_type: public_inbox
title: Don't create got in bfin_relocate_section
headline: 'Binutils/bfin: Don''t create .got in bfin_relocate_section'
tldr: Removes the creation of the .got section in `bfin_relocate_section` to avoid
  a segfault, instead reporting an unresolvable relocation error.
stakes: Prevents a potential segfault when linking Blackfin object files, especially
  when ABI mismatches are present, improving linker stability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- May expose existing ABI mismatch issues as linker errors instead of crashes.
- Simplifies the relocation process.
primer_expert: The patch reverts a change that created the `.got` section in `bfin_relocate_section`,
  which occurs late in the linking process. This late creation can lead to a segfault,
  especially with ABI mismatches. The fix involves reporting an error if the `.got`
  section is missing, relying on earlier checks (merge_private_bfd_data) to catch
  ABI incompatibilities. The Blackfin architecture uses a GOT for accessing global
  data.
primer_general: In the linking process, the Global Offset Table (GOT) is a data section
  used to hold the addresses of global variables. This allows position-independent
  code (PIC) to access global data without knowing the absolute address at compile
  time. This patch addresses a problem in the binutils linker when linking code for
  the Blackfin processor. By preventing the late creation of the GOT, this patch avoids
  potential crashes and ensures that linking process handles global variable addresses
  correctly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch removes the creation of the `.got` section within the `bfin_relocate_section` function in `elf32-bfin.c`. The original code created the `.got` section in `relocate_section`, which is too late in the linking process and can lead to a segfault. Instead, the patch now reports an unresolvable relocation error if the `.got` section has not already been created. This addresses a potential crash when linking incompatible Blackfin ABI object files.
