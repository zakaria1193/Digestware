---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- testing
- pointers
commit_hash: 6adfb81ac2a530d4ae2a48276ac00013a2d7c575
source_type: github
author: David Malcolm
headline: Add tests for pointer comparison bugs fixed by rewrite
tldr: New test cases ensure the static analyzer correctly handles pointer comparisons
  after a rewrite.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This patch adds regression tests for PR analyzer/109199 and PR analyzer/124703.
  These bugs were fixed by r17-609-g573b66baa6cb8d (''analyzer: fix pointer comparisons
  [PR125304]''). The new tests verify the correctness of the pointer comparison logic,
  particularly in scenarios involving null checks and comparisons involving heap-allocated
  memory.'
primer_glossary:
- term: static analyzer
  definition: A tool that analyzes source code to find potential bugs and vulnerabilities
    without executing the code. GCC's static analyzer looks for issues like null pointer
    dereferences, buffer overflows, and memory leaks.
- term: pointer comparison
  definition: Comparing two memory addresses. The analyzer needs to understand the
    nuances of pointer comparisons, including those involving null pointers, pointers
    to allocated memory, and pointers within the same object.
- term: regression test
  definition: A test case designed to ensure that a recent code change has not introduced
    new bugs or re-introduced old ones. It specifically verifies that previously fixed
    issues remain fixed.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6adfb81ac2a530d4ae2a48276ac00013a2d7c575
date: '2026-11-21'
is_stub: true
stub_reason: low_score
---

This commit introduces test coverage for two bugs (PR analyzer/109199 and PR analyzer/124703) that were resolved by a rewrite of the static analyzer's pointer comparison logic. The tests confirm that these specific issues are no longer present.
