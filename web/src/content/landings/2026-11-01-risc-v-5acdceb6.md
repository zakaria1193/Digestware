---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- register allocation
- optimization
- bugfix
commit_hash: 5acdceb6e77753e54c3de1c7d3a73bf3d457ca85
source_type: github
author: Jeff Law
headline: Prevent pseudo register creation after pseudos are disallowed on RISC-V
tldr: Fixes a bug on RISC-V where pseudo registers were incorrectly created after
  they were disallowed.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `synthesize_add` function in the RISC-V backend was being called
  through a new path after the `can_create_pseudos_p` check had already returned false.
  This commit modifies `synthesize_add` to return false if it would require creating
  a new pseudo register when `!can_create_pseudos_p`. This prevents the scheduler
  from erroneously creating pseudos in contexts where they are disallowed, thus avoiding
  potential register allocation issues and regressions.
primer_glossary:
- term: pseudo register
  definition: A temporary, compiler-managed register used during intermediate stages
    of compilation. Pseudo registers are not actual hardware registers and are later
    mapped to physical registers or spilled to memory.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles. GCC supports various RISC-V configurations.
- term: synthesize_add
  definition: A function within GCC's backend that likely generates RTL (Register
    Transfer Language) for an 'add' operation, possibly involving optimizations like
    peephole transforms or pseudo-register creation.
- term: can_create_pseudos_p
  definition: A predicate function in GCC's compiler internals that checks whether
    the compiler is currently allowed to create new pseudo registers. This is often
    tied to specific optimization passes or compiler states.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5acdceb6e77753e54c3de1c7d3a73bf3d457ca85
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This commit corrects a bug in the RISC-V backend where pseudo registers were being created even after the compiler had determined that no new pseudo registers should be allowed. This occurred due to a new path calling `synthesize_add` without adequately checking the pseudo-creation constraint. The fix ensures that `synthesize_add` returns false when pseudo creation is forbidden, preventing incorrect register allocation and potential regressions.
