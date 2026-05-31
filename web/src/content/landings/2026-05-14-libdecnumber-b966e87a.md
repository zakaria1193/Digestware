---
project: gcc
subsystem: libdecnumber
patch_id: null
tags:
- libdecnumber
- typo
- cleanup
commit_hash: b966e87aa42ad43837259b2e89571bbcfdd01ae5
source_type: github
author: Dhruv Chawla
headline: 'Libdecnumber: Correct typos in source files.'
tldr: This commit fixes typos across multiple libdecnumber source files.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit resolves typos in libdecnumber, which implements the Decimal
  Arithmetic Specification. Affected files include core arithmetic routines (`decBasic.c`,
  `decNumber.c`), context management (`decContext.c`), and internal headers (`decNumberLocal.h`).
  These fixes improve code clarity.
primer_general: This commit cleans up typos in libdecnumber. The libdecnumber library
  provides support for arbitrary-precision decimal arithmetic. Clean code improves
  readability and maintainability.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b966e87aa42ad43837259b2e89571bbcfdd01ae5
date: '2026-05-14'
is_stub: false
---

This commit corrects typos in various files within libdecnumber, a library for decimal arithmetic. The affected files include `decBasic.c`, `decCommon.c`, `decContext.c`, `decNumber.c`, and `decNumberLocal.h`. These changes improve code readability and maintainability.
