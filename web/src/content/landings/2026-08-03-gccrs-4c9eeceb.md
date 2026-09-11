---
project: gcc
subsystem: gccrs
patch_id: null
tags:
- gccrs
- rust
- linting
- unused variables
- compiler
commit_hash: 4c9eeceb42a98a55b6fa122e821f4bdef91e22d9
source_type: github
author: Aiman Najjar
headline: 'gccrs: Fix unused_assignment check logic'
tldr: Improves gccrs's unused assignment linting by tracking only the last assignment.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `UnusedChecker::visit` method in `rust-unused-checker.cc` has been
  updated to manage assignments more precisely. `UnusedContext::add_assign` now uses
  a new set to track assignments, and `remove_assign` and `is_variable_assigned` are
  adjusted to consider only the last assignment per variable. A new helper function,
  `is_assign_unused`, is introduced. This change ensures that the linter accurately
  identifies variables that are assigned a value but never read, particularly in cases
  of multiple assignments to the same variable.
primer_glossary:
- term: unused assignment
  definition: A situation in programming where a variable is assigned a value, but
    that value is never subsequently read or used before being overwritten or going
    out of scope. Compilers can often warn about this to help prevent bugs and dead
    code.
- term: linting
  definition: The process of analyzing source code to flag programming errors, stylistic
    errors, and suspicious constructs. Linters help improve code quality and prevent
    bugs.
- term: variable
  definition: A named storage location that can hold a value, which may change during
    program execution.
- term: assignment
  definition: The process of storing a value in a variable.
- term: UnusedChecker
  definition: A component within the gccrs compiler responsible for detecting unused
    variables, assignments, and other code constructs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4c9eeceb42a98a55b6fa122e821f4bdef91e22d9
date: '2026-08-03'
is_stub: false
stub_reason: ''
---

This patch refines gccrs's `unused_assignment` linting logic to correctly identify unused variables. It ensures that only the most recent assignment to a variable is tracked. If a variable is assigned a new value before the previous assignment has been used, the older assignment is now correctly flagged as potentially unused, preventing false positives. This addresses a bug where previous assignments might be overlooked.
