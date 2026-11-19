---
project: gcc
subsystem: gimple-ssa-warn-access
patch_id: null
tags:
- build
- compiler infrastructure
commit_hash: 78c5290e696d76fdbe7f3b006df9145d1ed7927c
source_type: github
author: Shiva S
headline: 'gimple-ssa-warn-access: Use gcc_unreachable in host code'
tldr: Compiler's host-compiled code now uses gcc_unreachable instead of a potentially
  unavailable __builtin_unreachable.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The file `gimple-ssa-warn-access.cc` is part of GCC's internal infrastructure
  and is compiled by the host C compiler, not the target compiler. Some host compilers
  may not define `__builtin_unreachable`. This commit replaces its use with `gcc_unreachable`,
  a portable macro defined within GCC's build system that handles the absence of the
  builtin. This ensures that the pass can be built and used even with host toolchains
  that lack this specific builtin, as demonstrated by a successful build on a non-glibc
  platform with an EDG-based host compiler.
primer_glossary:
- term: gimple-ssa-warn-access
  definition: A GCC compiler pass that analyzes code for potential memory access warnings
    using the Static Single Assignment (SSA) form of the Gimple intermediate representation.
- term: host compiler
  definition: The compiler used to build GCC itself. This is distinct from the target
    compiler, which GCC generates code for.
- term: gcc_unreachable
  definition: A macro defined within the GCC build system that serves as a portable
    way to indicate that a certain point in the code should never be reached. It is
    used in place of compiler-specific builtins like `__builtin_unreachable`.
- term: __builtin_unreachable
  definition: A GCC extension that informs the compiler that the current point in
    the code will never be reached. This allows for further optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/78c5290e696d76fdbe7f3b006df9145d1ed7927c
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

The `gimple-ssa-warn-access` pass, which is compiled by the host compiler, has been updated to use `gcc_unreachable` instead of `__builtin_unreachable`. This change ensures compatibility when the host compiler does not provide `__builtin_unreachable`, resolving build failures on non-standard host environments and aligning with GCC's internal error handling practices.
