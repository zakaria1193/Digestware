---
project: binutils
subsystem: bfd
patch_id: null
tags:
- arm
- binutils
- bfd
- gas
- gold
discussion_id: 20260528112347.105400-1-sivan.shani@arm.com
source_type: public_inbox
title: '[PATCH] gas, bfd, gold: Rename Arm v8/v9 architecture tags'
headline: 'gas, bfd, gold: Rename Arm v8/v9 architecture tags'
tldr: This patch renames Arm architecture tags to include profile suffixes (A, R,
  M) for consistency across binutils components.
proposer: Sivan Shani <sivan.shani@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The patch involves a large number of small changes across multiple files, increasing
  the risk of introducing subtle errors during the renaming and updating process.
- While the patch preserves existing numeric tag values, any external tools or scripts
  relying on the old tag names will need to be updated.
exchanges: []
primer_expert: This patch focuses on standardizing the naming of Arm architecture
  tags used within binutils components (BFD, GAS, Gold). The changes ensure consistency
  in how Arm architecture profiles (A, R, M) are identified, particularly within the
  context of AEABI (Arm Embedded ABI). The patch modifies `bfd/archures.c`, `bfd/bfd-in2.h`,
  `bfd/cpu-arm.c`, `bfd/elf32-arm.c`, `elfcpp/arm.h`, `gas/config/tc-arm.c`, `gold/arm.cc`,
  `include/elf/arm.h`, and `opcodes/arm-dis.c`.
primer_general: This patch addresses the naming conventions used to identify different
  versions and types of Arm processors within the binutils toolchain. Arm processors
  come in various profiles (A, R, and M) designed for different applications. This
  change ensures that the naming of these processors within the binutils source code
  is consistent and clear, making it easier for developers to work with Arm-based
  systems. Binutils is a collection of tools essential for software development, including
  the assembler (gas), linker (ld), and binary file descriptor library (bfd).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260528112347.105400-1-sivan.shani@arm.com
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

This patch renames Arm AEABI CPU architecture tag constants and macro definitions within gas, bfd, and gold to consistently include the profile suffix (A, R, or M) for A-profile architectures. The existing numeric tag values are preserved during this renaming. The patch updates the usage of these tags in BFD, GAS, and Gold, including attribute combination tables, architecture checks, and mach selection.
