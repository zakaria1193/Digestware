---
project: binutils
subsystem: sframe
patch_id: null
tags:
- sframe
- stack frame
- bug fix
- ABI
discussion_id: 3db3d0fa-e2de-403e-933d-e25b61c184c7@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH v2] sframe: Fix RA and FP stack recovery rules'
headline: 'sframe: Fix RA and FP stack recovery rules'
tldr: Confirms a fix for sframe stack recovery rules and requests confirmation from
  another maintainer.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Pings for a review and approval of a patch that fixes stack recovery rules
    for RA and FP in sframe, noting that a previous review was positive.
  quote: Gentle ping!
- author: Jens Remus <jens.remus@photonix.de>
  role: reviewer
  position: Approves the patch after it was updated, and asks another maintainer (@Indu)
    for their opinion.
  quote: 'Thank you! Looks good to me. @Indu: Do you agree?'
primer_expert: This discussion concerns a version 2 patch series for the sframe library,
  specifically addressing how return address (RA) and frame pointer (FP) recovery
  rules are interpreted. The fix involves changing the interpretation of `CFA + offset`
  to `*(CFA + offset)` in `include/sframe.h` and updating the sframe specification
  documentation. The patch aims to correct a subtle but important detail in how stack
  frame information is handled, particularly for AMD64 and AARCH64 architectures.
primer_glossary:
- term: sframe
  definition: A library for handling stack frame records, often used in debugging
    and profiling tools.
- term: CFA
  definition: Canonical Frame Address. A value that represents the base of the current
    stack frame, typically the address of the saved return address or the previous
    frame pointer.
- term: RA
  definition: Return Address. The memory address in the caller's function that execution
    should return to after the current function completes.
- term: FP
  definition: Frame Pointer. A register that typically points to the base of the current
    stack frame, used for accessing local variables and function arguments.
- term: stack recovery
  definition: The process of reconstructing the call stack, often used by debuggers
    or exception handlers to determine the sequence of function calls.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/3db3d0fa-e2de-403e-933d-e25b61c184c7@loongson.cn
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This email is a gentle ping regarding a patch that corrects the interpretation of register offset rules for RA (Return Address) and FP (Frame Pointer) stack recovery in sframe. The author has applied the suggested changes from a previous review, and one reviewer has approved. The ping is to solicit confirmation from another maintainer before proceeding.
