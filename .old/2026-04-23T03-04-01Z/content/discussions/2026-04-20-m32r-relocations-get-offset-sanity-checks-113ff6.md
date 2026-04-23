---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- m32r
- relocation
- fuzzing
- security
discussion_id: aeXEBvhXwRjo2qaW@squeak.grove.modra.org
source_type: public_inbox
title: m32r hi/lo reloc offset sanity checks
headline: M32R relocations get offset sanity checks
tldr: Adds relocation offset sanity checks for M32R architecture to prevent fuzzer-induced
  crashes.
stakes: Improves the robustness of binutils when processing M32R binaries, preventing
  crashes caused by malformed relocation offsets.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding sanity checks introduces a small performance overhead.
- The checks prevent crashes caused by invalid relocation offsets.
- The patch simplifies some existing code, improving readability.
exchanges:
- author: Alan Modra
  role: proposer
  position: Proposes adding sanity checks for relocation offsets in M32R architecture
    to prevent crashes.
  quote: This fixes another fuzzer attack.
primer_expert: This patch focuses on `bfd/elf32-m32r.c`, which implements ELF-specific
  handling for the M32R architecture within the Binary File Descriptor (BFD) library.
  The changes address potential out-of-bounds reads due to invalid relocation offsets.
  The functions `m32r_elf_hi16_reloc` and `m32r_elf_lo16_reloc` are responsible for
  processing HI16 and LO16 relocations, respectively. The patch adds checks to ensure
  that the offsets used to access section contents are within the bounds of the section,
  preventing crashes.
primer_general: Relocations are instructions that tell the linker how to modify addresses
  in a program's code or data when it's linked or loaded into memory.  The M32R is
  a type of computer processor architecture, and this patch improves the safety of
  handling relocations for programs compiled for this processor.  Specifically, it
  adds checks to make sure that the relocation instructions are valid and don't try
  to access memory outside of the allowed region, preventing crashes. The changes
  are in the BFD library, which is used to read and write different types of object
  files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch adds sanity checks for relocation offsets in the M32R architecture's ELF handling code. It fixes a fuzzer-discovered issue where invalid relocation offsets could lead to crashes. The changes include checks in `m32r_elf_hi16_reloc` and `m32r_elf_lo16_reloc` to ensure that relocation offsets are within the valid range of the section.
