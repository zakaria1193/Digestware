---
project: binutils
subsystem: powerpc
patch_id: null
tags:
- powerpc
- elf
- abi
- sframe
- review
discussion_id: CAJiQQZb6GDcQpuO6huPiCtW1tzXJFdGOPTCQjY3wWCicamWbzw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
headline: 'PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
tldr: Reviewer Indu Bhagat needs more time to test patches related to PowerPC SFrame
  support.
proposer: Indu Bhagat <ibhagatgnu@gmail.com>
consensus: Proposed
outcome: under_review
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Indu Bhagat
  role: reviewer
  position: Requests more time to test the SFrame support patches due to work commitments,
    and asks if a rebased v3 would be preferred.
  quote: Apologies I have not been able to find time in the last few weeks, due to
    some work related commitments. I expect to find a better balance in a few weeks.
    At this time, I wanted to run some stacktracer tests on ppc using your patches,
    but havent been able to get to the task.
- author: Abhay Kandpal
  role: proposer
  position: Previously pinged Indu for a review of v2 of the SFrame support patches
    and offered to post a rebased v3 if that would be easier.
  quote: null
primer_expert: This is a follow-up on a review of patches intended to add support
  for SFrame unwind information to the 64-bit PowerPC ELF ABI. The reviewer, Indu
  Bhagat, is currently unable to perform the necessary stacktracer tests due to external
  work commitments and is seeking to manage the review timeline, potentially by accepting
  a rebased version of the patches.
primer_glossary:
- term: SFrame
  definition: A specific type of stack frame or unwind information used in some calling
    conventions, particularly relevant for debugging and exception handling.
- term: 64-bit PowerPC ELF ABI
  definition: The Application Binary Interface for 64-bit PowerPC processors using
    the Executable and Linkable Format (ELF) for object files and executables.
- term: stacktracer
  definition: A tool or technique used to trace the execution flow of a program by
    examining the call stack.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAJiQQZb6GDcQpuO6huPiCtW1tzXJFdGOPTCQjY3wWCicamWbzw@mail.gmail.com
bugzilla_url: null
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

Indu Bhagat apologizes for the delay in reviewing Abhay Kandpal's patches for 64-bit PowerPC ELF ABI SFrame support. Work commitments have prevented Indu from running the necessary stacktracer tests. Indu expects to have more time in a few weeks and asks Abhay if he would prefer a rebased v3 instead of waiting for review of v2.
