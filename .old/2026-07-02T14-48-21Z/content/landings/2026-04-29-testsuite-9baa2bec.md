---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- plugin
- libstdc++
- uglification
- obfuscation
commit_hash: 9baa2bec9e0ef6f8098216777c9ada1425617d43
source_type: github
author: Jakub Jelinek
headline: 'testsuite: Add C++ plugin to check for libstdc++ header uglification'
tldr: A new GCC plugin checks for proper name uglification in libstdc++ headers, improving
  code obfuscation.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit adds `g++.dg/plugin/uglification_plugin.cc` to the GCC testsuite.
  This plugin checks for non-uglified names in libstdc++ headers, specifically function
  parameters, automatic variables, template arguments, and requires arguments. The
  plugin allows non-uglified names that are function/template names in the `std` namespace.
  The `uglification.C` test verifies the plugin's diagnostics.
primer_general: This commit adds a new tool to GCC's testing framework that improves
  the ability to hide the inner workings of the C++ standard library (libstdc++).
  The tool, called a plugin, checks that the names of variables and functions within
  the library are properly scrambled (uglified) to make it harder for someone to reverse
  engineer the code. This helps protect any proprietary algorithms or techniques used
  in the library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9baa2bec9e0ef6f8098216777c9ada1425617d43
date: '2026-04-29'
---

This commit introduces a new plugin to the GCC testsuite that checks for proper name uglification (obfuscation) in libstdc++ headers. The plugin identifies non-obfuscated function parameter names, automatic variable names, template arguments, and requires arguments, while making exceptions for names that appear as function/template names in the `std` namespace. A set of test cases is also added to verify the plugin's functionality across different C++ standards. This change enhances code obfuscation.
