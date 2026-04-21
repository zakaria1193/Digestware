---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- m32r
- relocation
- security
- fuzzing
discussion_id: aeXEBvhXwRjo2qaW@squeak.grove.modra.org
source_type: public_inbox
title: m32r hi/lo reloc offset sanity checks
headline: M32r hi/lo reloc offset sanity checks
tldr: Adds sanity checks for relocation offsets in the m32r architecture to prevent
  fuzzer- выявлено crashes.
stakes: This patch improves the security and stability of binutils by preventing potential
  crashes caused by malformed object files.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds additional checks to the relocation process, which may slightly impact performance.
- Improves the security and stability of binutils by preventing potential crashes
  caused by malformed object files.
- The checks are specific to the M32R architecture and may not be applicable to other
  architectures.
exchanges: []
primer_expert: This patch focuses on the M32R architecture's ELF relocation handling
  in binutils (`bfd/elf32-m32r.c`). It addresses potential out-of-bounds reads during
  relocation by adding checks to `m32r_elf_hi16_reloc` and `m32r_elf_lo16_reloc` to
  ensure that relocation offsets are within the bounds of the input section. The patch
  also modifies `m32r_elf_relocate_hi16` to include the input section and return a
  status.
primer_general: Relocation is the process of adjusting addresses in object files or
  executables when they are linked or loaded into memory. This patch focuses on the
  M32R architecture and adds checks to ensure that the relocation process does not
  attempt to access memory outside the valid bounds of the input section. This helps
  prevent crashes and security vulnerabilities.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch adds sanity checks for relocation offsets when processing M32R ELF files, specifically for HI16 and LO16 relocations. These checks prevent out-of-bounds memory accesses that can be triggered by maliciously crafted or corrupted object files, addressing a fuzzer-identified vulnerability.
