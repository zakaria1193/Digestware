---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- ace
- avx10
- instructions
- new-feature
discussion_id: 20261116081937.1879560-1-haochen.jiang@intel.com
source_type: public_inbox
title: Support new ACE instructions
headline: Support new ACE instructions
tldr: Introduces new x86 ACE instructions, including ACEv2 and ACE_OP_FP16/32/64,
  based on recent Intel specifications.
proposer: Haochen Jiang
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Expands the supported instruction set for x86 processors.
- Requires updates across multiple components of the binutils toolchain.
exchanges: []
primer_expert: This is the cover letter for a series of patches adding support for
  new Intel x86 instructions, specifically ACEv2 and ACE_OP_FP16/32/64, based on the
  'ACE v2 / AVX10.3 Specification'. The patches will update GAS and the opcodes library
  to recognize and correctly process these instructions, including their unique encoding
  and operand requirements.
primer_glossary:
- term: ACE
  definition: Advanced Core Extensions, a set of instruction set extensions for Intel
    processors.
- term: ACEv2
  definition: The second version of the Advanced Core Extensions instruction set.
- term: ACE_OP_FP16/32/64
  definition: Specific instructions within the ACE instruction set for floating-point
    operations.
- term: AVX10.3
  definition: A version of Intel's Advanced Vector Extensions instruction set, incorporating
    new features.
series_id: binutils:support new ace instructions
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116081937.1879560-1-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch series announces the introduction of support for new x86 instruction set extensions: ACEv2 and ACE_OP_FP16/32/64. These instructions are detailed in a recently published Intel specification document. The series aims to integrate these advanced instructions into the binutils toolchain, enabling assembly and disassembly for code utilizing these new features.
