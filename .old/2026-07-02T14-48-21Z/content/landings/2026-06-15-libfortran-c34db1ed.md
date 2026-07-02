---
project: gcc
subsystem: libfortran
patch_id: null
tags:
- fortran
- runtime
- bugfix
- i/o
commit_hash: c34db1ed893f309cb3a4b9e01a620423c10ca8b1
source_type: github
author: Jerry DeLisle
headline: Format produces incorrect output when contains 1x
tldr: A Fortran I/O bug where format specifiers containing '1x' caused incorrect output
  due to miscalculated `max_pos` is now resolved.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change addresses PR114618 within `libgfortran`'s `io/transfer.c`,
  specifically in `formatted_transfer_scalar_write`. The core issue involved the `max_pos`
  calculation being incorrect when tab edit descriptors (like '1x') were present in
  Fortran `FORMAT` strings, particularly with variations between stream and record
  I/O. The fix adjusts how `max_pos` is determined, ensuring that the buffer pointers
  for writing are correctly managed, preventing data corruption or skipping in the
  output stream. This is critical for Fortran's highly structured I/O model.
primer_general: When a Fortran program writes data, it often uses a `FORMAT` statement
  to precisely control how that data appears in the output file or on the screen.
  This format can include special instructions for spacing, like '1x', which means
  to skip one character space. This commit fixes a bug in the GCC Fortran runtime
  library (`libgfortran`) where using these spacing instructions could lead to incorrect
  output. The error occurred because the library miscalculated where the next character
  should be written, causing parts of the output to be overwritten or skipped. This
  fix ensures that the compiler correctly handles these formatting instructions regardless
  of the underlying input/output method, guaranteeing that your Fortran program's
  output looks exactly as intended.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c34db1ed893f309cb3a4b9e01a620423c10ca8b1
date: '2026-06-15'
is_stub: false
---

This commit fixes a bug in `libgfortran` where Fortran `FORMAT` statements, specifically those involving the '1x' edit descriptor for tabbing, could lead to incorrect output. The issue stemmed from an incorrect calculation of the `max_pos` (maximum write position) within `formatted_transfer_scalar_write`, causing text to be overwritten or skipped. The fix ensures `max_pos` is properly determined based on the file I/O method, guaranteeing correct formatting regardless of whether stream or regular I/O is used.
