---
project: gcc
subsystem: rtl-optimization
patch_id: null
tags:
- optimization
- rtl
- bugfix
commit_hash: cdb8a10e1a826670ad5555cfb7cd973bf41cfefe
source_type: github
author: Jakub Jelinek
headline: Fixes incorrect simplification of unsigned multiplication by one.
tldr: Corrects a bug in GCC's RTL optimization pass that misapplied a simplification
  for unsigned multiplication by one.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify_binary_operation_1` function in `simplify-rtx.cc` incorrectly
  set `side_effects_p` to true for `UMUL_HIGHPART` when the second operand was `x
  h* 1`. This commit corrects the `side_effects_p` argument for this specific case
  to `0` (false), resolving PR128119. A new test case `gcc.target/i386/pr128119.c`
  has been added.
primer_glossary:
- term: RTL
  definition: Register Transfer Language, an intermediate representation used internally
    by GCC. It describes operations on virtual registers and is optimized before code
    generation.
- term: side_effects_p
  definition: A predicate used in GCC's RTL optimizers to indicate whether an operation
    might have side effects (e.g., modifying memory, raising exceptions). This helps
    the optimizer determine if an operation can be safely reordered or removed.
- term: UMUL_HIGHPART
  definition: An RTL operation representing the higher-order bits of an unsigned multiplication
    result. Typically used in conjunction with a lower-order part to represent the
    full product of two large unsigned integers.
- term: PR128119
  definition: Problem Report 128119, a bug filed against the GCC compiler. This identifier
    links the commit to a specific issue tracked in the GCC bug tracking system.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cdb8a10e1a826670ad5555cfb7cd973bf41cfefe
date: '2026-11-21'
is_stub: false
stub_reason: ''
---

A bug in GCC's RTL optimization pass (specifically in `simplify_binary_operation_1`) has been fixed. The `side_effects_p` flag was incorrectly set for unsigned multiplication by one, leading to erroneous code generation. This change corrects the flag to ensure proper simplification and adds a test case to prevent regressions.
