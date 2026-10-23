---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- refactoring
- code structure
discussion_id: 20261022203309.1217773-1-Sarvesh.Chandra@amd.com
source_type: public_inbox
title: '[PATCH v3 1/2] gas: factor bundle-lock state into struct bundle_region'
headline: 'gas: factor bundle-lock state into struct bundle_region'
tldr: Refactors GAS's bundle lock mechanism by encapsulating state into a `struct
  bundle_region` for better management.
proposer: Sarvesh Chandra <Sarvesh.Chandra@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves code organization and maintainability by encapsulating state.
- Introduces a minor indirection but is a necessary step for future feature development.
exchanges:
- author: Sarvesh Chandra
  role: proposer
  position: Submits a patch to refactor GAS's bundle lock state into a dedicated structure.
  quote: 'Introduce a reusable struct bundle_region holding the frag, frchain,

    depth and alignment exponent of a bundle-locked region, replacing the

    separate bundle_lock_frag/bundle_lock_frchain/bundle_lock_depth globals.

    start_bundle and finish_bundle now take the alignment exponent as a

    parameter, and a region is opened and closed through new

    bundle_region_open and bundle_region_close helpers.


    This is a…'
primer_expert: This is a preparatory, non-functional change for GAS's assembly directive
  processing. It consolidates the per-region state for the `.bundle_lock` directive
  (specifically, the start fragment, fragment chain, and depth counter) into a `struct
  bundle_region`. This abstraction is designed to enable the future support of concurrent
  or alternative locking mechanisms, such as the proposed `.bundle_lock flex` mode,
  without modifying the core directive handling logic extensively.
primer_glossary:
- term: GAS
  definition: GNU Assembler. The assembler used in the GNU toolchain, responsible
    for converting assembly language code into machine code.
- term: struct
  definition: A composite data type in C programming language that groups together
    variables of different data types under a single name.
- term: frag
  definition: Abbreviation for 'fragment'. In GAS, a fragment represents a piece of
    output, such as code or data, that the assembler is constructing. These are chained
    together to form sections.
- term: frchain
  definition: Fragment chain. A linked list of fragments that together constitute
    a section in the output object file.
- term: .bundle_lock
  definition: An assembler directive used to align subsequent code to specific bundle
    boundaries, often for performance-sensitive code on architectures with instruction
    bundles.
series_id: 'binutils:gas: factor bundle-lock state into struct bundle_region'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261022203309.1217773-1-Sarvesh.Chandra@amd.com
bugzilla_url: null
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

This patch is the first part of a series introducing a flexible mode for the `.bundle_lock` directive in GAS. It refactors the existing global variables that managed the state of the strict bundle lock (fragment, fragment chain, depth) into a new `struct bundle_region`. This change is non-functional on its own but prepares the ground for supporting multiple types of bundle regions, such as the upcoming flex mode.
