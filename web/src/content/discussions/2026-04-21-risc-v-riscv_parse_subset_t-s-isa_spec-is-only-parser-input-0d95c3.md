---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- code clarity
- const correctness
- isa parsing
discussion_id: 923dd985-1100-4772-bc3c-f1af419c2815@suse.com
source_type: public_inbox
title: '[PATCH 13/19] RISC-V: riscv_parse_subset_t''s isa_spec is only parser input'
headline: 'Risc-V: Riscv_parse_subset_t''s isa_spec is only parser input'
tldr: Makes the `isa_spec` field in `riscv_parse_subset_t` const to clarify that it's
  only an input to the parsing process.
stakes: Improves code clarity and prevents accidental modification of the ISA specification
  during parsing, enhancing code reliability.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- This change is purely for code clarity and has no performance impact.
- It may require minor adjustments to existing code that modifies the `isa_spec` field
  (though it shouldn't).
- Makes the code slightly more self-documenting.
exchanges: []
primer_expert: The `riscv_parse_subset_t` structure, used in `bfd/elfxx-riscv.c`,
  contains the parsing state for RISC-V ISA extension strings. The `isa_spec` field
  indicates the ISA specification class (e.g., draft or ratified). This patch makes
  `isa_spec` a pointer-to-const to prevent accidental modification of the specification
  during parsing, thus improving code safety.
primer_general: When the toolchain parses RISC-V ISA extension strings, it needs to
  know which version of the specification to use. This patch ensures that the code
  that specifies the ISA version is not accidentally modified during the parsing process,
  which could lead to incorrect behavior.
series_id: 'binutils:risc-v: riscv_parse_subset_t''s isa_spec is only parser input'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/923dd985-1100-4772-bc3c-f1af419c2815@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the `isa_spec` field in the `riscv_parse_subset_t` structure to be a pointer to a constant `enum riscv_spec_class`. This change clarifies that the ISA specification is only an input to the parsing process and should not be modified during parsing.
