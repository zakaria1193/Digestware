---
project: gcc
subsystem: gcc/target/aarch64
patch_id: null
tags:
- aarch64
- internal
- bugfix
commit_hash: 37dcc821a450f9e14aa0bc27b60ac1f8007fc183
source_type: github
author: Alice Carlotti
headline: 'aarch64: Fix assert checking alias feature bits'
tldr: Corrected assertion for aarch64 feature flags improves internal accuracy.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `aarch64_get_extension_string_for_isa_flags` function's assertion
  was incorrectly validating the global `aarch64_isa_flags` instead of the function's
  `isa_flags` parameter. This commit rectifies the check to focus on the parameter.
  It also removes redundant cpuinfo feature string definitions for alias bits, which
  were causing false positives on the corrected assert.
primer_glossary:
- term: isa_flags
  definition: A parameter representing the instruction set architecture flags for
    a specific CPU or configuration.
- term: alias bits
  definition: Specific bits within feature flags that represent alternative or shorthand
    names for certain instruction set extensions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/37dcc821a450f9e14aa0bc27b60ac1f8007fc183
date: '2026-07-15'
is_stub: true
stub_reason: low_score
---

An assertion within the aarch64 target's feature detection logic has been corrected to accurately check for alias bits in the `isa_flags` parameter. Previously, it incorrectly checked the global `aarch64_isa_flags` value. Additionally, CPU info feature string entries for alias features were removed to prevent the corrected assert from being triggered erroneously.
