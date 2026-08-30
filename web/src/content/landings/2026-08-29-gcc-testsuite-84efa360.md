---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- size_t
commit_hash: 84efa3603680a7e6cbac30223c0f4b9837cda5cd
source_type: github
author: Georg-Johann Lay
headline: Skip tree-ssa test requiring 32-bit size_t on smaller architectures
tldr: A test for tree-ssa that assumes 32-bit size_t is now skipped on architectures
  with smaller size_t.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The tree-ssa testsuite contains cases that implicitly assume certain
  type sizes. This commit addresses PR 121264 by skipping a test that fails on platforms
  where size_t is less than 32 bits. The test is now conditional on the size32plus
  capability, ensuring it only runs on relevant platforms.
primer_glossary:
- term: tree-ssa
  definition: A GCC optimization pass that transforms the compiler's intermediate
    representation into a Static Single Assignment (SSA) form, facilitating various
    optimizations.
- term: size_t
  definition: An unsigned integer type that is capable of holding the size of any
    object in bytes. Its actual size is platform-dependent.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/84efa3603680a7e6cbac30223c0f4b9837cda5cd
date: '2026-08-29'
is_stub: true
stub_reason: low_score
---

This commit skips the gcc.dg/tree-ssa/pr121264.c test case. The test failed because it assumed a size_t type of at least 32 bits, which is not true on all architectures. By requiring the size32plus capability, the test is now correctly skipped when size_t is smaller than 32 bits, preventing spurious failures.
