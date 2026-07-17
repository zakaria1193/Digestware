---
project: gcc
subsystem: gcc/tree-optimization
patch_id: null
tags:
- optimization
- bitint
- compiler-pass
commit_hash: b032f71e16603f974b4cbc3d87752d21f43980af
source_type: github
author: Jakub Jelinek
headline: Fix potential overlap in bitint multiplication overflow checks
tldr: Ensures safe handling of bit-integer multiplication overflow by preventing overlap
  between destination and source operands.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `bitintlower` pass previously had a bug in `build_bitint_stmt_ssa_conflicts`
  where it did not correctly handle potential overlaps between the LHS (destination)
  and input operands for `__mulbitint3` and `__divmodbitint4` when `muldiv_p` was
  false. This commit ensures `IFN_MUL_OVERFLOW` and `IFN_UBSAN_CHECK_MUL` are always
  treated as `muldiv_p = true`, thereby guaranteeing that `use` operations on SSA
  operands are performed before the `def` on the LHS, preventing memory corruption
  in the libgcc functions.
primer_glossary:
- term: bitintlower
  definition: A GCC compiler pass responsible for lowering user-defined bit-integer
    types into machine-independent intermediate representations.
- term: SSA
  definition: Static Single Assignment form, an intermediate representation in compilers
    where every variable is assigned a value exactly once.
- term: LHS
  definition: Left-Hand Side, typically referring to the destination or the left operand
    in an assignment or expression.
- term: libgcc
  definition: The GCC runtime library that provides support for built-in functions
    and operations not directly supported by the target hardware.
- term: muldiv_p
  definition: A flag indicating whether an operation is a multiplication or division,
    which affects how operand overlaps are handled in the bitint lowering pass.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b032f71e16603f974b4cbc3d87752d21f43980af
date: '2026-07-16'
is_stub: false
stub_reason: ''
---

This commit addresses a potential issue in the `bitintlower` pass where the destination and source operands for multiplication overflow checks could overlap. It modifies `build_bitint_stmt_ssa_conflicts` to treat `IFN_MUL_OVERFLOW` and `IFN_UBSAN_CHECK_MUL` operations as multiplication/division types, preventing data corruption in libgcc's `__mulbitint3` calls.
