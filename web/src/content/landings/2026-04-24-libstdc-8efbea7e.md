---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- chrono
- C++
- standard library
commit_hash: 8efbea7eeef317c5d2699ef8ac638883577b19a2
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Disallows duration of cv-qualified types and references.'
tldr: The chrono::duration template can no longer be instantiated with cv-qualified
  or reference types, as per LWG 4481.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit implements LWG 4481, "Disallow chrono::duration<const
  T, P>", by adding a `static_assert` in `<bits/chrono.h>` that requires the `T` template
  parameter of `chrono::duration<T, P>` to be cv-unqualified and non-reference.  This
  change directly impacts the standard library''s `<chrono>` implementation. search_context:
  libstdc++ chrono::duration cv-qualified types references LWG 4481'
primer_general: The C++ standard library provides the `chrono` library for dealing
  with time and duration. The `chrono::duration` template represents a time interval.
  This commit restricts the types that can be used to represent the underlying value
  of a duration, preventing potential errors and ensuring consistency with the C++
  standard.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8efbea7eeef317c5d2699ef8ac638883577b19a2
date: '2026-04-24'
---

This commit enforces LWG 4481, which disallows the instantiation of `chrono::duration` with cv-qualified or reference types. This restriction is implemented via a `static_assert` that checks the type used to instantiate the duration. Corresponding testsuite adjustments are included.
