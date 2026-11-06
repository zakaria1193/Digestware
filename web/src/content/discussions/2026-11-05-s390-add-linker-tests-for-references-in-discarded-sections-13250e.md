---
project: binutils
subsystem: s390
patch_id: null
tags:
- binutils
- linker
- s390
- testing
- DWARF
discussion_id: 4ceac20f-69bb-4bd6-939e-85c47eae034c@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH] s390: Add linker tests for references in discarded sections'
headline: 's390: Add linker tests for references in discarded sections'
tldr: Andreas Krebbel reviews Jens Remus's patch adding S390 linker tests for discarded
  sections, suggesting minor documentation and test output adjustments.
proposer: Andreas Krebbel <krebbel@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improved test suite diagnostics and documentation clarity vs. the core linker logic.
- Ensuring the linker correctly handles references to discarded sections for PIE and
  shared libraries vs. the complexity of the s390 architecture.
exchanges:
- author: Jens Remus
  role: proposer
  position: Submitted a patch to add s390 linker tests for references in discarded
    sections, addressing issues with PIE executables and shared libraries.
  quote: 'Add test cases verifying the behavior when linking with references to

    symbols in discarded sections.


    Linking as PIE with a discarded section that contains a GOT reference

    triggers a BFD assertion ((h->got.offset & 1) != 0) because the GOT

    entry is allocated but never initialized.  Mark the PIE test as XFAIL.

    The PDE test passes because no dynamic relocations are needed.  The

    shared library test…'
- author: Andreas Krebbel
  role: reviewer
  position: Approves the patch but suggests minor improvements to test output and
    documentation.
  quote: 'Hi Jens,


    this ok, thanks!


    Just two minor nits. Feel free to ignore:


    - discard-pie.d doesn''t seem to include the expected output. So it would not
    turn into an XPASS automatically in case the problem goes away, right?

    - Should we, in discard-shared.d, document that the outcome is not what we want
    but rather what it is today?'
primer_expert: This discussion concerns linker test cases for the s390 architecture
  within Binutils. The patch introduces tests to verify the linker's behavior when
  symbols are referenced from sections that are marked for discarding. Specifically,
  it addresses issues related to Position Independent Executables (PIE) and shared
  libraries, where references to discarded sections can lead to assertion failures
  or spurious relocations. The review feedback focuses on improving the test suite's
  self-reporting capabilities and documentation clarity.
primer_glossary:
- term: linker
  definition: A program that combines various pieces of object code and libraries
    into a single executable program or library. It resolves symbol references between
    these pieces.
- term: s390
  definition: An IBM mainframe computer architecture. Binutils supports this architecture.
- term: discarded sections
  definition: Sections within an object file or executable that the linker is instructed
    to ignore or remove during the linking process. This is often used for optimization
    or to manage memory usage.
- term: PIE
  definition: Position Independent Executable. An executable program that can be loaded
    at any address in memory without modification. This is important for security
    features like ASLR.
- term: GOT
  definition: Global Offset Table. A table used in position-independent code (PIC)
    to store addresses of global variables and functions, allowing them to be accessed
    indirectly.
- term: XFAIL
  definition: Expected Failure. In a test suite, this marks a test that is known to
    fail for a specific reason, but is still run to ensure that the failure condition
    persists or to track regressions.
- term: R_390_NONE
  definition: A type of relocation specific to the s390 architecture. Relocations
    are instructions for the linker on how to adjust addresses in the code or data.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/4ceac20f-69bb-4bd6-939e-85c47eae034c@linux.ibm.com
bugzilla_url: null
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

Andreas Krebbel provides feedback on a patch that introduces linker test cases for the s390 architecture, specifically concerning references within discarded sections. Krebbel finds the patch acceptable but suggests two minor improvements: ensuring the `discard-pie.d` test case includes expected output for proper automated testing, and updating the documentation in `discard-shared.d` to reflect the current, rather than desired, linker behavior. The patch itself aims to verify how the linker handles symbols in discarded sections, particularly in PIE (Position Independent Executable) and shared library contexts.
