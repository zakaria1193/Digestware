---
project: binutils
subsystem: bfd
patch_id: null
tags:
- arm
- architecture
- gas
- bfd
discussion_id: 20260527130630.556955-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] gas, bfd: Rename Arm v8/v9 architecture tags'
headline: 'gas, bfd: Rename Arm v8/v9 architecture tags'
tldr: Renames Arm v8/v9 architecture tags in gas and bfd to include profile suffixes
  for A-profile, maintaining consistency and tag values.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Requires updating all references to the architecture tags in gas and bfd.
- Ensures consistent naming across the toolchain.
- Potential for compatibility issues if other tools rely on the old names.
exchanges:
- author: Sivan Shani <sivan.shani@arm.com>
  role: proposer
  position: Proposes renaming Arm AEABI CPU architecture tag constants to include
    the profile suffix for A-profile architectures, aiming for consistency and addressing
    gold build failures.
  quote: 'Rename the Arm AEABI CPU architecture tag constants to include the

    profile suffix for A-profile architectures. This makes the naming

    consistent with existing v8-R and v8-M tag names, while preserving the

    existing numeric tag values.'
primer_expert: This patch modifies the architecture tag definitions in gas and bfd,
  specifically for ARM. It changes constant names to include the profile (A, R, M)
  to be more explicit. This affects how the assembler and BFD identify and process
  different ARM architecture variants.
primer_general: When the toolchain deals with ARM processors, it distinguishes between
  different versions and types, such as ARMv8-A or ARMv9-M. These distinctions are
  encoded in architecture tags. This patch renames these tags in the assembler (gas)
  and the binary file descriptor library (BFD) to make them clearer by including the
  profile (A, R, M) in the name. This change helps ensure consistency and reduces
  ambiguity when specifying the target architecture.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260527130630.556955-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

This patch focuses on renaming the Arm architecture tag constants in gas and bfd to include the profile suffix (A) for A-profile architectures, bringing them into alignment with existing v8-R and v8-M tags. The existing numeric tag values are preserved. This involves updating BFD and GAS usage, covering attribute combination tables, architecture checks, and mach selection. The patch also addresses gold build failures reported by linaro checkers.
