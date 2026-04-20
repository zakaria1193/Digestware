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
tldr: Adds sanity checks for relocation offsets in the M32R architecture to prevent
  fuzzer-induced attacks.
stakes: Improves the security and reliability of binutils by preventing out-of-bounds
  memory access during relocation.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds runtime overhead for the added sanity checks.
- Improves security by preventing potential vulnerabilities.
- May expose previously hidden bugs in malformed input files.
primer_expert: This patch focuses on the M32R backend in binutils' ELF handling (`elf32-m32r.c`).
  It addresses potential vulnerabilities related to HI16 and LO16 relocations by adding
  offset validation. The changes include adding an `input_section` parameter and return
  status to `m32r_elf_relocate_hi16`.
primer_general: Relocation is the process of adjusting addresses in object files and
  executables so that they can be loaded at different memory locations. Binutils handles
  relocation as part of the linking and loading process.  This patch adds checks to
  ensure that the offsets used during relocation are valid, preventing potential security
  vulnerabilities caused by malformed input files that could cause out-of-bounds memory
  accesses.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch adds sanity checks to the M32R ELF backend to validate relocation offsets before accessing section contents. This prevents potential out-of-bounds reads or writes that could be triggered by specially crafted input files (fuzzing). The patch modifies `elf32-m32r.c` to include these checks and simplify sign extension.
