---
project: binutils
subsystem: bfd
patch_id: null
tags:
- arm
- architecture
- tags
- gas
- bfd
discussion_id: 0c1140de-35bf-41a6-8e25-d165e8eeace0@arm.com
source_type: public_inbox
title: 'Re: [PATCH] gas, bfd: Rename Arm v8/v9 architecture tags'
headline: 'gas, bfd: Rename Arm v8/v9 architecture tags'
tldr: Renames Arm AEABI CPU architecture tag constants in gas and bfd to include the
  profile suffix for A-profile architectures, but needs build failure fixes.
proposer: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
consensus: Needs Revision
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- The renaming aims for consistency but requires updating all references to the tags
  in the codebase.
- The patch attempts to preserve existing numeric tag values to minimize disruption.
exchanges:
- author: Richard Earnshaw (foss)
  role: reviewer
  position: Requests build failure fixes, specifically with `--enable-gold`.
  quote: 'This is a nice cleanup, but you need to fix the build failures (in gold)
    that the linaro checkers picked up on.


    Try building with --enable-gold.'
primer_expert: This patch renames the architecture tags used in the ARM backend of
  binutils (specifically in gas and bfd) to include profile suffixes (A, R, M) for
  better consistency. These tags are used to identify the target architecture during
  assembly and linking. The changes affect `bfd/elf32-arm.c`, `elfcpp/arm.h`, `gas/config/tc-arm.c`,
  and `include/elf/arm.h`.
primer_general: Binutils is a collection of binary tools, including the GNU assembler
  (gas) and the Binary File Descriptor library (BFD). The assembler translates assembly
  code into machine code, and BFD provides a uniform interface for manipulating different
  object file formats. This patch modifies the way ARM architectures are identified
  within binutils, renaming architecture tags to include profile suffixes (A, R, M)
  for clarity and consistency. This ensures that the correct code is generated and
  linked for the intended ARM processor.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/0c1140de-35bf-41a6-8e25-d165e8eeace0@arm.com
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

Sivan Shani proposed renaming the Arm AEABI CPU architecture tag constants to include the profile suffix for A-profile architectures. This change aims to make the naming consistent with existing v8-R and v8-M tag names while preserving the existing numeric tag values. The patch updates BFD and GAS usage accordingly, including attribute combination tables, architecture checks, and mach selection. Richard Earnshaw notes that the patch needs build failure fixes, specifically when building with `--enable-gold`.
