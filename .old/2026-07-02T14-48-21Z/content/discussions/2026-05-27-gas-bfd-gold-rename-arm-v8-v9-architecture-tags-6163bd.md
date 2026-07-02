---
project: binutils
subsystem: bfd
patch_id: null
tags:
- arm
- architecture
- gas
- bfd
- gold
discussion_id: 20260527141948.683770-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] gas, bfd, gold: Rename Arm v8/v9 architecture tags'
headline: 'gas, bfd, gold: Rename Arm v8/v9 architecture tags'
tldr: Renames Arm architecture tags in gas, bfd, and gold to include profile suffixes
  for A-profile architectures, maintaining consistency and tag values.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Requires updating all references to the architecture tags in gas, bfd, and gold.
- Ensures consistent naming across the toolchain.
- Potential for compatibility issues if other tools rely on the old names.
exchanges:
- author: Sivan Shani <sivan.shani@arm.com>
  role: proposer
  position: Proposes renaming Arm AEABI CPU architecture tag constants and macro definitions
    to include the profile suffix for A-profile architectures, aiming for consistency.
  quote: 'Rename the Arm AEABI CPU architecture tag constants and macro definitions
    to include the

    profile suffix for A-profile architectures. This makes the naming

    consistent with existing v8-R and v8-M tag names, while preserving the

    existing numeric tag values.'
primer_expert: This patch touches the architecture definitions used by gas, bfd, and
  gold to handle Arm binaries.  The changes primarily involve renaming constants to
  include the profile (A, R, M) for better clarity and consistency, impacting how
  the tools identify and process different Arm architectures.
primer_general: When working with different ARM processors, the toolchain needs to
  know the specific architecture version and profile (A, R, or M). This information
  is stored as architecture tags. This patch renames these tags in the assembler (gas),
  the binary file descriptor library (BFD), and the linker (gold) to make them consistent
  and easier to understand, particularly by explicitly including the profile type
  in the tag name.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260527141948.683770-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

This patch renames the Arm architecture tags in gas, bfd, and gold to include the profile suffix for A-profile architectures (e.g., v8-A). The change aims for naming consistency with existing v8-R and v8-M tags, while preserving numeric tag values. This involves updates to BFD, GAS, and Gold, including attribute combination tables, architecture checks, and mach selection.  This makes the architecture more explicit.
