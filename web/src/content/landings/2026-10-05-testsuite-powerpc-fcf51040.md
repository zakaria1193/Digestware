---
project: gcc
subsystem: testsuite/powerpc
patch_id: null
tags:
- testsuite
- powerpc
- endianness
- AltiVec
commit_hash: fcf510403586ecd715c31b357993a16d106eade8
source_type: github
author: Jeevitha
headline: Fix vec-permute-ext test on Power10BE
tldr: Corrects byte indices in a PowerPC vec-permute test for big-endian compatibility.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `vec-permute-ext` test on Power10BE incorrectly selected bytes
  for vector double values due to byte indices matching LE representations. This patch
  modifies the permutation indices in `gcc.target/powerpc/vec-permute-ext-runnable.c`
  to ensure correct byte selection and achieve the expected -4.0 result.
primer_glossary:
- term: vec-permute-ext
  definition: An AltiVec intrinsic for permuting bytes within a vector register, potentially
    extending values.
- term: Power10BE
  definition: The Power10 processor architecture in Big-Endian mode.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fcf510403586ecd715c31b357993a16d106eade8
date: '2026-10-05'
is_stub: true
stub_reason: low_score
---

This commit corrects the `vec-permute-ext-runnable.c` test for Power10 big-endian targets. The original permutation indices, suitable for little-endian systems, produced incorrect results on big-endian systems by selecting different bytes within vector double values. The indices have been updated to ensure endian-correctness and the expected output of -4.0.
