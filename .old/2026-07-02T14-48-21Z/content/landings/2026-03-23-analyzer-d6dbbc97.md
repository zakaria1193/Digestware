---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- refactoring
- code organization
- diagnostics
commit_hash: d6dbbc97dd44b41ea7dfa6582b8bdf8578e0ef78
source_type: github
author: David Malcolm
headline: 'Analyzer: Split pending_diagnostic subclasses from region-model.cc'
tldr: The GCC analyzer's diagnostic subclasses have been split into separate files
  for better organization and maintainability.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC static analyzer uses `pending_diagnostic` objects to represent
  potential errors detected during analysis.  This commit splits the definitions of
  several subclasses of `pending_diagnostic` (e.g., `poisoned_value_diagnostic`) into
  their own `.cc` files.  The change affects `Makefile.in`, `region-model.cc`, and
  introduces new files like `poisoned-value-diagnostic.cc` and `shift-diagnostics.cc`.  This
  is a refactoring; other parts of the compiler are unlikely to depend directly on
  these analyzer internals.
primer_general: The GCC static analyzer examines code to identify potential errors
  before a program is run. When the analyzer finds a potential issue (like writing
  to a read-only memory location or using an undefined value), it generates a diagnostic
  message. This commit reorganizes the analyzer's internal code by separating the
  different types of diagnostic messages into their own files. This makes the analyzer's
  code easier to understand and maintain, as each type of diagnostic is now in its
  own module. This refactoring doesn't change the analyzer's functionality or the
  types of warnings it produces.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d6dbbc97dd44b41ea7dfa6582b8bdf8578e0ef78
date: '2026-03-23'
---

The GCC static analyzer's code has been refactored to improve organization by splitting various `pending_diagnostic` subclasses from `region-model.cc` into their own dedicated files. This change moves classes like `poisoned_value_diagnostic`, `shift_count_negative_diagnostic`, `shift_count_overflow_diagnostic`, `write_to_const_diagnostic`, and `write_to_string_literal_diagnostic` into separate `.cc` files. Factory functions are used to create instances of these diagnostics, enabling the move. The refactoring enhances code modularity and simplifies maintenance of the analyzer.
