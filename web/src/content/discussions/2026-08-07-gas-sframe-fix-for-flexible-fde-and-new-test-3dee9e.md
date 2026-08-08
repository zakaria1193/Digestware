---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- sframe
- FDE
- debugging
discussion_id: 20260807143544.1154106-1-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH v2 0/2] gas: sframe: Fix for flexible FDE and new test'
headline: 'gas: sframe: Fix for flexible FDE and new test'
tldr: Updated patch series fixes SFrame generation for flexible FDE and adds a new
  test case.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves the accuracy of exception frame generation for targets supporting flexible
  FDE.
- Adds a test case to maintain code quality and prevent regressions in stack unwinding
  logic.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Submits a v2 patch series to fix SFrame generation for flexible FDE and
    add a test case for a dangling pointer issue.
  quote: For changes in v2 see individual patch notes. Patch 1 fixes the generation
    of SFrame if a target supports SFrame V3 flexible FDE. Patch 2 adds a test for
    the issue Nick fixed with commit fa11363bc9ad ("Ensure that sframe_xlate_ctx_cleanup()
    doe snot leave any dangling pointers").
primer_expert: This patch series updates `gas`'s SFrame support. Version 2 addresses
  issues with flexible FDE generation on targets that support SFrame V3. It also includes
  a new test case to ensure a previously fixed dangling pointer bug in `sframe_xlate_ctx_cleanup`
  remains resolved. This impacts exception handling and debugging information generation.
primer_glossary:
- term: gas
  definition: The GNU Assembler, responsible for converting assembly language code
    into machine code.
- term: sframe
  definition: Likely refers to a specific format or mechanism for representing stack
    frames, particularly for debugging or exception handling purposes.
- term: FDE
  definition: Frame Description Entry. Part of the DWARF debugging information format,
    describing how to unwind the stack frame for a given function.
- term: flexible FDE
  definition: An enhanced or more adaptable version of the Frame Description Entry
    format, allowing for more complex or efficient stack unwinding information.
- term: CFI
  definition: Call Frame Information. A standard used to describe the layout of stack
    frames, enabling accurate stack unwinding for debugging and exception handling.
- term: dangling pointers
  definition: Pointers that reference memory locations that have been deallocated
    or are otherwise invalid, leading to potential crashes or security vulnerabilities.
series_id: 'binutils:gas: sframe: fix for flexible fde and new test'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260807143544.1154106-1-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-08-07'
is_stub: false
stub_reason: ''
---

Jens Remus presents version 2 of a patch series for `gas`'s SFrame implementation. The first patch addresses issues with generating SFrame when a target supports flexible FDE, and the second patch introduces a new test case to verify a fix for dangling pointers in `sframe_xlate_ctx_cleanup`. The changes aim to improve correctness and robustness in exception frame handling.
