---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- type safety
commit_hash: 83bfd74e630e8920d95998e5925cd8958f31dcce
source_type: github
author: Georg-Johann Lay
headline: Fixes PR111036 test case by using __UINTPTR_TYPE__.
tldr: Corrects a test case by using the correct pointer-sized integer type to resolve
  a cast warning.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit resolves a testsuite failure in PR111036 where the `pr111036.c`
  test case used `unsigned long int` for a pointer-to-integer cast, leading to a `[-Wpointer-to-int-cast]`
  warning. The fix replaces `unsigned long int` with `__UINTPTR_TYPE__`, which is
  the standard and portable type for holding pointer values as integers, thus aligning
  the test case with correct type usage.
primer_glossary:
- term: __UINTPTR_TYPE__
  definition: A C99 standard type that is guaranteed to be able to hold a void pointer.
    It is the correct type to use when casting pointers to integers for non-semantic
    purposes, ensuring portability across different architectures where pointer and
    integer sizes may vary.
- term: PR111036
  definition: A bug report filed against the GCC compiler's testsuite, related to
    incorrect type usage in a test case leading to pointer-to-integer cast warnings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/83bfd74e630e8920d95998e5925cd8958f31dcce
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

The test case `pr111036.c` failed with a warning about casting a pointer to an integer of a different size because it incorrectly used `unsigned long int` instead of `__UINTPTR_TYPE__`. This commit updates the test to use `__UINTPTR_TYPE__`, resolving the warning and ensuring type correctness. This addresses PR testsuite/111036.
