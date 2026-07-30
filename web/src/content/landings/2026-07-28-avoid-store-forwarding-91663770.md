---
project: gcc
subsystem: avoid-store-forwarding
patch_id: null
tags:
- optimization
- rtl
- bugfix
- ice
commit_hash: 91663770f795fd02688c1da004337a1e7c94e810
source_type: github
author: Konstantinos Eleftheriou
headline: Unshare load destination when re-applying store-forwarding extension.
tldr: Fixes a resource sharing issue in the store-forwarding avoidance pass that could
  lead to compiler internal errors.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `avoid-store-forwarding.cc`, when store forwarding is avoided but
  the load instruction is not eliminated (i.e., the store only partially covers the
  load), the extension wrapping the load's `MEM` is reapplied. This reapplication
  previously reused the `SET_DEST` of the load as the destination for the new move
  instruction. If this destination was a `SUBREG`, it resulted in `rtx` sharing between
  the load and the new move, violating `verify_rtx_sharing`. This commit resolves
  this by ensuring `copy_rtx` is used to create a distinct destination `rtx` for the
  move instruction, preventing the ICE r…
primer_glossary:
- term: avoid-store-forwarding
  definition: A compiler optimization or pass that prevents or manages the speculative
    forwarding of data from a store operation to a subsequent load operation within
    the same instruction stream. This is often done to preserve program correctness
    in specific scenarios, such as when aliasing is complex or when memory ordering
    needs to be strictly controlled.
- term: store forwarding
  definition: An optimization where the result of a store operation is immediately
    made available to subsequent load operations, potentially bypassing the memory
    subsystem for performance gains.
- term: ICE
  definition: 'Internal Compiler Error. A serious error occurs within the compiler
    itself, preventing it from completing the compilation process. These typically
    indicate bugs in the compiler. '
- term: rtx
  definition: Register Transfer. The fundamental data structure in GCC's RTL intermediate
    representation, representing registers, memory locations, constants, and operations.
- term: SUBREG
  definition: A machine-dependent RTL construct representing a portion of a larger
    register. For example, using the lower 32 bits of a 64-bit register.
- term: verify_rtx_sharing
  definition: An internal GCC function or assertion that checks if the same RTL object
    is being shared by multiple instruction objects, which can lead to incorrect code
    generation if not handled properly.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/91663770f795fd02688c1da004337a1e7c94e810
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

The `avoid-store-forwarding` pass in GCC could incorrectly share a destination register (`rtx`) between two instructions when a load was preserved after a partial store-forwarding avoidance. This was particularly problematic when the destination was a `SUBREG`, leading to an `verify_rtx_sharing` ICE. The fix ensures the destination is unshared using `copy_rtx` when rebuilding the affected move instruction, resolving the ICE and passing new test cases.
