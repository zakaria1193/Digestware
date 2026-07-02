---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- assembler
- deprecation
- sysregs
discussion_id: b59017c7-f41b-41a0-8525-48fdd92545b1@arm.com
source_type: public_inbox
title: 'Re: [PATCH 3/3] aarch64: deprecate mpamv2_vid sysregs'
headline: 'Aarch64: Deprecate mpamv2_vid sysregs'
tldr: A patch for the AArch64 assembler introduces warnings for deprecated MPAMv2_VID
  system registers, with discussion on the redundancy of warnings and test suite…
proposer: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Guides developers away from using deprecated system registers, improving code portability
  and compatibility with current and future Arm architectures.
- Rationalizes the reporting of architectural errors and deprecation warnings.
- Prepares the toolchain for eventual removal of deprecated feature support.
- Ensures clear communication to users about the status of architectural features.
exchanges:
- author: Richard Earnshaw
  role: proposer
  position: Proposes a patch to deprecate `mpamv2_vid` system registers in the AArch64
    assembler by issuing warnings upon their use, as these registers are tied to an
    unimplemented architectural feature.
  quote: Why a warning when there was an earlier error?
- author: Jan Beulich
  role: reviewer
  position: Questions the necessity of a deprecation warning when an architectural
    error is already issued for the same register and suggests suppressing informational
    messages in test output.
  quote: Why a warning when there was an earlier error?
- author: Richard Earnshaw (foss)
  role: maintainer
  position: Argues that both an architectural error and a deprecation warning are
    technically correct and provides a rationale for maintaining both. Also acknowledges
    the suggestion to suppress informational messages in tests but prioritizes the
    primary objective of deprecation.
  quote: Well technically both are correct. The selected processor (architecture)
    forbids it, and there's no point in trying to enable it because it's deprecated.
    Two reasons not to use it :)
primer_expert: This patch operates within the GNU Assembler (`gas`) for the AArch64
  architecture, specifically targeting the handling of system registers (sysregs).
  The `mpamv2_vid` sysregs are part of the "Memory Partitioning and Monitoring" (MPAM)
  extension, specifically version 2, which was a proposed architectural feature that
  ultimately did not see hardware implementation and has since been removed from the
  Arm architecture specifications. The patch modifies `gas/config/tc-aarch64.c` and
  test cases in `gas/testsuite/gas/aarch64/sysreg/` to issue warnings when these registers
  are encountered during asse…
primer_general: This discussion is about an update to the assembler for ARM's 64-bit
  processors (AArch64). Processors have special internal controls called 'system registers'
  that manage various features. Some of these, known as `mpamv2_vid` registers, were
  part of a planned feature for managing memory, but this feature was never actually
  put into computer chips and has been removed from the official ARM specifications.
  The assembler will now issue a 'warning' if developers try to use these outdated
  registers. The conversation also includes a minor debate about whether it's useful
  to show both an error and a warning for the same outdated register, as well as suggestions
  for how to make the test reports clearer.
series_id: 'binutils:aarch64: deprecate mpamv2_vid sysregs'
series_role: reply
series_parts:
- title: 'aarch64: deprecate mpamv2_vid sysregs'
  url: https://inbox.sourceware.org/binutils/f513f0a3-bee9-41fd-b6f2-c2e015a29456@suse.com
  n: 3
  total: 3
- title: 'aarch64: deprecate mpamv2_vid sysregs'
  url: https://inbox.sourceware.org/binutils/20260625143639.3909071-4-rearnsha@arm.com
  n: 3
  total: 3
url: https://inbox.sourceware.org/binutils/b59017c7-f41b-41a0-8525-48fdd92545b1@arm.com
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This discussion focuses on a patch for the AArch64 assembler that deprecates `mpamv2_vid` system registers by issuing warnings when they are used. These registers are associated with a feature that has been removed from the Arm architecture specification due to lack of implementation. The patch modifies the assembler's test suite to include scenarios where both an architectural error and a deprecation warning might occur for the same register, sparking a minor debate about the redundancy of such combined messages. There's also a suggestion to improve test output by suppressing informational messages.
