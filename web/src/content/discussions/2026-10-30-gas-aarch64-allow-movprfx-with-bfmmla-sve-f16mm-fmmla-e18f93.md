---
project: binutils
subsystem: gas/aarch64
patch_id: null
tags:
- AArch64
- assembler
- SVE
- SIMD
discussion_id: 58ee584c-5e7e-4aa7-6393-8d19b6bd7b99@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: [PATCH] gas/aarch64: Allow movprfx with bfmmla, sve-f16mm fmmla'
headline: 'gas/aarch64: Allow movprfx with bfmmla, sve-f16mm fmmla'
tldr: Fixes the gas assembler to correctly handle the 'movprfx' instruction with specific
  Advanced SIMD and SVE floating-point multiplication-accumulation instructio…
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures correct assembly of specific instruction sequences at the cost of maintaining
  instruction decoding tables.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: proposer
  position: Acknowledges a previous error and provides a fix, noting a pattern of
    similar mistakes with new instructions. The patch updates opcode tables and adds
    test cases for 'movprfx' with 'bfmmla' and 'sve-f16mm fmmla'.
  quote: 'Oops - ok, thanks!


    (I''m getting a sense of déjà vu here - because it seems we made the same

    mistake with new b?mmla instructions two years running.  I''ll have to keep an

    eye out for that next year.)'
primer_expert: This change targets the gas assembler's AArch64 backend. Specifically,
  it corrects the handling of the `movprfx` instruction when used with certain Advanced
  SIMD (SVE) floating-point multiplication-accumulation instructions (`bfmmla`, `sve-f16mm
  fmmla`). The issue was that these SVE instructions were incorrectly disallowed after
  a `movprfx`, leading to assembly errors or incorrect code generation. The fix updates
  the AArch64 instruction tables and adds relevant test cases.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture, used in modern mobile devices and servers.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    converting assembly code into machine code.
- term: movprfx
  definition: A prefix instruction in ARM assembly that conditionally moves a register's
    value based on a condition code. It's often used to optimize instruction sequences.
- term: bfmmla
  definition: An AArch64 Advanced SIMD instruction for performing fused multiply-accumulate
    operations on BFloat16 data.
- term: sve-f16mm
  definition: Refers to Scalable Vector Extension (SVE) instructions for performing
    fused multiply-accumulate operations with 16-bit floating-point (F16) data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/58ee584c-5e7e-4aa7-6393-8d19b6bd7b99@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in the AArch64 assembler (gas) where the 'movprfx' instruction was not correctly allowed in conjunction with 'bfmmla' and 'sve-f16mm fmmla' instructions. The fix involves updating opcode tables and adding test cases to ensure proper assembly of these instruction sequences. The author notes a recurring nature to similar mistakes with new instructions.
