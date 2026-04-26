---
project: glibc
subsystem: aarch64
patch_id: null
tags:
- glibc
- aarch64
- SME
- error handling
- testing
discussion_id: 20260423102256.103668-1-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH v2 0/1] aarch64: simplify __libc_arm_za_disable failure path and add
  a test case'
headline: 'aarch64: simplify __libc_arm_za_disable failure path and add a test case'
tldr: This patch simplifies the failure path of the __libc_arm_za_disable function
  for aarch64 and adds a test case to exercise the abort path.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Simplifies the failure path of `__libc_arm_za_disable`, reducing code complexity.
- Adds a test case to verify the abort path, increasing code robustness.
- Reduces code size by removing unnecessary instructions.
exchanges:
- author: Muhammad Kamran <muhammad.kamran@arm.com>
  role: proposer
  position: Proposes simplifying the failure path of `__libc_arm_za_disable` by removing
    code related to call frame preservation and adding a test case to exercise the
    abort path.
  quote: 'The failure tail of __libc_arm_za_disable only leads to

    __libc_fatal, so it does not need to preserve call frame state.'
primer_expert: This patch modifies `__libc_arm_za_disable` in glibc's AArch64-specific
  code. The function is responsible for disabling Scalable Matrix Extension (SME)
  ZA tiles. The patch simplifies the code path that leads to `__libc_fatal` and adds
  a test case to ensure the abort path is correctly triggered when the TPIDR2 block
  contains invalid data. AArch64 SME is relatively new, so not all toolchain devs
  will be familiar.
primer_general: This patch focuses on improving the error handling of a specific function
  in the GNU C Library (glibc) for AArch64 architecture.  The function `__libc_arm_za_disable`
  is related to disabling a hardware feature called Scalable Matrix Extension (SME),
  which is used for accelerating matrix operations.  When `__libc_arm_za_disable`
  encounters a fatal error, it calls another function `__libc_fatal` to terminate
  the program. This patch simplifies the error handling path and adds a test to ensure
  that the program aborts correctly when the hardware feature cannot be disabled.
series_id: 'glibc:aarch64: simplify __libc_arm_za_disable failure path and add a test
  case'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260423102256.103668-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-04-23'
---

This patch simplifies the failure handling within the `__libc_arm_za_disable` function on AArch64 systems.  Specifically, it removes unnecessary code related to call frame preservation in the fatal error path. Additionally, it introduces a new test case (`tst-sme-za-disable-fail.c`) that triggers the abort path by providing a TPIDR2 block with invalid data, ensuring the process terminates as expected.  This improves code clarity and adds robustness by testing the error handling.
