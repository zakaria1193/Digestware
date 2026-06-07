---
project: gcc
subsystem: gcc/optabs
patch_id: null
tags:
- optimization
- code generation
- bugfix
commit_hash: 0e4fe83c0679b656123832140964dc1ecef77d1c
source_type: github
author: Richard Sandiford
headline: Correct can_open_code_p handling of abs and neg operations
tldr: GCC's `can_open_code_p` now correctly identifies whether absolute value and
  negation operations can be generated as open code, resolving an inconsistency in
  ho…
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In GCC, `optabs-query.cc` contains functions like `can_open_code_p`
  and `can_implement_p`, which are crucial for code generation decisions. `can_open_code_p`
  determines if an operation can be inlined as direct instructions, avoiding library
  calls. This change addresses a logical flaw where `can_open_code_p` was inadvertently
  using `can_implement_p` to check for `abs` and `neg` operations, leading to an over-optimistic
  assessment. Although this specific fix has limited practical impact due to `AND`
  and `XOR` lacking libgcc2 functions, the correction aligns `can_open_code_p` with
  its intended s…
primer_general: When a compiler like GCC translates your C or C++ code into machine
  instructions, it has to decide how to implement certain operations. Sometimes, it
  can generate direct machine instructions (called "open code") for an operation,
  like adding two numbers. Other times, it might need to call a helper function from
  a runtime library (like `libgcc2`) to perform a more complex task. The `can_open_code_p`
  function helps the compiler decide if a particular operation can be turned directly
  into machine code. This commit fixes a subtle bug where `can_open_code_p` was sometimes
  misinterpreting whether the `abs` (absolute value) and `neg` (negation) operations
  could be represented as open code. Although this particular bug had little practical
  effect, fixing it clarifies the compiler's internal logic, ensuring it makes the
  correct decisions about generating efficient code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0e4fe83c0679b656123832140964dc1ecef77d1c
date: '2026-06-06'
is_stub: false
---

The `can_open_code_p` function in GCC, which determines if an operation can be implemented directly by the compiler without relying on a library call, previously used `can_implement_p` for `abs` and `neg` operations. This was semantically incorrect because `can_implement_p` checks for *any* implementation, including library functions, rather than strictly open code. This commit updates `optabs-query.cc` to ensure `can_open_code_p` consistently uses itself when querying for `AND` and `XOR`, matching the intended behavior for open-coded operations.
