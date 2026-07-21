---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- pattern matching
- backend
commit_hash: 58c8c3e3bd04e59fc2de82708c5e12e7b5db4f43
source_type: github
author: Kael Andrew Alonzo Franco
headline: 'match: Optimize neeq pattern and fix typo in matcher'
tldr: Simplifies a pattern for the 'ne eq' comparison in the GCC matcher and corrects
  a typo.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `match.pd` file contains patterns used by GCC's backend to recognize
  and optimize specific sequences of operations. This change targets the `ne eq` (not
  equal, equal) comparison, which typically reduces to a constant comparison. By combining
  two existing patterns into one, the matcher becomes more concise. The typo fix in
  `zero_one_valued_p` ensures the correct operand is evaluated for this predicate.
  These changes simplify the backend's RTX matching logic.
primer_glossary:
- term: pattern matching
  definition: A technique used by compilers to recognize specific structures or sequences
    in the intermediate representation (IR) that can be replaced by more efficient
    code or simplified further.
- term: RTX
  definition: Representation of intermediate code in GCC, used by the backend to describe
    operations and data. RTX stands for 'RePresentation of code EXpression'.
- term: ne eq
  definition: A logical comparison combining 'not equal' and 'equal'. In many contexts,
    this can be simplified or optimized.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/58c8c3e3bd04e59fc2de82708c5e12e7b5db4f43
date: '2026-07-20'
is_stub: false
stub_reason: ''
---

This commit refactors the GCC matcher by combining two patterns for the `ne eq` (not equal, equal) condition into a single, more efficient pattern. Additionally, it corrects a typo in the `zero_one_valued_p` check, changing 'C' back to 'X' to ensure the pattern correctly identifies the intended operand. This optimization aims to simplify the pattern matching logic and improve the backend's efficiency in handling specific comparison combinations.
