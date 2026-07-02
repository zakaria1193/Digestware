---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- arm
- isa
- deprecation
discussion_id: 20260702124446.3296717-1-rearnsha@arm.com
source_type: public_inbox
title: '[committed v4 0/7] aarch64: deprecate some ISA features'
headline: 'aarch64: deprecate some ISA features'
tldr: Deprecates several AArch64 ISA features that were specified but not implemented
  in products, marking the first step towards eventual removal.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: committed
impact_score: 5
sentiment_score: 9
technical_tradeoffs:
- Deprecating features first allows users to adapt gradually before full removal,
  minimizing disruption.
- Reverting previous implementation commits ensures consistency but requires careful
  conflict resolution if the original commits had subsequent changes.
- Removing unused features simplifies the toolchain maintenance and reduces code complexity.
exchanges:
- author: Richard Earnshaw
  role: proposer
  position: Introduces deprecation warnings for unused AArch64 ISA features as a step
    toward their eventual removal from the tools.
  quote: null
- author: Richard Earnshaw
  role: contributor
  position: Removes a stray comment from opcode/aarch64.h that was left after a flag
    bit was removed.
  quote: null
- author: Richard Earnshaw
  role: contributor
  position: Adds warnings for instructions related to the unimplemented TME feature
    and updates existing warning functions.
  quote: null
- author: Richard Earnshaw
  role: contributor
  position: Removes MLBI instruction from a system register alias test, as MLBI is
    related to unimplemented features.
  quote: null
- author: Richard Earnshaw
  role: contributor
  position: Reverts a previous commit that added support for MLBI system instructions,
    as MLBI is now considered obsolete.
  quote: null
- author: Richard Earnshaw
  role: contributor
  position: Reverts a commit that added FEAT_MPAMv2_VID system registers, as this
    feature has been withdrawn by Arm.
  quote: null
- author: Richard Earnshaw
  role: contributor
  position: Removes the '+mpamv2' feature option from the assembler configuration,
    aligning with the withdrawal of the feature.
  quote: null
- author: Richard Earnshaw
  role: contributor
  position: Updates the NEWS file to reflect the withdrawal of the MPAMv2_VID feature.
  quote: null
primer_expert: Arm has withdrawn certain architectural features for AArch64 that,
  while defined, never saw product implementation. This series addresses the binutils
  assembler's response to this withdrawal. It marks features like TME (Transactional
  Memory Extension) and MPAMv2_VID (Memory Partitioning and Monitoring v2) as deprecated,
  issuing warnings if they are used. Subsequent commits in the series revert previous
  additions of these features and clean up related tests and documentation. The ultimate
  goal is to remove support for these unused features entirely from the toolchain.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: ISA
  definition: Instruction Set Architecture, defining the set of instructions that
    a processor can execute.
- term: TME
  definition: Transactional Memory Extension, a set of instructions designed to simplify
    the implementation of transactional memory.
- term: MPAMv2_VID
  definition: Memory Partitioning and Monitoring version 2, a feature for managing
    and monitoring memory resources, with specific Video ID (VID) aspects.
- term: Deprecation
  definition: Marking a feature or component as obsolete, indicating that it will
    be removed in a future version, often accompanied by warnings.
- term: gas
  definition: The GNU Assembler.
series_id: 20260702124446.3296717-1-rearnsha@arm.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260702124446.3296717-1-rearnsha@arm.com
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

Richard Earnshaw's patch series introduces deprecation warnings for several AArch64 ISA features that were specified but never implemented in actual products. This is the initial step towards potentially removing support for these features from the tools entirely. Features affected include TME (Transactional Memory Extension) and MPAMv2_VID (Memory Partitioning and Monitoring v2), with the latter involving reverts of previous commits to correctly remove support. The series also includes NEWS file updates and test suite adjustments.
