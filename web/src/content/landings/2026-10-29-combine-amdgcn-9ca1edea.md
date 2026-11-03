---
project: gcc
subsystem: combine, amdgcn
patch_id: null
tags:
- amdgcn
- combine
- optimization
- vector
commit_hash: 9ca1edea42f626844222ac4befa1e97675514b6c
source_type: github
author: Andrew Stubbs
headline: 'combine, amdgcn: Fix ICE truncating wide vectors; allow packed accesses
  [PR122583]'
tldr: Fixes an ICE in the combine pass related to truncating wide vectors and allows
  packed accesses on GCN.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCN backend previously disallowed misaligned vector accesses due
  to an ICE in the `combine` pass when dealing with packed structs. The ICE occurred
  in `force_to_mode`'s call to `gen_lowpart_or_truncate` when truncating a wide vector
  (`V4DI`) to a narrow integer mode (`SI`). GCN lacks integer modes wider than `TImode`,
  causing `int_mode_for_mode` to fail. This patch modifies `gen_lowpart_or_truncate`
  to return `(clobber (const_int 0))` in such cases, allowing the combination to fail
  cleanly and removing the workaround that hindered packed accesses.
primer_glossary:
- term: ICE
  definition: Internal Compiler Error, a condition where the compiler encounters an
    unexpected internal state and terminates.
- term: combine pass
  definition: A compiler optimization pass that combines sequences of RTL (Register
    Transfer Language) operations into more efficient forms.
- term: amdgcn
  definition: The GCC backend for AMD's Graphics Core Next (GCN) architecture, used
    for GPGPU computation.
- term: subreg
  definition: A subregister, which refers to a part of a larger register. In this
    context, it relates to accessing parts of vector registers.
- term: packed structs
  definition: Struct data types where members are laid out contiguously in memory
    with no padding, potentially leading to misaligned data.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC.
- term: gen_lowpart_or_truncate
  definition: An RTL function used to truncate or extract the lower part of an operand.
- term: V4DI
  definition: A vector data type containing 4 doubleword (64-bit) elements.
- term: SImode
  definition: GCC's internal mode for a single integer (typically 32-bit).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9ca1edea42f626844222ac4befa1e97675514b6c
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This commit resolves an ICE in the combine pass on the AMD GCN backend that occurred when truncating wide vectors. The issue stemmed from assumptions about vector register subdivision. By fixing `gen_lowpart_or_truncate` to handle cases where no suitable integer mode exists, the ICE is avoided. This also allows GCN to correctly handle misaligned vector accesses, resolving issues like PR122583.
