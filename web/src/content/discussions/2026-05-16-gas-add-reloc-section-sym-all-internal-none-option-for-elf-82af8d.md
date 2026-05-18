---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- ELF
- relocation
- symbol
discussion_id: CAN30aBE8hRqOUoo5zPNkcnSuPxy5Ox1yL5NN4CeOLiUu3vmMtA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3] gas: add --reloc-section-sym={all, internal, none} option for
  ELF'
headline: 'gas: Add --reloc-section-sym={all, internal, none} option for ELF'
tldr: Introduces --reloc-section-sym option to control conversion of local symbols
  to section symbols in ELF relocations, aiding debugging and tooling.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding a new command-line option increases the complexity of the assembler.
- Converting local symbols to section symbols reduces the size of the symbol table,
  but can make debugging more difficult.
- Preserving local symbols can increase the size of the symbol table, but can improve
  the debugging experience.
exchanges:
- author: Fangrui Song <i@maskray.me>
  role: proposer
  position: Proposes adding the `--reloc-section-sym` option to control the conversion
    of local symbols to section symbols. The option has `all`, `internal`, and `none`
    modes.
  quote: 'Add --reloc-section-sym to control this conversion:


    - all (default): convert all eligible local symbols

    - internal: only convert compiler-generated locals (.L prefix)

    - none: never convert; keep all symbols as-is in relocations'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the proposal and requests confirmation that the new tests
    pass across a wide range of targets.
  quote: 'Okay, provided you checked the new tests pass for a wide range of targets.

    In particular ...'
primer_expert: This patch modifies the ELF object file emission logic in `gas` to
  control the conversion of local symbols to section symbols during relocation. This
  conversion reduces `.symtab` size but can hinder debugging. The new option allows
  control over this behavior.
primer_general: The GNU assembler (`gas`) translates assembly code into object files,
  which contain machine code and metadata like symbols and relocation information.  Relocations
  are adjustments the linker makes to code and data addresses.  This patch adds a
  command-line option to `gas` that affects how local symbols are represented in these
  relocations, potentially impacting debugging and linking behavior.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAN30aBE8hRqOUoo5zPNkcnSuPxy5Ox1yL5NN4CeOLiUu3vmMtA@mail.gmail.com
bugzilla_url: null
date: '2026-05-16'
is_stub: false
---

This patch introduces the `--reloc-section-sym` option to the GNU assembler (gas) for ELF files.  This option controls how local symbols are converted to section symbols during relocation. The change intends to help with debugging and support tools that rely on preserved symbol names.
