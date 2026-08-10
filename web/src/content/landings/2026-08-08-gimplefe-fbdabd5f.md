---
project: gcc
subsystem: gimplefe
patch_id: null
tags:
- gimple
- frontend
- debugging
commit_hash: fbdabd5f9a27c80a19767918adaa1ee968cf4adf
source_type: github
author: Andrea Pinski
headline: 'gimplefe: Add support for REF_REVERSE_STORAGE_ORDER on mem'
tldr: Enables the GIMPLE frontend to set and display the reverse storage order flag
  for memory references.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Extends the GIMPLE frontend (`gimple-parser.cc`) to parse and set `REF_REVERSE_STORAGE_ORDER`
  on `MEM_REF` nodes, addressing difficulties encountered while debugging PRs 126729
  and 126570. It also updates `tree-pretty-print.cc` to dump this flag when present
  in GIMPLE output. This provides better visibility into memory access patterns involving
  reversed byte order, crucial for cross-endian compatibility and optimization.
primer_glossary:
- term: GIMPLE
  definition: Generic Intermediate Representation. A three-address intermediate representation
    used by GCC after the initial parsing and before lower-level RTL transformations.
    It is designed to be simpler and easier to optimize than RTL.
- term: gimplefe
  definition: The GIMPLE Frontend, responsible for processing C/C++ code and generating
    GIMPLE intermediate representation.
- term: MEM_REF
  definition: A GCC internal representation for a memory reference, indicating an
    access to a specific memory location.
- term: REF_REVERSE_STORAGE_ORDER
  definition: A flag indicating that the byte order within a multi-byte memory access
    is reversed relative to the target architecture's standard endianness. This is
    relevant for compatibility with systems of differing endianness.
discussion_id_link: github:gcc-mirror/gcc#126729
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fbdabd5f9a27c80a19767918adaa1ee968cf4adf
date: '2026-08-08'
is_stub: false
stub_reason: ''
---

This commit enhances the GIMPLE frontend to support the `REF_REVERSE_STORAGE_ORDER` flag for memory references. Previously, it was difficult to determine if this flag was set on a `MEM_REF`. The change allows the GIMPLE frontend to set this flag and also enables it to be dumped in GIMPLE mode, aiding in debugging and ensuring correct handling of memory access order.
