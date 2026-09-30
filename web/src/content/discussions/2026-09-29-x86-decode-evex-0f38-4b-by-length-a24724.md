---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- EVEX
- decoder
- ACE
discussion_id: 0ed0b87d09a08fe6f3093838df68d04491c42ce4.1790705096.git.RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH v4 2/7] x86: decode EVEX 0F38 4B by length'
headline: 'x86: decode EVEX 0F38 4B by length'
tldr: Modifies the EVEX decoder to correctly handle instructions with non-zero L'L,
  a prerequisite for ACE instructions.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves decoder accuracy for a specific instruction encoding.
- Enables support for future instruction sets like ACE.
exchanges: []
primer_expert: The EVEX prefix is an extension to VEX used in AVX-512 and later instruction
  sets. This patch modifies the `evex_len_table` and related files in `opcodes/` to
  ensure that the disassembler correctly associates instruction byte sequences starting
  with `0F38 4B` with their corresponding lengths, even when the L'L signaling of
  the EVEX prefix is set. This is a prerequisite for decoding new ACE V1 instructions
  that leverage these features.
primer_glossary:
- term: EVEX
  definition: A 4-byte instruction prefix used in AVX-512 and later x86 instruction
    sets to encode features like vector length, rounding, and masking. It extends
    the capabilities of the older VEX prefix.
- term: L'L field
  definition: A field within the EVEX prefix that typically encodes vector length
    information. Modifying how this field is interpreted is crucial for supporting
    new instruction sets that may use it differently.
- term: ACE
  definition: AI Compute Extensions, a set of x86 instructions designed to accelerate
    AI and machine learning workloads.
- term: disassembler
  definition: A program that converts machine code into assembly language source code.
- term: opcodes
  definition: The part of an instruction that specifies the operation to be performed.
    In binutils, 'opcodes' refers to the component responsible for instruction decoding
    and encoding.
series_id: 'binutils:x86: decode evex 0f38 4b by length'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/0ed0b87d09a08fe6f3093838df68d04491c42ce4.1790705096.git.RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch adjusts the EVEX decoder in binutils to properly process entries where the L'L field is non-zero. This is a necessary change to ensure that ACE instructions, which may utilize non-zero L'L values, are decoded correctly.
