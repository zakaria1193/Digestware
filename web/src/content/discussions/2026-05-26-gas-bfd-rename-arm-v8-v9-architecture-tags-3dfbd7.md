---
project: binutils
subsystem: bfd
patch_id: null
tags:
- ARM
- architecture
- tags
- BFD
- GAS
discussion_id: 20260526153155.196966-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] gas, bfd: Rename Arm v8/v9 architecture tags'
headline: 'gas, bfd: Rename Arm v8/v9 architecture tags'
tldr: Renames Arm architecture tags to include the profile suffix for A-profile architectures,
  improving consistency, while preserving the numeric tag values.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Requires updating all references to the old tag names in BFD and GAS.
- No functional change, only renaming for clarity.
exchanges: []
primer_expert: This patch focuses on standardizing the naming convention for ARM architecture
  tags within the GNU binutils, specifically in the BFD (Binary File Descriptor) library
  and GAS (GNU Assembler). Consistent naming improves maintainability and reduces
  ambiguity when dealing with different ARM profiles (A, R, M).
primer_general: This patch renames internal identifiers used by the binutils (a suite
  of binary tools) to refer to different versions of the ARM processor architecture.
  This change makes the names more consistent and easier to understand, which helps
  developers working on the tools.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260526153155.196966-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-05-26'
is_stub: false
---

Sivan Shani proposes renaming the Arm AEABI CPU architecture tag constants to include the profile suffix (e.g., 'A') for A-profile architectures. This change aims to provide consistent naming with existing v8-R and v8-M tag names.  The patch updates BFD and GAS usage accordingly while preserving the existing numeric tag values.
