---
project: gcc
subsystem: gcc/middle-end
patch_id: null
tags:
- optimization
- compiler-internals
- bugfix
commit_hash: 4b99a9a276291e7b8d4d52b6a6da8e7016d8c588
source_type: github
author: Richard Biener
headline: RTL expansion ranger use is disabled at O0 optimization level
tldr: GCC now explicitly disables the RTL expansion ranger when compiling at -O0 to
  prevent unintended optimizations.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The RTL expansion ranger is a component within the GCC middle-end responsible
  for expanding certain RTL patterns into more primitive operations. In the context
  of `-O0` (no optimization), its activation could lead to unexpected code transformations
  that deviate from the intended behavior of a non-optimized compilation. The fix
  involves guarding the ranger's use within `cfgexpand.cc`'s `pass_expand::execute`
  method with an `optimize` check, ensuring it only runs when optimizations are explicitly
  enabled. This aligns with the long-standing principle that `-O0` should produce
  code as close as po…
primer_general: Compilers work in several stages, and one of the later stages involves
  converting an intermediate representation of your code into something called Register
  Transfer Language (RTL), which is very close to machine instructions. The 'RTL expansion
  ranger' is a part of this process that can rearrange or simplify these instructions
  to make them more efficient. When you compile your code with the `-O0` flag, you're
  telling the compiler not to perform any optimizations, usually because you want
  to debug the code and have it execute exactly as written. This change prevents the
  RTL expansion ranger from running when `-O0` is used, ensuring that no unintended
  optimizations occur that could make debugging more difficult or alter the program's
  behavior subtly.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4b99a9a276291e7b8d4d52b6a6da8e7016d8c588
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This commit disables the use of the RTL expansion ranger when GCC is compiling with the `-O0` optimization flag. The ranger, a component responsible for certain RTL (Register Transfer Language) expansions, was inadvertently active even without optimizations. Disabling it ensures that `-O0` strictly maintains the original program structure without introducing any unplanned optimizations or transformations.
