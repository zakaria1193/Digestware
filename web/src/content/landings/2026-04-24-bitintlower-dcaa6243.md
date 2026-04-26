---
project: gcc
subsystem: bitintlower
patch_id: null
tags:
- bitint
- bugfix
- middle-end
commit_hash: dcaa624319dc58ed8b1f51f6e0718cba94d7a3b9
source_type: github
author: Jakub Jelinek
headline: 'bitintlower: Padding bit fixes, part 5'
tldr: Fixes padding bit handling for __builtin_{add,sub,mul}_overflow for _BitInt.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The commit modifies `bitint_large_huge::finish_arith_overflow` and
  `bitint_large_huge::lower_addsub_overflow` in `gimple-lower-bitint.cc`. The changes
  ensure that padding bits are correctly extended during `__builtin_{add,sub,mul}_overflow`
  operations on `_BitInt` types.  `bitintlower` is responsible for lowering the `_BitInt`
  type to lower-level operations. A search for "GCC bitintlower padding" clarifies
  the problem.
primer_general: '`_BitInt` is a feature that allows programmers to define integer
  types with a specific number of bits. When performing arithmetic operations on `_BitInt`
  types, the compiler needs to handle *padding bits*, which are extra bits added to
  ensure correct results. This commit fixes a bug in the compiler''s handling of padding
  bits during overflow checks for `_BitInt` types. Search for "GCC _BitInt padding"
  for more background.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dcaa624319dc58ed8b1f51f6e0718cba94d7a3b9
date: '2026-04-24'
---

This commit addresses padding bit handling for `__builtin_{add,sub,mul}_overflow` for `_BitInt`, resolving PR123635. It ensures correct extension of padding bits in partial and full limbs during overflow checks, handling cases where the result of the operation is ignored. This fix completes the padding bit handling for `_BitInt`, ensuring correct overflow behavior for extended bit integers.
