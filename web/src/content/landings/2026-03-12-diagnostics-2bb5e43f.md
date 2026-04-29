---
project: gcc
subsystem: diagnostics
patch_id: null
tags:
- diagnostics
- memory management
- refactoring
commit_hash: 2bb5e43f9c0444eab33a9201057fb1bae6b20e86
source_type: github
author: David Malcolm
headline: 'Diagnostics: Use label_text in diagnostics::option_id_manager'
tldr: Improves memory management in the diagnostics subsystem by using label_text
  for option IDs.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit modifies the diagnostics subsystem to use `label_text` for
  option names and URLs, replacing manual memory management. It also converts `sarif_builder::m_rule_id_set`
  from a `hash_set <free_string_hash>` to `std::set<std::string>`, removing manual
  memory management in SARIF report generation. This affects `diagnostics/context.h`,
  `diagnostics/option-id-manager.h`, `diagnostics/sarif-sink.cc` and other files.
primer_general: This commit focuses on improving the diagnostics subsystem of GCC,
  which is responsible for generating warnings and errors during compilation. It replaces
  manual memory management with more modern C++ constructs like `label_text` and `std::set`.
  This reduces the risk of memory leaks and simplifies the code base, leading to a
  more robust and maintainable compiler.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2bb5e43f9c0444eab33a9201057fb1bae6b20e86
date: '2026-03-12'
---

This commit improves memory management within the GCC diagnostics subsystem. It replaces manual memory management for option names and URLs with `label_text`, leveraging standard containers to manage the set of rule IDs in SARIF output, which simplifies the code and reduces the risk of memory leaks.  This change impacts the generation of diagnostic messages and SARIF reports.
