---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- Blackfin
- ABI
- relocation
discussion_id: aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
source_type: public_inbox
title: Don't create got in bfin_relocate_section
headline: Don't create .got in bfin_relocate_section.
tldr: The Blackfin ABI mandates that .got be created before relocate_section to avoid
  segfaults or unresolved relocation errors.
stakes: Fixes a potential segfault when linking incompatible object files for the
  Blackfin architecture.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Avoids creating sections too late in the linking process.
- Enforces stricter adherence to the Blackfin ABI.
- May expose pre-existing issues with missing .got sections.
primer_expert: The Blackfin ABI requires the .got section to exist before `relocate_section`
  to avoid crashes when linking objects with mismatched PIC/non-PIC expectations.  Creating
  the .got in `relocate_section` is too late. Failure to create .got earlier should
  result in an unresolvable relocation error. Interaction with `merge_private_bfd_data`
  flags ABI mismatches earlier.
primer_general: The Global Offset Table (.got) is a data section used in shared libraries
  and position-independent executables (PIE) to hold the addresses of global variables.  The
  compiler doesn't know where these globals will be loaded in memory, so the .got
  provides a level of indirection.  The linker fills in the .got entries with the
  actual runtime addresses. This proposal concerns the Blackfin architecture ABI within
  binutils, specifically the creation and handling of the .GOT during relocation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

This patch removes the creation of the .got (Global Offset Table) section within the `bfin_relocate_section` function.  Instead, it enforces that the .got section must already exist before relocation occurs, reporting an error if it doesn't. This change aligns with the Blackfin ABI requirements and prevents potential issues when linking incompatible object files.
