---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- Blackfin
- GOT
- relocation
discussion_id: aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
source_type: public_inbox
title: Don't create got in bfin_relocate_section
headline: Don't create got in bfin_relocate_section
tldr: This patch prevents the linker from creating a .got section in `bfin_relocate_section`
  to avoid a segmentation fault when linking incompatible object files.
stakes: Fixes a potential crash when linking Blackfin object files with incompatible
  ABIs, improving linker stability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch reverts a previous change that introduced a potential
  segfault. The rationale for the revert seems sound.
technical_tradeoffs:
- May expose existing ABI mismatches that were previously hidden.
- Relies on earlier checks to detect ABI incompatibility.
primer: The Global Offset Table (.got) is a data section used in shared libraries
  and position-independent executables to hold absolute addresses of global variables.
  Relocation is the process of assigning load addresses for position-dependent code
  and data.  The Blackfin is a family of embedded microprocessors.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch removes the creation of a `.got` (Global Offset Table) section within the `bfin_relocate_section` function.  Instead, it makes the linker report an unresolvable relocation error if the `.got` section has not already been created. This resolves a potential segmentation fault when linking incompatible Blackfin ABI objects.
