---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- debugging
- static analysis
- value range
commit_hash: 4d4ccbd5a52e4c9963318a7d7966bed08be9b806
source_type: github
author: David Malcolm
headline: 'analyzer: Show value ranges in svalue::dump'
tldr: The static analyzer now displays value range information when dumping svalue
  nodes, aiding debugging.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch modifies `analyzer/svalue.cc` to include value range information
  in the `svalue::dump` output. It introduces `value_range::print` in `value-range.cc`
  and `value-range.h` to format the value range information. This enhancement aids
  in debugging the static analyzer by providing more context about the state of `svalue`
  nodes during analysis.
primer_general: The GCC compiler includes a static analyzer that attempts to find
  potential bugs in code before it is run. This commit enhances the debugging capabilities
  of the static analyzer by adding the ability to display the range of possible values
  that a variable can hold at different points in the code. This information can be
  invaluable for understanding how the analyzer is working and for identifying the
  root cause of potential issues that the analyzer flags.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4d4ccbd5a52e4c9963318a7d7966bed08be9b806
date: '2026-05-06'
---

The static analyzer now includes value range information when dumping `svalue` nodes for debugging purposes. This allows developers to inspect the range of possible values for each node, which can be helpful for understanding the analyzer's reasoning and diagnosing issues in the code being analyzed. The value range is displayed in the output of `svalue::dump`.
