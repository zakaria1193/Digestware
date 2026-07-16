---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- wchar_t
- c++23
commit_hash: fb0c03ee7afca608cba0419629184b8f442085e2
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Fix std module to work with --disable-wchar_t'
tldr: Removes unnecessary aliases and declarations from std module headers when wchar_t
  is disabled.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The std module's C++23 interface exposes various stream and format-related
  entities. When `_GLIBCXX_USE_WCHAR_T` is not defined (due to `--disable-wchar_t`
  configuration), certain wide-character-dependent entities like `wspanbuf` and `wosyncstream`
  should not be declared or exported. This commit revises `std.cc.in` and related
  headers to conditionally include these declarations, preventing spurious errors
  and ensuring correctness for non-wide builds.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fb0c03ee7afca608cba0419629184b8f442085e2
date: '2026-07-13'
is_stub: true
stub_reason: low_score
---

The C++ standard library's std module now correctly handles configurations where wchar_t is disabled. This change removes superfluous declarations in headers like <format>, <spanstream>, and <syncstream> that were previously included even when not applicable. This prevents potential issues and ensures the module conforms to the build configuration.
