---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- arm
- testing
- architecture
discussion_id: 20260702135419.3316452-1-rearnsha@arm.com
source_type: public_inbox
title: '[committed] aarch64: Adjust architecture version for mpamv2 tests'
headline: 'aarch64: Adjust architecture version for mpamv2 tests'
tldr: Test suite adjustment to reflect that Armv9.3a now permits mpamv2.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Lowering the architecture version requirement for tests makes them applicable to
  a wider range of compatible hardware/configurations.
- Ensuring test accuracy requires keeping pace with evolving architecture specifications.
- This change is specific to the test suite and does not affect the core assembler
  functionality beyond test coverage.
exchanges:
- author: Richard Earnshaw
  role: proposer
  position: Adjusts test suite architecture versions for mpamv2 to reflect that Armv9.3a
    now permits its use.
  quote: null
primer_expert: The AArch64 architecture defines various features and system registers.
  The MPAM (Memory Partitioning and Monitoring) feature, specifically version 2 (mpamv2),
  is related to memory system monitoring and partitioning. This change updates the
  gas assembler's test suite to acknowledge that Armv9.3a, a recent extension of the
  Arm architecture, now supports and permits the use of these mpamv2 features. Previously,
  the tests might have been configured for a later or different version that implicitly
  covered mpamv2.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: mpamv2
  definition: Memory Partitioning and Monitoring version 2, a feature in Arm architectures
    for managing and monitoring memory usage.
- term: Armv9.3a
  definition: A specific version of the Arm architecture specification, indicating
    a set of features and capabilities.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
series_id: 20260702135419.3316452-1-rearnsha@arm.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260702135419.3316452-1-rearnsha@arm.com
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

This commit adjusts the architecture version requirement for `mpamv2` tests in the binutils gas test suite. Armv9.3a now officially permits the use of `mpamv2`, so the tests are updated to reflect this newer architecture version, lowering the minimum requirement.
