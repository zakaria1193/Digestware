---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- lexer
- fixed-format
- nist
commit_hash: 0bffd1dd17133367b3a8580a30cb4599ce1f98b2
source_type: github
author: James K. Lowden
headline: Cobol parser now handles tabs in fixed-format input more leniently.
tldr: Cobol lexer now treats a tab in columns 1-6 as if columns 1-7 were blank, improving
  NIST test compatibility.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The COBOL front-end's lexer (lexio.cc, scan.l) has been modified to
  adjust its handling of TAB characters in fixed-format source files. Previously,
  a TAB in columns 1-6 affected only the indicator column. This change expands the
  affected area to columns 1-7, ensuring that subsequent characters are correctly
  parsed as COBOL code, not ignored or misinterpreted. Additionally, symbol lookup
  for CLASS types has been optimized.
primer_glossary:
- term: fixed-format input
  definition: A source code format where code must adhere to specific column positions
    for different elements, common in older languages like COBOL.
- term: lexer
  definition: The component of a compiler that breaks source code into a stream of
    tokens (lexemes).
- term: NIST tests
  definition: Tests developed by the National Institute of Standards and Technology,
    used here to ensure compliance with COBOL standards.
- term: CLASS types
  definition: In COBOL, refers to data types that represent object-oriented classes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0bffd1dd17133367b3a8580a30cb4599ce1f98b2
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

The COBOL compiler's lexer has been updated to better handle fixed-format input. A tab character in columns 1-6 will now cause the parser to treat columns 1-7 as blank, aligning with NIST test requirements. This change also improves the fast symbol-lookup for CLASS types.
