---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- vectorization
- bitfields
- bugfix
commit_hash: cfddb495c2f4cfc556588ea21ec322c885661b02
source_type: github
author: Richard Biener
headline: Fix bitfield vectorization with SSO for PR128414
tldr: Corrects bitfield vectorization by preventing the use of components with reverse
  storage order, fixing a miscompilation bug.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit fixes PR tree-optimization/128414 by adding a check in
  `bitfields_to_lower_p` within `tree-if-conv.cc`. The check rejects components that
  have a `reverse_storage_order` set. This prevents incorrect vectorization of bitfields
  when they are laid out in memory in a way that the vectorizer's lowering pass does
  not handle properly, particularly when interacting with Short-Stack Optimization
  (SSO) related transformations that might expose such component orders.
primer_glossary:
- term: bitfield
  definition: A field within a structure or union that occupies a specified number
    of bits, which may be less than the number of bits in a byte. Useful for packing
    data tightly.
- term: vectorization
  definition: A compiler optimization technique that transforms loops to execute operations
    on multiple data elements in parallel using SIMD instructions.
- term: SSO
  definition: Short-Stack Optimization. A compiler optimization that might involve
    using stack space more efficiently, potentially affecting how data is laid out
    or accessed.
- term: miscompilation
  definition: A situation where a compiler produces incorrect output code for a given
    source program, leading to wrong program behavior at runtime.
- term: storage order
  definition: The order in which bytes or bits of a data element are stored in memory.
    This can be affected by endianness and specific data structure layouts.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cfddb495c2f4cfc556588ea21ec322c885661b02
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This commit resolves a miscompilation issue (PR tree-optimization/128414) related to vectorizing bitfields when Short-Stack Optimization (SSO) is involved. The fix prevents the lowering of bitfields that use components with a reverse storage order. A new test case is added to verify the correction.
