---
project: gcc
subsystem: regrename
patch_id: null
tags:
- regrename
- optimization
- assembly
commit_hash: cfc8ba7fa91eb7bf12fb7cd01542ddee2c337fb0
source_type: github
author: Andrew Stubbs
headline: Register renamer handles memory addresses with segments
tldr: Fixes register renaming for memory addresses containing explicit segment components.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `scan_rtx_address` function in `regrename.cc` now recursively processes
  UNSPEC elements within MEM address expressions that represent explicit segments.
  This ensures that register renaming correctly identifies and assigns registers for
  memory accesses involving segmented addressing, preventing incorrect register allocation
  on architectures where 32-bit registers must accommodate 64-bit addresses (e.g.,
  using non-contiguous register pairs).
primer_glossary:
- term: Register Rename
  definition: A compiler optimization pass that renames registers to eliminate false
    dependencies, improve liveness analysis, and facilitate other optimizations. It
    helps manage register allocation by ensuring each value has a unique register
    throughout its lifetime.
- term: MEM
  definition: An RTL construct representing a memory operand, specifying an address
    and its associated data.
- term: UNSPEC
  definition: An RTL construct representing an operation not directly supported by
    standard RTL, often used for target-specific or internal compiler operations.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC.
    It is more hardware-oriented than GIMPLE and closer to assembly code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cfc8ba7fa91eb7bf12fb7cd01542ddee2c337fb0
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

The register rename pass in GCC has been updated to correctly handle memory addresses that include explicit segment information. Prior to this change, the pass could misidentify register components in segmented addresses, potentially corrupting 64-bit addresses on targets with 32-bit registers by placing address parts in non-contiguous registers. The fix in `regrename.cc` ensures that arbitrary UNSPECs used as segments are properly recursed into.
