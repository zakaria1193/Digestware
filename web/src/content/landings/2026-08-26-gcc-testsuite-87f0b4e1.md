---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- type safety
commit_hash: 87f0b4e17f798d1e273f89e6c43f1df83fb5133f
source_type: github
author: Georg-Johann Lay
headline: Fixes PR49330 test case by using __UINTPTR_TYPE__.
tldr: Corrects a test case by replacing unsigned long with __UINTPTR_TYPE__ to fix
  a pointer-to-integer cast warning.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit fixes a testcase for PR49330 that incorrectly used `unsigned
  long` instead of `__UINTPTR_TYPE__` for pointer-to-integer casts. This led to a
  `[-Wpointer-to-int-cast]` warning on some platforms where `unsigned long` has a
  different size than a pointer. The change ensures the test case correctly uses the
  type intended for pointer-sized integer representations.
primer_glossary:
- term: __UINTPTR_TYPE__
  definition: A C99 standard type that is guaranteed to be able to hold a void pointer.
    It is the correct type to use when casting pointers to integers for non-semantic
    purposes, ensuring portability across different architectures where pointer and
    integer sizes may vary.
- term: PR49330
  definition: A bug report filed against the GCC compiler, related to incorrect type
    usage in a test case leading to pointer-to-integer cast warnings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/87f0b4e17f798d1e273f89e6c43f1df83fb5133f
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

A test case in PR49330 failed with a warning about casting a pointer to an integer of a different size because it used `unsigned long` instead of `__UINTPTR_TYPE__`. This commit rectifies the test by using the appropriate type, resolving the warning and addressing PR49330 and PR52641.
