---
project: gcc
subsystem: config/arc
patch_id: null
tags:
- gcc
- backend
- refactoring
commit_hash: 0dcc5c9324663982991d4e221b94f6e8adba6a6c
source_type: github
author: Trevor Saunders
headline: Use label_ref_label for more LABEL_REF reads across multiple backends
tldr: Refactors LABEL_REF reads in multiple GCC backends to use label_ref_label for
  consistency and potentially better error handling.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors multiple machine-description files (e.g., arc.cc,
  arm.cc) to replace direct reads of `XEXP` for `LABEL_REF` tree nodes with calls
  to `label_ref_label`. The `LABEL_REF` is a standard GCC internal representation
  for symbolic labels used in jump instructions or address calculations. Using `label_ref_label`
  provides a more abstract and potentially safer way to access the label's `name`
  field, ensuring consistency across different targets.
primer_glossary:
- term: LABEL_REF
  definition: An internal GCC representation (tree node) for a symbolic label. It's
    used to represent references to labels, such as those in jump instructions or
    when calculating addresses of code or data.
- term: XEXP
  definition: A macro in GCC's internal representation that accesses an operand of
    a tree node. Using XEXP directly can be less safe than using accessor functions,
    as it bypasses some checks and abstractions.
- term: label_ref_label
  definition: A GCC internal function that safely accesses the label's name from a
    `LABEL_REF` tree node. It abstracts away the direct memory access details, providing
    a more robust interface.
- term: GCC backends
  definition: The part of the GCC compiler responsible for translating the compiler's
    intermediate representation into machine-specific assembly code for a particular
    processor architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0dcc5c9324663982991d4e221b94f6e8adba6a6c
date: '2026-11-08'
is_stub: true
stub_reason: low_score
---

This commit updates several GCC backends, including ARC, ARM, AVR, CRIS, M68k, MCORE, PA, PDP11, RS6000, and SPARC, to use the `label_ref_label` function when reading LABEL_REF operands. This change standardizes how these backends handle label references, potentially improving robustness and simplifying future maintenance.
