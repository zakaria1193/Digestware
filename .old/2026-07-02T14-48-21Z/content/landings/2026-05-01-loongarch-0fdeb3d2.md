---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- assembler
- loongarch
- testsuite
- alignment
commit_hash: 0fdeb3d24aab6990e8846dcbd0dede0c70ddf111
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'LoongArch: Fix readelf test for instruction alignment.'
tldr: Adjusts a readelf test for LoongArch to correctly verify 4-byte alignment of
  machine instructions in both 32-bit and 64-bit objects.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch modifies the `insn_align_4.d` test in the LoongArch assembler
  testsuite. The original test's `readelf` check was too strict, causing failures
  on 32-bit objects. The fix loosens the regex to verify the presence of '.text' section
  with alignment of 4 bytes rather than matching the entire line.
primer_general: The GNU assembler (`gas`) translates assembly code into machine code.
  This commit fixes a test case for the LoongArch architecture that checks whether
  machine instructions are properly aligned in memory. Correct alignment is crucial
  for performance. The fix ensures that the test works correctly for both 32-bit and
  64-bit LoongArch programs, by relaxing the matching criteria in the test.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260501124928.617DE46A9CD7@sourceware.org
date: '2026-05-01'
---

A `readelf` test for LoongArch was failing on 32-bit objects because it was over-specifying the expected output. This commit modifies the test to be less specific, ensuring that it correctly verifies the 4-byte alignment of machine instructions for both loongarch32 and loongarch64.
