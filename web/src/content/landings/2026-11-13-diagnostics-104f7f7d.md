---
project: gcc
subsystem: diagnostics
patch_id: null
tags:
- diagnostics
- analyzer
- markup
commit_hash: 104f7f7d145d1d6e8a773c31442fdc782b44f681
source_type: github
author: David Malcolm
headline: Diagnostics gain new markup representation
tldr: A new tree-like markup representation for diagnostic messages is introduced
  to better support analyzer changes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's diagnostics system gains a new `diagnostics::markup` class, implemented
  in `diagnostics/markup.cc/.h`. This is a tree-based structure for representing diagnostic
  message components, intended to facilitate upcoming improvements to the analyzer's
  diagnostic reporting, particularly for complex cases and richer output formats.
primer_glossary:
- term: GCC analyzer
  definition: A static analysis component within GCC that inspects code without executing
    it, aiming to find bugs and provide information about program behavior.
- term: SARIF
  definition: Static Analysis Results Interchange Format, a standard JSON-based format
    for the output of static analysis tools.
- term: tree-like representation
  definition: A data structure organized hierarchically, where elements are nodes
    connected by edges, resembling a tree.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/104f7f7d145d1d6e8a773c31442fdc782b44f681
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

A new tree-like representation for diagnostic messages has been added to GCC's diagnostics infrastructure. This initial version is simple and primarily serves upcoming changes in the analyzer. Future work aims to enrich this markup to support richer output formats like HTML and Markdown in SARIF.
