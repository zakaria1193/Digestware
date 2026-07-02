---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- string_view
- cpp20
commit_hash: bbcc9da1f026b202c692e0b47eeacd28e0c69c0d
source_type: github
author: Tomasz Kamiński
headline: Use type_identity_t for operator<=> parameter [PR114400]
tldr: This commit updates the `operator<=>` parameter type in `std::string_view` to
  use `type_identity_t`.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit changes the parameter type of `operator<=>` in `std::string_view`
  to use `type_identity_t` instead of `__type_identity_t`. This resolves LWG3950 and
  matches a prior change to `operator==`. The difference between `__type_identity`
  and `type_identity` is observable, ensuring exact resolution.
primer_general: This commit pertains to the `std::string_view` class in the C++ standard
  library, which provides a non-owning reference to a string. The `operator<=>` is
  the three-way comparison operator (introduced in C++20) that returns a result indicating
  whether one value is less than, equal to, or greater than another. Using `type_identity_t`
  ensures consistent type handling in comparisons.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bbcc9da1f026b202c692e0b47eeacd28e0c69c0d
date: '2026-05-13'
is_stub: false
---

This commit modifies the parameter type of the `operator<=>` in `std::string_view` to use `type_identity_t` instead of `__type_identity_t`. This change aligns with a similar update to `operator==` and fully addresses LWG3950, which concerns the specification of `std::basic_string_view` comparison operators.
