---
project: gcc
subsystem: profile_probability
patch_id: null
tags:
- gcc
- compiler
- profile-guided optimization
- bug fix
commit_hash: 1123e52e811349dc880a5fc1abe4d5d427fcf70c
source_type: github
author: Artemiy Volkov
headline: Fixes for profile probability sqrt() method to return correct values and
  avoid infinite loops
tldr: Corrects `profile_probability::sqrt()` to return the computed value and prevents
  infinite loops due to precision errors.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit corrects two bugs in the `profile_probability::sqrt()`
  method within `profile-count.cc`. The first bug was that the method incorrectly
  returned `m_val` (the input value) instead of `val` (the computed result). The second
  fix addresses an infinite loop condition by changing the `while` loop's termination
  condition on line 511, preventing it from occurring when `min_range` becomes greater
  than `max_range` due to floating-point precision issues.
primer_glossary:
- term: profile_probability
  definition: A component within GCC that likely analyzes and models the probability
    of different execution paths or values based on profile data.
- term: sqrt()
  definition: The square root function, commonly used in mathematical and statistical
    calculations.
- term: m_val
  definition: Likely represents the 'member value' or initial input value within the
    `profile_probability` class's `sqrt()` method.
- term: val
  definition: Likely represents the computed result or the actual value produced by
    the `sqrt()` operation within the `profile_probability` class.
- term: min_range
  definition: The lower bound of a range of possible values.
- term: max_range
  definition: The upper bound of a range of possible values.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1123e52e811349dc880a5fc1abe4d5d427fcf70c
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

This commit addresses two issues in the `sqrt()` method of GCC's `profile_probability` class. Firstly, it corrects the method to return the calculated result (`val`) instead of the input value (`m_val`), ensuring accurate square root computations for probability distributions. Secondly, it modifies the loop condition to prevent potential infinite loops that could occur when precision errors cause `min_range` to exceed `max_range` during calculations.
