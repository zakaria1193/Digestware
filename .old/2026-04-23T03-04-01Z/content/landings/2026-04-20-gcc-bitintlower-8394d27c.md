---
project: gcc
subsystem: gcc/bitintlower
patch_id: null
tags:
- bitint
- risc-v
- bugfix
commit_hash: 8394d27cfea0adf784e414068b5c0da32ff8efdf
source_type: github
author: Jakub Jelinek
headline: 'Bitintlower: Fixes padding bit issues.'
tldr: Addresses issues related to padding bits in bit integers, fixing test failures
  on RISC-V architecture.
why_it_matters: Ensures correct behavior of bit integer operations with padding, preventing
  unexpected results and potential security vulnerabilities.  Specifically important
  for RISC-V.
impact_score: 6
impact_rationale: Fixes incorrect behavior in bit integer operations, resolving test
  failures and improving correctness, particularly on RISC-V.
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch continues the work on `gimple-lower-bitint.cc`, focusing
  on fixing issues related to extended bit integers and padding.  The primary changes
  involve updates to `bitintext.h` and the addition of new test cases (`bitint-88.c`
  and `bitint-89.c`) to specifically target padding-related problems in bit integer
  operations.
primer_general: Bit integers are integer data types with non-standard sizes. This
  commit addresses issues related to handling padding bits in bit integers, which
  are extra bits added to ensure proper memory alignment. The changes fix problems
  detected on RISC-V architecture, ensuring the compiler correctly handles bit integer
  operations with padding.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8394d27cfea0adf784e414068b5c0da32ff8efdf
date: '2026-04-20'
---

This commit fixes issues with padding bits in bit integers, specifically addressing failures observed on a RISC-V system.  It corrects the use of the `__riscv__` macro in `bitintext.h` and includes new tests to cover shifts and other padding-related problems. This resolves failures in multiple bitint tests when padding is involved.
