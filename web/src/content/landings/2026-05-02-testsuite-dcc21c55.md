---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- libstdc++
- vxworks
- threading
commit_hash: dcc21c5517eeaec3d41cbf7790e833f24a1f8c87
source_type: github
author: Alexandre Oliva
headline: 'Testsuite: Reorder clock::now calls in semaphore test'
tldr: Reorders clock::now calls in a semaphore test to avoid false positives on VxWorks
  due to slow clock calls.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses a test failure in `libstdc++`'s semaphore test
  (`testsuite/30_threads/semaphore/try_acquire_until.cc`) on VxWorks. The `clock::now()`
  function's slow execution on VxWorks can cause consecutive calls to yield different
  results, leading to false positives. Reordering the calls mitigates this issue.
primer_general: The C++ standard library provides threading primitives like semaphores
  for synchronizing access to shared resources. The libstdc++ library includes a testsuite
  to verify the correct behavior of these primitives. This commit modifies a test
  case that uses `clock::now()` to measure time, and reorders the timing calls to
  avoid spurious failures on the VxWorks operating system, where the clock may have
  lower resolution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dcc21c5517eeaec3d41cbf7790e833f24a1f8c87
date: '2026-05-02'
---

This commit reorders calls to `clock::now()` in the `semaphore/try_acquire_until.cc` test within the libstdc++ testsuite. On VxWorks, `clock::now()` calls can be slow, increasing the likelihood of consecutive calls returning different results. The reordering aims to prevent false positives during testing.
