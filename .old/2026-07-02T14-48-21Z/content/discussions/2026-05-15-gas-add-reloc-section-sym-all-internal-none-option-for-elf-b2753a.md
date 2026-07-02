---
project: binutils
subsystem: gas
patch_id: null
tags:
- assembler
- gas
- relocation
- elf
- symbols
discussion_id: 20260228061955.23818-1-i@maskray.me
source_type: public_inbox
title: 'Re: [PATCH v3] gas: add --reloc-section-sym={all, internal, none} option for
  ELF'
headline: 'gas: Add --reloc-section-sym={all, internal, none} option for ELF'
tldr: GAS gets a new option to control conversion of local symbols to section symbols
  in relocations, aiding debugging and symbol preservation.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Smaller `.symtab` size vs. preserving symbol names for debugging.
- Increased complexity in the assembler.
exchanges:
- author: Fangrui Song <maskray@sourceware.org>
  role: proposer
  position: Proposes a new assembler option `--reloc-section-sym` to control conversion
    of local symbols to section symbols in ELF relocations.
  quote: 'Add --reloc-section-sym to control this conversion:


    - all (default): convert all eligible local symbols

    - internal: only convert compiler-generated locals (.L prefix)

    - none: never convert; keep all symbols as-is in relocations'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Requests confirmation that the new tests pass on a wide range of targets.
  quote: Okay, provided you checked the new tests pass for a wide range of targets.
- author: Fangrui Song <i@maskray.me>
  role: contributor
  position: Replies to the review from Jan Beulich.
  quote: null
primer_expert: The GNU Assembler (GAS) converts local symbols to section symbols in
  ELF relocations under specific conditions, reducing the size of the `.symtab`.  The
  `--reloc-section-sym` option provides finer-grained control over this conversion.  This
  affects ELF symbol table generation and relocation processing.
primer_general: The GNU Assembler (GAS) translates assembly code into machine code.  During
  this process, it generates relocations, which specify how addresses need to be adjusted
  when the code is linked.  Symbols represent addresses of code or data. This patch
  introduces a new option to control how local symbols are handled during relocation,
  which can be useful for debugging and other specialized tools.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/88097170-c97c-4388-81bc-a2b5e53a89ef@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

A new assembler option, `--reloc-section-sym`, controls the conversion of local symbols to section symbols (STT_SECTION) in ELF relocations.  This conversion, which minimizes `.symtab` size, can now be disabled or limited to compiler-generated symbols.  The option helps with debugging and supports tools that rely on preserved symbol names.
