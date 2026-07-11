---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- type traits
- testing
commit_hash: ce964ffb653f7134f93b662a332a9467677066ac
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Test has_unique_object_representations with incomplete types.'
tldr: Tests `has_unique_object_representations` with incomplete types, addressing
  LWG4113.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a negative test for `std::has_unique_object_representations`
  to catch incorrect instantiations with incomplete types as arrays, aligning with
  LWG4113. The standard library's trait should not be evaluated for incomplete types
  that would be disallowed according to the standard's wording.
primer_glossary:
- term: libstdc++
  definition: The C++ standard library implementation used by GCC.
- term: has_unique_object_representations
  definition: A C++ type trait that checks if a type has unique object representations,
    meaning no two distinct objects of that type have the same bit pattern. It's crucial
    for certain optimizations and serialization.
- term: incomplete type
  definition: A type in C++ for which the definition is not yet complete. For example,
    a forward declaration of a class or struct, or an array where the size is not
    specified.
- term: LWG4113
  definition: A specific issue (numbered 4113) raised and resolved by the C++ Library
    Working Group (LWG), concerning the behavior of `std::has_unique_object_representations`
    with incomplete types.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ce964ffb653f7134f93b662a332a9467677066ac
date: '2026-07-10'
is_stub: true
stub_reason: low_score
---

A new negative test case has been added to libstdc++ to verify that `std::has_unique_object_representations` correctly handles incomplete types, particularly in array contexts. This addresses the Library Working Group issue LWG4113, which specified disallowing `has_unique_object_representations` for incomplete arrays.
