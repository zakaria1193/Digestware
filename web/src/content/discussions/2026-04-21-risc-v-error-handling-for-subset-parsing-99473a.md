---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- error handling
- isa parsing
- binutils
discussion_id: bac6731e-3043-4f89-9805-ca17d5bfa0f9@suse.com
source_type: public_inbox
title: '[PATCH 14/19] RISC-V: error handling for subset parsing'
headline: 'Risc-V: Error handling for subset parsing'
tldr: Improves error handling in RISC-V ISA string parsing, ensuring consistent state
  after errors in `.option arch` and `-march`.
stakes: Prevents inconsistent toolchain behavior and ensures that invalid ISA strings
  don't silently corrupt the build process.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Copying the subset list adds a small performance overhead.
- The added checks increase code complexity.
exchanges: []
primer_expert: The RISC-V backend needs to parse ISA extension strings given via command-line
  arguments (e.g. `-march=rv64gc`) or assembler directives (`.option arch, ...`).
  This patch ensures that errors during parsing don't corrupt the internal `riscv_parse_subset_t`
  state. It rolls back changes on errors in `.option` and resets to defaults for `-march`.
primer_general: When compiling code for RISC-V, the compiler and assembler need to
  know which extensions to the base RISC-V instruction set are available. This information
  is provided via command-line arguments or assembler directives. This patch improves
  the error handling when parsing these extension strings, ensuring that the toolchain
  doesn't end up in a broken state if the string is invalid.
series_id: 'binutils:risc-v: error handling for subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/bac6731e-3043-4f89-9805-ca17d5bfa0f9@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch improves error handling during RISC-V ISA string parsing in binutils. It ensures that errors in parsing the `.option arch` directive or the `-march` command-line option do not leave the toolchain in an inconsistent state. Specifically, it preserves prior state for `.option` and resets to defaults for `-march` when errors occur.
