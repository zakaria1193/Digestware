---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- compiler
- extension
discussion_id: CAHT-pJyhD7wN37W26zOuqgke6U2+TKdr2DuSiAR_WHjG6AKoGw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add Zama16b extension support'
headline: 'RISC-V: Add Zama16b extension support'
tldr: New RISC-V extension 'Zama16b' for Binutils, complementing GCC support.
proposer: Nelson Chu <nelson.chu1990@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Nelson Chu
  role: maintainer
  position: Approves the patch to add Zama16b extension support to Binutils, as GCC
    already supports it, and requests it be committed.
  quote: Okay, if Gcc already supported it then we should at least recognize it in
    Binutils. Please commit, thanks.
primer_expert: This patch updates Binutils to recognize the RISC-V 'Zama16b' extension.
  The extension has already been incorporated into GCC, and this change ensures that
  the assembler and related tools can correctly parse and handle code using this new
  instruction set extension. It involves updating internal lists of supported extensions
  and related test cases.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA).
- term: Zama16b
  definition: A specific extension for the RISC-V architecture, likely related to
    arithmetic or matrix operations.
- term: extension
  definition: An optional set of instructions that can be added to a base instruction
    set architecture to provide additional functionality.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAHT-pJyhD7wN37W26zOuqgke6U2+TKdr2DuSiAR_WHjG6AKoGw@mail.gmail.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

Nelson Chu approves the patch to add support for the RISC-V Zama16b extension in Binutils, noting its existing support in GCC. The patch adds Zama16b to the list of supported standard extensions in BFD and updates the assembler's NEWS and test suite.
