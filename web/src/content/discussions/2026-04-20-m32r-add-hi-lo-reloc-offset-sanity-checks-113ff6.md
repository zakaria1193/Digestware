---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- binutils
- relocation
- m32r
- fuzzing
discussion_id: aeXEBvhXwRjo2qaW@squeak.grove.modra.org
source_type: public_inbox
title: m32r hi/lo reloc offset sanity checks
headline: 'M32r: Add hi/lo reloc offset sanity checks'
tldr: Adds sanity checks for reloc offsets in the M32R architecture to prevent out-of-bounds
  memory access, fixing a fuzzer-discovered vulnerability.
stakes: Improves the security and stability of binutils by preventing potential crashes
  or vulnerabilities caused by invalid relocation offsets.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Slight performance overhead due to additional checks.
- Increased code complexity.
primer_expert: The patch addresses a fuzzer-discovered vulnerability in `elf32-m32r.c`
  related to relocation handling. Specifically, it adds checks to ensure that relocation
  offsets for HI16 and LO16 relocations are within the bounds of the section being
  relocated. Failure to do so can lead to out-of-bounds reads. `bfd_reloc_offset_in_range`
  provides the safe offset check.
primer_general: Relocations are adjustments made to executable or object code by the
  linker to account for different memory addresses where code and data are loaded.
  These adjustments are described by relocation entries which contain an offset indicating
  where in the code the adjustment needs to be made. This patch enhances the safety
  of the binutils, specifically the part that handles M32R binaries, by adding checks
  that these offsets are valid before the linker attempts to use them, preventing
  potential crashes or security issues.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch adds sanity checks for relocation offsets in the M32R architecture's `elf32-m32r.c` file. The checks prevent out-of-bounds memory access when handling HI16 and LO16 relocations, addressing a vulnerability identified by fuzzing. The patch also simplifies sign extension and removes unnecessary casts. An input_section parameter is added to m32r_elf_relocate_hi16.
