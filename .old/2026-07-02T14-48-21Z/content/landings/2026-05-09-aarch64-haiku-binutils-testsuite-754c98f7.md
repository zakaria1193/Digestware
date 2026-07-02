---
project: binutils
subsystem: aarch64/haiku/binutils/testsuite
patch_id: null
tags:
- testsuite
- haiku
- aarch64
- pei
commit_hash: 754c98f7bc449954db564b0dadc479209d884362
source_type: public_inbox
author: Maciej W. Rozycki <macro@sourceware.org>
headline: 'Aarch64/Haiku/binutils/testsuite: Suppress PEI test'
tldr: The PEI test is suppressed for AArch64 Haiku targets in the binutils testsuite.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `binutils/testsuite/binutils-all/aarch64/pei-aarch64-little.d`
  to exclude Haiku targets.  The exclusion is due to the lack of a PEI BFD target
  in the default Haiku configuration.  This prevents a regression introduced by enabling
  ELF tests.
primer_general: The binutils testsuite verifies the correct behavior of binutils utilities.  PEI
  (Pre-EFI Initialization) is a part of the UEFI (Unified Extensible Firmware Interface)
  specification, related to early system initialization.  This commit suppresses a
  PEI-related test for AArch64 Haiku targets because Haiku doesn't provide a default
  PEI BFD target, preventing test failures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260509144145.163674BA2E12@sourceware.org
date: '2026-05-09'
---

The PEI (Pre-EFI Initialization) test is now suppressed for AArch64 Haiku targets in the binutils testsuite. This prevents a regression caused by enabling ELF tests with Haiku targets, as there is no PEI BFD target included by default with the Haiku target configuration.
