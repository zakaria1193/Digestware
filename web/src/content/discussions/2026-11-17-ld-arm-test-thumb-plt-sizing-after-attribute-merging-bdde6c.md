---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- ARM
- linking
discussion_id: 8114a419-dadc-406a-997d-dc2e2275dc7c@foss.st.com
source_type: public_inbox
title: 'Re: [PATCH] ld: arm: Test Thumb PLT sizing after attribute merging'
headline: 'ld: arm: Test Thumb PLT sizing after attribute merging'
tldr: Gentle ping for review of a patch that adds regression tests for Thumb PLT sizing
  issues in the ARM linker.
proposer: Torbjorn SVENSSON <torbjorn.svensson@foss.st.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Torbjorn SVENSSON
  role: proposer
  position: Follows up on a previously submitted patch by gently pinging for review.
  quote: Another gentle ping! :)
primer_expert: This thread concerns a patch for the GNU linker (ld) targeting ARM
  processors. Specifically, it addresses an issue with Procedure Linkage Table (PLT)
  sizing when linking Thumb-only code with Thumb-2 support. The problem arises from
  differing attribute merging during linking, leading to incorrect space allocation
  for PLT entries and subsequent corruption.
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    to resolve function calls to external libraries at runtime.
- term: Thumb
  definition: A 16-bit instruction set architecture for ARM processors, designed for
    code density.
- term: Thumb-2
  definition: An extension to the Thumb instruction set that includes both 16-bit
    and 32-bit instructions, offering improved performance and code density.
- term: ARM linker
  definition: The component of the GNU toolchain responsible for combining object
    files and libraries into an executable or shared library for ARM processors.
series_id: 8114a419-dadc-406a-997d-dc2e2275dc7c@foss.st.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8114a419-dadc-406a-997d-dc2e2275dc7c@foss.st.com
bugzilla_url: null
date: '2026-11-17'
is_stub: false
stub_reason: ''
---

This is a follow-up to a patch submitted in October that addresses a PLT sizing bug in the ARM linker when linking Thumb-only code with Thumb-2 support. The bug occurs due to a mismatch in PLT header and entry sizes between ARM and Thumb, leading to corrupted PLT instructions. The author is pinging for a review of the patch and its associated test cases.
