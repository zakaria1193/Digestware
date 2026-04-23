---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- buffer underrun
- security
discussion_id: e631583c-2890-4bb3-917f-2af5cccd2aa3@suse.com
source_type: public_inbox
title: '[PATCH 15/19] RISC-V: avoid buffer underrun in subset parsing'
headline: 'Risc-V: Avoid buffer underrun in subset parsing'
tldr: Fixes a potential buffer underrun in RISC-V ISA extension parsing and improves
  code clarity.
stakes: Prevents potential crashes due to out-of-bounds memory access and improves
  the reliability of RISC-V toolchain.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased code safety with added boundary checks.
- Slight performance overhead due to additional checks, but negligible compared to
  the cost of a crash.
exchanges: []
primer_expert: The RISC-V backend in binutils uses a custom parser (`bfd/elfxx-riscv.c`)
  to handle ISA extensions specified via `-march` and `.option arch`. The code in
  `riscv_parse_extensions` and `riscv_update_subset1` incorrectly accessed memory
  before the start of the buffer when checking for the `<number>p` suffix. This patch
  adds a check to avoid the underrun.
primer_general: The binutils suite includes assemblers and linkers that need to understand
  the instruction sets they are working with. For RISC-V, which has a modular ISA
  with many extensions, the tools need to parse the list of extensions enabled.  This
  patch fixes a bug where the parser could try to read memory before the beginning
  of the string, leading to crashes. It prevents the tool from reading invalid memory
  locations.
series_id: 'binutils:risc-v: avoid buffer underrun in subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/e631583c-2890-4bb3-917f-2af5cccd2aa3@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch addresses a potential buffer underrun in the RISC-V ISA extension parsing logic. The code now checks for the case where 'p' is the first character of the extension, preventing an invalid memory access. The patch also improves code indentation for better readability.
