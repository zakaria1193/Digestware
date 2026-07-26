---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- vector
- extension
- assembler
discussion_id: 36f87cee-df61-46de-8919-83ff26fda06f@suse.com
source_type: public_inbox
title: '[PATCH v4 03/12] RISC-V: replace INSN_V_EEW64'
headline: 'RISC-V: replace INSN_V_EEW64'
tldr: Introduce INSN_CLASS_ZVE64X for RISC-V vector instructions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves code clarity and correctness by using more specific instruction classes.
- Replaces a generic flag with a more specialized enum, potentially simplifying logic
  elsewhere.
exchanges: []
primer_expert: This patch refactors the RISC-V vector extension handling by replacing
  the generic `INSN_V_EEW64` flag with a dedicated instruction class `INSN_CLASS_ZVE64X`.
  This allows for more precise logic in BFD and the assembler, particularly when determining
  compatibility between the base 'v' extension, ZVE32X, and ZVE64X. It ensures that
  instructions intended only for 64-bit effective element width extensions (like ZVE64X)
  are correctly handled and diagnosed, especially when ZVE32X is enabled.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: INSN_V_EEW64
  definition: A flag indicating that a vector instruction supports a 64-bit effective
    element width.
- term: INSN_CLASS_ZVE64X
  definition: A new instruction class representing RISC-V vector instructions that
    are part of the ZVE64X extension.
- term: ZVE32X
  definition: A RISC-V vector extension that provides 32-bit element width support.
- term: ZVE64X
  definition: A RISC-V vector extension that provides 64-bit element width support.
- term: BFD
  definition: Binary File Descriptor library, a GNU component that abstracts different
    object file formats.
series_id: 'binutils:risc-v: replace insn_v_eew64'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/36f87cee-df61-46de-8919-83ff26fda06f@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch replaces the `INSN_V_EEW64` flag with the more specific `INSN_CLASS_ZVE64X` in the RISC-V assembler and BFD library. This change improves clarity by properly categorizing instructions that support the ZVE64X extension, making diagnostics and subset checks more accurate, especially concerning the interaction between ZVE32X and ZVE64X.
