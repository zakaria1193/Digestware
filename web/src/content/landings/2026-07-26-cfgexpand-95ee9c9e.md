---
project: gcc
subsystem: cfgexpand
patch_id: null
tags:
- optimization
- middle-end
- verification
- memory-aliasing
commit_hash: 95ee9c9e74eb93414bbcd76b02e1fcbec383f2ce
source_type: github
author: Kyrylo Tkachov
headline: 'cfgexpand: Verify partitions do not share MEM_EXPR'
tldr: cfgexpand now verifies that partitions do not share a MEM_EXPR to prevent miscompilations.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'Introduces a post-partitioning check in cfgexpand to enforce an invariant:
  distinct stack slots should not share a `MEM_EXPR`. Previously, `MEM_EXPR`-based
  disambiguation in passes like load/store pair fusion could incorrectly fuse accesses
  to separate stack slots if they shared a common `MEM_EXPR` base and offset, leading
  to miscompiles. This new check, enabled by `flag_checking`, runs after RTL is assigned
  to partitions, turning potential miscompiles into ICEs.'
primer_glossary:
- term: cfgexpand
  definition: A GCC pass responsible for expanding control flow graphs and allocating
    RTL for basic blocks.
- term: partition
  definition: In the context of out-of-SSA, a partition represents a set of memory
    locations that are treated as a single unit for analysis and transformation.
- term: MEM_EXPR
  definition: A GCC internal representation for memory references, typically involving
    a base address and an offset.
- term: load/store pair-fusion pass
  definition: An optimization pass that fuses adjacent load and store operations that
    access memory at similar locations for improved performance.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used within
    GCC to describe programs before they are lowered to machine code.
- term: ICE
  definition: Internal Compiler Error, a situation where the compiler encounters an
    unrecoverable error during its execution, typically indicating a bug within the
    compiler itself.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/95ee9c9e74eb93414bbcd76b02e1fcbec383f2ce
date: '2026-07-26'
is_stub: false
stub_reason: ''
---

A new verification function, `verify_partition_mem_exprs`, has been added to `cfgexpand.cc`. It checks that distinct stack slots carrying a `MEM_EXPR` are not incorrectly identified as a single object by the load/store pair-fusion pass. This prevents miscompilations that occurred when accesses to different memory locations were fused due to shared `MEM_EXPR` bases and offsets. The check is performed per function when `flag_checking` is enabled.
