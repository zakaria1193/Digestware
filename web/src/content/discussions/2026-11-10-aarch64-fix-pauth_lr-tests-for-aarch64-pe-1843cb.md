---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- PE/COFF
- testing
discussion_id: 3272e5b4-6489-7d7a-d21a-838007947677@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: [PATCH] aarch64: Fix PAuth_LR tests for aarch64-pe'
headline: 'aarch64: Fix PAuth_LR tests for aarch64-pe'
tldr: Fixes aarch64-pe build failure by adjusting .balign to .org for section alignment.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Replaced a potentially problematic alignment directive with a more compatible padding
  method.
exchanges:
- author: Muhammad Kamran
  role: proposer
  position: Submitted a patch to fix aarch64-pe build failures related to section
    alignment.
  quote: 'It addresses the aarch64-pe failure reported by Alan [1], where the

    PAuth_LR tests used .balign 0x40000 and caused a non-representable

    2**18 .text section alignment for PE/COFF objects.


    The patch replaces that with .org-based padding and relaxes the expected

    disassembly to account for PE/COFF symbol spelling.'
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: maintainer
  position: Accepted and pushed the patch.
  quote: Thanks - I've pushed it for you.
primer_expert: This patch corrects a test case in the aarch64 PE/COFF target. The
  original test used a large `.balign` directive which is not well-supported by PE/COFF
  section alignment, causing a failure. The fix uses `.org` for padding and adjusts
  test expectations.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/3272e5b4-6489-7d7a-d21a-838007947677@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

A patch addresses a build failure in aarch64-pe targets. The issue stemmed from using .balign 0x40000, which resulted in a non-representable section alignment for PE/COFF objects. The fix replaces this with .org-based padding and relaxes disassembly expectations for PE/COFF symbol spelling.
