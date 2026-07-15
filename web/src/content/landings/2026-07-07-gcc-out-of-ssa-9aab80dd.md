---
project: gcc
subsystem: gcc/out-of-ssa
patch_id: null
tags:
- optimization
- out_of_ssa
- gcc
commit_hash: 9aab80ddc5b2fa0eef80008e718067ab45f42c50
source_type: github
author: Kyrylo Tkachov
headline: Out-of-SSA uses spill predicate for partition declarations
tldr: Fixes memory corruption from overlapping partitions in out-of-SSA form by using
  the correct spill predicate.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The out-of-ssa pass can create partitions of a VAR_DECL to represent
  non-overlapping live ranges. When these live ranges overlap, the partitions are
  not split. Existing code used BLKmode to approximate memory decisions for spilling
  these partitions, leading to MEM_EXPRs being created at offset zero for all spilled
  slots. This change modifies `remove_ssa_form` to call `split_overlapping_partition_decls`,
  which uses `use_register_for_decl` to determine if a partition should be spilled
  to memory. Overlapping partitions are split after TER, with the original decl retaining
  its metadata and new ar…
primer_glossary:
- term: out-of-SSA
  definition: A compiler optimization pass that converts Static Single Assignment
    (SSA) form back into a more traditional three-address code representation. This
    is often done to facilitate optimizations that are difficult to express in SSA
    form or to reduce pressure on the compiler's internal representation.
- term: partition decls
  definition: In the context of the out-of-SSA pass, these are temporary declarations
    created to represent portions of a variable's lifetime or memory location. When
    a variable's SSA versions have overlapping live ranges, partitions are used to
    manage the storage for these overlapping parts.
- term: spill predicate
  definition: A condition or function used by the compiler to determine whether a
    variable or temporary value needs to be stored (spilled) from a CPU register to
    memory. This is typically done when there are not enough registers available to
    hold all live values.
- term: TER
  definition: Tree Edge Reordering. A phase in GCC's optimization pipeline that reorders
    basic blocks. It aims to improve instruction locality and reduce control flow
    overhead. This commit splits overlapping partitions after TER.
- term: VAR_DECL
  definition: A GCC internal tree node representing a variable declaration. It stores
    information about a variable, such as its type, scope, and location.
- term: MEM_EXPR
  definition: A GCC internal tree expression representing a memory access. It can
    encapsulate addressing modes and offsets for reading from or writing to memory.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9aab80ddc5b2fa0eef80008e718067ab45f42c50
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

The out-of-SSA pass sometimes leaves multiple partitions sharing a base variable declaration when their live ranges overlap. This commit corrects how these overlapping partitions are spilled to memory. Previously, approximations were used, leading to distinct memory slots being combined and causing corruption. The change now uses the same spill predicate as used during expansion, ensuring that distinct memory slots are properly allocated and accessed, preventing data corruption.
