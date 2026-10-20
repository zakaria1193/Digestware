---
project: gcc
subsystem: gcc/bitintlower
patch_id: null
tags:
- bitint
- lowering
- rotate
commit_hash: 013ac06a2d75f392a3acf8d2f775f1e9fdc54815
source_type: github
author: Jakub Jelinek
headline: 'bitintlower: Fix _BitInt rotates with signed operands'
tldr: Correctly lowers large/huge _BitInt rotates involving signed operands, fixing
  incorrect casts and missing uses.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The gimple-lower-bitint pass incorrectly handled LROTATE_EXPR and RROTATE_EXPR
  involving signed large/huge _BitInt operands. When the right-hand side operand was
  not a constant, the pass mistakenly cast the signed operand to the same signed type
  instead of its unsigned counterpart, and the result of this cast was unused. This
  patch corrects the cast target to the unsigned type and ensures the cast result
  is properly utilized in the lowered GIMPLE code.
primer_glossary:
- term: _BitInt
  definition: A GCC extension for arbitrary-precision integers, allowing users to
    specify integers of any bit width.
- term: gimple-lower-bitint
  definition: A GCC compiler pass that lowers operations on _BitInt types into GIMPLE,
    GCC's intermediate representation.
- term: LROTATE_EXPR / RROTATE_EXPR
  definition: Intermediate Representation (IR) expressions representing left and right
    bitwise rotations, respectively.
- term: GIMPLE
  definition: GCC's Internal Multiple Expression processing, a three-address intermediate
    representation used within the compiler.
- term: INTEGER_CST
  definition: An intermediate representation node representing a constant integer
    value.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/013ac06a2d75f392a3acf8d2f775f1e9fdc54815
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in the lowering of large and huge _BitInt rotates when a signed operand is involved. Previously, the code incorrectly cast signed operands to themselves instead of their unsigned variants and failed to use the cast result. This resolves a bug where these operations were not handled correctly, ensuring proper code generation for bit-integer rotates.
