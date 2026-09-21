---
project: gcc
subsystem: fold-mem-offsets
patch_id: null
tags:
- optimization
- rtl
- bugfix
commit_hash: fc96e933de8d29f91ad7ab9cf982ad498bc5c9d0
source_type: github
author: Konstantinos Eleftheriou
headline: Group fold-mem-offsets changes by shared fold insns
tldr: Corrects fold-mem-offsets to group related changes by shared instructions, preventing
  incorrect optimizations.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `fold-mem-offsets` pass in `fold-mem-offsets.cc` previously grouped
  changes based on the register defined by the last fold insn in a def-chain. This
  commit refactors this grouping mechanism to use a `fold_groups` class which identifies
  connected components of roots that share a fold insn. This is managed using a union-find
  data structure. If any root within a component cannot be updated (e.g., due to offset
  limitations like `LDRSB` range), its entire component is cancelled. Furthermore,
  all surviving groups are committed in a single `change_insns` call, eliminating
  a previous sort over gr…
primer_glossary:
- term: fold-mem-offsets
  definition: A GCC optimization pass that folds constant values into memory offset
    calculations.
- term: insn
  definition: Abbreviation for instruction, typically referring to machine instructions
    or RTL (Register Transfer Language) in GCC's internal representation.
- term: def-chain
  definition: A sequence of definitions where the output of one operation becomes
    the input of the next.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used in GCC
    that describes operations on registers and memory.
- term: union-find
  definition: A data structure that keeps track of a set of elements partitioned into
    a number of disjoint (non-overlapping) subsets. It is efficient for grouping related
    items.
- term: PR126412
  definition: Problem Report 126412, indicating a bug in the GCC compiler that this
    commit aims to fix.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fc96e933de8d29f91ad7ab9cf982ad498bc5c9d0
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This change addresses a bug in the `fold-mem-offsets` pass where related memory offset computations were not correctly grouped. Previously, changes were grouped based on the final register defined by a fold instruction, which could lead to incorrect zeroing of shared base offsets if different chains ended in different registers. The fix now groups changes by the connected components of roots sharing a fold instruction, ensuring that if any part of a component cannot be updated, the entire group is rolled back, preventing incorrect optimizations and fixing PR126412.
