---
project: binutils
subsystem: binutils
patch_id: null
tags:
- H8
- linker
- testsuite
- default architecture
- embedded
discussion_id: 20260711005517.744460-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH v3 2/2] ld testsuite: Update "__patchable_function_entries section
  [2-6]" test cases'
headline: 'ld testsuite: Update "__patchable_function_entries section [2-6]" test
  cases'
tldr: Updates ld test cases to accommodate the change in default H8 architecture.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures the test suite remains valid after the default architecture change.
- Requires updating tests that were sensitive to address size differences between
  H8/300 and H8/300H.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Submits a patch to update ld test cases that failed due to the switch
    from H8/300 to H8/300H as the default architecture, adjusting for the change in
    address size.
  quote: 'Changing the default H8 architecture from H8/300 to H8/300H caused these

    test cases to fail, as shown below. H8/300H uses 32-bit addresses in its

    default advanced mode, whereas H8/300 uses 16-bit addresses. The following

    patch updates the affected test cases accordingly.'
primer_expert: This patch is part of a series (see previous digest item) that changes
  the default H8 architecture in binutils from H8/300 to H8/300H. This change has
  ripple effects, particularly in the linker's test suite. The H8/300H architecture,
  in its default advanced mode, uses 32-bit addresses, whereas the H8/300 uses 16-bit
  addresses. Test cases specifically examining sections like `__patchable_function_entries`
  now need to be adjusted to reflect this change in address representation and potential
  section size differences.
primer_glossary:
- term: ld testsuite
  definition: A collection of tests designed to verify the correct functionality of
    the GNU linker (ld).
- term: __patchable_function_entries
  definition: A section in an executable or object file, often used in embedded systems
    or for specific compiler features, that contains entries pointing to functions
    that may be patched or modified at runtime. The addressing and size of this section
    can depend on the target architecture.
- term: H8/300H
  definition: A specific microcontroller variant in the Renesas H8 family, characterized
    by its 32-bit internal architecture and addressing capabilities, often used in
    embedded systems.
- term: H8/300
  definition: An earlier and simpler variant of the Renesas H8 microcontroller family,
    typically operating with a 16-bit address space in its default configuration.
- term: linker
  definition: A program that combines object files and libraries into a single executable
    or library, resolving symbol references and performing address adjustments.
series_id: 'binutils:ld testsuite: update "__patchable_function_entries section [2-6]"
  test cases'
series_role: reply
series_parts:
- title: 'ld testsuite: Update "__patchable_function_entries section [2-6]" test cases'
  url: https://inbox.sourceware.org/binutils/20260710145801.744425-1-jdx@o2.pl
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/20260711005517.744460-1-jdx@o2.pl
bugzilla_url: null
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

This patch addresses test case failures in the ld test suite resulting from the change in the default H8 architecture to H8/300H. The H8/300H variant uses 32-bit addresses in its default advanced mode, differing from the H8/300's 16-bit addresses, which caused existing test cases related to the `__patchable_function_entries` section to fail. The patch updates these tests to align with the new addressing behavior.
