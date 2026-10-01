---
project: binutils
subsystem: ld-pe
patch_id: null
tags:
- linker
- pe
- refactoring
- symbols
discussion_id: AS4PR02MB79027501F30490ABF58445F6838B2@AS4PR02MB7902.eurprd02.prod.outlook.com
source_type: public_inbox
title: '[PATCH 1/2] ld-pe: Refactor code dealing with -exclude-symbols'
headline: 'ld-pe: Refactor code dealing with -exclude-symbols'
tldr: Refactors PE linker code for handling excluded symbols to be more generic for
  future use.
proposer: Luca Bacci <luca.bacci@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Introduces a refactoring that adds complexity for future extensibility.
exchanges: []
primer_expert: This patch refactors the linker's handling of symbol exclusion lists
  within the PE backend. It generalizes the data structure used to store excluded
  symbols, moving from a specific `def_file_exclude_symbol` structure to a more flexible
  `def_file_symbol_list`. This change is a preparatory step for upcoming modifications
  that will leverage this more generic structure to handle additional directives,
  such as `-undefined` symbols.
primer_glossary:
- term: ld-pe
  definition: The GNU linker's backend for handling Portable Executable (PE) files,
    commonly used on Windows.
- term: -exclude-symbols
  definition: A linker option or directive that specifies symbols to be excluded from
    the final output, often to prevent linking conflicts or unwanted symbols.
- term: DEF module-definition files
  definition: Text files used with Windows linkers to define module properties, such
    as exported functions and data.
- term: PE
  definition: Portable Executable, the file format used for executables, DLLs, and
    object code in Windows operating systems.
series_id: 'binutils:ld-pe: refactor code dealing with -exclude-symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/AS4PR02MB79027501F30490ABF58445F6838B2@AS4PR02MB7902.eurprd02.prod.outlook.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch refactors the `ld-pe` code that handles the `-exclude-symbols` directive. The changes aim to make the symbol exclusion mechanism more generic, preparing it for use in related functionalities that will be implemented in subsequent commits. The core change involves restructuring data structures to accommodate a more general symbol list handling.
