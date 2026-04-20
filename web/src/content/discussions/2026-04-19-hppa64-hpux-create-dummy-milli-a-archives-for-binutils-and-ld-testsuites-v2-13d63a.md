---
project: binutils
subsystem: hppa64-hpux
patch_id: null
tags:
- binutils
- ld
- hppa64-hpux
- testsuite
- linker script
discussion_id: alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [SPAM] Re: [PATCH] hppa64-hpux: Create dummy milli.a archives for binutils
  and ld testsuites [v2]'
headline: 'hppa64-hpux: Create dummy milli.a archives for binutils and ld testsuites
  [v2]'
tldr: Discussion of test failures in hppa64-hpux target, specifically related to missing
  milli.a archive and section merging.
stakes: Ensuring testsuite passes for hppa64-hpux target is important for maintaining
  the toolchain's support for that platform.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Creating dummy archives might mask underlying issues.
- Adjusting linker scripts can impact linking behavior.
- Disabling section merging might have performance implications.
exchanges: []
primer_expert: The HPPA backend for binutils and ld has specific requirements, particularly
  around section merging and library dependencies (`milli.a`).  The discussion indicates
  issues with how `.text` sections are handled during relocatable linking, potentially
  requiring adjustments to the linker script or backend code.
primer_general: This discussion focuses on testing the binutils toolchain (assembler,
  linker, etc.) for a specific architecture (HPPA) and operating system (HP-UX). During
  testing, certain expected files or libraries might be missing, leading to test failures.  The
  linker's behavior in merging code sections can also cause unexpected results. The
  thread explores the reasons for these failures and potential solutions, such as
  modifying linker scripts.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
bugzilla_url: null
date: '2026-04-19'
---

This discussion thread revolves around failures in the binutils and ld testsuites for the hppa64-hpux target. The initial patch aimed to fix failures due to a missing `milli.a` archive. Maciej Rozycki is double-checking for new failures. John David Anglin points out other failures related to section merging and suggests the linker script might need adjustments.
