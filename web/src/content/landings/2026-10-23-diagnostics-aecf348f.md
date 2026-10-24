---
project: gcc
subsystem: diagnostics
patch_id: null
tags:
- diagnostics
- documentation
commit_hash: aecf348fc7920e0a3d7119aa1fd16fddef964928
source_type: github
author: David Malcolm
headline: Correct terminology in GCC diagnostics comment.
tldr: GCC diagnostics comment updated to use 'diagnostic sinks' instead of 'output
  formats'.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The comment in `gcc/diagnostics/context.cc` within the `context::report_diagnostic`
  function has been updated. The phrase 'output formats' has been replaced with 'diagnostic
  sinks' to align with the current terminology used within the diagnostics subsystem.
  This change is purely cosmetic and intended to improve the clarity and consistency
  of the codebase's documentation.
primer_glossary:
- term: diagnostic sinks
  definition: Components or handlers within the GCC compiler that receive and process
    diagnostic messages (errors, warnings, etc.) for output.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aecf348fc7920e0a3d7119aa1fd16fddef964928
date: '2026-10-23'
is_stub: true
stub_reason: low_score
---

This commit makes a non-functional change to a comment within the GCC diagnostics system. The term 'output formats' has been replaced with the more accurate terminology 'diagnostic sinks' in the `context::report_diagnostic` function's comment. This change clarifies the terminology used in the codebase without altering any behavior.
