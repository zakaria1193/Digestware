---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- m32r
- elf
- relocation
- fuzzing
discussion_id: aeXEBvhXwRjo2qaW@squeak.grove.modra.org
source_type: public_inbox
title: m32r hi/lo reloc offset sanity checks
headline: m32r hi/lo reloc offset sanity checks
tldr: This patch adds sanity checks for relocation offsets in the M32R ELF backend
  to prevent crashes caused by malformed binaries.
stakes: This patch improves the robustness of the linker, preventing crashes when
  processing untrusted or malformed binaries.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds overhead to relocation processing due to the added checks.
- May reject valid binaries if the relocation information is slightly out of bounds
  (though this is unlikely).
- Improves security and stability by preventing crashes due to invalid relocation
  offsets.
exchanges: []
primer_expert: The patch targets `bfd/elf32-m32r.c`, specifically the handling of
  HI16 and LO16 relocations for the M32R architecture. It ensures that relocation
  offsets are within the bounds of the input section to prevent out-of-bounds memory
  accesses.  The `bfd_reloc_offset_in_range` function is used to perform the offset
  validation.
primer_general: When linking object files, the linker uses relocation information
  to update addresses in the code. This patch fixes a potential security issue in
  the binutils linker when processing M32R (Mitsubishi 32-bit RISC) object files.  It
  adds checks to ensure that the offsets specified in the relocation information are
  valid, preventing the linker from reading or writing to invalid memory locations,
  which could lead to a crash or potentially arbitrary code execution.  Fuzzers are
  tools that automatically generate potentially malformed inputs to find such vulnerabilities.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses a fuzzer-discovered vulnerability in the M32R ELF backend of binutils. It adds sanity checks to the `m32r_elf_hi16_reloc` and `m32r_elf_lo16_reloc` functions to validate relocation offsets before accessing section contents. It also simplifies sign extension and makes minor adjustments to function calls.
