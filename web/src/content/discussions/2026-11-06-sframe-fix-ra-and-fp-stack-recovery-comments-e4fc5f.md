---
project: binutils
subsystem: sframe
patch_id: null
tags:
- binutils
- sframe
- documentation
- stack unwinding
- comments
discussion_id: 20261106082226.3803346-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH] sframe: Fix RA and FP stack recovery comments'
headline: 'sframe: Fix RA and FP stack recovery comments'
tldr: A patch corrects comments in the `sframe.h` header file to accurately reflect
  how Return Address (RA) and Frame Pointer (FP) stack recovery values are interpre…
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Improved comment accuracy for `sframe` definitions vs. no functional code change.
- Ensuring clarity for developers maintaining stack unwinding logic.
exchanges:
- author: mengqinggang
  role: proposer
  position: Submitted a patch to fix comments in `sframe.h` related to RA and FP stack
    recovery, changing the interpretation from addition to dereferencing.
  quote: 'Fix the interpreted typo and change CFA + offset to *(CFA + offset)

    for RA and FP stack recovery.'
primer_expert: This is a documentation-only patch for the `sframe` (stack frame unwind
  information) component within Binutils. It corrects comments in `sframe.h` to accurately
  reflect how Frame Pointer (FP) and Return Address (RA) values are recovered from
  the stack. The change clarifies that offsets are used as memory addresses to dereference,
  rather than being directly added to the CFA (Call Frame Address) or a base register
  to obtain the FP/RA values.
primer_glossary:
- term: sframe
  definition: Stack Frame unwind information. This data structure and associated logic
    in Binutils helps in unwinding the call stack, typically used for debugging and
    profiling.
- term: RA
  definition: Return Address. The address in the calling function to which the program
    should return after the current function completes.
- term: FP
  definition: Frame Pointer. A register that points to the beginning of a stack frame,
    used to access local variables and parameters within a function.
- term: CFA
  definition: Call Frame Address. The canonical address of the stack frame. It's used
    as a reference point for calculating the locations of other values within the
    stack frame, such as saved registers.
- term: stack recovery
  definition: The process of retrieving saved register values (like RA and FP) from
    the stack during stack unwinding to reconstruct the state of previous stack frames.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261106082226.3803346-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

This patch corrects comments in `include/sframe.h` to accurately describe the stack recovery mechanism for Return Address (RA) and Frame Pointer (FP) registers. Previously, comments indicated that stack recovery involved adding an offset to the Call Frame Address (CFA) or a base register. The corrected comments now clarify that these offsets are used to dereference a memory location, signifying that the actual RA and FP values are stored at `*(CFA + offset)` or `*(BASE_REG + offset)` respectively, rather than being directly calculated by adding the offset.
