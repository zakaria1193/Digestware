---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
commit_hash: d45381550ec25de9c5eb7168bad85586109b4991
source_type: github
author: Richard Biener
headline: tree-optimization/60075 - fix address-space handling in PRE
tldr: Corrects address-space handling in the PRE optimization pass.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In the SSA-based PRE pass (`tree-ssa-pre.cc`) and its verification
  component (`tree-ssa-sccvn.cc`), `COMPONENT_REF` operations were not correctly preserving
  address-space information derived from the `FIELD_DECL`. This commit modifies `copy_reference_ops_from_ref`
  and `create_component_ref_by_pieces_1` to properly account for address-space qualifiers,
  fixing PR60075.
primer_glossary:
- term: PRE
  definition: Partial Redundancy Elimination is a compiler optimization technique
    that eliminates redundant computations within a program. It aims to compute each
    expression at most once.
- term: COMPONENT_REF
  definition: A GCC internal representation node used to access a member of a structure
    or array. It represents dereferencing a pointer to a structure and accessing a
    specific field.
- term: FIELD_DECL
  definition: A declaration of a field within a structure or union type in GCC's internal
    representation.
- term: address-space qualification
  definition: Specifies that a memory access or pointer refers to a particular memory
    region or segment, which can affect how accesses are performed and optimized.
- term: SSA
  definition: Static Single Assignment form is an intermediate representation for
    compilers where every variable is assigned exactly once. It simplifies many optimization
    passes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d45381550ec25de9c5eb7168bad85586109b4991
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in the Partial Redundancy Elimination (PRE) optimization pass where address-space qualification was disregarded when handling COMPONENT_REF operations. By ensuring that the address-space context is correctly considered, this resolves a bug (PR60075) and ensures more accurate optimization. A new test case has been added to verify the fix.
