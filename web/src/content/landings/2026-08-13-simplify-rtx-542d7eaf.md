---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- optimization
- bugfix
- compiler-internals
- gcc
commit_hash: 542d7eaf767057fbd224d44dbc1772dea3e41891
source_type: github
author: Rohith Kapelli
headline: 'simplify-rtx: Widen memory attributes in "c ? a : a" fold'
tldr: Fixes a bug where folding conditional expressions incorrectly narrowed memory
  alias information, potentially leading to dead code elimination.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `simplify_ternary_operation` pass incorrectly folds `IF_THEN_ELSE(cond,
  a, a)` to `a` using `rtx_equal_p`, which bypasses memory attribute checks. This
  led to the loss of alias set information when `a` represented memory loads with
  different attributes. A specific test case involving `ce1` and subsequent dead code
  elimination exposed this, causing stale values to be returned. The fix modifies
  the fold to merge memory attributes using logic similar to `merge_memattrs`, ensuring
  only common attributes (like alias set 0, minimal alignment, and shared `MEM_EXPR`)
  are retained. Flags like `MEM…
primer_glossary:
- term: simplify-rtx
  definition: A GCC compiler pass that simplifies and optimizes Runtime Text Exchange
    (RTX) expressions, which represent the compiler's internal intermediate representation.
- term: RTX
  definition: Runtime Text Exchange is GCC's internal representation of code. It's
    a set of C data structures used to represent programs during compilation, allowing
    various optimization passes to operate on the code.
- term: fold
  definition: In compiler optimization, 'folding' refers to replacing an expression
    with a simpler, equivalent one. For example, folding a constant expression like
    '2 + 3' into '5'.
- term: memory attributes
  definition: Metadata associated with memory accesses that provides information about
    aliasing, trapping behavior, and read-only status. These attributes help the compiler
    make correct optimization decisions.
- term: alias set
  definition: A grouping of memory accesses that are known not to refer to the same
    memory location. Accesses within the same alias set might alias, while accesses
    in different sets are guaranteed not to.
- term: MEM_EXPR
  definition: An RTX expression type representing a memory reference, often used in
    optimizations where the specific memory location or its properties are important.
- term: dead code elimination
  definition: A compiler optimization that removes code that does not affect the program's
    output or behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/542d7eaf767057fbd224d44dbc1772dea3e41891
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

A bug in GCC's `simplify-rtx` pass allowed the folding of ternary operations like 'c ? a : a' to incorrectly narrow memory attributes. This happened because `rtx_equal_p` ignored memory attributes, leading to a single `MEM` reference being used even when the two conditional arms had incompatible alias sets. This could result in subsequent passes incorrectly removing seemingly dead store operations, leading to stale return values. The fix ensures the folded expression inherits only the memory attributes guaranteed by both operands, merging alias sets and other attributes appropriately.
