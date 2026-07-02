---
project: gcc
subsystem: gcc/aarch64
patch_id: null
tags:
- test
- aarch64
- sve
commit_hash: e7bac3ec7ebc88e538a0fa53d054b32cdee82978
source_type: github
author: Wilco Dijkstra
headline: AArch64 test vcond_18.c is updated for consistency
tldr: GCC's AArch64 test suite received an update to align the vcond_18.c test with
  current compiler behavior.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This update pertains to the GCC testsuite for AArch64, specifically
  within the SVE (Scalable Vector Extension) portion. The `vcond_18.c` test likely
  exercises vector conditional instructions and predicates, which are critical for
  efficient vector programming on AArch64. The change implies either a desired change
  in generated assembly or an adjustment to the expected output due to other compiler
  changes, ensuring the ongoing correctness of the SVE implementation.
primer_general: When you write code, a compiler translates it into instructions that
  a computer's processor can understand. Because processors vary, compilers have different
  'backends' for each architecture, like AArch64. To ensure the compiler does its
  job correctly across these architectures, a comprehensive test suite exists, containing
  many small programs designed to test specific features. This commit updates one
  of those test programs, `vcond_18.c`, for the AArch64 architecture. This ensures
  that when the compiler is changed or updated, this test still correctly verifies
  that the compiler generates the right instructions for conditional operations used
  in vector programming, which is important for performance. This change helps maintain
  the quality and correctness of the compiler over time.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e7bac3ec7ebc88e538a0fa53d054b32cdee82978
date: '2026-06-10'
is_stub: true
stub_reason: low-score
---

This commit updates the `vcond_18.c` test case within GCC's AArch64 test suite. The changes bring the test up to date with expected output or behavior, ensuring it accurately verifies the compiler's functionality for vector conditional operations on AArch64. This is a routine maintenance task to keep the test suite reliable and current.
