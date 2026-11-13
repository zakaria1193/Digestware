---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- linker
- discarded sections
- PIE
- testing
discussion_id: 676c9592-c147-437a-95c6-71f6f1f2a584@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH] s390: Add linker tests for references in discarded sections'
headline: 's390: Add linker tests for references in discarded sections'
tldr: Author withdraws a patch to add s390 linker tests, as the issue it addresses
  is being fixed by a new patch that ports a general fix from x86.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Needs Revision
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The original patch added specific tests, but a more general fix for the underlying
  issue is being applied, making the original tests redundant. This is a tradeoff
  between specific bug reproduction and implementing a robust, general solution.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: proposer
  position: Explains that a patch adding s390 linker tests for discarded sections
    is being withdrawn because a more general fix is being submitted.
  quote: 'Meanwhile I realized that I should have done better research: This started
    out as porting the aarch64 relr-discard-* tests for my WIP s390 support for DT_RELR,
    where the PIE test ran into the assertion. ... The tests from this patch are now
    part of my new patch that ports the x86-64 fix, that I just sent for review:'
- author: Andreas Krebbel <andreas.krebbel@de.ibm.com>
  role: reviewer
  position: Provided feedback on the patch, suggesting minor improvements to the test
    cases.
  quote: 'Just two minor nits. Feel free to ignore:

    - discard-pie.d doesn''t seem to include the expected output. So it would not
    turn into an XPASS automatically in case the problem goes away, right?

    - Should we, in discard-shared.d, document that the outcome is not what we want
    but rather what it is today?'
primer_expert: The original patch aimed to add linker test cases for s390 concerning
  references to symbols within discarded sections, particularly when linking position-independent
  executables (PIE). An assertion in `finish_dynamic_symbol` was triggered due to
  GOT entries being allocated but not initialized when sections were discarded. This
  follow-up clarifies that the tests are being superseded by a patch that implements
  a more general fix, ported from x86-64, which also addresses the assertion by correctly
  handling symbol dynamic-ness.
primer_glossary:
- term: s390
  definition: IBM's mainframe processor architecture.
- term: linker
  definition: A program that combines various object files and libraries into a single
    executable or library. It resolves symbol references and assigns addresses.
- term: discarded sections
  definition: Sections of an object file that the linker decides to omit from the
    final executable, typically because they are empty or contain data/code not required
    for execution.
- term: PIE
  definition: Position-Independent Executable. An executable program that can be loaded
    and run at any memory address. This is important for security features like Address
    Space Layout Randomization (ASLR).
- term: GOT
  definition: Global Offset Table. A table used in position-independent code to store
    addresses of global variables and functions, allowing indirect access.
- term: Assertion
  definition: A statement in a program that must be true at a certain point. If the
    assertion fails, the program typically terminates, indicating a bug.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/676c9592-c147-437a-95c6-71f6f1f2a584@linux.ibm.com
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

Jens Remus explains that a patch intended to add linker tests for references in discarded sections on s390 is being withdrawn. He initially created the tests to document an assertion failure related to PIE and discarded sections. However, he discovered that the underlying issue is not specific to DT_RELR or s390 but is a general problem also seen on x86 and RISC-V. A new patch, which ports the x86-64 fix for this issue to s390, has been submitted.
