---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- assembler
- gas
- loongarch
- test case
discussion_id: afSgc4Rp5QmZdQBD@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: LoongArch: Enforce 4-byte align for machine instructions'
headline: 'LoongArch: Fix test for instruction alignment'
tldr: Fixes a test case for LoongArch instruction alignment that was over-specified,
  causing failures on 32-bit objects.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Fixes a broken test case, ensuring proper instruction alignment is enforced.
- The looser regex may be less precise, but still confirms the essential alignment
  property.
exchanges: []
primer_expert: This patch modifies a gas test case for LoongArch. The test checks
  that machine instructions are 4-byte aligned. The original test used `readelf -S`,
  which produces different output for 32-bit vs 64-bit objects.  The fix uses `readelf
  -W -S` and a less specific regex to accommodate both.
primer_general: This patch fixes a test case for the LoongArch assembler. The test
  ensures that instructions are properly aligned in memory (every instruction starts
  at an address that is a multiple of 4). The original test failed because it was
  too strict and didn't account for differences in how 32-bit and 64-bit programs
  are formatted. The fix makes the test more general so that it works correctly for
  both 32-bit and 64-bit programs.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afSgc4Rp5QmZdQBD@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-01'
---

Alan Modra corrects a test case (`insn_align_4.d`) for LoongArch instruction alignment. The original test was too specific and failed on 32-bit objects due to differences in readelf output.  The patch relaxes the test to match the `.text` section alignment of 4 bytes without specifying other details.
