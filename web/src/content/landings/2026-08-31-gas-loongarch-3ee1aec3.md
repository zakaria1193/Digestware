---
project: binutils
subsystem: gas/loongarch
patch_id: null
tags:
- loongarch
- assembler
- relocations
- bugfix
commit_hash: 3ee1aec36a32879294dd15b3d9aab740520fa8eb
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Emit relocations for .long 0x2eef - symbol'
tldr: LoongArch assembler now correctly emits relocations for expressions involving
  subtraction with a symbol.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses an issue in `gas/config/tc-loongarch.c` where
  expressions of the form `constant - symbol` used with `.long` directives failed
  to generate appropriate relocations. The problem stemmed from `fx_addsy` being NULL
  in `fixup_segment`, preventing `md_apply_fix` from handling these cases. The fix
  involves setting `fx_addsy` to `abs_section_sym` within `md_apply_fix`, ensuring
  that the assembler can correctly generate the required ADD/SUB relocations for LoongArch.
primer_glossary:
- term: relocation
  definition: A directive in object code that tells the linker how to modify certain
    instructions or data before the executable code can be run. This typically involves
    adjusting addresses or offsets to be correct in the final program image.
- term: .long
  definition: An assembler directive that instructs the assembler to output a 32-bit
    integer value. In this context, it's used to embed constants or results of expressions
    directly into the code or data sections.
- term: ADD/SUB relocations
  definition: Specific types of relocations used to encode the result of an addition
    or subtraction at link time. This commit ensures these are generated correctly
    for expressions involving a symbol.
- term: symbol
  definition: A name that represents a memory address or a value within a program.
    Symbols are used by assemblers and linkers to refer to variables, functions, or
    labels.
- term: Program Counter (PC)
  definition: A register in the CPU that stores the address of the next instruction
    to be executed. Instructions or data that refer to addresses relative to the PC
    are called PC-relative.
- term: fixup
  definition: A process performed by the assembler or linker to resolve addresses
    or apply relocations. It corrects placeholder values in instructions or data to
    their final, correct values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260831081124.D5B494BA2E27@sourceware.org
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

The LoongArch assembler has been updated to correctly emit relocations for expressions like `.long 0x2eef - symbol`. Previously, the assembler could not generate these relocations when `fx_addsy` was NULL in `fixup_segment`. This change modifies `md_apply_fix` to set `fx_addsy` to `abs_section_sym`, enabling the generation of necessary relocations.
