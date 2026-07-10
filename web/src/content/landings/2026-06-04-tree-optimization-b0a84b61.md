---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-optimization
- arithmetic
commit_hash: b0a84b6100389c5b24658743252a7ff259ba0816
source_type: github
author: Zhou Xuhang
headline: 'tree-optimization: Recognize widened unsigned multiply overflow checks'
tldr: GCC now recognizes and optimizes widened unsigned multiply overflow checks,
  canonicalizing them to a specific overflow detection pattern.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change enhances `match.pd` to recognize overflow checks for unsigned
  widened multiplications. It first canonicalizes shifted high-half forms to a widened
  comparison against the narrow type's maximum (e.g., `(a*b) >> N == MAX_T`). Subsequently,
  this comparison is folded to `IFN_MUL_OVERFLOW` if the target has native support,
  optimizing checks for conditions like `(unsigned short)(a*b) > 65535`.
primer_glossary:
- term: tree-optimization
  definition: GCC's middle-end optimization framework that operates on an intermediate
    representation called GENERIC/GIMPLE, which resembles an abstract syntax tree.
- term: widened multiplication
  definition: A multiplication operation where the operands are promoted to a wider
    type before multiplication. For example, multiplying two 16-bit integers into
    a 32-bit result.
- term: overflow check
  definition: A check to determine if the result of an arithmetic operation exceeds
    the representable range of the data type.
- term: canonicalize
  definition: To transform an expression or pattern into a standard, unique form,
    making it easier for optimizations to recognize and manipulate.
- term: IFN_MUL_OVERFLOW
  definition: An internal GCC pattern representing an unsigned multiplication overflow
    check, used by the optimizer.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b0a84b6100389c5b24658743252a7ff259ba0816
date: '2026-06-04'
is_stub: false
stub_reason: ''
---

GCC's tree optimization pass can now recognize and optimize overflow checks involving widened unsigned multiplications. The compiler canonicalizes patterns where a multiplication result is shifted and compared against the maximum value of the narrow type into a widened comparison form. This form is then further simplified to `IFN_MUL_OVERFLOW` when the target architecture supports direct unsigned multiply-overflow instructions, enabling more efficient code generation.
