---
project: binutils
subsystem: haiku/testsuite
patch_id: null
tags:
- haiku
- testsuite
- elf
- arm
- ldscripts
discussion_id: alpine.DEB.2.21.2604280040070.28583@angie.orcam.me.uk
source_type: public_inbox
title: '[PING^2][PATCH 0/6] Haiku/testsuite: Enable ELF tests'
headline: 'Haiku/testsuite: Enable ELF tests'
tldr: This series enables ELF tests for Haiku, addressing previous shortcomings and
  potential regressions across Haiku targets.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enabling new tests increases the test execution time.
- Fixes to ldscripts may be required to support specific Haiku targets.
- Improved confidence in binutils functionality on Haiku.
exchanges: []
primer_expert: This series enables ELF tests in the binutils testsuite for the Haiku
  OS. It involves changes to testsuite configurations and potentially linker scripts
  (`ldscripts`). Enabling these tests provides better coverage and validation of binutils
  functionality on Haiku, across different architectures.
primer_general: Binutils is a collection of binary tools, such as the linker and assembler,
  essential for software development. Testsuites verify the correctness of these tools
  across different platforms. This patch series enables the ELF (Executable and Linkable
  Format) tests for the Haiku operating system within the binutils testsuite, ensuring
  that the tools function correctly on Haiku.
series_id: 'binutils:haiku/testsuite: enable elf tests'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2604280040070.28583@angie.orcam.me.uk
bugzilla_url: null
date: '2026-04-27'
---

This patch series enables ELF tests for the Haiku operating system in the binutils testsuite. The series includes preparatory changes to avoid regressions across different Haiku targets. The proposer notes that most changes are testsuite-related, with one addressing missing veneer sections in the ARM/Haiku linker scripts. The approved non-ARM patches will be committed, and the ARM maintainers will handle the ARM-specific fixes.
