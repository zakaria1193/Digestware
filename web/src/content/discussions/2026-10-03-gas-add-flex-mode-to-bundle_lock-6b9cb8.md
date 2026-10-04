---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- x86
- optimization
- directive
discussion_id: 20261003081706.717320-1-Sarvesh.Chandra@amd.com
source_type: public_inbox
title: '[PATCH] gas: add flex mode to .bundle_lock'
headline: 'gas: add flex mode to .bundle_lock'
tldr: Enables GAS to accept oversized sequences in .bundle_lock directives for flexible
  alignment.
proposer: Sarvesh Chandra <Sarvesh.Chandra@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Potential for reduced performance if oversized sequences negate the benefits of
  strict bundling.
- Increased complexity in the assembler's directive parsing and validation logic.
exchanges:
- author: Sarvesh Chandra <Sarvesh.Chandra@amd.com>
  role: proposer
  position: Proposes to add a flex mode to `.bundle_lock` that allows sequences larger
    than the bundle size, and includes new test cases for various lock scenarios.
  quote: 'Allow .bundle_lock flex to accept sequences larger than the bundle size.

    Keep the existing alignment handling and strict checks for ordinary locks.


    Add tests for straddling, non-straddling, oversized, and nested locks.'
primer_expert: This patch modifies the gas assembler to introduce a 'flex' mode for
  the `.bundle_lock` directive. Previously, `.bundle_lock` enforced strict alignment
  based on `bundle_align_p2`, preventing sequences from exceeding a calculated bundle
  size. The change allows this check to be bypassed when `bundle_flex_lock` is enabled,
  accommodating oversized sequences while maintaining existing alignment rules for
  non-flex locks. New test cases are added to cover these expanded capabilities.
primer_glossary:
- term: gas
  definition: GNU Assembler, the assembler used in the GNU toolchain, responsible
    for converting assembly language code into machine code.
- term: .bundle_lock
  definition: An assembler directive used to group instructions into bundles, often
    for performance or alignment purposes on certain architectures.
- term: flex mode
  definition: A mode of operation for `.bundle_lock` that relaxes strict size constraints,
    allowing for sequences that might otherwise be rejected.
- term: alignment
  definition: The practice of arranging data or instructions in memory at specific
    addresses, often multiples of a certain number, to improve processing efficiency.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261003081706.717320-1-Sarvesh.Chandra@amd.com
bugzilla_url: null
date: '2026-10-03'
is_stub: false
stub_reason: ''
---

This patch introduces a 'flex mode' to the `.bundle_lock` directive in GNU Assembler (GAS), allowing sequences larger than the defined bundle size. It preserves existing alignment handling and strict checks for ordinary locks. New test cases are included to cover various scenarios, including straddling, non-straddling, oversized, and nested locks.
