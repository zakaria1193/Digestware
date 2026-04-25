---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- ld
- testsuite
- glibc
- x86-64
discussion_id: aemFOnCeDuwcGR7V@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] ld: Limit PR ld/34088 test to Linux/x86-64 and Linux/aarch64'
headline: 'ld: Limit PR ld/34088 test to Linux/x86-64 and Linux/aarch64'
tldr: Limits the PR ld/34088 test to Linux/x86-64 and Linux/aarch64 due to its dependency
  on a glibc-specific libm.a linker script.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Reduces test coverage by limiting the platforms on which the test is executed.
- Simplifies the test environment by removing dependencies on specific glibc configurations
  on certain platforms.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Acknowledges the patch to limit the test.
  quote: Thanks.
primer_expert: This patch modifies the testsuite to limit the scope of a specific
  linker test (`PR ld/34088`). The test relies on the presence of a specific linker
  script (`libm.a`) within glibc, which is only available on Linux/x86-64 and Linux/aarch64.
  By limiting the test to these platforms, the patch avoids failures on other architectures
  where this specific glibc setup is not present.
primer_general: The linker combines compiled code into an executable.  Test suites
  ensure the linker works correctly.  This patch limits a specific linker test to
  run only on Linux systems with x86-64 and AArch64 architectures.  The reason for
  the limitation is that the test depends on a particular setup of the glibc math
  library, which is only present on those systems.  This avoids test failures on systems
  where the specific glibc setup is not available.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aemFOnCeDuwcGR7V@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-23'
---

H.J. Lu proposes limiting the execution of the `PR ld/34088` test case to Linux/x86-64 and Linux/aarch64 architectures. The test depends on a specific `libm.a` linker script found in glibc for those architectures, which contains the `feclearexcept` function. Alan Modra acknowledges the change.
