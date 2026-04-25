---
project: gcc
subsystem: c++/reflection
patch_id: null
tags:
- c++
- reflection
- templates
- bugfix
commit_hash: f78cb5ae260a88d9499d1496f3ba6fd54dd04bac
source_type: github
author: Marek Polacek
headline: 'C++/reflection: Fix error on dependent class template reflection.'
tldr: Fixes a bogus error when reflecting on a dependent class template.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The fix modifies `tsubst_qualified_id` in `cp/pt.cc` to avoid the "instantiation
  yields a type" error during reflection. It checks `!reflecting_p` instead of `name_lookup_p`
  to determine if the error should be suppressed. This addresses PR c++/124926.
primer_general: C++ reflection allows programs to inspect and manipulate their own
  structure at runtime.  Templates are code blueprints that can work with different
  data types.  A dependent class template is one where the definition depends on a
  template parameter. The compiler needs to be able to correctly handle these complex
  scenarios when doing reflection, and this patch fixes a case where it was issuing
  an incorrect error.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f78cb5ae260a88d9499d1496f3ba6fd54dd04bac
date: '2026-04-22'
---

The compiler was incorrectly issuing an error when reflecting on dependent class templates, specifically when a template's inner type turned out to be a class. The fix refrains from issuing the error in reflection contexts, allowing reflection of the TEMPLATE_DECL. This avoids spurious errors when reflecting on valid code constructs.
