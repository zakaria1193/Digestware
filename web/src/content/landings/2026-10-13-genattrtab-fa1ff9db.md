---
project: gcc
subsystem: genattrtab
patch_id: null
tags:
- optimization
- genattrtab
- build system
- performance
commit_hash: fa1ff9dba46c29992d443e1a22a6a4a21fa0c493
source_type: github
author: Kyrylo Tkachov
headline: 'genattrtab: Deduplicate attribute value simplifications'
tldr: Reduces redundant work in attribute table generation by simplifying values only
  once per unique set.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `optimize_attrs` pass in `genattrtab.cc` previously re-simplified
  attribute values for instruction codes that had identical attribute sets. This patch
  introduces a hash table keyed by attribute values and alternatives to group such
  instruction codes. Simplification is now performed only once per group, with other
  instruction codes inheriting the results. This drastically cuts down computation,
  particularly for targets with many repeated attribute value patterns.
primer_glossary:
- term: genattrtab
  definition: A GCC internal tool that generates attribute tables used by various
    backends for instruction selection and scheduling.
- term: optimize_attrs
  definition: A function within genattrtab that simplifies attribute values based
    on other attributes for a given instruction code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fa1ff9dba46c29992d443e1a22a6a4a21fa0c493
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This commit enhances `genattrtab`'s `optimize_attrs` function by avoiding repeated simplifications of attribute values for instruction codes that share the same attribute alternatives and values. A hash table now groups identical instruction codes, ensuring simplification occurs only for the first instance. Subsequent identical codes reuse the computed values, significantly speeding up `genattrtab` for various backends, especially AArch64 and RISC-V.
