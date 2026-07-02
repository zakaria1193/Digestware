---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- bugfix
- data_conversion
- numeric_operations
commit_hash: feb4dcd40582aeb331cd20b51951c6848023664e
source_type: github
author: Robert Dubner
headline: GCOBOL improves MOVE routines and fixes negative zero handling
tldr: GCOBOL now correctly implements `MOVE COMP-3 to NumericDisplay` and resolves
  "negative zero" bugs resulting from truncated moves, enhancing data integrity.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change enhances the GCOBOL compiler's semantic actions for `MOVE`
  statements, particularly for `COMP-3` to `NumericDisplay` conversions. The core
  issue was the incorrect handling of truncated moves, which could lead to a 'negative
  zero' representation in packed-decimal or numeric-display fields. The `move.cc`
  file sees the introduction of `clear_negative_zero`, a utility to normalize zero
  values, and modifications to `mh_numeric_display`, `mh_packed_to_packed`, and `mh_numdisp_to_packed`
  to correctly apply this. The implementation also includes new `mh_packed_to_numdisp`
  to handle the sp…
primer_general: In COBOL programming, the `MOVE` statement is used to copy data from
  one variable to another. However, different types of variables store data in different
  ways. For example, `COMP-3` (packed decimal) stores numbers efficiently, while `NumericDisplay`
  stores them as characters for display. This update improves how the GCOBOL compiler
  handles moving data between these types, especially when the target variable is
  smaller than the source and the data needs to be truncated. Crucially, it fixes
  a bug where truncating a zero value could incorrectly result in a 'negative zero',
  which can cause unexpected behavior in financial or numerical calculations. The
  changes ensure that COBOL programs relying on these data types and `MOVE` operations
  will now handle numerical values, including zero, with greater accuracy and consistency.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/feb4dcd40582aeb331cd20b51951c6848023664e
date: '2026-06-14'
is_stub: false
---

This commit significantly improves GCOBOL's `MOVE` routines, specifically addressing the implementation of `MOVE COMP-3 to NumericDisplay`. It also corrects long-standing errors where truncated moves to numeric-display and packed-decimal formats could create an erroneous "negative zero" value. The fixes involve new routines like `clear_negative_zero` and expanded test coverage to ensure correct behavior and data integrity.
