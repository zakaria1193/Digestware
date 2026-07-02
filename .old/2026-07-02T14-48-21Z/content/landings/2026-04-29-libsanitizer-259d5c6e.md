---
project: gcc
subsystem: libsanitizer
patch_id: null
tags:
- libsanitizer
- build
- kernel
- linux
commit_hash: 259d5c6ef7ca0b7fb07acf97538fa7ba590c8e8b
source_type: github
author: Jakub Jelinek
headline: 'Libsanitizer: Fix up build against latest kernel headers'
tldr: This commit fixes a build failure in libsanitizer caused by the removal of the
  linux/scc.h header from recent Linux kernels.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: libsanitizer provides runtime instrumentation for detecting memory
  safety violations. This commit ports an LLVM patch that removes the dependency on
  the linux/scc.h header, which was recently removed from the Linux kernel.  The change
  is in sanitizer_platform_limits_posix.cpp, suggesting it pertains to defining platform-specific
  limits for POSIX systems. This resolves build failures on systems with newer kernel
  headers.
primer_general: Libsanitizer is a set of runtime libraries that help detect memory
  errors, data races, and other undefined behavior in programs. It relies on system
  headers for platform-specific definitions. This commit fixes a build issue caused
  by recent changes in the Linux kernel headers, specifically the removal of the linux/scc.h
  header file. By removing the dependency on this header, the compiler can successfully
  build libsanitizer against newer kernel versions, ensuring that the sanitizers remain
  functional.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/259d5c6ef7ca0b7fb07acf97538fa7ba590c8e8b
date: '2026-04-29'
---

The recent removal of the linux/scc.h header from the Linux kernel caused build failures in libsanitizer.  This commit cherry-picks a fix from LLVM to address this issue. The macros defined in the removed header have not been actively used since around 2013, suggesting minimal functional impact.
