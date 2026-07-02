---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- assembler
- deprecation
- isa
discussion_id: 424a399b-f88e-4049-9e35-8ad72894f309@arm.com
source_type: public_inbox
title: 'Re: [PATCH 2/3] aarch64: warn if the TME feature is used during assembly.'
headline: 'Aarch64: Warn if the TME feature is used during assembly'
tldr: A patch for the AArch64 assembler introduces a warning for the deprecated Transactional
  Memory Extension (TME) feature, with discussion on clarifying the scope…
proposer: Richard Earnshaw <Richard.Earnshaw@arm.com>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Guides developers away from using deprecated architectural features, improving compatibility
  with future hardware and software.
- Prepares the toolchain for eventual removal of deprecated feature support, reducing
  maintenance overhead.
- Introduces minor changes to assembler output (warnings) for affected code.
- Improves code quality by applying `const` correctness in new code.
exchanges:
- author: Richard Earnshaw (foss)
  role: proposer
  position: Proposes a patch to warn users if they attempt to use the deprecated TME
    feature in AArch64 assembly, as part of a move to remove support for unused ISA
    features.
  quote: Arm has obsoleted the TME feature from the architecture because no implementations
    were ever produced. The assembler will now warn if instructions from this extension
    are detected during assembly.
- author: Jan Beulich
  role: reviewer
  position: Asks for clarification regarding the specific Arm targets affected by
    the TME deprecation and suggests using `const` pointers in new code for improved
    type safety.
  quote: The only reference to which targets are affected is "Arm" at the start of
    the sentence. Yet it's not arm*-*-* that this talks about. May I ask for clarifying
    this here?
- author: Richard Earnshaw
  role: maintainer
  position: Acknowledges the feedback and indicates that the clarification on target
    scope is handled in a subsequent patch in the series, also agreeing to review
    pointer usage for `const` correctness.
  quote: Fair point. Will clarify. In fact, I rewrote this section in patch 3, which
    handles this.
primer_expert: This patch modifies the GNU Assembler (`gas`) for the AArch64 architecture.
  Specifically, it impacts `gas/config/tc-aarch64.c` and `gas/NEWS` by introducing
  a warning mechanism for the Transactional Memory Extension (TME). TME was an optional
  AArch64 ISA feature that did not see hardware implementation and was subsequently
  removed from the architecture specification. The assembler now flags usage of TME
  instructions during source processing to discourage their use and prepare for eventual
  removal of support. The discussion also touches upon C coding standards, such as
  the use of `const` point…
primer_general: This discussion is about an update to the assembler, a program that
  translates human-readable assembly code into machine code for ARM's 64-bit processors
  (AArch64). A feature called 'Transactional Memory Extension' (TME) was once planned
  for these processors but was never actually built into any real chips and has now
  been officially removed from the ARM specification. This update to the assembler
  will now give a 'warning' if someone tries to use TME instructions in their code.
  This helps developers avoid using features that won't work on real hardware. There's
  also a smaller discussion about how to write the code itself, suggesting using 'constant
  pointers' to make the code clearer and safer.
series_id: 'binutils:aarch64: warn if the tme feature is used during assembly'
series_role: reply
series_parts:
- title: 'aarch64: warn if the TME feature is used during assembly.'
  url: https://inbox.sourceware.org/binutils/2591315c-7bd8-4c5c-a6ab-d4b653ebb28f@arm.com
  n: 2
  total: 3
- title: 'aarch64: warn if the TME feature is used during assembly.'
  url: https://inbox.sourceware.org/binutils/bd5d99a4-8a6d-4f45-99c6-8268c28b21a6@suse.com
  n: 2
  total: 3
- title: 'aarch64: warn if the TME feature is used during assembly.'
  url: https://inbox.sourceware.org/binutils/20260625143639.3909071-3-rearnsha@arm.com
  n: 2
  total: 3
url: https://inbox.sourceware.org/binutils/424a399b-f88e-4049-9e35-8ad72894f309@arm.com
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This discussion revolves around a patch to the AArch64 assembler that introduces a warning when the deprecated Transactional Memory Extension (TME) feature is used during assembly. TME was removed from the Arm architecture specification due to a lack of implementations, and this change aims to guide developers away from using it. During review, there was a request to clarify the scope of the warning (which Arm targets are affected) and a suggestion to use `const` pointers in new code for better type safety. The patch is part of a larger series to deprecate unused ISA features.
