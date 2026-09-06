---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- disassembler
- evex
discussion_id: 20260905094650.388140-1-RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH] x86: fix EVEX no-broadcast disassembly when W=1'
headline: 'x86: fix EVEX no-broadcast disassembly when W=1'
tldr: Fixes objdump to correctly identify invalid broadcast encodings for EVEX instructions
  when the W-bit is set.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses a bug in the x86 disassembler within binutils.
  It concerns the EVEX instruction prefix, specifically the handling of the 'no-broadcast'
  mode when the EVEX.W bit is set to 1. The disassembler was failing to reject encodings
  that were invalid according to the EVEX specification for W=1, while correctly handling
  the W=0 case. The fix involves marking the relevant operand mode as non-broadcastable
  before the EVEX.W-dependent path.
primer_glossary:
- term: EVEX
  definition: An advanced instruction prefix used in x86 processors for SIMD operations,
    supporting features like extended registers, vector lengths, and masking.
- term: no-broadcast
  definition: A mode in EVEX instructions where the data element is not broadcast
    from a scalar to a vector register.
- term: W-bit
  definition: A bit within the EVEX prefix that affects the operand size or other
    instruction semantics.
- term: objdump
  definition: A utility that displays information from object files, including disassembly
    of machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260905094650.388140-1-RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in the binutils disassembler where it incorrectly accepts certain EVEX instruction encodings that specify broadcasting when it's not allowed (specifically for the W=1 case). The fix ensures that these invalid encodings are flagged as errors, matching assembler behavior.
