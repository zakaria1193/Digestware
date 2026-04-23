---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- elf
- blackfin
- got
- relocation
discussion_id: aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
source_type: public_inbox
title: Don't create got in bfin_relocate_section
headline: Don't create got in bfin_relocate_section
tldr: This patch prevents the creation of a .got section in `bfin_relocate_section`
  to avoid a segfault when linking incompatible object files.
stakes: Prevents a segfault when linking Blackfin object files with incompatible ABIs,
  improving linker stability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- May reintroduce the original crash if `--no-warn-mismatch` is used to suppress ABI
  mismatch errors.
- Simplifies the relocation process by removing late section creation.
- Improves linker stability by ensuring correct section ordering.
exchanges: []
primer_expert: The patch modifies `bfd/elf32-bfin.c`, specifically the `bfin_relocate_section`
  function. It removes the code that creates the `.got` section within this function.  Instead,
  it checks if the `.got` section exists and reports an error if it doesn't. This
  ensures that the `.got` section is created earlier in the linking process, preventing
  potential issues with section ordering and output.
primer_general: When linking object files, the linker combines different sections
  of code and data into a single executable. The Global Offset Table (GOT) is a section
  used to store the addresses of global variables. This patch fixes a problem in the
  binutils linker for the Blackfin processor where the GOT was being created too late
  in the linking process, potentially leading to errors or crashes.  The patch ensures
  that the GOT is created at the correct time, preventing these issues.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch reverts a change introduced by commit 7a84e3daf81a which created a `.got` section in `bfin_relocate_section`. The commit aimed to fix a crash when linking incompatible object files (normal vs. FD-PIC).  However, creating sections this late in the linking process is problematic and can lead to issues.  The patch now reports an unresolvable relocation error if `.got` has not already been created.
