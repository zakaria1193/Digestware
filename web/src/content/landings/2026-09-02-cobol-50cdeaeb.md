---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- optimization
- lexer
- syntax
commit_hash: 50cdeaeb5cf2acbc65ef3860186003a0137e8260
source_type: github
author: James K. Lowden
headline: Cobol lexer performance boosted and syntax extended.
tldr: Cobol compiler's lexer is significantly faster after optimization, and new syntax
  extensions for redefined tables and copybooks are supported.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The COBOL lexer (lexio.cc, scan.l, symbols.cc) has undergone significant
  optimization by refactoring symbol table access. The use of `symbol_find()` with
  a map-based lookup and improvements to `scanner_cache_update` (now removed in favor
  of direct map access) reduce the time spent scanning symbol tables, a bottleneck
  identified in profiling. New parsing capabilities include support for `EXIT RETURNING`
  and enhanced handling of `PIC` clauses like `9(2)9(3)` and `9(name)`, as well as
  improved diagnostic messages for copybooks and redefined tables.
primer_glossary:
- term: lexer
  definition: The component of a compiler that breaks source code into a stream of
    tokens (lexemes).
- term: symbol table
  definition: A data structure used by a compiler to store information about identifiers
    (variables, functions, etc.) in a program.
- term: Wredefines-table
  definition: A diagnostic or syntax element in COBOL related to table redefinitions.
- term: Wcopybook-found
  definition: A diagnostic in COBOL that reports when a copybook (reusable code snippet)
    is found or used.
- term: PIC clause
  definition: In COBOL, a PICTURE clause that defines the data type and format of
    a data item.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/50cdeaeb5cf2acbc65ef3860186003a0137e8260
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

This commit makes substantial performance improvements to the COBOL compiler's lexer by optimizing symbol table lookups, which previously consumed a large portion of the lexer's time. It also introduces syntax extensions, including support for `Wredefines-table` diagnostics and more accurate reporting of `Wcopybook-found` diagnostics. Additionally, the lexer now supports more flexible PIC clauses and string concatenation.
