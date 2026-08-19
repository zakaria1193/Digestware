---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- alpha
- optimization
commit_hash: ec5e102d66f182c9028fb88a7354a32a73ed0347
source_type: github
author: Matt Turner
headline: Skip memory comparison tests on Alpha
tldr: Tests for memory comparison optimization are skipped on Alpha due to its handling
  of memory accesses.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `combine` pass on Alpha does not narrow memory comparisons, unlike
  some other targets. Tests like `cmp-mem-const-*.c` look for specific scan patterns
  related to narrowing memory comparisons (e.g., from `.I` to `HI`). Since Alpha does
  not perform this optimization, these patterns are never matched. The commit adds
  skips for these tests on Alpha, mirroring existing skips on Sparc and HPPA.
primer_glossary:
- term: combine pass
  definition: A compiler optimization pass that combines or simplifies instructions,
    often looking for opportunities to use more efficient, narrower operations.
- term: Narrow memory comparisons
  definition: Optimizing memory comparisons by using a smaller data width (e.g., comparing
    a word instead of a double-word) when possible, which can lead to more efficient
    instructions.
- term: .I
  definition: Represents an integer machine mode, typically a word-sized integer.
- term: HI
  definition: Represents a half-word integer machine mode.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:testsuite: skip cmp-mem-const on alpha'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ec5e102d66f182c9028fb88a7354a32a73ed0347
date: '2026-08-18'
is_stub: true
stub_reason: low_score
---

Several test cases (`cmp-mem-const-*.c`) check for compiler optimizations that narrow memory comparisons. Alpha's combine pass does not perform this narrowing for memory accesses, causing these tests to fail. Similar to Sparc and HPPA, these tests are now skipped on Alpha.
