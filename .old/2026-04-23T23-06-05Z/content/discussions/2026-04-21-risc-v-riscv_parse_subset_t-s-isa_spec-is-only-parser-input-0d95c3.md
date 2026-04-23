---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- assembler
- code clarity
- const correctness
discussion_id: 923dd985-1100-4772-bc3c-f1af419c2815@suse.com
source_type: public_inbox
title: '[PATCH 13/19] RISC-V: riscv_parse_subset_t''s isa_spec is only parser input'
headline: 'Risc-V: Riscv_parse_subset_t''s isa_spec is only parser input'
tldr: Modifies `riscv_parse_subset_t` to treat `isa_spec` as a read-only input to
  clarify parsing behavior.
stakes: Improves code clarity and prevents accidental modification of the ISA specification
  during parsing.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved code safety and clarity by preventing accidental modification of the ISA
  specification.
- No performance impact.
exchanges: []
primer_expert: This patch refactors the `riscv_parse_subset_t` structure in `bfd/elfxx-riscv.c`
  to clarify that the `isa_spec` field is only an input to the parsing process. By
  changing the field to `const enum riscv_spec_class *isa_spec` and adjusting `riscv_get_default_ext_version`
  accordingly, the code prevents unintended modification of the ISA specification
  during parsing.
primer_general: The binutils tools need to parse the RISC-V ISA specification. This
  patch makes a small change to prevent the parser from accidentally modifying the
  ISA specification during parsing. This improves code maintainability by clarifying
  the intended use of the `isa_spec` field.
series_id: 'binutils:risc-v: riscv_parse_subset_t''s isa_spec is only parser input'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/923dd985-1100-4772-bc3c-f1af419c2815@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch modifies the `riscv_parse_subset_t` structure to treat the `isa_spec` field as a read-only input. By making the field a pointer-to-const and removing indirection in `riscv_get_default_ext_version()`, the code clearly indicates that parsing does not alter the ISA specification.
