---
project: glibc
subsystem: arm
patch_id: null
tags:
- arm
- static PIE
- security
- relocation
- glibc
discussion_id: 20260424134932.1638126-1-adhemerval.zanella@linaro.org
source_type: public_inbox
title: '[PATCH] arm: Enable static-pie support (BZ 34098)'
headline: 'Arm: Enable static-pie support (BZ 34098)'
tldr: Enables static PIE support for arm-*-linux-gnueabi, requiring gcc support and
  adjusting start.S to avoid loading main from the GOT.
proposer: Adhemerval Zanella <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Increased security due to position-independent execution vs. increased binary size.
- Requires toolchain support (GCC) to correctly set linker options.
exchanges: []
primer_expert: This patch enables static PIE support for ARM, requiring changes to
  `sysdeps/arm/configure`, `sysdeps/arm/configure.ac`, and `sysdeps/arm/start.S`.
  Static PIE binaries are fully position-independent, loaded at a random address by
  the OS, and require no relocations.
primer_general: Position Independent Executables (PIE) are a security feature that
  allows the operating system to load a program at a random address in memory. This
  makes it more difficult for attackers to exploit vulnerabilities in the code.  Static
  PIE binaries include all the code needed to run, without relying on shared libraries,
  and are loaded at a random address. This patch enables static PIE support for ARM
  architectures in glibc.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260424134932.1638126-1-adhemerval.zanella@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

This patch enables static PIE (Position Independent Executable) support for ARM architectures in glibc. It requires a corresponding GCC patch. The `start.S` file is adjusted to prevent loading `main` from the Global Offset Table (GOT).
