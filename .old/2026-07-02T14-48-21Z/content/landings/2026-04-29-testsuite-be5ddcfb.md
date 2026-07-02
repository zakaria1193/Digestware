---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- plugin
- uglification
- C++
commit_hash: be5ddcfb41747926851964dcfda161725c557e3f
source_type: github
author: Jakub Jelinek
headline: 'testsuite: Diagnose non-uglified names even in requires exprs'
tldr: The GCC testsuite now checks for non-uglified names in requires expressions,
  lambda parameters, and captures, enhancing code obfuscation capabilities.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `g++.dg/plugin/uglification_plugin.cc` to walk
  `REQUIRES_EXPR_PARMS` of `REQUIRES_EXPR`, `TEMPLATE_PARMS_CONSTRAINTS` and `DECL_INITIAL`
  of `CONCEPT_DECL` during the plugin check. It adds test cases to `g++.dg/plugin/uglification.C`
  to verify the plugin's behavior in these scenarios. This ensures that non-uglified
  names are diagnosed even within requires expressions and lambda constructs when
  the uglification plugin is enabled.
primer_general: This commit enhances GCC's ability to obfuscate code by renaming symbols
  to make them harder to understand (uglification). The changes ensure that the compiler
  can detect and rename symbols even within advanced C++ features like requires expressions
  (used in concepts) and lambda functions. The updated testsuite verifies that the
  uglification process works correctly in these cases, making the compiled code more
  difficult to reverse engineer.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/be5ddcfb41747926851964dcfda161725c557e3f
date: '2026-04-29'
---

This commit extends the GCC testsuite and the uglification plugin to diagnose non-uglified names within requires expressions, lambda parameters and captures. The plugin now walks REQUIRES_EXPR_PARMS of REQUIRES_EXPR and also traverses TEMPLATE_PARMS_CONSTRAINTS and DECL_INITIAL of CONCEPT_DECL to identify non-uglified names. New test cases are added to verify that the plugin correctly identifies non-uglified names in these contexts. This change improves the effectiveness of code obfuscation by ensuring that names are consistently uglified throughout the code.
