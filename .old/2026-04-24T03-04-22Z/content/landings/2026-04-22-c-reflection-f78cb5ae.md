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
headline: 'C++/reflection: Reflect on dependent class template'
tldr: Fixes an error when reflecting on dependent class templates, allowing reflection
  on both types and non-types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The issue arises in ``tsubst_qualified_id`` within ``pt.cc`` when handling
  ``REFLECT_EXPR`` for dependent class templates. The code incorrectly issued an error
  because it couldn't determine the type of ``Inner`` in ``Cls<T>::template Inner``.
  The fix adjusts the logic to avoid this error when reflection is active, allowing
  the reflection of the ``TEMPLATE_DECL``.
primer_general: Reflection in C++ enables a program to inspect and modify its own
  structure and behavior at runtime.  Dependent class templates are templates that
  depend on template parameters. This commit fixes a bug in the compiler that prevented
  reflection from working correctly with dependent class templates. With this fix,
  the compiler can now correctly reflect on these templates, allowing programs to
  examine their structure and properties at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f78cb5ae260a88d9499d1496f3ba6fd54dd04bac
date: '2026-04-22'
---

Previously, the compiler would incorrectly issue an error when reflecting on a dependent class template such as ``Cls<T>::template Inner``, because it couldn't determine in advance what it would substitute into.  The fix refrains from issuing the error and takes the reflection of the ``TEMPLATE_DECL``, ensuring reflection works correctly for both types and non-types in this context.
