---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- risc-v
- optimization
discussion_id: 20261022203055.1217638-1-Sarvesh.Chandra@amd.com
source_type: public_inbox
title: '[PATCH v3 0/2] gas: add a flex mode to .bundle_lock'
headline: 'gas: add a flex mode to .bundle_lock'
tldr: Introduces a flexible variant of the .bundle_lock directive in GAS for aligning
  hot code regions of unknown length.
proposer: Sarvesh Chandra <Sarvesh.Chandra@amd.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Introduces flexibility for aligning code regions of unknown length, potentially
  improving performance for hot paths.
- Requires careful management of strict and flex locking states to avoid conflicts
  or unexpected behavior.
exchanges:
- author: Sarvesh Chandra
  role: proposer
  position: Submits a patch series to introduce a flexible mode for the .bundle_lock
    directive in GAS.
  quote: 'This series adds a flexible variant of .bundle_lock to gas.  v3 splits the

    earlier single patch into a mechanical refactor (1/2) and the functional

    change (2/2), and addresses Jan''s review of v2.


    .bundle_lock flex N aligns the start of a bundle-locked region to 2**N but, unlike
    a strict .bundle_lock, allows the region to exceed one bundle and cross bundle
    boundaries.  It is meant for aligning th…'
primer_expert: This proposal introduces a new variant, `.bundle_lock flex N`, to GAS's
  existing bundle locking mechanism. While strict `.bundle_lock` enforces alignment
  within a single bundle, the flex mode relaxes this to allow alignment to a power-of-two
  boundary (`2**N`) for regions of potentially unknown length, designed for optimizing
  hot code paths like loops. The implementation includes refactoring the internal
  bundle region state management to support both strict and flex modes independently.
primer_glossary:
- term: GAS
  definition: GNU Assembler. The assembler used in the GNU toolchain, responsible
    for converting assembly language code into machine code.
- term: .bundle_lock
  definition: An assembler directive used to align subsequent code to specific bundle
    boundaries, often for performance-sensitive code on architectures with instruction
    bundles.
- term: bundle
  definition: A group of instructions that are fetched, decoded, or executed together
    by the processor. Alignment to bundle boundaries can improve performance.
- term: hot region
  definition: A section of code that is executed frequently, making it a prime candidate
    for optimization.
- term: relaxation
  definition: A process during linking or assembly where the assembler or linker resolves
    relative addresses and adjusts code to achieve optimal placement and correct offsets,
    especially for position-independent code.
series_id: 'binutils:gas: add a flex mode to .bundle_lock'
series_role: cover
series_parts:
- title: 'gas: add a flex mode to .bundle_lock'
  url: https://inbox.sourceware.org/binutils/20261022203319.1217827-1-Sarvesh.Chandra@amd.com
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/20261022203055.1217638-1-Sarvesh.Chandra@amd.com
bugzilla_url: null
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

This patch series introduces a flexible mode for the `.bundle_lock` directive in the GNU Assembler (GAS). The new `.bundle_lock flex N` directive allows alignment of a code region to `2**N` boundaries, but permits the region to cross bundle boundaries and have an unknown final length. This is intended for aligning hot code paths, such as loops, where the exact size is not known at assembly time. The series also refactors the internal state management for bundle locking to support this new mode.
