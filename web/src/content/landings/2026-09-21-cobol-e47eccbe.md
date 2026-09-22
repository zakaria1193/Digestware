---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- optimization
- performance
commit_hash: e47eccbe6d118023e4fe83bde14075729c40e030
source_type: github
author: Robert Dubner
headline: 'cobol: Improve numeric-edited formatting speed by moving processing to
  compile time.'
tldr: COBOL numeric-edited output formatting is faster by performing PICTURE clause
  processing at compile time instead of runtime.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change optimizes the `cbl_field_t::encode_numeric` function in
  GCC's COBOL compiler by shifting `PICTURE` clause interpretation from runtime to
  compile time. The `expand_expanded` routine, now used in `symbols.cc` and `util.cc`,
  pre-processes the `PICTURE` string at compile time, embedding the necessary formatting
  data. This eliminates the need for runtime interpretation of the `PICTURE` clause
  for each conversion, improving performance for numeric-edited fields. The changes
  affect `genapi.cc`, `symbols.cc`, `symbols.h`, `util.cc`, `libgcobol.cc`, and `valconv.cc`.
primer_glossary:
- term: numeric-edited
  definition: A data type in COBOL that represents a number formatted for display
    according to a PICTURE clause. It includes elements like currency symbols, decimal
    points, and leading zeros.
- term: PICTURE clause
  definition: A COBOL clause used to define the format and editing rules for a data
    item, particularly for numeric and edited numeric fields.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e47eccbe6d118023e4fe83bde14075729c40e030
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

The performance of converting numerical strings to numeric-edited variables in GCC's COBOL compiler has been significantly improved. This optimization is achieved by moving the processing of `PICTURE` clauses, which define the format of edited numeric output, from runtime execution to compile time. This reduces the overhead during program execution by pre-calculating and embedding formatting information directly into the compiled code.
