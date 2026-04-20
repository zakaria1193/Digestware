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
headline: m32r hi/lo reloc offset sanity checks
tldr: This patch adds sanity checks to relocation offsets for the m32r architecture
  to prevent crashes from malformed binaries.
stakes: Improves the security and stability of the toolchain by preventing crashes
  caused by maliciously crafted or corrupted binaries.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds additional checks, which may slightly increase relocation processing time.
- Improves security by preventing out-of-bounds memory access.
- May reject some malformed binaries that were previously processed without error.
exchanges: []
primer_expert: This patch addresses a security issue in the m32r ELF backend related
  to relocation processing. Specifically, it adds checks to ensure that relocation
  offsets are within the bounds of the section, preventing potential out-of-bounds
  memory accesses during relocation. The functions `m32r_elf_hi16_reloc`, `m32r_elf_relocate_hi16`,
  and `m32r_elf_lo16_reloc` are modified to include these checks.
primer_general: Relocation is the process of adjusting addresses in a compiled program
  when it is linked or loaded into memory.  The binutils toolchain handles relocation
  for various architectures and file formats. This patch focuses on the m32r architecture,
  adding checks to ensure that the offsets used during relocation are valid. This
  prevents potential security vulnerabilities where a malformed executable could cause
  the toolchain to access memory outside of the intended bounds, leading to a crash
  or potentially arbitrary code execution.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

Alan Modra submits a patch that fixes a fuzzer-discovered vulnerability in the binutils handling of m32r relocations. The patch adds sanity checks for relocation offsets in `m32r_elf_hi16_reloc` and `m32r_elf_lo16_reloc` functions, and also adds an input_section parameter and return status to `m32r_elf_relocate_hi16`.
