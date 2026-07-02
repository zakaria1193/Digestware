---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- ARM
- architecture
- binutils
- feature flag
discussion_id: a96afba9-1a37-4784-a996-0944b5d8e6c6@arm.com
source_type: public_inbox
title: 'Re: [PATCH v3 6/7] aarch64: Remove +mpamv2 feature option'
headline: 'aarch64: Remove +mpamv2 feature option'
tldr: Removes the obsolete +mpamv2 feature option from the aarch64 architecture.
proposer: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes a now-obsolete feature flag, simplifying the build configuration.
- Ensures consistency with current ARM architecture specifications.
exchanges:
- author: Richard Earnshaw (foss)
  role: proposer
  position: Removes the +mpamv2 architecture option and adjusts tests because MPAMv2
    details now only use system registers and are optional from Armv9.3-a.
  quote: The remaining mpamv2 details only use system registers; so by our conventions
    we do not use a feature option to enable them.  Remove the now +mpamv2 architecture
    option and adjust the tests accordingly.
- author: Alice Carlotti
  role: reviewer
  position: Asks if 'now' was a typo in the proposer's statement.
  quote: Is "now" a typo?
- author: Richard Earnshaw (foss)
  role: proposer
  position: Clarifies that 'now' was not a typo but that 'redundant' should have followed
    it, and provides context on the timing of the specification change.
  quote: No, but the word 'redundant' should have been after it :)
primer_expert: This patch removes the `+mpamv2` feature flag from the aarch64 configuration
  in binutils. This is because the MPAMv2 controls are now exclusively managed via
  system registers, and the feature itself is no longer a mandatory part of the architecture
  from Armv9.3-a onwards. The change simplifies the feature set and aligns binutils
  with the evolving ARM architecture specifications.
primer_glossary:
- term: MPAMv2
  definition: Memory Partitioning and Monitoring version 2, a feature in ARM architectures
    for managing and monitoring memory access at a hardware level.
- term: System Register
  definition: Special-purpose registers in ARM processors used for configuration,
    control, and status information, often related to system-level features.
- term: AArch64
  definition: The 64-bit execution state of the ARMv8 architecture and its successors.
series_id: 'binutils:aarch64: remove +mpamv2 feature option'
series_role: reply
series_parts:
- title: 'aarch64: Remove +mpamv2 feature option'
  url: https://inbox.sourceware.org/binutils/5242e8c6-4060-b712-4180-1b9d70e18e84@e124511.cambridge.arm.com
  n: 6
  total: 7
url: https://inbox.sourceware.org/binutils/a96afba9-1a37-4784-a996-0944b5d8e6c6@arm.com
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

This patch series proposes removing the `+mpamv2` feature option for the aarch64 architecture in binutils. The change is motivated by the fact that MPAMv2 related details now only use system registers and are no longer controlled by a specific feature option, with MPAMv2 becoming optional from Armv9.3-a. The author clarifies a potential typo and explains the rationale behind the change.
