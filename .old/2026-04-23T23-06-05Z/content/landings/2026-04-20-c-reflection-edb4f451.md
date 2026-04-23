---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- warnings
- libstdc++
commit_hash: edb4f451b6aaa6d6c6851f2cb83313f9c30c36e2
source_type: github
author: Marek Polacek
headline: Suppress bogus -Wmissing-field-initializers warning with <meta>.
tldr: This commit suppresses false -Wmissing-field-initializers warnings when using
  the `<meta>` reflection feature.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit modifies `std::meta::data_member_options` in the libstdc++
  standard library to initialize its members, specifically related to C++ reflection.  The
  initialization suppresses the `-Wmissing-field-initializers` warning, improving
  the user experience when working with reflection features. The change is specific
  to the C++ front end and its interaction with the standard library's reflection
  components.
primer_general: The C++ compiler can warn about uninitialized fields in a struct.  However,
  with the new reflection features, these warnings can sometimes be incorrectly triggered.
  This commit fixes this issue by explicitly initializing fields in the `std::meta::data_member_options`
  structure. This prevents the compiler from issuing false warnings about missing
  field initializers when using C++ reflection, resulting in cleaner builds.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/edb4f451b6aaa6d6c6851f2cb83313f9c30c36e2
date: '2026-04-20'
---

The commit addresses an issue where the compiler was emitting `-Wmissing-field-initializers` warnings for code using the `<meta>` reflection feature.  To resolve this, the members of `std::meta::data_member_options` are initialized to suppress the warning. Initializers have been added for `alignment`, `bit_width`, and `annotations` members.
