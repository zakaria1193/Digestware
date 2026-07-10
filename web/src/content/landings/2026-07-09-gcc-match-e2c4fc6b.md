---
project: gcc
subsystem: gcc/match
patch_id: null
tags:
- gcc
- optimization
- pattern matching
commit_hash: e2c4fc6b1cff0d32dd7e6e4049d87c5193fea6dc
source_type: github
author: Eikansh Gupta
headline: Simplify copysign pattern for constants
tldr: GCC match.pd simplifies copysign with constant arguments to use a simplified
  form.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit introduces a new pattern in `match.pd` to optimize calls
  to `copysign` where the second argument is a constant. The pattern `(trunc)copysign
  ((extend)x, CST)` is recognized, and due to `copysign`'s behavior where only the
  sign of the second argument matters, it's simplified to `copysign (x, -1.0/1.0)`
  or `copysign (x, 1.0)` based on `CST`'s sign. This likely targets tree-SSA or similar
  middle-end optimizations and is guarded by PR112472.
primer_glossary:
- term: match.pd
  definition: A file containing pattern definitions for GCC's pattern matching system,
    used for tree transformations and optimizations. It describes how to recognize
    and rewrite specific code structures.
- term: copysign
  definition: A function that returns a floating-point value with the magnitude of
    the first argument and the sign of the second argument.
- term: trunc
  definition: A cast or operation that truncates a value, typically a floating-point
    number, to a smaller type or representation.
- term: extend
  definition: A cast or operation that extends a value, typically an integer or floating-point
    number, to a larger type or representation.
- term: CST
  definition: Abbreviation for 'constant' in the context of GCC's internal representation.
    It refers to a constant value used in patterns.
- term: tree-ssa
  definition: Static Single Assignment form. An intermediate representation used in
    optimizing compilers like GCC, where each variable is assigned exactly once. It
    simplifies many analysis and transformation passes.
- term: PR112472
  definition: Problem Report number 112472. This indicates a bug or issue that has
    been reported and is being tracked in the GCC bug tracking system.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:match: simplify `(trunc)copysign ((extend)x, cst)` to `copysign (x,
  -1..0)` [pr112472]'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e2c4fc6b1cff0d32dd7e6e4049d87c5193fea6dc
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

GCC's pattern matching (`match.pd`) is updated to simplify `copysign` operations where one argument is a constant. The pattern `(trunc)copysign ((extend)x, CST)` can now be reduced to `copysign (x, -1.0/1.0)`, depending on the sign of the constant. This change is accompanied by a new test case for validation.
