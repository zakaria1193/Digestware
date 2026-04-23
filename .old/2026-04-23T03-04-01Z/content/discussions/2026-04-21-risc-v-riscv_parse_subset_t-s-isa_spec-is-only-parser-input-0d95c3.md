---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- disassembler
- code cleanup
discussion_id: 923dd985-1100-4772-bc3c-f1af419c2815@suse.com
source_type: public_inbox
title: '[PATCH 13/19] RISC-V: riscv_parse_subset_t''s isa_spec is only parser input'
headline: 'Risc-V: Riscv_parse_subset_t''s isa_spec is only parser input'
tldr: Simplifies RISC-V ISA parsing by making `isa_spec` a const pointer, clarifying
  its role as input only.
stakes: Minor code cleanup; improves code clarity and maintainability by clarifying
  the role of `isa_spec`.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Code becomes more self-documenting and easier to reason about.
- No functional change.
exchanges: []
primer_expert: The `riscv_parse_subset_t` structure is used to pass parsing context
  to the RISC-V ISA subset parsing functions. This patch changes `isa_spec` from `enum
  riscv_spec_class *` to `const enum riscv_spec_class *`, indicating that the parsing
  process does not modify the pointed-to value.
primer_general: When assembling or disassembling RISC-V code, the toolchain needs
  to know which version of the RISC-V specification is being used. This patch makes
  a minor code change to clarify how the version of the specification is passed to
  the code that parses the architecture string.
series_id: 'binutils:risc-v: riscv_parse_subset_t''s isa_spec is only parser input'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/923dd985-1100-4772-bc3c-f1af419c2815@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the `riscv_parse_subset_t` structure to make the `isa_spec` field a pointer-to-const. This change clarifies that the ISA specification is only used as input to the parsing process and is not modified during parsing. It also removes an unnecessary indirection in `riscv_get_default_ext_version`.
