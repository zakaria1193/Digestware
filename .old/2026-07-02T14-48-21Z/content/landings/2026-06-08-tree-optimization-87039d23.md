---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- bugfix
- vectorization
- types
commit_hash: 87039d23cb9ab43f74da905226e1fac9b4de10bc
source_type: github
author: Richard Biener
headline: Vectorization pattern for constant multiplication now correctly sets vector
  types.
tldr: A bug preventing correct vector type assignment for constant multiplication
  patterns in vectorization has been resolved.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch targets `vect_synth_mult_by_constant` in `tree-vect-patterns.cc`,
  resolving an issue where the vector type for a synthesized constant multiplication
  pattern, especially when an unsigned conversion was required, was not correctly
  updated. This oversight meant the pattern statement retained the signed result's
  vector type, confusing subsequent analyses, such as UB checks for reduction vectorization,
  and potentially leading to wrong code in general. The fix ensures the emitted sequence
  statements for the pattern are assigned the correct vector type, maintaining type
  consistency and co…
primer_general: Compilers try to make your code faster by using "vectorization," which
  allows a single instruction to operate on multiple pieces of data at once. This
  is especially useful for loops that perform the same operation many times. This
  commit fixes a bug in GCC's vectorization process related to how it handles multiplying
  integers by a constant value. The problem was that when the compiler tried to create
  a vectorized version of such a multiplication, and a conversion to an 'unsigned'
  integer type was needed, it sometimes assigned the wrong data type (a 'signed' vector
  type instead of an 'unsigned' one) to the vectorized instruction. This could lead
  to incorrect calculations or errors, particularly in specialized scenarios like
  reducing a vector to a single result. The fix ensures that the compiler assigns
  the correct data type, making vectorization more reliable and preventing potential
  errors in your programs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/87039d23cb9ab43f74da905226e1fac9b4de10bc
date: '2026-06-08'
is_stub: false
---

This commit addresses a bug in GCC's vectorization pass where, during the pattern recognition of integer multiplication by a constant, the appropriate unsigned vector type was not being assigned to the resulting pattern statement. This omission could lead to incorrect vector types, particularly affecting code dealing with undefined behavior checks for vector reduction and potentially causing wrong code in non-reduction cases. The fix ensures that the correct vector type is explicitly assigned, improving the accuracy of vectorized code.
