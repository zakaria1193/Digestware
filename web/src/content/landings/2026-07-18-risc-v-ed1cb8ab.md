---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- lra
- bugfix
commit_hash: ed1cb8abdbf61d86c4b85b3b69d375fdefae2e21
source_type: github
author: Luke Zhuang
headline: Fix LRA crash related to TLSDESC clobber updates.
tldr: Resolved a crash in the RISC-V LRA caused by incorrect clobber updates for TLSDESC.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit targets a crash in the RISC-V Late Register Allocator (LRA),
  specifically linked to the handling of Thread-Local Storage Descriptor (TLSDESC)
  relocations. The crash occurs due to incorrect clobber information associated with
  vector register operations (`RVVM8QI`) when generating TLSDESC sequences. The fix
  replaces the use of `RVVM8QI` with `RVVM1QI` in the `(@tlsdesc<mode>)` pattern in
  `riscv.md`, which resolves the immediate crashing bug, and a new test case `tlsdesc_clobber_lra.c`
  is added for verification.
primer_glossary:
- term: LRA
  definition: Late Register Allocation, a phase in the compiler backend that performs
    final register allocation after most optimizations are complete.
- term: TLSDESC
  definition: Thread-Local Storage Descriptor. A mechanism used on some architectures
    to access thread-local variables, often involving a descriptor that holds the
    address of the variable.
- term: clobber
  definition: In compiler instruction scheduling and register allocation, a 'clobber'
    refers to a register or memory location that an instruction modifies and whose
    prior value is no longer needed.
- term: RVVM8QI
  definition: Likely refers to a specific RISC-V Vector Machine mode, possibly indicating
    8-element quantity/integer operations.
- term: RVVM1QI
  definition: Similar to RVVM8QI, likely a RISC-V Vector Machine mode, possibly for
    1-element quantity/integer operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ed1cb8abdbf61d86c4b85b3b69d375fdefae2e21
date: '2026-07-18'
is_stub: false
stub_reason: ''
---

A fuzz-testing initiative uncovered a crash in the RISC-V Late Register Allocation (LRA) phase, triggered by specific clobber updates associated with TLSDESC. This commit addresses the issue by replacing `RVVM8QI` with `RVVM1QI` in the relevant instruction definitions in the RISC-V machine description. A new test case is included to demonstrate the fix and prevent regressions.
