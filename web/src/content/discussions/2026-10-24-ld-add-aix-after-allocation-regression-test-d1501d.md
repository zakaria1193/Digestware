---
project: binutils
subsystem: ld
patch_id: null
tags:
- aix
- linker
- test
- regression
- embedded
discussion_id: 20261024095819.1905597-4-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 3/3] ld: add AIX after-allocation regression test'
headline: 'ld: add AIX after-allocation regression test'
tldr: Introduces a test case for AIX linker emulations to verify correct handling
  of foreign inputs and retargeted outputs.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures correct error handling in AIX linker emulations for specific failure cases.
- Provides coverage for retargeting scenarios.
- Requires an embedded object file for self-contained testing.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Adds a new regression test for AIX linker emulations to cover scenarios
    with foreign inputs and retargeted outputs, ensuring clean failure and no crashes.
  quote: 'The test writes a fixed x86-64 relocatable object and links it with each
    of the four AIX emulations, once with no linker script and once with a script
    that retargets the output to elf32-little.


    Without the two fixes the test has 8 unexpected failures (crashes or failures
    without clean diagnostic). With them it has 8 passes.'
primer_expert: This patch introduces a test suite for the AIX linker emulations, specifically
  targeting issues identified in other patches regarding foreign inputs and retargeted
  outputs. The test embeds an x86-64 relocatable object and attempts to link it using
  various AIX emulations, both in their native mode and when retargeted to a generic
  ELF format via a linker script. The test asserts that in these error conditions
  (architecture mismatch, unsupported retargeting), the linker exits cleanly with
  status 1, provides the expected diagnostic message, and does not crash or leave
  artifacts. This is crucial f…
primer_glossary:
- term: AIX
  definition: Advanced Interactive eXecutive, a Unix operating system developed by
    IBM.
- term: regression test
  definition: A test designed to ensure that a recent code change has not negatively
    impacted existing functionality.
- term: relocatable object
  definition: An object file that contains code and data, and includes information
    that allows it to be combined with other object files and libraries during the
    linking process.
- term: linker script
  definition: A file that provides instructions to the linker on how to map sections,
    handle symbols, and control the output file layout.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
series_id: 'binutils:ld: add aix after-allocation regression test'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024095819.1905597-4-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This patch adds a new regression test (`ld-powerpc/aix-retarget.exp`) to specifically test the AIX linker emulations. The test links an embedded x86-64 relocatable object with AIX emulations, both with and without a linker script that retargets the output to a generic ELF format. It verifies that the linker fails cleanly with an architecture mismatch diagnostic, does not crash, and produces no output file, ensuring the fixes in the preceding patches work correctly.
