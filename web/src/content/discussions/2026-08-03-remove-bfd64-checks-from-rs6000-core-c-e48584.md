---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- powerpc
- rs6000
- aix
- patch-testing
discussion_id: LV8PR15MB64889B70540DD638F812F9FED6D52@LV8PR15MB6488.namprd15.prod.outlook.com
source_type: public_inbox
title: 'RE: Remove BFD64 checks from rs6000-core.c'
headline: Remove BFD64 checks from rs6000-core.c
tldr: Aditya Kamath confirms Alan Modra's fix works and offers further assistance
  for PowerPC AIX.
proposer: Aditya Kamath <Aditya.Kamath1@ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Aditya Kamath <Aditya.Kamath1@ibm.com>
  role: contributor
  position: Confirms that Alan Modra's fix works and offers further collaboration
    on PowerPC AIX.
  quote: So your fix works.
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Acknowledges confirmation of the fix and states that two patches have
    been pushed.
  quote: 'Thanks for testing it for me.  I made another small fix and pushed

    both patches.'
primer_expert: This is a brief follow-up on a patch submitted by Alan Modra to the
  GNU Binutils project, specifically concerning the rs6000 (PowerPC) backend. The
  patch aimed to remove redundant BFD64 checks from `rs6000-core.c`. Aditya Kamath,
  presumably involved with PowerPC development, tested the patch and confirmed its
  correctness. This suggests the patch is likely to be merged or has already been
  merged.
primer_glossary:
- term: rs6000
  definition: The codename for IBM's 32-bit PowerPC processor architecture, commonly
    associated with the AIX operating system. Binutils support for rs6000 covers its
    specific instruction set and object file formats.
- term: BFD64
  definition: Refers to the 64-bit variant of the Binary File Descriptor library used
    by GNU Binutils. Object file formats like ELF have 32-bit and 64-bit versions,
    and BFD provides a way to handle them.
- term: PowerPC
  definition: A RISC instruction set architecture developed by Apple, IBM, and Motorola.
    It has been used in various computing platforms, including older Macs, servers,
    and embedded systems.
- term: AIX
  definition: Advanced Interactive eXecutive, IBM's proprietary Unix operating system.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/LV8PR15MB64889B70540DD638F812F9FED6D52@LV8PR15MB6488.namprd15.prod.outlook.com
bugzilla_url: null
date: '2026-08-03'
is_stub: false
stub_reason: ''
---

Aditya Kamath confirms that Alan Modra's previously submitted fix for removing BFD64 checks from rs6000-core.c functions correctly. Kamath offers his availability for collaboration on PowerPC AIX related matters. This exchange appears to be a follow-up on a patch submission where testing and confirmation were requested.
