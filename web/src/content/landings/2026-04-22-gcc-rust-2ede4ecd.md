---
project: gcc
subsystem: gcc/rust
patch_id: null
tags:
- optimization
- name resolution
- data flow analysis
commit_hash: 2ede4ecdee9e806008ab9bd836be4714c49b8902
source_type: github
author: Arthur Cohen
headline: Marklive now looks up variables in types namespace
tldr: The Rust front-end's marklive pass can now correctly identify live variables
  by searching in both value and type namespaces.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `MarkLive::find_value_definition` function in `gcc/rust/checks/lints/rust-lint-marklive.cc`
  is part of the dataflow analysis for determining live variables. By extending the
  lookup to include the Types namespace alongside the Values namespace, the pass can
  now correctly identify variables that might be referenced within type contexts,
  which was previously overlooked.
primer_general: Compilers often have a stage called 'marklive' which determines which
  variables are still important and might be used later in the program. This helps
  the compiler optimize code by removing unused variables. This commit improves the
  Rust front-end's 'marklive' stage by allowing it to look for variables in more places,
  specifically in the 'Types Namespace' in addition to the 'Values Namespace.' This
  means the compiler will be better at identifying truly "live" variables, leading
  to more accurate code optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2ede4ecdee9e806008ab9bd836be4714c49b8902
date: '2026-04-22'
is_stub: false
stub_reason: ''
---

The marklive pass in the Rust front-end has been updated to consider the Types namespace when looking up variable definitions. Previously, it only searched the Values namespace, potentially missing live variables and leading to incorrect analysis. This change improves the accuracy of live variable analysis.
