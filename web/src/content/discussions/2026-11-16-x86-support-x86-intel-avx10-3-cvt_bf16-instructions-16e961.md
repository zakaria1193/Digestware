---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- avx10
- bfloat16
- instructions
- assembler
discussion_id: 20261116081322.1851772-3-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH 2/3] x86: Support x86 Intel AVX10.3 CVT_BF16 instructions'
headline: 'x86: Support x86 Intel AVX10.3 CVT_BF16 instructions'
tldr: Adds support for AVX10.3 CVT_BF16 instructions in binutils, including assembler
  and disassembler updates.
proposer: Haochen Jiang
consensus: Under Review
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Enables support for a new floating-point format (BFloat16) on x86.
- Requires updates to opcode definitions and test suites.
exchanges: []
primer_expert: This patch adds support for AVX10.3's BFloat16 conversion instructions.
  It updates the opcode table (`i386-opc.tbl`) and associated disassembler files (`i386-dis-*.h`,
  `i386-dis.c`) to recognize these instructions. The changes also extend the gas test
  suite with new `.d` and `.s` files for both native and x86-64 configurations to
  verify correct assembly and disassembly. Prefix and length tables within the disassembler
  are also revised.
primer_glossary:
- term: AVX10.3
  definition: A version of Intel's Advanced Vector Extensions instruction set, which
    includes enhancements over previous versions like AVX10.2.
- term: CVT_BF16
  definition: Instructions that convert data formats to or from BFloat16 (Brain Floating
    Point), a 16-bit floating-point format optimized for machine learning.
- term: BFloat16
  definition: A 16-bit floating-point format with a similar exponent range to FP32
    but less precision, widely used in machine learning training.
- term: EVEX
  definition: An advanced instruction encoding scheme used in AVX-512 and later x86
    extensions, capable of encoding longer instructions and supporting more features
    than previous schemes like VEX.
series_id: 'binutils:x86: support x86 intel avx10.3 cvt_bf16 instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116081322.1851772-3-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch provides support for the AVX10.3 Convert to BFloat16 (CVT_BF16) instructions. Building upon AVX10.2, AVX10.3 introduces several new instruction groups, and this patch focuses on the BF16 conversion instructions. It updates the assembler's test suite and opcode definitions to correctly handle these new instructions, ensuring compatibility with code using this feature.
