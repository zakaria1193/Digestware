---
project: gcc
subsystem: gcc/config/gcn
patch_id: null
tags:
- gcn
- assembler
- llvm-mc
- build
commit_hash: 3dfe871a2cdc7db2645fcdf21a2ff0c081e051af
source_type: github
author: Thomas Schwinge
headline: 'GCC: Adjust for GCN assembler ''llvm-mc'' after removing HAVE_GNU_AS'
tldr: GCC now correctly uses LLVM's 'llvm-mc' assembler for GCN targets, fixing regressions
  caused by the removal of the HAVE_GNU_AS check.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Following the removal of `HAVE_GNU_AS`, the GCN target configuration,
  which relies on `llvm-mc` as its assembler (`gas=no`), was broken. The generic `ASM_V_SPEC`
  in `gcc/specs` was applied, causing GCC's verbose driver output (`-v`) to be passed
  to `llvm-mc`, which resulted in assembler errors. This patch defines a specific
  `ASM_V_SPEC` for the `gcn` target in `gcc/config/gcn/gcn.h` to correctly handle
  assembler options for `llvm-mc`, preventing the misapplication of `-v` and restoring
  functionality for GCN builds.
primer_general: GCC is a compiler that translates source code into machine code. It
  uses an assembler to convert assembly language into object files. This commit addresses
  an issue specific to compiling code for Graphics Core Next (GCN) hardware. GCC recently
  removed a check that specifically identified the GNU assembler (`as`). For GCN,
  GCC uses a different assembler from the LLVM project ('llvm-mc'). After the check
  was removed, GCC incorrectly passed options meant for the GNU assembler (like verbose
  output flags) to 'llvm-mc', causing build failures. This fix ensures that GCC uses
  the correct assembler options for 'llvm-mc' when building for GCN, resolving the
  compatibility problem.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3dfe871a2cdc7db2645fcdf21a2ff0c081e051af
date: '2026-05-18'
is_stub: false
stub_reason: ''
---

This commit corrects an issue where GCC's GCN backend, which uses LLVM's 'llvm-mc' as its assembler, regressed after the removal of the `HAVE_GNU_AS` configuration check. The old check implicitly handled the distinction between GNU `as` and other assemblers. Without it, GCC's default `ASM_V_SPEC` was applied, causing the `-v` option (used in verbose mode) to be passed to `llvm-mc`, which it does not support. The fix defines `ASM_V_SPEC` specifically for the GCN target to prevent this.
