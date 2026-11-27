---
project: gcc
subsystem: bitintlower
patch_id: null
tags:
- bitint
- compiler
- optimization
- dead code
commit_hash: 9da087da59f1014a58c8fd57cf7f9c2ec3f9265e
source_type: github
author: Jakub Jelinek
headline: 'bitintlower: Remove stmts with zero lhs uses instead of trying to expand
  them [PR128994]'
tldr: Improves bitint lowering by removing dead statements instead of processing them,
  fixing a coalescing confusion issue.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gimple_lower_bitint` pass previously attempted to lower statements
  like rotate, minmax, or abs even if their results were unused (zero lhs uses). This
  can occur after certain transformations or if dead code elimination passes are disabled.
  Such dead statements could confuse the bitint coalescing logic. This patch modifies
  the pass to remove these dead statements directly, improving code generation and
  fixing issues related to coalescing. It also adds a new test case (`bitint-152.c`)
  to verify this behavior.
primer_glossary:
- term: bitintlower
  definition: The compiler pass responsible for lowering arbitrary-precision integers
    (`_BitInt`) into machine-representable operations.
- term: zero lhs uses
  definition: Refers to statements where the result (left-hand side) is not subsequently
    used by any other part of the code, effectively making the statement dead code.
- term: coalescing
  definition: A compiler optimization technique that merges similar or redundant operations
    to simplify code or improve efficiency. In this context, it refers to the process
    of combining bitint operations.
- term: dead statements
  definition: Code constructs whose results are never used and therefore have no effect
    on the program's outcome.
- term: SSA_NAME
  definition: Static Single Assignment form name. In SSA form, each variable has only
    one assignment, and each assignment to a variable creates a new version of that
    variable, distinguished by a version number.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9da087da59f1014a58c8fd57cf7f9c2ec3f9265e
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This commit modifies the `gimple_lower_bitint` pass to remove statements with no uses on their left-hand side (dead statements) rather than attempting to lower them. This change addresses an issue where the bitint coalescing mechanism was confused by these dead statements, leading to incorrect code generation. By removing them upfront, the compiler generates better code and avoids the confusion, also introducing a new test case to cover this scenario.
