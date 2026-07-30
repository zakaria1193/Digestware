---
project: binutils
subsystem: gas
patch_id: null
tags:
- debugging
- dwarf
- assembler
- sframe
- cfi
discussion_id: 20260729163445.2563223-2-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 1/2] gas: sframe: Fix non-SP/FP CFA base register if flexible FDE'
headline: 'gas: Fix non-SP/FP CFA base register with flexible FDE'
tldr: Allows gas to generate SFrame V3 FDEs with non-SP/FP CFA base registers when
  flexible FDE is supported.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Enables generation of more accurate debugging information for specific architectures
  and compiler configurations, potentially at the cost of slightly increased complexity
  in the assembler's SFrame handling logic.
exchanges:
- author: Jens Remus
  role: proposer
  position: Submits a patch to allow gas to generate SFrame V3 FDEs even when a non-SP/FP
    register is used as the CFA base. The change modifies gas/gen-sframe.c to permit
    this when flexible FDE is supported, and adjusts the testsuite to skip tests on
    affected targets.
  quote: 'If a target supports SFrame V3 flexible FDE, a non-SP/FP CFA base

    register can be represented.  Do not warn and skip generating FDE, if

    .cfi_def_cfa_offset with a non-SP/FP register in effect, if target

    supports flexible FDE.'
primer_expert: This change in gas/gen-sframe.c updates the handling of `.cfi_def_cfa_offset`
  instructions. Previously, it restricted the CFA base register to SP/FP, warning
  and skipping FDE generation otherwise. With SFrame V3 and its flexible FDE feature,
  non-SP/FP registers can be used as the CFA base, necessitating this change to avoid
  generating invalid or incomplete debugging information.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project. It translates assembly
    language code into object files.
- term: SFrame
  definition: A DWARF debugging information extension for stack frame unwinding, primarily
    used by the GNU toolchain.
- term: FDE
  definition: A DWARF (Debugging With Attributed Record Formats) common debugging
    table entry that describes how to unwind the stack for a particular function.
- term: CFA
  definition: Common Frame Address, a conceptual address that represents the 'top'
    of a stack frame. It's often described relative to a base register (like SP or
    FP) and an offset.
- term: .cfi_def_cfa_offset
  definition: A DWARF Common Information Entry (CIE) directive that defines the CFA
    using an offset from the current stack pointer. It typically implies the SP is
    the base register.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to provide
    information about compiled programs.
series_id: 'binutils:gas: sframe: fix non-sp/fp cfa base register if flexible fde'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260729163445.2563223-2-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

Jens Remus proposes a change to gas's SFrame V3 support to correctly handle non-SP/FP CFA base registers. Currently, gas warns and skips FDE generation in this scenario. This patch allows FDE generation if the target supports flexible FDE, addressing a limitation in DWARF CFI representation.
