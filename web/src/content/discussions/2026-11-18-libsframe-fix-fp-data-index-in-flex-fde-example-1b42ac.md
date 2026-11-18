---
project: binutils
subsystem: libsframe
patch_id: null
tags:
- binutils
- libsframe
- documentation
- debugging
- FDE
discussion_id: 20261118063516.3752034-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH] libsframe: Fix FP data index in flex FDE example'
headline: 'libsframe: Fix FP data index in flex FDE example'
tldr: A documentation fix in libsframe corrects the indexing for frame pointer (FP)
  data in a flexible exception data (FDE) example.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Documentation accuracy vs. potential confusion for users relying on the example.
- Minor fix that improves correctness of the specification.
exchanges: []
primer_expert: This patch addresses a documentation error within the `libsframe` library's
  specification regarding flexible FDEs. The `sframe-spec.texi` file contains an example
  demonstrating how to generate stack traces. The error lies in the indices used to
  access frame pointer (FP) tracking data when dealing with the Return Address (RA)
  and its offset. The fix correctly assigns `fp_data_index` to 4 for RA-valid entries
  and 3 for invalid RA offsets, ensuring the example accurately reflects the SFrame
  specification.
primer_glossary:
- term: libsframe
  definition: A library likely related to stack frame unwinding or exception handling,
    providing mechanisms to parse and interpret stack trace information.
- term: FP
  definition: Frame Pointer. A register or memory location that typically points to
    the base of the current function's stack frame, used for accessing local variables
    and parameters.
- term: FDE
  definition: Frame Description Entry. Data structures used in debugging information
    (like DWARF) that describe how to unwind the stack for a particular function.
- term: flexible FDE
  definition: A type of Frame Description Entry that allows for more dynamic or variable
    structures, possibly to optimize space or handle complex unwinding scenarios.
- term: RA
  definition: Return Address. The memory address where the program should resume execution
    after the current function returns.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261118063516.3752034-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This patch corrects an error in the `libsframe` documentation's example of generating stack traces using flexible FDEs. Specifically, it adjusts the data word indexes used for frame pointer tracking. The fix ensures that index 4 is used when RA-valid entries are present, and index 3 is used when the RA offset is invalid, aligning the example with the specification.
