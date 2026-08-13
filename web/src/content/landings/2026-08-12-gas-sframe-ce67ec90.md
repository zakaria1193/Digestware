---
project: binutils
subsystem: gas/sframe
patch_id: null
tags:
- gas
- sframe
- cfi
- debugging
commit_hash: ce67ec902d836898d93c62f71ff2e97f774a0b95
source_type: public_inbox
author: Jens Remus <jremus@sourceware.org>
headline: 'gas: Add test for signal frame with unsupported CFI'
tldr: 'gas: Adds a test case for handling unsupported CFI directives in signal frames.'
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a test for sframe generation in gas. Specifically,
  it targets the behavior when .cfi_signal_frame is used with unsupported CFI directives.
  The expected behavior is to generate an empty FDE instead of a full one. This test
  validates the fix introduced in fa11363bc9ad, which addressed dangling pointers
  in sframe_xlate_ctx_cleanup().
primer_glossary:
- term: gas
  definition: The GNU Assembler, which translates assembly language code into machine
    code.
- term: SFrame
  definition: A debugging information format used by some toolchains to represent
    stack frame layout. It's processed by gas and consumed by debuggers.
- term: CFI
  definition: Control Flow Integrity. In this context, it refers to directives used
    by the assembler to describe the structure of stack frames for debugging purposes.
- term: FDE
  definition: Frame Description Entry. A data structure within debugging information
    that describes how to unwind the stack for a particular function or code region.
- term: .cfi_signal_frame
  definition: An assembler directive that indicates the start of a signal frame, which
    has specific unwinding requirements different from regular function calls.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260812124048.CE97D4BB24DE@sourceware.org
date: '2026-08-12'
is_stub: true
stub_reason: low_score
---

A new test case has been added to verify the behavior of gas when encountering unsupported Control Flow Integrity (CFI) directives within signal frames. In such scenarios, gas typically skips the generation of a full Stack Frame (SFrame) description and instead produces an "empty" Frame Description Entry (FDE). This test ensures this behavior is correctly handled and aligns with a previous fix for dangling pointers during context cleanup.
