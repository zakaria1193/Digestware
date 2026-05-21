---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- build
- bugfix
commit_hash: 1aababb8e205a441fe55f9acecc8c6c1ca552ec6
source_type: github
author: Nathan Myers
headline: 'libstdc++: Fix Build Failures After acfdad706d8'
tldr: This commit fixes build failures in libstdc++ caused by a recent commit.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit reverts a symbol swept up in GLIBCXX_3.4.21 in `config/abi/pre/gnu.ver`
  and guards a declaration under `#if __cpp_exceptions` in `include/bits/basic_string.tcc`.
  This is a straightforward fix for build breakage, of interest to libstdc++ maintainers
  and those tracking ABI stability.
primer_general: This commit resolves build errors in the C++ standard library (libstdc++)
  that arose from a recent update.  The changes involve adjusting the library's versioning
  information and adding a conditional check to prevent a compiler warning. These
  fixes ensure that the library can be built successfully, allowing developers to
  use the latest version of GCC without encountering build-related issues.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1aababb8e205a441fe55f9acecc8c6c1ca552ec6
date: '2026-05-19'
is_stub: false
---

This commit addresses build failures in libstdc++ introduced by commit acfdad706d8. It removes a symbol that was inadvertently included in `GLIBCXX_3.4.21` and adds a guard to quiet a warning related to exception handling. This ensures that the library builds correctly after the previous changes.
