---
project: glibc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- optimization
- backtrace
- abi
- sme
discussion_id: 20260421130804.66597-1-muhammad.kamran@arm.com
source_type: public_inbox
title: 'Re: [PATCH] aarch64: simplify __libc_arm_za_disable failure path'
headline: 'Aarch64: Simplify __libc_arm_za_disable failure path'
tldr: A patch simplifies the failure path of `__libc_arm_za_disable` by using a tailcall,
  which may affect backtraces.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Under Review
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Tailcall reduces stack usage but may alter backtrace information.
- Simplifying the failure path reduces code complexity but could obscure debugging
  information.
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: reviewer
  position: Suggests changing the call to `__libc_fatal` to a tailcall to improve
    backtrace context.
  quote: This should be changed to a tailcall.
- author: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
  role: other
  position: Agrees with the change.
  quote: null
primer_expert: This patch modifies the `__libc_arm_za_disable` function, which is
  likely related to disabling the Scalable Matrix Extension (SME) on AArch64. Turning
  a regular call into a tailcall impacts stack unwinding and debugging. This is relevant
  for AArch64 ABI and debugging tools.
primer_general: This patch focuses on the AArch64 architecture and aims to simplify
  the error handling path within a function called `__libc_arm_za_disable`. This function
  likely disables some feature (possibly related to specialized hardware) and the
  patch modifies how it handles failures. By using a 'tailcall', the program can potentially
  reduce overhead, but it might also change the information available during debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982E0F97547E99DC1128678832D2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-22'
---

This patch simplifies the failure path of the `__libc_arm_za_disable` function in glibc for AArch64. Wilco Dijkstra suggests changing a call to `__libc_fatal` to a tailcall to improve context in backtraces. The original patch aimed to avoid preserving the caller's stack frame, but the tailcall provides sufficient context.
