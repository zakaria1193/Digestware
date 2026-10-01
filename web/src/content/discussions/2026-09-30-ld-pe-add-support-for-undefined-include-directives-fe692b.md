---
project: binutils
subsystem: ld-pe
patch_id: null
tags:
- linker
- pe
- coff
- symbols
discussion_id: AS4PR02MB79022E31710C9D4F0BC23868838B2@AS4PR02MB7902.eurprd02.prod.outlook.com
source_type: public_inbox
title: '[PATCH 2/2] ld-pe: Add support for -undefined, -include directives'
headline: 'ld-pe: Add support for -undefined, -include directives'
tldr: Extends PE linker support for undefined symbol directives and DEF module-definition
  files.
proposer: Luca Bacci <luca.bacci@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increases complexity of the PE linker's parsing logic.
exchanges: []
primer_expert: This change modifies the PE (Windows Portable Executable) linker within
  GNU binutils to recognize and process directives related to undefined symbols. It
  extends support to both the `.drectve` section in COFF objects and standard DEF
  (module-definition) files. The primary motivation is to correctly handle symbols
  marked with the `used` attribute, ensuring they are not optimized away by the toolchain,
  aligning PE behavior with similar mechanisms in ELF.
primer_glossary:
- term: ld-pe
  definition: The GNU linker's backend for handling Portable Executable (PE) files,
    commonly used on Windows.
- term: COFF
  definition: Common Object File Format, a file format for object files used on Windows
    and other systems.
- term: DEF module-definition files
  definition: Text files used with Windows linkers to define module properties, such
    as exported functions and data.
- term: used attribute
  definition: A compiler attribute that marks a symbol as being used, preventing the
    compiler or linker from discarding it, even if it appears unused.
- term: retain attribute
  definition: An ELF-specific attribute that serves a similar purpose to the 'used'
    attribute, preventing symbols from being discarded.
series_id: 'binutils:ld-pe: add support for -undefined, -include directives'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/AS4PR02MB79022E31710C9D4F0BC23868838B2@AS4PR02MB7902.eurprd02.prod.outlook.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch enhances the PE (Portable Executable) linker's capabilities by adding support for specifying undefined symbol names. This can now be done through linker directives within COFF object files' `.drectve` section or as statements in DEF module-definition files. This functionality is crucial for retaining symbols with the `used` attribute, preventing them from being discarded by the compiler or linker, similar to ELF's `retain` attribute.
