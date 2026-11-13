---
project: binutils
subsystem: sframe
patch_id: null
tags:
- SFrame
- stack unwinding
- documentation
- binutils
discussion_id: c3a9f24e-6198-48cf-8050-c11d34de297d@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH v2] sframe: Fix RA and FP stack recovery rules'
headline: 'sframe: Fix RA and FP stack recovery rules'
tldr: Reviewer approves v2 of a patch fixing typos in SFrame stack recovery rules
  for RA and FP.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves documentation accuracy for stack frame recovery rules.
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Submitted v2 of a patch to fix typos in SFrame stack recovery rules for
    RA and FP.
  quote: "Fix the interpreted typo and change CFA + offset to *(CFA + offset)\nfor\
    \ RA and FP stack recovery.\n---\nv1 -> v2:\n  Add changes to libsframe/doc/sframe-spec.texi."
- author: Jens Remus <jremus@linux.ibm.com>
  role: reviewer
  position: Approves the patch, finding it good, and asks for a second reviewer's
    opinion.
  quote: 'Thank you! Looks good to me. @Indu: Do you agree?'
primer_expert: This patch corrects the SFrame (Stack Frame) specification for how
  Return Address (RA) and Frame Pointer (FP) are recovered from the stack. Previously,
  the documentation incorrectly stated that values were directly added to the Call
  Frame Address (CFA), implying pointer dereferencing was not involved. This revision
  clarifies that the recovery involves dereferencing the address calculated by CFA
  + offset, ensuring accurate stack unwinding, particularly for architectures like
  AMD64 and AARCH64.
primer_glossary:
- term: SFrame
  definition: SFrame (Stack Frame) is a proposed standard for stack unwinding information,
    aiming to provide a generic way for debuggers and runtime systems to reconstruct
    the call stack.
- term: RA
  definition: Return Address. The memory address that the program will return to after
    a function call completes.
- term: FP
  definition: Frame Pointer. A register that typically points to the base of the current
    function's stack frame, used for accessing local variables and parameters.
- term: CFA
  definition: Call Frame Address. The address on the stack that defines the current
    stack frame. It's often used as a reference point for calculating offsets to local
    variables, parameters, and saved registers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c3a9f24e-6198-48cf-8050-c11d34de297d@linux.ibm.com
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

Jens Remus reviews a patch (v2) that corrects typographical errors in the SFrame specification, specifically changing 'CFA + offset' to '*(CFA + offset)' for Return Address (RA) and Frame Pointer (FP) stack recovery rules. He asks Indu for their agreement and notes that Indu's email address has been updated in MAINTAINERS.
