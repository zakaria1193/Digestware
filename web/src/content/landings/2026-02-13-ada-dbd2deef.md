---
project: gcc
subsystem: ada
patch_id: null
tags:
- ada
- build
- windows
commit_hash: dbd2deefe760b711635de13b465b2fd209d26930
source_type: github
author: Eric Botcazou
headline: 'Ada: Fixes build failure for Windows platforms'
tldr: This commit adds a missing `with` clause to `s-interr__sigaction.adb`, resolving
  a build failure on Windows.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The file `s-interr__sigaction.adb` is part of the Ada runtime library
  related to signal handling. The missing `with` clause caused a dependency resolution
  failure on Windows. No interaction with other subsystems is apparent.
primer_general: Ada programs often interact with the operating system through a set
  of standardized interfaces.  This patch fixes a build error in the Ada runtime library
  by explicitly stating that a certain file (`s-interr__sigaction.adb`) depends on
  operating system interfaces.  This dependency was previously implicit or assumed,
  but making it explicit resolves a build failure on Windows.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dbd2deefe760b711635de13b465b2fd209d26930
date: '2026-02-13'
is_stub: false
---

The Ada runtime library requires a `with` clause for `System.OS_Interface` in `s-interr__sigaction.adb` to compile correctly on Windows platforms. This patch adds the missing clause, resolving a build failure and ensuring the library can be built successfully.
