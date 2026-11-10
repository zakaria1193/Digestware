---
project: gcc
subsystem: gimple-ssa-sprintf
patch_id: null
tags:
- gimple
- cleanup
- dead code
commit_hash: d67fa1bc7b98b70ff7964729f8a5c7496fd9182a
source_type: github
author: Shiva S
headline: 'gimple-ssa-sprintf: Remove unused format_result increment operator'
tldr: An unused postfix increment operator for `format_result` is removed.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In the `gimple-ssa-sprintf` pass, the `format_result` class is used
  to manage format strings. This commit removes the `format_result::operator++(int)`
  method. This operator was a postfix increment and was never called. Furthermore,
  the class's copy constructor is private and undefined, meaning this operator would
  have resulted in a linking error if it had been used. Its removal cleans up the
  class definition.
primer_glossary:
- term: gimple-ssa-sprintf
  definition: A GCC optimization pass that specifically analyzes and potentially optimizes
    code involving `sprintf`-like functions using the Gimple Intermediate Representation
    and Static Single Assignment (SSA) form.
- term: postfix increment operator
  definition: An operator (e.g., `++`) that increments a variable after its current
    value has been used in an expression.
- term: copy constructor
  definition: A constructor used to create a new object as a copy of an existing object.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d67fa1bc7b98b70ff7964729f8a5c7496fd9182a
date: '2026-11-10'
is_stub: true
stub_reason: low_score
---

The postfix increment operator `operator++(int)` for the `format_result` class in `gimple-ssa-sprintf.cc` has been removed. This operator was never used and would have failed to link due to its private, undefined copy constructor.
