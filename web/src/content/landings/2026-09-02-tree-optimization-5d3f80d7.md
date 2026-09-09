---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- endianness
- tree
commit_hash: 5d3f80d7d9baf9207bb037a85ad78f3bcee4e41b
source_type: github
author: Richard Biener
headline: 'tree-optimization: Preserve reverse storage order during reference translation'
tldr: 'tree-optimization: Fixes incorrect bit numbering by punting reference translation
  through aggregate copies when storage order is reversed.'
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: When `vn_reference_lookup_3` translates a reference through an aggregate
  copy, it may reduce the lookup to the aggregate's RHS base plus offset, discarding
  original operands. If either the original access or the RHS access has `reverse_storage_order`,
  this reduction loses the flag. The fix makes `vn_reference_lookup_3` punt if all
  operands are consumed and reverse storage order is involved in either access, preserving
  the flag through the outermost operand.
primer_glossary:
- term: tree-optimization
  definition: A phase in GCC that manipulates the compiler's intermediate representation
    (the 'tree') to perform various optimizations.
- term: reverse storage order
  definition: A property of data types or components where the byte order is reversed
    compared to the natural endianness of the system, affecting how bits within bytes
    are interpreted.
- term: aggregate copy
  definition: A copy operation involving a structure or array, where multiple elements
    are copied together.
- term: VN (Value Numbering)
  definition: A compiler optimization technique that identifies and represents equivalent
    expressions with the same value number.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5d3f80d7d9baf9207bb037a85ad78f3bcee4e41b
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

This commit enhances the `vn_reference_lookup_3` function in the tree-optimization pass to correctly handle references within aggregate copies that have a reversed storage order. Previously, if the lookup reduced to a base plus offset and consumed all original operands, the reverse storage order information was lost. This led to incorrect interpretation of stored bytes with wrong bit numbering on assignment. The fix makes the function punt in such cases, preserving the correct storage order and preventing value misinterpretation.
