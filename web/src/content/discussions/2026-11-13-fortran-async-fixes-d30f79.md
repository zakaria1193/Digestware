---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- io
- compiler
discussion_id: '133'
source_type: github_pr
title: Fortran async fixes
headline: Fortran async fixes
tldr: Adds support for array spans in Fortran I/O operations.
proposer: suvarchal
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds new function declarations to support array span I/O, increasing the compiler's
  feature set.
exchanges:
- author: suvarchal
  role: proposer
  position: Proposes adding new I/O call identifiers for Fortran array spans.
  quote: "iocall[IOCALL_X_ARRAY_SPAN] = gfc_build_library_function_decl_with_spec\
    \ (\n\tget_identifier (PREFIX(\"transfer_array_span\")), \". w w . . \",\n\tvoid_type_node,\
    \ 4, dt_parm_type, pvoid_type_node,\n\tinteger_type_node, gfc_charlen_type_node);\n\
    \n  iocall[IOCALL_X_ARRAY_SPAN_WRITE]\n    = gfc_build_library_function_decl_with_spec\
    \ (\n\tget_identifier (PREFIX(\"transfer_array_span_write\")), \". w r . . \"\
    ,\n\tvoid_type_…"
primer_expert: This PR modifies the Fortran frontend's I/O handling by adding support
  for `transfer_array_span` and `transfer_array_span_write`. These are new I/O call
  identifiers that will be used by the intermediate representation generation for
  Fortran I/O statements involving array spans, likely for more efficient data transfer
  in specific I/O scenarios.
primer_glossary:
- term: array span
  definition: A contiguous portion of an array, often defined by a start index, end
    index, and stride, used for efficient data manipulation and I/O.
- term: I/O call identifiers
  definition: Enums or constants used within the compiler's internal representation
    to signify specific input/output operations, mapping to runtime library functions.
series_id: null
series_role: standalone
series_parts: []
url: https://github.com/gcc-mirror/gcc/pull/133
bugzilla_url: null
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

This pull request introduces new I/O call identifiers for handling array spans, specifically for `transfer_array_span` and `transfer_array_span_write`.
These additions aim to improve the Fortran compiler's ability to manage and transfer data within array structures during I/O operations.
