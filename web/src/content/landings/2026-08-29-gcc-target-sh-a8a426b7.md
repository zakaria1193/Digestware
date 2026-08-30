---
project: gcc
subsystem: gcc/target/sh
patch_id: null
tags:
- target/sh
- optimization
- testsuite
commit_hash: a8a426b750a7397a628ce73226f41f5f5e232518
source_type: github
author: Jeff Law
headline: Update SH testsuite output after branch duplication changes
tldr: SH testsuite expected output updated to reflect changes from branch duplication
  optimization.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit resolves a testsuite regression on SH ports triggered by
  the phiopt pass's conditional replication over a PHI of comparisons. The test failures
  in gcc.target/sh/pr51244-20.c stemmed from changes in assembler output, specifically
  fewer `tst` instructions on non-sh2a targets. The fix consolidates scan-assembler
  expectations for sh2a and !sh2a, aligning the testsuite with the improved code generation.
primer_glossary:
- term: branch duplication
  definition: An optimization technique where code blocks guarded by conditional branches
    are duplicated to avoid the overhead of the branch itself.
- term: PHI node
  definition: In SSA form, a special node that merges values from different control
    flow paths.
- term: scan-assembler
  definition: A testsuite utility that analyzes the generated assembly code to verify
    specific instructions or patterns.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a8a426b750a7397a628ce73226f41f5f5e232518
date: '2026-08-29'
is_stub: true
stub_reason: low_score
---

This commit updates the expected output for the SH testsuite following recent changes in branch duplication optimization. Aldy's PHI of comparisons change introduced a minor regression on sh3 ports. The fix merges expectations for sh2a and non-sh2a ports and updates the scan-assembler tests to match the improved generated code, resolving lingering test failures.
