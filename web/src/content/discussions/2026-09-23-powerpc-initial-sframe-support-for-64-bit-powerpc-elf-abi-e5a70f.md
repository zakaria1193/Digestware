---
project: binutils
subsystem: powerpc
patch_id: null
tags:
- patch
- powerpc
- binutils
- abi
- sframe
discussion_id: 832a1da9-344a-46cb-a061-1ccbb501a024@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH v2] PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
headline: 'PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
tldr: Gentle ping for review of v2 patch series for PowerPC SFrame support.
proposer: Abhay Kandpal
consensus: Under Review
outcome: under_review
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Implementing SFrame support requires careful adherence to the ABI, potentially impacting
  performance if not optimized.
- Ensuring compatibility with existing debugging tools and unwinders is crucial.
exchanges:
- author: Abhay Kandpal
  role: proposer
  position: Follows up on the review of the v2 patch series for PowerPC SFrame support,
    offering to create a rebased v3 to ease the review process.
  quote: Hi Indu, gentle ping on the v2 review - happy to post a rebased v3 instead
    if that's easier.
- author: Indu Bhagat
  role: reviewer
  position: Previously confirmed interest in reviewing the patch series and stated
    that v2 applies easily to the current master branch.
  quote: Thanks for confirming. I should be able to work on the V2 (V2 seems to apply
    almost easily on current master).
primer_expert: This is a follow-up on a patch series (v2) for adding SFrame support
  to the 64-bit PowerPC ELF ABI in binutils. SFrame is a stack frame unwinding mechanism.
  The author is seeking a review from Indu Bhagat and offers to provide a v3 if it
  simplifies the process. The core task involves implementing ABI-compliant stack
  frame setup and teardown for PowerPC 64-bit targets.
primer_glossary:
- term: SFrame
  definition: A specific mechanism used for stack frame unwinding, particularly relevant
    for debugging and exception handling on certain architectures like PowerPC.
- term: PowerPC
  definition: A family of RISC instruction set architectures developed by Apple, IBM,
    and Motorola.
- term: ELF ABI
  definition: Executable and Linkable Format Application Binary Interface. Defines
    the low-level conventions for how programs are compiled, linked, and executed
    on a specific architecture and operating system.
- term: stack frame unwinding
  definition: The process of determining the call stack at a given point, typically
    used by debuggers and exception handling mechanisms to reconstruct the sequence
    of function calls.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/832a1da9-344a-46cb-a061-1ccbb501a024@linux.ibm.com
bugzilla_url: null
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

This email is a follow-up, or 'gentle ping', regarding the review of version 2 of a patch series that adds initial SFrame support for the 64-bit PowerPC ELF ABI in binutils. The author offers to rebase the series into a v3 if that would facilitate the review process.
