---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- risc-v
- assembly
- extensions
discussion_id: 12dc45996d624469e295ee64d18d6a65@linux.alibaba.com
source_type: public_inbox
title: (no subject)
headline: 'RISC-V: Add support for XXTVarith and XXTVcoder extensions'
tldr: Follow-up on a previous patch to add RISC-V XXTVarith and XXTVcoder extensions.
proposer: Bohan Lei <garthlei@linux.alibaba.com>
consensus: Under Review
outcome: under_review
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding support for vendor-specific extensions requires careful integration.
- Ensuring the patch is reviewed and merged.
exchanges:
- author: Bohan Lei <garthlei@linux.alibaba.com>
  role: proposer
  position: Follows up on a previous patch to request a review for RISC-V XXTVarith
    and XXTVcoder extensions.
  quote: Ping.  Could anyone help review the vendor-extension patch?
primer_expert: 'This is a follow-up message regarding a patch for the binutils project,
  specifically targeting the RISC-V architecture. The patch proposes adding support
  for two new extensions: XXTVarith and XXTVcoder. The author is seeking a review
  of this vendor-extension patch.'
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer (RISC) principles.
- term: XXTVarith
  definition: A proposed or existing extension for the RISC-V architecture, likely
    related to variable-length operations or arithmetic.
- term: XXTVcoder
  definition: A proposed or existing extension for the RISC-V architecture, possibly
    related to variable-length encoding or vector operations.
- term: vendor extension
  definition: Custom instructions or features added by a specific hardware vendor
    to a standard architecture, such as RISC-V.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/12dc45996d624469e295ee64d18d6a65@linux.alibaba.com
bugzilla_url: null
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

Bohan Lei is pinging the mailing list for a review of a previously submitted patch that adds support for the XXTVarith and XXTVcoder extensions to the RISC-V architecture in binutils. A link to the original patch on patchwork is provided.
