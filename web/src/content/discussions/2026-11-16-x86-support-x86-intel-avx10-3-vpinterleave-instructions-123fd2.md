---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- avx10
- vpinterleave
- instructions
- encoding
discussion_id: 20261116081322.1851772-4-haochen.jiang@intel.com
source_type: public_inbox
title: '[PATCH 3/3] x86: Support x86 Intel AVX10.3 VPINTERLEAVE instructions'
headline: 'x86: Support x86 Intel AVX10.3 VPINTERLEAVE instructions'
tldr: Adds support for AVX10.3 VPINTERLEAVE instructions, noting encoding differences
  compared to VEX-based instructions.
proposer: Haochen Jiang
consensus: Under Review
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adds support for new vector interleaving instructions.
- Highlights differences in instruction encoding (EVEX vs. VEX) for similar functionality.
exchanges: []
primer_expert: This patch adds support for the AVX10.3 VPINTERLEAVE instructions.
  It updates `opcodes/i386-opc.tbl` and the disassembler's EVEX-related header files
  and C source. The gas test suite is also expanded with new `.d`, `.s`, and `.exp`
  files. The summary notes that the 128-bit versions use EVEX encoding, resulting
  in a longer encoding than comparable VEX-based VPUNPCK instructions, with potential
  for future code size optimizations.
primer_glossary:
- term: AVX10.3
  definition: A version of Intel's Advanced Vector Extensions instruction set, which
    includes enhancements over previous versions like AVX10.2.
- term: VPINTERLEAVE
  definition: An instruction that interleaves elements from two source registers into
    a destination register, part of the AVX10.3 instruction set.
- term: VPUNPCK
  definition: Vector Unpack High/Low instructions, used to interleave elements from
    vector registers.
- term: EVEX
  definition: An advanced instruction encoding scheme used in AVX-512 and later x86
    extensions, capable of encoding longer instructions and supporting more features
    than previous schemes like VEX.
- term: VEX
  definition: Vector Extension, an instruction encoding scheme used in AVX and AVX2
    that replaced the older SSE prefixing scheme.
series_id: 'binutils:x86: support x86 intel avx10.3 vpinterleave instructions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261116081322.1851772-4-haochen.jiang@intel.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch introduces support for the AVX10.3 VPINTERLEAVE instructions into binutils. These instructions provide functionality similar to 128-bit VPUNPCK instructions but use a longer EVEX encoding for the %xmm registers. The patch updates the assembler's test suite and opcode definitions to handle these new instructions correctly. An optimization to reduce code size for the 128-bit versions is planned for a future patch.
