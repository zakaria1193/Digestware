---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- extension
- binutils
- assembler
- bfd
discussion_id: CA+yXCZA45rLKW9CXmod+aLUmvYrgUkj_sV13i1Sj=TDj3bxaBQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add Svukte 1.0 extension support'
headline: 'RISC-V: Add Svukte 1.0 extension support'
tldr: Binutils now supports the RISC-V Svukte 1.0 extension for address-independent
  fault latency.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds support for a new RISC-V extension, increasing compatibility with evolving
  RISC-V standards.
- Restricts the extension to RV64, as per its requirements, ensuring correct usage.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: Proposes adding support for the RISC-V Svukte 1.0 extension, detailing
    its implications and requirements.
  quote: 'Add the Svukte extension for address-independent fault latency [1].

    Register version 1.0, imply Zicsr and reject RV32, since the extension

    requires Sv39.


    Test the RV64 architecture attribute, RV32 rejection and -march help.'
- author: Kito Cheng <kito.cheng@gmail.com>
  role: maintainer
  position: Merged the patch, indicating successful integration.
  quote: pushed :)
primer_expert: This change modifies binutils' BFD and GAS components to recognize
  and correctly process the RISC-V Svukte extension. Svukte, related to virtual memory
  and fault handling, requires Sv39 and is thus restricted to RV64. The changes involve
  updating internal tables and adding specific checks for RV32.
primer_glossary:
- term: Svukte
  definition: A RISC-V extension related to address-independent fault latency.
- term: Zicsr
  definition: A RISC-V extension that provides access to Control and Status Registers
    (CSRs).
- term: RV32
  definition: The 32-bit version of the RISC-V Instruction Set Architecture.
- term: RV64
  definition: The 64-bit version of the RISC-V Instruction Set Architecture.
- term: Sv39
  definition: A RISC-V virtual memory architecture standard, defining page table sizes
    and address translation.
- term: BFD
  definition: Binary File Descriptor library, a cross-target binary file format manipulation
    library used by binutils.
- term: GAS
  definition: The GNU Assembler, part of the binutils package.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZA45rLKW9CXmod+aLUmvYrgUkj_sV13i1Sj=TDj3bxaBQ@mail.gmail.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

This patch adds support for the RISC-V Svukte 1.0 extension, which is used for address-independent fault latency. The extension is registered with version 1.0, implies Zicsr, and rejects RV32 as it requires Sv39. Tests for RV64 architecture attribute, RV32 rejection, and -march help have been included.
