---
project: binutils
subsystem: binutils
patch_id: null
tags:
- m32r
- relocation
- sanity check
- fuzzing
- security
discussion_id: aeXEBvhXwRjo2qaW@squeak.grove.modra.org
source_type: public_inbox
title: m32r hi/lo reloc offset sanity checks
headline: m32r hi/lo reloc offset sanity checks
tldr: This patch adds sanity checks for relocation offsets in the m32r architecture
  to prevent a crash caused by a fuzzer.
stakes: Improves the robustness of binutils by preventing crashes due to malformed
  input, enhancing security.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds additional checks, potentially increasing the runtime of the linker.
- Improves robustness by preventing crashes due to invalid relocation offsets.
- No new features added.
exchanges: []
primer_expert: This patch modifies `bfd/elf32-m32r.c` to add relocation offset sanity
  checks to the m32r architecture's ELF handling code.  This prevents out-of-bounds
  reads caused by crafted ELF files with invalid relocation offsets.  The patch adds
  checks to `m32r_elf_hi16_reloc`, `m32r_elf_relocate_hi16`, and `m32r_elf_lo16_reloc`
  to validate the offsets before accessing the section contents.  This is a security
  fix to address a fuzzer-discovered vulnerability.
primer_general: Relocation is the process of adjusting addresses in object files or
  executables when they are linked or loaded into memory.  The ELF format uses relocation
  entries to specify how these adjustments should be made. This patch adds checks
  to ensure that the relocation offsets are valid for the Renesas M32R architecture.  These
  checks prevent the linker from attempting to read or write data outside of the allocated
  memory for the section which can lead to crashes or security vulnerabilities. Fuzzing
  is a testing technique that involves providing a program with randomly generated
  inputs to try and trigger unexpected behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses a potential security vulnerability found by fuzzing. It enhances the sanity checks for relocation offsets in the m32r architecture's ELF handling code. Specifically, it checks the relocation offsets in `m32r_elf_hi16_reloc` and `m32r_elf_lo16_reloc` functions, and adds checks to `m32r_elf_relocate_hi16` to ensure offsets are within bounds before accessing section contents.
