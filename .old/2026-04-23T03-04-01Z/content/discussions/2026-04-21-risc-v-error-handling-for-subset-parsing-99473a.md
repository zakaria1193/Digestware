---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- error handling
- architecture string
discussion_id: bac6731e-3043-4f89-9805-ca17d5bfa0f9@suse.com
source_type: public_inbox
title: '[PATCH 14/19] RISC-V: error handling for subset parsing'
headline: 'Risc-V: Error handling for subset parsing'
tldr: Improves error handling during RISC-V ISA subset parsing, preserving state on
  failure.
stakes: Ensures consistent behavior when parsing RISC-V architecture strings with
  invalid extensions or conflicting options.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Introduces code to copy and restore the parsing state.
- Improves the robustness of the assembler by ensuring a consistent state after parsing
  errors.
exchanges: []
primer_expert: The RISC-V backend uses `riscv_parse_subset` and related functions
  to interpret the `-march=` option and `.option arch` directives.  Previously, a
  parsing failure could leave the assembler in an inconsistent state. This patch ensures
  that the global `riscv_rps_as` structure is either fully updated or left unchanged
  upon a parsing error.
primer_general: When you compile RISC-V code, you specify the target architecture
  using the `-march=` option.  Inside assembly code, you can use `.option arch` to
  specify the architecture for a specific section of code.  This patch ensures that
  if you specify an invalid architecture string, the assembler will either use the
  previous architecture, or a default architecture, rather than entering into an undefined
  state.
series_id: 'binutils:risc-v: error handling for subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/bac6731e-3043-4f89-9805-ca17d5bfa0f9@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch improves error handling in RISC-V ISA subset parsing. When parsing architecture strings (e.g., via the `-march=` option or `.option arch` directive) fails, the patch ensures that previous state is preserved for `.option arch`, preventing unexpected enabling of conflicting extensions. For `-march=`, default values are applied on parsing failure.
