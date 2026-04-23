---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- relocation
- symbol table
- ELF
discussion_id: CAN30aBGtNMZnt6VVSvzj8hfaN4J92+Nk7X_VeOJFP7ZJPExQHQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3] gas: add --reloc-section-sym={all,internal,none} option for
  ELF'
headline: GAS adds --reloc-section-sym option for ELF
tldr: GAS now has a `--reloc-section-sym` option to control conversion of local symbols
  to section symbols in relocations, aiding debugging and tool compatibility.
stakes: Provides more control over symbol generation in assembly, which can be useful
  for debugging, binary analysis, and compatibility with other tools.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Converting local symbols to section symbols can reduce the size of the symbol table,
  but may hinder debugging.
- The `--reloc-section-sym` option adds complexity to the assembler.
- The `internal` setting relies on compiler-generated symbol naming conventions which
  might not always be reliable.
exchanges:
- author: Fangrui Song
  role: proposer
  position: Proposes adding `--reloc-section-sym` to control conversion of local symbols
    to section symbols, useful for debugging and tool compatibility.
  quote: 'Add --reloc-section-sym to control this conversion:


    - all (default): convert all eligible local symbols

    - internal: only convert compiler-generated locals (.L prefix)

    - none: never convert; keep all symbols as-is in relocations'
primer_expert: GAS (GNU Assembler) converts assembly code into object files. During
  this process, local symbols may be converted to section symbols in relocations,
  which can reduce the size of the `.symtab` section. The `--reloc-section-sym` option
  provides control over this conversion process. This is relevant for ELF (Executable
  and Linkable Format) files.  The conversion involves manipulating symbol table entries
  and relocation records, impacting the final object file's structure.
primer_general: The GNU Assembler (GAS) is a tool that translates human-readable assembly
  language into machine code that a computer can execute. During this translation,
  the assembler creates a symbol table, which is a list of names and addresses used
  in the program. This patch adds a new option to GAS that lets you control how the
  assembler handles local symbols (names that are only used within a specific part
  of the code) during the creation of relocation records (information about how to
  adjust addresses when the code is linked).  This control helps with debugging and
  ensures compatibility with other tools.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAN30aBGtNMZnt6VVSvzj8hfaN4J92+Nk7X_VeOJFP7ZJPExQHQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-20'
---

This patch adds the `--reloc-section-sym` option to GAS (GNU Assembler) for ELF files. This option controls the conversion of local symbols to section symbols in relocations. The option has three settings: `all` (default), `internal` (compiler-generated locals only), and `none` (no conversion). This feature is useful for debugging and for tools that benefit from preserved symbol names.
