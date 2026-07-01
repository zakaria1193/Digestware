---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- filesystem
- testing
- symlinks
commit_hash: 92bfcd8a041bdf32c2c1098ad9cc6734eaf973e7
source_type: github
author: Adam Wood
headline: 'libstdc++: Test symlink behavior of remove and remove_all'
tldr: Tests added to ensure fs::remove and fs::remove_all do not follow symlinks.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds test cases to `testsuite/27_io/filesystem/operations/remove.cc`
  and `remove_all.cc` to verify that `fs::remove` and `fs::remove_all` do not dereference
  symlinks. The tests ensure that when a symlink is provided as an argument, or when
  encountered during a recursive removal, the symlink itself is removed instead of
  its target, aligning with expected POSIX semantics for these operations.
primer_general: This change adds tests to ensure that C++ standard library functions
  for removing files and directories behave correctly when encountering symbolic links.
  Symbolic links are pointers to other files or directories. The tests verify that
  `fs::remove` and `fs::remove_all` will delete the symlink file itself, rather than
  the file or directory it points to. This clarification is important for predictable
  file management in C++ programs, especially on systems where symlinks are common.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/92bfcd8a041bdf32c2c1098ad9cc6734eaf973e7
date: '2026-06-30'
is_stub: true
stub_reason: low_score
---

New test cases have been added to verify that `fs::remove` and `fs::remove_all` functions in libstdc++ correctly delete symbolic links themselves rather than following them to their targets. These tests specifically check the behavior when a symlink points to a directory or when symlinks are present within a directory, ensuring the functions operate as expected without dereferencing symlinks.
