---
project: gcc
subsystem: internal-fn
patch_id: null
tags:
- internal-fn
- compiler
- validation
commit_hash: dc661da3a8b9f524fb8acf99006835e368a0c7c8
source_type: github
author: Kyrylo Tkachov
headline: 'internal-fn: Record argument counts for direct internal functions'
tldr: Enables validation of argument counts for direct internal functions.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `direct_internal_fn_info` structure in `internal-fn.h` is extended
  to include `nargs_min` and `nargs_max` fields. These are populated in the `direct_internal_fn_info`
  initializers for various internal functions. A new helper function `direct_internal_fn_nargs_ok_p`
  is introduced to check these counts. The `vectorizable` field is resized to accommodate
  these new counts. This change enables verification of the number of arguments passed
  to direct internal functions, catching errors related to argument counts which were
  previously only detected by expanders.
primer_glossary:
- term: Direct Internal Function
  definition: A type of internal function in GCC that has a direct mapping to a specific
    operation or intrinsic, often with a fixed set of arguments.
- term: Expander
  definition: A piece of code within the compiler that translates an intermediate
    representation (like GIMPLE) into lower-level instructions or optimized forms.
- term: Vectorizer
  definition: A compiler pass that attempts to transform scalar code into vector (SIMD)
    code to improve performance on multi-core processors.
- term: GIMPLE
  definition: GCC's internal three-assignment representation, an intermediate language
    used for optimization.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dc661da3a8b9f524fb8acf99006835e368a0c7c8
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch enhances the information stored for direct internal functions by recording the minimum and maximum number of expected arguments. This allows for more robust validation of internal function calls, preventing errors where expanders expect a certain number of arguments but receive a different count. New `TYPE`s are introduced for variations like masked loads/stores to correctly associate argument counts. This change also asserts that calls have a valid number of arguments.
