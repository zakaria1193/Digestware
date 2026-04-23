---
project: glibc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- glibc
- SME
- ZA
- error handling
discussion_id: 20260421130804.66597-1-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH] aarch64: simplify __libc_arm_za_disable failure path'
headline: Simplify __libc_arm_za_disable failure path in aarch64
tldr: This patch simplifies the failure path of __libc_arm_za_disable and adds a test
  case to exercise it.
stakes: Simplifying the failure path reduces code complexity and improves maintainability.
  The new test ensures the abort path functions correctly.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Simplifying the code reduces overhead in the failure path.
- Adding a test case increases the size of the test suite, but improves confidence
  in the code's correctness.
exchanges:
- author: Muhammad Kamran
  role: proposer
  position: Proposes simplifying the failure path of `__libc_arm_za_disable` and adding
    a test case.
  quote: 'The failure tail of __libc_arm_za_disable only leads to

    __libc_fatal, so it does not need to preserve call frame state.'
- author: Florian Weimer
  role: reviewer
  position: Acknowledges Muhammad Kamran's patch.
  quote: null
primer_expert: '`__libc_arm_za_disable` is used to disable the Scalable Matrix Extension
  (SME) ZA state on AArch64. The failure path involves shutting down SME and calling
  `__libc_fatal`. This patch simplifies the code in this path. The new test case exercises
  the abort path, ensuring the code behaves as expected.'
primer_general: This patch focuses on improving the robustness of the GNU C Library
  (glibc) on ARM 64-bit (AArch64) systems. Specifically, it simplifies the code that
  handles errors when disabling the Scalable Matrix Extension (SME), a feature that
  accelerates certain types of calculations. It also adds a test case to ensure that
  this error-handling code works correctly, preventing unexpected program behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260421130804.66597-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-04-21'
---

Muhammad Kamran proposes simplifying the failure path in the `__libc_arm_za_disable` function for aarch64. The patch removes unnecessary code related to call frame state preservation, since the failure path leads only to `__libc_fatal`.  It also introduces `tst-sme-za-disable-fail`, a new test case that triggers the abort path, ensuring the process terminates with SIGABRT and the expected fatal message. Florian Weimer reviewed the patch.
