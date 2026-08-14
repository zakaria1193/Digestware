---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- assembler
- relocations
- symbolic expressions
discussion_id: 20260813170736.1880481-2-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 1/3] LoongArch: Emit relocations for .long 0x2eef - symbol'
headline: 'LoongArch: Emit relocations for .long 0x2eef - symbol'
tldr: Enables correct relocation generation for symbolic subtraction expressions.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enables correct handling of symbolic subtraction expressions, improving code generation
  accuracy.
- Fixes a bug that prevented certain relocations from being generated.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Proposes to set `fx_addsy` to `abs_section_sym` in `md_apply_fix` to enable
    relocation generation for expressions like `.long 0x2eef - symbol`.
  quote: null
primer_expert: This patch addresses a limitation in the LoongArch assembler's relocation
  handling. Specifically, it corrects the `md_apply_fix` function to properly set
  the `fx_addsy` field when processing symbolic subtraction expressions (e.g., `constant
  - symbol`). The absence of this symbolic addend prevented the generation of necessary
  relocations, such as `R_LARCH_ADD64` or `R_LARCH_SUB64`, which are crucial for correctly
  resolving addresses at link time. The fix ensures that these expressions are now
  handled by setting `fx_addsy` to point to the absolute section symbol.
primer_glossary:
- term: relocation
  definition: Information embedded in an object file that describes how to modify
    symbolic addresses and constants when linking. It tells the linker which parts
    of the code or data need to be adjusted based on the final memory layout.
- term: assembler
  definition: A program that translates assembly language into machine code. It also
    generates relocation information for the linker.
- term: symbol
  definition: A named identifier in a program that refers to a memory location, variable,
    or function. The linker uses symbols to resolve references between different parts
    of the code.
- term: fx_addsy
  definition: A field within the fixup structure that likely represents the addend
    symbol used in a relocation calculation. Setting it correctly is crucial for generating
    the appropriate relocation type.
- term: abs_section_sym
  definition: A symbol representing the absolute address of a section. Used here to
    provide a base for relocation calculations when a symbolic subtraction involves
    a constant and a symbol.
series_id: 'binutils:loongarch: emit relocations for .long 0x2eef - symbol'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260813170736.1880481-2-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This patch enables the LoongArch assembler to correctly emit relocations for expressions like '.long 0x2eef - symbol'. Previously, the assembler failed to generate these relocations because `fx_addsy` was incorrectly set to NULL. The fix involves setting `fx_addsy` to `abs_section_sym` in `md_apply_fix` to ensure proper relocation handling.
