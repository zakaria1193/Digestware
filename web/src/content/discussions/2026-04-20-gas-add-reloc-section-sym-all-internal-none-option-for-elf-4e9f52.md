---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- elf
- relocation
- symbol
discussion_id: CAN30aBGtNMZnt6VVSvzj8hfaN4J92+Nk7X_VeOJFP7ZJPExQHQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3] gas: add --reloc-section-sym={all,internal,none} option for
  ELF'
headline: 'gas: Add --reloc-section-sym={all,internal,none} option for ELF'
tldr: Adds a `--reloc-section-sym` option to the assembler to control conversion of
  local symbols to section symbols in relocations.
stakes: This change provides finer-grained control over symbol generation in the assembler,
  which can be useful for debugging and tools that depend on preserved symbol names.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adds a new command-line option, increasing complexity.
- May increase the size of the symbol table if symbol conversion is disabled.
- Could potentially impact performance if tools rely on the conversion for optimization.
exchanges: []
primer_expert: The GNU Assembler (GAS) converts local symbols to STT_SECTION symbols
  in ELF relocations under certain conditions, folding the original symbol's offset
  into the addend. This optimization reduces the number of .symtab entries when a
  section has multiple local symbols referenced by relocations. This patch adds a
  command-line option to control this behavior, useful for debugging or tools that
  rely on specific symbol names.
primer_general: The GNU Assembler (GAS) translates assembly code into object code,
  which is a low-level representation of the program.  During assembly, symbols are
  created to represent memory locations and functions.  In ELF files, relocations
  are used to resolve addresses at link time.  This patch proposes adding a new command-line
  option to the assembler that controls how local symbols (symbols only visible within
  a single file) are represented in the object code's relocation entries.  This can
  affect the size of the symbol table and can be important for debugging and other
  tools that rely on specific symbol information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAN30aBGtNMZnt6VVSvzj8hfaN4J92+Nk7X_VeOJFP7ZJPExQHQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-20'
---

This patch introduces a new assembler option, `--reloc-section-sym`, to control when the assembler converts local symbols to section symbols in ELF relocations. The option accepts three values: `all` (default), `internal` (convert compiler-generated locals), and `none` (disable conversion).
