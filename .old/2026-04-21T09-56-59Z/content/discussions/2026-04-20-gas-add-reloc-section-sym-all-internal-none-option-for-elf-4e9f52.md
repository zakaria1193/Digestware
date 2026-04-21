---
project: binutils
subsystem: gas
patch_id: null
tags:
- assembler
- gas
- symbols
- relocations
- ELF
discussion_id: CAN30aBGtNMZnt6VVSvzj8hfaN4J92+Nk7X_VeOJFP7ZJPExQHQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3] gas: add --reloc-section-sym={all,internal,none} option for
  ELF'
headline: 'Gas: Add --reloc-section-sym={all,internal,none} option for ELF'
tldr: Adds a command-line option to control the assembler's conversion of local symbols
  to section symbols when generating relocations.
stakes: This change allows more control over symbol table generation, which can be
  useful for debugging and tools that rely on preserved symbol names.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a new command-line option, increasing the complexity of the assembler.
- Provides more control over symbol table generation, which can be useful for debugging
  and tools that rely on preserved symbol names.
- May increase the size of the symbol table if the `none` option is used.
exchanges: []
primer_expert: The GNU assembler converts local symbols to section symbols in certain
  cases to reduce the size of the symbol table. This patch adds a command-line option
  to control this behavior. Relevant files include `gas/as.c` and `gas/doc/as.texi`.
primer_general: The GNU assembler (gas) translates assembly code into object code.
  During this process, it generates a symbol table that contains information about
  symbols used in the code.  This symbol table is used by the linker to resolve references
  between different object files. To reduce the size of the symbol table, the assembler
  can convert local symbols (symbols that are only used within a single object file)
  to section symbols, which refer to the section of memory where the symbol is located.
  This conversion can be problematic for debugging and tools that rely on preserved
  symbol names.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAN30aBGtNMZnt6VVSvzj8hfaN4J92+Nk7X_VeOJFP7ZJPExQHQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-20'
---

This patch introduces the `--reloc-section-sym` option to the GNU assembler. The option allows users to control how the assembler handles local symbols when generating relocations for ELF files.  The option has three modes: `all`, `internal`, and `none`.
