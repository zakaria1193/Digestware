---
project: glibc
subsystem: arm
patch_id: null
tags:
- glibc
- arm
- static-pie
- security
- toolchain
discussion_id: 20260424134932.1638126-1-adhemerval.zanella@linaro.org
source_type: public_inbox
title: '[PATCH] arm: Enable static-pie support (BZ 34098)'
headline: 'arm: Enable static-pie support (BZ 34098)'
tldr: This patch enables static-pie support for arm-*-linux-gnueabi, requiring proper
  toolchain support to set the expected linker options.
proposer: Adhemerval Zanella <adhemerval.zanella@linaro.org>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Requires a recent version of GCC with static PIE support for ARM.
- Slightly increased binary size due to the position-independent code.
- Improved security due to address space randomization.
- Potential performance improvements in some cases due to reduced reliance on dynamic
  linking.
exchanges: []
primer_expert: This patch enables static PIE for ARM targets in glibc. Static PIE
  binaries are linked as position-independent executables, but without requiring dynamic
  relocation at runtime, improving security and potentially startup time.  The configure
  script and `start.S` are modified to accommodate this. This requires a sufficiently
  recent GCC to provide the necessary linker support.
primer_general: Position Independent Executables (PIE) improve security by allowing
  the operating system to load a program at a random address, making it harder for
  attackers to exploit vulnerabilities. Static PIE is a variation where the program
  is built to be position-independent at compile time, rather than relying on dynamic
  linking. This patch enables static PIE support for ARM processors in glibc, the
  standard C library, provided that the toolchain (compiler and linker) also supports
  it.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260424134932.1638126-1-adhemerval.zanella@linaro.org
bugzilla_url: null
date: '2026-04-24'
---

This patch enables static-pie (position independent executable) support for the arm architecture in glibc. It requires corresponding support in the toolchain (gcc) to correctly set the linker options. The `start.S` file is adjusted to avoid loading `main` from the GOT (Global Offset Table).
