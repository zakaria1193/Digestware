---
project: binutils
subsystem: elf
patch_id: null
tags:
- binutils
- elf
- powerpc
- core-dump
discussion_id: fafaa1eb-a3ea-4108-9076-103b09b2c548@linux.ibm.com
source_type: public_inbox
title: 'Re: Ping Re: [PATCH v1] PowerPC: Add NT_PPC_DMR core file support'
headline: 'Ping Re: [PATCH v1] PowerPC: Add NT_PPC_DMR core file support'
tldr: Developer pings for a review of a patch adding support for NT_PPC_DMR core file
  notes on PowerPC.
proposer: Abhay Kandpal <abhay@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Abhay Kandpal <abhay@linux.ibm.com>
  role: proposer
  position: Pings for a review of a patch adding PowerPC NT_PPC_DMR core file support,
    indicating readiness for further changes.
  quote: null
primer_expert: This patch adds support for a new ELF note type, NT_PPC_DMR, to the
  binutils suite. This note type is specifically for PowerPC processors and will store
  Dense Math Registers (DMR) in core files. This is essential for post-mortem debugging
  of applications running on future PowerPC hardware that utilizes these registers.
primer_glossary: []
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/fafaa1eb-a3ea-4108-9076-103b09b2c548@linux.ibm.com
bugzilla_url: null
date: '2026-08-07'
is_stub: false
stub_reason: ''
---

Abhay Kandpal is following up on a patch that adds support for the NT_PPC_DMR note type in core files for PowerPC. This new note type will carry the contents of Dense Math Registers (DMR) for a future PowerPC processor. The patch includes modifications to BFD and readelf to handle this new information, with GDB support planned as a follow-up.
