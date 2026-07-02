---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- AArch64
- SEH
- exception handling
- binutils
- ARM
discussion_id: akP1XoGoSq19O_4h@arm.com
source_type: public_inbox
title: 'Re: [PATCH v10 1/1] aarch64: Implement Structured Exception Handling (SEH)
  on AArch64'
headline: 'aarch64: Implement Structured Exception Handling (SEH) on AArch64'
tldr: Addresses review comments for a patch implementing SEH on AArch64, clarifying
  field names and exception handling logic.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Ensuring accurate representation of unwind information for SEH.
- Balancing immediate implementation with thorough validation on all relevant architectures
  (e.g., big-endian).
- Clarity and correctness of variable naming in complex data structures.
exchanges:
- author: Alice Carlotti
  role: reviewer
  position: Clarifies that variable renaming was intended for local variables within
    a function, not for field names, and that 'offset_shift' and 'reg_shift' are correct
    as they represent shift amounts.
  quote: 'I think you misinterpreted my review - I wanted you to rename the local
    variables in seh_aarch64_add_unwind_element: divided_by -> offset_multipler regn_divided_by
    -> reg_multiplier


    The offset_shift and reg_shift field names were fine, and the new names are wrong
    (because the values are shift amounts, not multipliers).  Please change the field
    names back to offset_shift and reg_shift.'
- author: Evgeny Karpov
  role: proposer
  position: Acknowledges the feedback on variable renaming and clarifies the logic
    for checking function size, stating that the condition is primarily to catch previously
    existing issues related to alignment calculation.
  quote: "Ok, it was not clear in the previous comment. \n\nfunc_size had mostly been\
    \ calculated correctly in the past,\nexcept in some cases when the alignment was\
    \ not handled correctly.\nIn that case, func_size was calculated as a negative\
    \ value.\nThe issue with the code alignment has been fixed, however \nthat condition\
    \ still checks that case."
- author: Alice Carlotti
  role: reviewer
  position: Questions the necessity of checking `func_size >= 0` and expresses concern
    about committing code that is not validated for big-endian hosts.
  quote: 'Can you explain why there''s no need to check when func_size >= 0?  It looks
    to me like we could end up in that case without the function size being fully
    evaluated, but I don''t really understand what this is checking.


    I think deliberately committing code that is broken for a big endian host, and
    then testing and fixing it later, is the wrong approach when doing it correctly
    is no more complex (a…'
- author: Evgeny Karpov
  role: proposer
  position: Reiterates that the check for negative `func_size` handles a specific
    past issue and commits to validating big-endian host support separately if needed.
  quote: 'It does not look like a common case for aarch64-w64-mingw32 target,

    however it will be validated, and required changes will be done if needed.'
primer_expert: This discussion revolves around a patch implementing Structured Exception
  Handling (SEH) for the AArch64 architecture in binutils. Key points of contention
  include the correct naming of fields related to unwind information (e.g., `offset_shift`
  vs. `offset_multipler`) and the rationale for specific checks within the exception
  handling code. The discussion also touches upon the importance of validating code
  on big-endian hosts, even if they are not the primary target.
primer_glossary:
- term: SEH
  definition: Structured Exception Handling, a mechanism for handling runtime errors
    and exceptions in a structured way, commonly used in Windows.
- term: AArch64
  definition: The 64-bit execution state of the ARMv8 architecture and its successors.
- term: Unwind Information
  definition: Data structures used by exception handling mechanisms to trace back
    the call stack when an exception occurs.
- term: Big-Endian
  definition: A computer architecture where the most significant byte is stored at
    the lowest memory address.
series_id: 'binutils:aarch64: implement structured exception handling (seh) on aarch64'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/akP1XoGoSq19O_4h@arm.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This discussion on implementing Structured Exception Handling (SEH) for AArch64 addresses feedback from a previous review. The proposer clarifies misunderstandings regarding the renaming of variables (`offset_shift` vs. `offset_multipler`) and explains the rationale behind the exception handling logic for function sizes. Concerns about big-endian host validation are also acknowledged, with a commitment to address it.
