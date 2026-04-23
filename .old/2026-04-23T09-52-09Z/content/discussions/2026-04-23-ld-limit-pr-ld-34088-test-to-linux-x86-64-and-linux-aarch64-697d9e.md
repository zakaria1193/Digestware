---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- testsuite
- platform-specific
discussion_id: aemFOnCeDuwcGR7V@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] ld: Limit PR ld/34088 test to Linux/x86-64 and Linux/aarch64'
headline: 'ld: Limit PR ld/34088 test to Linux/x86-64 and Linux/aarch64'
tldr: Limits a test for PR ld/34088 to Linux/x86-64 and Linux/aarch64 because it depends
  on libm.a with feclearexcept included in a linker script.
stakes: Avoids test failures on platforms where the required libm.a setup is not available.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Avoids test failures on unsupported platforms.
- Reduces test coverage by limiting the test to specific platforms.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Acknowledges the patch, indicating acceptance.
  quote: Thanks.
primer_expert: This patch modifies the testsuite for the binutils linker (`ld`). It
  restricts the execution of a test case for a specific bug fix (PR ld/34088) to only
  run on Linux x86-64 and AArch64. This is done because the test relies on the presence
  of the `feclearexcept` function within `libm.a` as specified by a linker script,
  a setup specific to those platforms. The linker script uses the `GROUP` command,
  which affects archive extraction.
primer_general: Software projects often have automated tests to ensure that the code
  works correctly. Sometimes, a test might depend on specific features of the operating
  system or hardware. This patch limits a particular test for the binutils linker
  (`ld`) to only run on certain versions of Linux (x86-64 and AArch64). The test depends
  on a specific mathematical library (`libm.a`) having a particular function (`feclearexcept`)
  and being set up in a certain way using a linker script. Since this setup is only
  available on those Linux versions, running the test elsewhere would cause it to
  fail.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aemFOnCeDuwcGR7V@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-23'
---

This patch limits the execution of a specific linker test (related to PR ld/34088) to Linux on x86-64 and AArch64 architectures. The test relies on `libm.a` containing the `feclearexcept` function, which is included via a linker script. This specific setup is only implemented for these two platforms, so limiting the test avoids failures on other architectures.
