---
project: glibc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- SME
- ZA
- tailcall
- glibc
discussion_id: 20260421130804.66597-1-muhammad.kamran@arm.com
source_type: public_inbox
title: 'Re: [PATCH] aarch64: simplify __libc_arm_za_disable failure path'
headline: 'aarch64: simplify __libc_arm_za_disable failure path'
tldr: AArch64 patch simplifies the __libc_arm_za_disable failure path by using a tailcall
  to __libc_fatal.
proposer: Wilco Dijkstra
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: reviewer
  position: Suggests changing the code to use a tailcall to `__libc_fatal`.
  quote: This should be changed to a tailcall.
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: other
  position: Summarizes the purpose of the original patch, which is to simplify the
    failure tail of `__libc_arm_za_disable`.
  quote: 'The failure tail of __libc_arm_za_disable only leads to

    __libc_fatal, so it does not need to preserve call frame state.'
primer_expert: This patch modifies the `__libc_arm_za_disable` function, which is
  responsible for disabling the Scalable Matrix Extension (SME) Zeroing Array (ZA)
  on AArch64. The SME is a relatively new extension, and proper handling of its state,
  including disabling it upon failures, is crucial for system stability. The use of
  a tailcall affects stack unwinding and debugging.
primer_general: The Scalable Matrix Extension (SME) is an extension to the AArch64
  architecture that provides support for matrix operations. This patch modifies the
  `__libc_arm_za_disable` function, which is used to disable the SME's Zeroing Array
  (ZA). The patch aims to simplify the code and improve efficiency of the failure
  path.  A tailcall is a specific type of function call where the calling function
  does nothing after the called function returns, allowing the compiler to optimize
  the code by replacing the call with a jump.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982E0F97547E99DC1128678832D2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-22'
---

This patch simplifies the failure path in the `__libc_arm_za_disable` function on AArch64. Instead of preserving the caller's stack frame, it uses a tailcall to `__libc_fatal`. Wilco Dijkstra supports the change, arguing that preserving the caller's frame at the point of the call to `__libc_arm_za_disable` provides sufficient context.
