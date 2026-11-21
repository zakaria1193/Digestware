---
project: gcc
subsystem: gcc/bitintlower
patch_id: null
tags:
- gcc
- optimization
- bugfix
commit_hash: 4abe2b137f26173c489f4acb96f662ea542a0519
source_type: github
author: Jakub Jelinek
headline: Handle COMPLEX_CST lowering for _BitInt types
tldr: GCC's bitintlower pass now correctly handles complex constants involving _BitInt
  types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gimple-lower-bitint.cc` pass, specifically functions like `lower_complexexpr_stmt`
  and `lower_stmt`, lacked support for `COMPLEX_CST` nodes when dealing with `_BitInt`
  types. This was problematic because, while GCC doesn't support `_Complex _BitInt`
  directly, `_BitInt` types can appear in the real and imaginary parts of standard
  `_Complex` types, or as results of overflow operations. This commit extends the
  lowering logic to handle `COMPLEX_CST` by decomposing them into their constituent
  `_BitInt` components, and also adjusts the SSA name discovery to consider `COMPLEX_TYPE`s
  involving `…
primer_glossary:
- term: _BitInt
  definition: A GCC extension allowing arbitrarily sized integer types, specified
    as `_BitInt(N)` where N is the number of bits.
- term: lowering
  definition: The process of transforming high-level or complex intermediate representations
    into simpler ones that are closer to machine code. In GCC, this often involves
    converting specific types or expressions into more fundamental operations.
- term: COMPLEX_CST
  definition: GCC's internal representation for a complex number constant.
- term: COMPLEX_TYPE
  definition: GCC's internal representation for a complex number type.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation used in
    compilers where each variable is assigned a value exactly once. It simplifies
    many program analyses and optimizations.
- term: GIMPLE
  definition: GCC's primary intermediate representation for optimization, which is
    a three-address pseudo-assembly language.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4abe2b137f26173c489f4acb96f662ea542a0519
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

GCC's `bitintlower` pass, responsible for lowering `_BitInt` types, has been updated to correctly handle `COMPLEX_CST` constructs. Previously, it did not account for complex constants formed with `_BitInt` types, leading to miscompilations when these constructs were encountered after certain optimizations like CFG cleanup removed edges. This change ensures that complex expressions involving `_BitInt` are properly lowered, fixing a bug where these were not handled and could lead to incorrect code generation.
