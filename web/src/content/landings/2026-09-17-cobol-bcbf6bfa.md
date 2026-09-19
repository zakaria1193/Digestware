---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- libgcobol
- bugfix
commit_hash: bcbf6bfa83dbd0c3d3885062db2f7162dd22e9dd
source_type: github
author: Xavier Del Campo Romero
headline: 'cobol: Fix cblte-fe-month for CBL_CHECK_FILE_EXIST'
tldr: Cobol file existence check date month calculation corrected.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The CBL_CHECK_FILE_EXIST intrinsic in libgcobol returns file metadata,
  including date components. This commit fixes an off-by-one error in the month field
  (`tm_mon`) processing by adding 1, as `struct tm`'s `tm_mon` is 0-indexed (0-11)
  while the Cobol intrinsic might expect 1-indexed months.
primer_glossary:
- term: struct tm
  definition: A structure defined in C's time.h that holds calendar date and time
    components, such as year, month, day, hour, minute, and second. The month field
    (`tm_mon`) is 0-indexed, representing January as 0 and December as 11.
- term: cblte-fe-month
  definition: An internal variable or field within libgcobol related to the month
    component of a file's date, likely for the CBL_CHECK_FILE_EXIST intrinsic.
- term: CBL_CHECK_FILE_EXIST
  definition: A libgcobol intrinsic function that checks for the existence of a file
    and updates internal buffers based on file metadata.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bcbf6bfa83dbd0c3d3885062db2f7162dd22e9dd
date: '2026-09-17'
is_stub: true
stub_reason: low_score
---

This commit corrects the month calculation within the CBL_CHECK_FILE_EXIST function in libgcobol. The `tm_mon` member of the `struct tm` time structure uses a 0-based index for months (0-11), not 1-12 as was previously assumed. Adding 1 to `cblte-fe-month` now aligns with the expected month representation.
