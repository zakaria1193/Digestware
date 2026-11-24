---
project: gcc
subsystem: codeview
patch_id: null
tags:
- debug
- codeview
- c++
commit_hash: 6ed52bcf46c4c5abc598d8980bcadd6ad3cb692c
source_type: github
author: Oleg Tolmatcev
headline: Codeview handles nested types in anonymous structures.
tldr: Fixes infinite recursion in CodeView generation when processing nested types
  within anonymous structures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `dwarf2codeview.cc`, `get_type_num_struct` previously suffered from
  re-entrancy issues when handling nested types within anonymous structures. Visiting
  a parent type could lead to infinite recursion if the nested type's structure was
  not yet complete. This patch defers processing of parent definitions until the nested
  type is finalized and correctly handles types appended during the flushing of deferred
  types. It also ensures that complete definitions are maintained for unnamed member
  types to differentiate them from forward references.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ed52bcf46c4c5abc598d8980bcadd6ad3cb692c
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

This commit addresses an issue in CodeView debug info generation where visiting a nested type's parent could lead to infinite recursion within unfinished anonymous structures. The solution defers parent processing until the nested type is complete and handles deferred parent definitions. It also ensures distinct types, even when unnamed, are kept complete to avoid issues with indistinguishable forward references.
