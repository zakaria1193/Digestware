---
project: gcc
subsystem: gcc/rust
patch_id: null
tags:
- name resolution
- imports
- modules
commit_hash: 2d7aeae0fd0aeb54dfeb7ad59d58d19f346223e1
source_type: github
author: Arthur Cohen
headline: Imports and modules are properly resolved in segments within the Rust front-end
tldr: The Rust front-end for GCC now correctly resolves imports and modules within
  path segments by allowing multiple mappings of the same usage and treating imports…
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change in `gcc/rust/resolve/rust-early-name-resolver-2.0.cc` (specifically
  `Early::finalize_rebind_import`) now correctly processes imports as potential glob
  containers. Additionally, `NameResolutionContext::map_usage` in `rust-name-resolution-context.cc`
  is updated to allow multiple mappings for a single usage. This is crucial for Rust's
  hierarchical module system and `use` declarations, where a single identifier might
  be resolved via various paths or re-exports, and ensures that the name resolver
  correctly captures all relevant aliases and re-exports, which is tested by `import_in_type…
primer_general: In programming, 'imports' and 'modules' are ways to organize and reuse
  code by bringing in functionalities from other files or libraries. Sometimes, a
  single name can refer to different things depending on how it's imported or organized
  within a module. This commit improves how the Rust front-end for GCC understands
  these complex relationships. It now correctly handles situations where a name might
  be imported in multiple ways, and it treats imports more flexibly, recognizing them
  as potential 'containers' for many different items. This makes the compiler much
  better at figuring out what names refer to, especially in programs that extensively
  use imports and modules.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2d7aeae0fd0aeb54dfeb7ad59d58d19f346223e1
date: '2026-03-24'
is_stub: false
stub_reason: ''
---

This commit enhances name resolution in the Rust front-end by improving how imports and modules are handled within path segments. It allows for multiple mappings of the same usage, enabling more flexible resolution, and treats imports as potential glob containers. These changes ensure a more accurate and robust resolution of complex module structures and imports within Rust code.
