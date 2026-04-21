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
tldr: The assembler gains a `--reloc-section-sym` flag to control conversion of local
  symbols to section symbols in ELF relocations, aiding debugging and symbol pres…
stakes: This change impacts debugging workflows and tools relying on symbol names,
  by providing finer control over relocation symbol generation.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased assembler complexity.
- Potential for larger symbol tables when disabling conversion.
- Improved debugging experience with preserved symbol names.
- Adds a new command-line option.
exchanges: []
primer_expert: The assembler's ELF backend converts local symbols to STT_SECTION symbols
  under certain conditions, folding the original symbol's offset into the addend.  This
  reduces the size of `.symtab` but requires the presence of the STT_SECTION symbol.  The
  new flag `--reloc-section-sym` allows users to disable or restrict this conversion.  Values
  `all`, `internal`, and `none` control the scope of the conversion, with `internal`
  targeting compiler-generated locals.
primer_general: When assembling code, the assembler creates symbols that represent
  memory locations.  Relocations are instructions that tell the linker how to update
  these memory locations when combining multiple object files.  By default, the assembler
  may convert some local symbols (symbols only visible within a single object file)
  into section symbols, which refer to the entire section of code or data.  This conversion
  can reduce the size of the symbol table but may hinder debugging or tools that rely
  on specific symbol names. The `--reloc-section-sym` option provides control over
  this conversion process.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAN30aBGtNMZnt6VVSvzj8hfaN4J92+Nk7X_VeOJFP7ZJPExQHQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-20'
---

This patch introduces the `--reloc-section-sym` option to the GNU Assembler (GAS) for ELF targets.  This option controls how GAS handles relocations for local symbols, specifically whether they are converted to reference the section symbol (STT_SECTION). The option accepts three values: `all` (default, convert all eligible symbols), `internal` (convert only compiler-generated locals with `.L` prefix), and `none` (never convert, keep all symbols as-is).  The goal is to improve debugging and support tools that rely on preserved symbol names.
