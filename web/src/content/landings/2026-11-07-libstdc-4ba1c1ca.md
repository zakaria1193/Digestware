---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- locale
- warnings
- newlib
commit_hash: 4ba1c1cad51b5fa4c409a8e8d926c8e10e1b9563
source_type: github
author: Thomas Schwinge
headline: Fix type-limits warnings in libstdc++ newlib ctype_members.cc.
tldr: Resolves compiler warnings about unsigned comparisons in libstdc++'s newlib
  ctype implementation.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libstdc++` locale implementation for newlib, specifically in `config/locale/newlib/ctype_members.cc`,
  contains logic for character narrowing (`do_narrow`) that triggers `-Wtype-limits`
  warnings when compiled with `-Werror`. The warnings arise from comparisons like
  `__wc >= 0` where `__wc` is an unsigned type. This patch introduces a `use_table`
  helper function, similar to the one in `config/locale/gnu/ctype_members.cc`, to
  correctly handle these comparisons and avoid the warnings. The `ctype<wchar_t>::do_narrow`
  methods now utilize this helper.
primer_glossary:
- term: libstdc++
  definition: The standard C++ library implementation provided by GCC. It includes
    the C++ standard library headers and their implementations.
- term: ctype
  definition: In C and C++, character classification and conversion functions, typically
    found in the <cctype> or <locale> headers. This relates to the `std::ctype` facet
    in the C++ locale framework.
- term: -Wtype-limits
  definition: A GCC compiler warning flag that detects comparisons that are likely
    to be always true or always false due to the properties of the data types involved
    (e.g., comparing an unsigned integer to a negative number).
- term: wchar_t
  definition: A distinct integer type capable of representing the largest supported
    character set. It is used for wide character strings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4ba1c1cad51b5fa4c409a8e8d926c8e10e1b9563
date: '2026-11-07'
is_stub: true
stub_reason: low_score
---

This commit resolves compiler warnings related to unsigned expression comparisons in `libstdc++-v3/config/locale/newlib/ctype_members.cc`. The code was triggering `-Wtype-limits` warnings because unsigned variables were being compared against zero, which is always true. The fix mirrors a previous patch applied to the GNU locale version, introducing a helper function `use_table` to correctly handle character narrowing.
