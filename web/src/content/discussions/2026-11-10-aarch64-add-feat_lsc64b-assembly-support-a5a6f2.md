---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembly
- disassembler
- architecture
discussion_id: 7196fcee-4530-0b45-2dcb-826d081ee508@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: [PATCH] aarch64: Add FEAT_LSC64B assembly support'
headline: 'aarch64: Add FEAT_LSC64B assembly support'
tldr: Adds assembly and disassembly support for AArch64's FEAT_LSC64B extension and
  its associated instructions.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Muhammad Kamran
  role: proposer
  position: Submitted a patch to add support for the AArch64 FEAT_LSC64B extension.
  quote: "Add the +lsc64b architecture extension and the LSC64B instructions:\n\n\t\
    - LDA64B\n\t- STL64B\n\t- STL64BV\n\t- STL64BV0\n\nFEAT_LSC64B implies FEAT_LSCP,\
    \ while the LSC64B instructions also\nrequire FEAT_LS64.  Model this by making\
    \ +lsc64b depend on +lscp and\nrequiring both LSC64B and LS64 in the opcode feature\
    \ set.\n\nReuse the existing LS64 Rt operand as FEAT_LSC64B shares the same operand\n\
    constraints as FEA…"
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: maintainer
  position: Acknowledged the patch and implied it would be processed.
  quote: null
primer_expert: This patch adds support for the FEAT_LSC64B extension, which includes
  new load/store exclusive instructions for AArch64. It correctly models feature dependencies
  and adds tests for assembler and disassembler behavior.
primer_glossary:
- term: FEAT_LSC64B
  definition: An AArch64 architecture feature extension providing new cache control
    instructions.
- term: FEAT_LSCP
  definition: An AArch64 architecture feature extension related to Load-Store Cache
    operations.
- term: FEAT_LS64
  definition: An AArch64 architecture feature extension for 64-byte Load-Store operations.
- term: Rt register
  definition: A general-purpose register in the ARM architecture, often used for data
    transfer.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/7196fcee-4530-0b45-2dcb-826d081ee508@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-10'
is_stub: false
stub_reason: ''
---

This patch introduces support for the FEAT_LSC64B architecture extension in the AArch64 assembler and disassembler. It adds definitions for new instructions like LDA64B and STL64B, models the extension's dependencies on FEAT_LSCP and FEAT_LS64, and includes comprehensive tests for the new functionality.
