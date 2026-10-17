---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- ARM
- Thumb
- PLT
- testing
discussion_id: 20261016183928.2402166-1-torbjorn.svensson@foss.st.com
source_type: public_inbox
title: '[PATCH] ld: arm: Test Thumb PLT sizing after attribute merging'
headline: 'ld: arm: Test Thumb PLT sizing after attribute merging'
tldr: Adds a test case to verify correct Thumb PLT sizing in the ARM linker after
  attribute merging, addressing a previously fixed overflow bug.
proposer: Torbjörn SVENSSON <torbjorn.svensson@foss.st.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 7
technical_tradeoffs:
- Adds test coverage, improving confidence in the fix for the PLT sizing bug.
- The test is specific to ARM Thumb targets, limiting its broader applicability.
exchanges:
- author: Torbjörn SVENSSON <torbjorn.svensson@foss.st.com>
  role: proposer
  position: Submits a patch to add a regression test for a Thumb PLT sizing bug in
    the ARM linker, seeking approval for master and binutils-2_47-branch.
  quote: 'Add regression coverage for bd8942a0e049a466f9b649364bf53445fb47dd0c.


    I stumbled upon the PLT sizing bug fixed by the above commit when

    linking the GCC LTO test pr87906 with -shared for a Thumb-only

    arm-none-eabi target with Thumb-2 support.'
- author: Christophe Lyon <christophe.lyon@arm.com>
  role: reviewer
  position: Seeks clarification on whether the submitted patch only adds a test case.
  quote: 'Hi Torbjörn!


    Do IUC that:

    - your patch only adds a test, and it'
- author: Torbjorn SVENSSON <torbjorn.svensson@foss.st.com>
  role: contributor
  position: Confirms that the patch adds a test case for the PLT sizing bug, and that
    the bug itself was fixed in an earlier commit.
  quote: Yes, the patch only adds a test. The actual fix for the PLT sizing bug (bd8942a0e049a466f9b649364bf53445fb47dd0c)
    is already in master and binutils-2_47-branch.
primer_expert: This patch introduces a regression test for an ARM-specific bug in
  the GNU linker (`ld`) related to Procedure Linkage Table (PLT) generation for Thumb
  code. The bug involved an overflow when calculating PLT entry sizes due to a mismatch
  in ARM attributes between input objects, leading to corrupted PLT instructions.
  The test targets Thumb-only targets with Thumb-2 support, as Thumb-1-only targets
  are handled differently.
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used by dynamic linkers to resolve
    function calls to shared libraries at runtime. It acts as an indirection layer.
- term: Thumb
  definition: An instruction set architecture for ARM processors, typically offering
    more compact code than the standard ARM instruction set.
- term: ARM attributes
  definition: Metadata embedded in object files that describes architectural features,
    such as the instruction set (ARM or Thumb) and processor variant, used by the
    linker to ensure compatibility.
- term: regression test
  definition: A test designed to ensure that a previously fixed bug does not reappear
    after code changes.
- term: attribute merging
  definition: The process by which the linker combines architectural or target-specific
    attributes from multiple input object files to determine the properties of the
    final executable.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016183928.2402166-1-torbjorn.svensson@foss.st.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

Torbjörn Svensson submits a patch to add a regression test for an issue in the ARM linker's Procedure Linkage Table (PLT) sizing when handling Thumb code. The issue, fixed in binutils 2.47.0, caused an overflow due to a mismatch between PLT header and entry sizes when merging attributes from different object files. This test specifically targets Thumb-only targets with Thumb-2 support.
