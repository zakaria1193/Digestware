---
project: gcc
subsystem: gcc/cp/reflection
patch_id: null
tags:
- c++
- reflection
- memory-management
commit_hash: d66469b5bfe5983ca35a562c89384427f6029a3e
source_type: github
author: Marek Polacek
headline: Fix nits in C++ reflection string translation and length handling.
tldr: Corrects memory management and string length interpretation in GCC's C++ reflection
  implementation.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/cp/reflect.cc`, this patch refactors string handling within
  reflection evaluation functions. It corrects a memory leak by ensuring `ostr.text`
  is freed when `cpp_translate_string` succeeds. Additionally, it adjusts how string
  lengths are handled, specifically in `eval_exception__S_exception_cvt_tofrom_utf8`,
  to correctly use `TREE_STRING_LENGTH` as a size rather than assuming it's a null-terminated
  string length plus one, aligning with the `tree.h` definition.
primer_glossary:
- term: C++ reflection
  definition: A feature that allows a program to inspect and modify its own structure
    and behavior at runtime or compile time. GCC's implementation is part of its experimental
    support for C++26 reflection proposals.
- term: TREE_STRING_LENGTH
  definition: A macro or field in GCC's internal representation (tree) that stores
    the length of a string constant.
- term: ostr.text
  definition: A pointer to a character buffer used for output strings within the reflection
    code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d66469b5bfe5983ca35a562c89384427f6029a3e
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This commit addresses two issues in GCC's C++ reflection subsystem. First, it ensures that dynamically allocated string buffers are properly freed after use in `cpp_translate_string`. Second, it corrects the interpretation of `TREE_STRING_LENGTH` to align with its documented behavior (size, not null-terminated length), preventing off-by-one errors when calculating string lengths.
