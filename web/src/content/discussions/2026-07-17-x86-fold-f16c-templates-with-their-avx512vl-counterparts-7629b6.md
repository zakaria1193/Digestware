---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- AVX
- F16C
- performance
discussion_id: 1d918dc0-4b90-4093-b261-b91bdf372d39@suse.com
source_type: public_inbox
title: '[PATCH 2/2] x86: fold F16C templates with their AVX512VL counterparts'
headline: 'x86: fold F16C templates with their AVX512VL counterparts'
tldr: Consolidates F16C instruction templates with AVX512VL counterparts and addresses
  issues with explicit feature disabling.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Consolidating templates simplifies the assembler's internal representation but requires
  careful handling of feature dependencies.
- Ensuring that explicit feature disabling (`.no{fma,f16c}`) continues to work correctly
  with new AVX512VL instructions adds complexity but maintains backward compatibility
  and avoids silent breaking changes.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Submits the patch to fold F16C templates with AVX512VL and discusses related
    issues discovered, proposing a solution.
  quote: 'It''s not quite clear why this wasn''t done so far. These, conceptually,

    aren''t any different from the FMA ones.


    Doing so actually made me notice a flaw in FMA template handling, which is

    being fixed alongside making the necessary changes to accommodate F16C:

    Both features aren''t prereqs of AVX512F. When they''re disabled, enabling

    AVX512VL would still not allow the 128- and 256-bit forms to assemb…'
primer_expert: This patch refactors the x86 instruction template handling in `gas`
  by merging F16C instruction templates with their AVX512VL counterparts. This follows
  a pattern established for FMA instructions. A side effect of this change is the
  exposure of an issue where enabling AVX512VL could inadvertently allow F16C or FMA
  instructions to be assembled even if those specific feature bits were explicitly
  disabled via `.arch .no{fma,f16c}`. The commit's accompanying text discusses how
  this could break older code that relied on such explicit disabling for correctness.
  The proposed solution involves ensuri…
primer_glossary:
- term: F16C
  definition: A set of x86 instructions that perform conversions between 16-bit and
    32-bit floating-point formats.
- term: AVX512VL
  definition: AVX-512 Vector Length Extensions, which allow AVX-512 instructions to
    operate on 128-bit (XMM) and 256-bit (YMM) registers, in addition to 512-bit (ZMM)
    registers.
- term: instruction template
  definition: A pattern or schema used by an assembler to represent a machine instruction,
    often including variations for different operands or features.
- term: FMA
  definition: Fused Multiply-Add, an instruction set extension that performs a multiplication
    and an addition in a single operation, often with higher precision.
- term: EVEX
  definition: An extended 512-bit vector instruction encoding used by AVX-512 instructions.
- term: .arch
  definition: An assembler directive used to specify the target architecture or feature
    set for code generation.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
series_id: 'binutils:x86: fold f16c templates with their avx512vl counterparts'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/1d918dc0-4b90-4093-b261-b91bdf372d39@suse.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch folds F16C instruction templates with their AVX512VL counterparts, similar to how FMA instructions were handled previously. This consolidation is deemed conceptually straightforward. The changes also uncover and fix a flaw in FMA template handling where AVX512VL could be enabled even if FMA/F16C were explicitly disabled. A related issue is raised: code using `.arch .no{fma,f16c}` might assemble to AVX512VL EVEX forms when AVX512 support is added, breaking previous protection. The proposed solution is to reject AVX512VL forms if FMA/F16C are explicitly disabled.
