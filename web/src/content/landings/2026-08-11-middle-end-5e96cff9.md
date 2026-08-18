---
project: gcc
subsystem: middle-end
patch_id: null
tags:
- compiler
- optimization
- middle-end
commit_hash: 5e96cff93ecaa8bc4c8309241853f74ba638aaf8
source_type: github
author: Josef Melcr
headline: Unset stdarg when lowering assumptions.
tldr: GCC now correctly unsets the 'stdarg' flag when lowering function assumptions.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gimple-low.cc`, the `lower_assumption` function temporarily sets
  the `stdarg` flag on a function's declaration when building its body, as the argument
  count and types are not yet known. This commit ensures that after the argument list
  is constructed, the `stdarg` flag is unset from the function's `struct function`,
  aligning the internal representation with the resolved arguments.
primer_glossary:
- term: stdarg
  definition: A C/C++ convention for handling functions with a variable number of
    arguments (variadic functions), such as `printf`. The `stdarg` flag indicates
    that a function accepts such arguments.
- term: GIMPLE
  definition: GCC's Internal Machine-Element Optimizer. It is an intermediate representation
    used for performing optimizations within the compiler's middle-end.
- term: lowering
  definition: The process of transforming code from one intermediate representation
    to another, typically from a higher-level, more abstract form to a lower-level,
    more machine-oriented form.
- term: assumption
  definition: In the context of compiler optimizations, an assumption might refer
    to a condition or property that the compiler infers or is told about an input
    program, which can then be used to enable further optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5e96cff93ecaa8bc4c8309241853f74ba638aaf8
date: '2026-08-11'
is_stub: true
stub_reason: low_score
---

This patch corrects an issue in GCC's middle-end where the 'stdarg' flag remained set on a function's declaration even after its variable arguments were determined during the lowering of assumptions. This ensures the function's signature accurately reflects its argument list, preventing potential misinterpretations.
