---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- parsing
- ISA
- code clarity
- const correctness
discussion_id: 34971eef-60d6-402e-bf4e-33259d13e09c@suse.com
source_type: public_inbox
title: '[PATCH v2 11/16] RISC-V: riscv_parse_subset_t''s isa_spec is only parser input'
headline: 'RISC-V: riscv_parse_subset_t''s isa_spec is only parser input'
tldr: Makes the `isa_spec` field in `riscv_parse_subset_t` const to clarify that it's
  an input-only value for parsing RISC-V ISA subsets.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Ready to Land
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improved code clarity by marking a field as const.
- Potential for compiler optimizations due to const annotation.
exchanges: []
primer_expert: The `riscv_parse_subset_t` structure is used when parsing RISC-V ISA
  subset strings. The `isa_spec` field indicates the specification class (e.g., draft,
  ratified). This patch changes `bfd/elfxx-riscv.h` and `bfd/elfxx-riscv.c` to reflect
  that `isa_spec` is an immutable input.
primer_general: When processing computer programs, parsing is the process of analyzing
  a string of text, either in natural language or in a computer language, to determine
  its logical structure. In binutils, parsing is used to understand command-line options
  and other inputs. This patch changes an internal data structure related to parsing
  RISC-V instruction set architecture (ISA) subsets to clearly indicate that a field
  should not be modified during the parsing process, improving code clarity and preventing
  potential errors.
series_id: 'binutils:risc-v: riscv_parse_subset_t''s isa_spec is only parser input'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/34971eef-60d6-402e-bf4e-33259d13e09c@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch modifies the `riscv_parse_subset_t` structure to make the `isa_spec` field a pointer to a const `enum riscv_spec_class`. This change clarifies that the `isa_spec` field is only used as input during parsing and is not modified. The patch also removes an unnecessary indirection in `riscv_get_default_ext_version()`. Reviewers have approved the patch.
