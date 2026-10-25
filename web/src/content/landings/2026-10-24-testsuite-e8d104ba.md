---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- hppa
- hpux
commit_hash: e8d104ba967635f041d0e5dd15edbc147a10d11c
source_type: github
author: John David Anglin
headline: Fix fwrite-3.c scan-tree-dump failure on hppa*-*-hpux*
tldr: 'Testsuite: Restricts a tree dump optimization check to exclude HPPA targets
  lacking fputc_unlocked.'
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test gcc.dg/fwrite-3.c expects inter-procedural constant folding
  for `fwrite_unlocked` calls into `fputc_unlocked`. This optimization is valid when
  `fputc_unlocked` is available. On hppa*-*-hpux*, `fwrite_unlocked` exists but `fputc_unlocked`
  does not. The test's scan-tree-dump assertion for this folding fails because the
  optimization path is not taken, but the assertion expects it. This commit adds a
  target exclusion for hppa*-*-hpux* in the `scan-tree-dump-times` check to resolve
  this mismatch.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e8d104ba967635f041d0e5dd15edbc147a10d11c
date: '2026-10-24'
is_stub: true
stub_reason: low_score
---

The fwrite-3.c test case expected a fwrite_unlocked call to be optimized into fputc_unlocked. However, the HPPA runtime environment for hppa*-*-hpux* provides fwrite_unlocked but not fputc_unlocked. This commit restricts the scan-tree-dump check for fputc_unlocked to exclude these HPPA targets, preventing a tree dump mismatch and allowing the test to pass.
