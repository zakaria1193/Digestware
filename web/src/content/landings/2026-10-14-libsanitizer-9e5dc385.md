---
project: gcc
subsystem: libsanitizer
patch_id: null
tags:
- build
- autoconf
commit_hash: 9e5dc38543418730291b90de2d03263a60ce5b8f
source_type: github
author: Sam James
headline: 'libsanitizer: Add comment for AC_CHECK_SIZEOF use'
tldr: Adds a comment to libsanitizer's configure.ac explaining the use of AC_CHECK_SIZEOF.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit clarifies the usage of the autoconf macro AC_CHECK_SIZEOF
  within libsanitizer's configure.ac. While the macro itself is not directly invoked
  in the original code, its cached result is used. The added comment explains this
  usage, improving clarity for developers maintaining the build system.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9e5dc38543418730291b90de2d03263a60ce5b8f
date: '2026-10-14'
is_stub: true
stub_reason: low_score
---

This commit adds a clarifying comment to libsanitizer's configure.ac file. The comment explains the purpose of AC_CHECK_SIZEOF, which was previously unclear as only its cache variable was being used, not the macro itself. This improves maintainability of the build configuration.
