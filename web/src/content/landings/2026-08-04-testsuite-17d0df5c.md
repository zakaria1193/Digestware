---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- arm
- atomic
commit_hash: 17d0df5cdb1b2983481612e4e454f659bc5ff738
source_type: github
author: Jakub Jelinek
headline: 'testsuite: Fix up gcc.dg/torture/bitint-100.c test.'
tldr: Ensures atomic operations on bit-integers are tested correctly for ARM targets.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `gcc.dg/torture/bitint-100.c` uses atomic operations on `_BitInt(17)`.
  On certain ARM targets like `armv6s-m`, standard atomic support might not be available
  or require specific linker flags. This patch adds a `dg-require-effective-target
  sync_int_long` directive to the test case. This ensures the test only runs on configurations
  where `sync_int_long` is supported, which implicitly covers the necessary atomic
  primitives for `_BitInt(17)` on platforms like ARM, preventing linkage errors.
primer_glossary:
- term: _BitInt(N)
  definition: A GCC extension for arbitrary-precision integers, where N specifies
    the number of bits.
- term: torture suite
  definition: A collection of test cases in GCC designed to stress-test specific compiler
    features or expose deep bugs, often involving complex or unusual code constructs.
- term: atomic operations
  definition: Operations that are guaranteed to execute indivisibly, preventing race
    conditions in multithreaded environments. Examples include compare-and-swap.
- term: linker flags
  definition: Options passed to the linker to control how object files are combined
    into an executable or library. For example, `-latomic` might be needed for atomic
    operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/17d0df5cdb1b2983481612e4e454f659bc5ff738
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This commit adjusts a test case (`bitint-100.c`) in GCC's torture suite to correctly handle atomic operations on `_BitInt(17)` for ARM targets. Previously, this test could fail due to missing linker flags for atomic operations on specific ARM architectures. The fix ensures that the test also requires the `sync_int_long` effective target, which properly aligns the atomic operation requirements for the tested bit-integer size.
