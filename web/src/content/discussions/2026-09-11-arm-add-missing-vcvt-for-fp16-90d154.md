---
project: binutils
subsystem: arm
patch_id: null
tags:
- arm
- assembler
- floating-point
- fp16
- instruction
discussion_id: 650a3109-9194-4c8e-b078-ee454f0b06a0@arm.com
source_type: public_inbox
title: '[PATCH] arm: Add missing vcvt for FP16'
headline: 'arm: Add missing vcvt for FP16'
tldr: Patch adds missing VCVT instructions for FP16 to binutils' ARM support, mapping
  them to existing FPv3 Half Precision instructions.
proposer: Andre Vieira <andre.simoesdiasvieira@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 8
technical_tradeoffs:
- Adds support for important FP16 VCVT instructions, enabling better utilization of
  half-precision capabilities.
- Maps new instructions to legacy internal names, which improves compatibility but
  may reduce clarity for developers unfamiliar with the internal mapping.
exchanges:
- author: Andre Vieira <andre.simoesdiasvieira@arm.com>
  role: proposer
  position: Submitted a patch to add missing VCVT instructions for FP16 to binutils,
    mapping them to existing FPv3 Half Precision instructions.
  quote: 'Add missing VCVT (between floating-point and fixed-point, floating-point)
    for FP16, see https://support.arm.com/documentation/ddi0597/2026-03/SIMD-FP-Instructions/VCVT--between-floating-point-and-fixed-point--floating-point---Convert-between-floating-point-and-fixed-point-


    This was implemented in the same way the other FP16 instructions were added, by
    mapping them to existing FPv3 Half Precision…'
- author: Richard Earnshaw <Richard.Earnshaw@arm.com>
  role: reviewer
  position: Approved the patch but expressed concern over the confusing mapping of
    new instructions to legacy internal names.
  quote: 'This is ok. Thanks for fixing it up.


    I''ll state for the record that I find this mapping of instructions to a legacy-style
    internal name that never existed (we''d moved to UAL before these instructions
    were added) *very* confusing, especially given the lack of documentation for them.


    But it is what it is, and this does not affect the validity of your patch; just
    the number of brain cycles that I…'
- author: Andre Vieira <andre.simoesdiasvieira@arm.com>
  role: proposer
  position: Acknowledged the reviewer's feedback on the naming convention.
  quote: "On 11/09/2026 11:02, Richard Earnshaw wrote:\n>\n> This is ok. Thanks for\
    \ fixing it up.\n> \n> I'll state for the record that I find this mapping of instructions\
    \ to \n> a legacy-style internal name that never existed (we'd moved to UAL \n\
    > before these instructions were added) *very* confusing, especially \n> given\
    \ the lack of documentation for them.\n> \n> But it is what it is, and this does\
    \ not affect t…"
primer_expert: This patch adds assembler support within binutils for the ARM FP16
  (half-precision floating-point) VCVT instructions. These instructions convert between
  floating-point and fixed-point formats, and also between different floating-point
  formats. The implementation maps these new FP16-specific conversions to existing
  underlying FPv3 half-precision instruction encodings, ensuring compatibility with
  older ARM architectures that might not directly expose distinct FP16 VCVT opcodes.
primer_glossary:
- term: VCVT
  definition: Vector Convert instruction in ARM's SIMD (NEON) and VFP extensions,
    used for converting data between different numerical formats such as floating-point
    and fixed-point, or between different floating-point precisions.
- term: FP16
  definition: Half-precision floating-point format, using 16 bits to represent a floating-point
    number. It offers lower memory usage and potentially faster operations compared
    to single-precision (FP32) or double-precision (FP64).
- term: ARM
  definition: A family of reduced instruction set computing (RISC) architectures commonly
    used in mobile devices, embedded systems, and increasingly in servers and laptops.
- term: FPv3
  definition: Floating-Point Version 3 architecture for ARM processors, which includes
    support for half-precision (FP16) floating-point operations.
- term: UAL
  definition: Unified Assembler Language. A syntax for ARM assembly language that
    unified different instruction set syntaxes (like ARM, Thumb, Thumb-2) into a single,
    more consistent form.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/650a3109-9194-4c8e-b078-ee454f0b06a0@arm.com
bugzilla_url: null
date: '2026-09-11'
is_stub: false
stub_reason: ''
---

This patch introduces support for missing VCVT instructions (conversions between floating-point and fixed-point, and between floating-point types) for FP16 (half-precision floating-point) in binutils' ARM assembler. The implementation maps these to existing FPv3 Half Precision instructions, following the pattern used for other FP16 instructions. The changes have been tested across various ARM configurations.
