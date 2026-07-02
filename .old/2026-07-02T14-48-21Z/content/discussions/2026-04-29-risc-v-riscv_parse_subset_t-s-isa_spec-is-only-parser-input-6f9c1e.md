---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- isa_spec
- const correctness
discussion_id: 6f9b7f7b-87a6-4a51-85e4-a1be9b6825c4@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 13/19] RISC-V: riscv_parse_subset_t''s isa_spec is only parser,
  input'
headline: 'RISC-V: riscv_parse_subset_t''s isa_spec is only parser input'
tldr: Makes the ``isa_spec`` field in the ``riscv_parse_subset_t`` struct a pointer-to-const
  to clarify it's only an input to the parser.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- None, this is a const-correctness improvement.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: States that making the field a pointer-to-const clarifies that parsing
    won't alter the field and removes indirection from ``riscv_get_default_ext_version``.
  quote: Make the field pointer-to-const and drop indirection from riscv_get_default_ext_version().
    This way it's more clear that parsing won't alter the field.
primer_expert: The RISC-V backend uses the ``riscv_parse_subset_t`` struct to manage
  the parsing of RISC-V architecture strings. The ``isa_spec`` field indicates the
  specification class (e.g., draft, ratified). This patch changes the field to be
  a pointer to const, signaling that the parser should not modify this value. The
  affected code is in ``bfd/elfxx-riscv.c`` and ``bfd/elfxx-riscv.h``.
primer_general: When the compiler parses the RISC-V architecture string, it uses a
  data structure (``riscv_parse_subset_t``) to keep track of the parsing state. The
  ``isa_spec`` field in this structure indicates which version of the RISC-V specification
  is being used.  This patch makes it clear that the parser doesn't change the specification
  version during parsing.
series_id: 'binutils:risc-v: riscv_parse_subset_t''s isa_spec is only parser, input'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/6f9b7f7b-87a6-4a51-85e4-a1be9b6825c4@iscas.ac.cn
bugzilla_url: null
date: '2026-04-29'
---

This patch modifies the ``riscv_parse_subset_t`` struct to make the ``isa_spec`` field a pointer to a constant value. This change clarifies that the parsing process won't alter the ``isa_spec`` field, which specifies the RISC-V specification class.
