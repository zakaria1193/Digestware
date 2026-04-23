---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- error handling
- isa extensions
discussion_id: bac6731e-3043-4f89-9805-ca17d5bfa0f9@suse.com
source_type: public_inbox
title: '[PATCH 14/19] RISC-V: error handling for subset parsing'
headline: 'Risc-V: Error handling for subset parsing'
tldr: Improves error handling in RISC-V ISA subset parsing to prevent conflicting
  extensions from being enabled after a parsing failure.
stakes: Ensures consistent and predictable behavior when parsing RISC-V ISA extensions,
  preventing unexpected instruction availability.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved robustness and predictability at the cost of increased code complexity.
- Preserves prior assembler state on parsing failure.
exchanges: []
primer_expert: The RISC-V backend in binutils uses a custom parser (`bfd/elfxx-riscv.c`)
  to handle ISA extensions specified via `-march` and `.option arch`.  This patch
  addresses a flaw where a parsing failure could lead to an inconsistent state in
  the enabled extensions.  The changes ensure that, upon failure, the previous state
  is preserved for `.option arch` and defaults are applied for `-march`.
primer_general: The binutils suite includes assemblers and linkers that need to understand
  the instruction sets they are working with. For RISC-V, which has a modular ISA
  with many extensions, the tools need to parse the list of extensions enabled.  This
  patch improves the robustness of the parsing process, ensuring that errors don't
  lead to a corrupted or inconsistent instruction set configuration, preserving the
  tool's correct behavior.
series_id: 'binutils:risc-v: error handling for subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/bac6731e-3043-4f89-9805-ca17d5bfa0f9@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch improves error handling in RISC-V ISA subset parsing within binutils. It ensures that when parsing the `-march` option or `.option arch` directive fails, previously enabled extensions are not inadvertently disabled, and conflicting new extensions aren't enabled. The patch also refactors code for better readability and consistency.
