---
project: binutils
subsystem: hppa64-hpux
patch_id: null
tags:
- binutils
- linker
- HPPA
- HPUX
- testsuite
discussion_id: alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [SPAM] Re: [PATCH] hppa64-hpux: Create dummy milli.a archives for binutils
  and ld testsuites [v2]'
headline: 'hppa64-hpux: Create dummy milli.a archives for binutils and ld testsuites
  [v2]'
tldr: Discussion of test failures on hppa64-hpux related to missing milli.a archive
  and section merging issues.
stakes: Addresses testsuite failures on hppa64-hpux platform, ensuring correct behavior
  of binutils and linker.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Proposed
outcome: proposed
sentiment_score: 5
sentiment_rationale: Neutral discussion about test failures and potential solutions.
technical_tradeoffs: []
primer: HPPA (Hewlett-Packard Precision Architecture) is a family of reduced instruction
  set computing (RISC) architectures developed by Hewlett-Packard. `hpux` is a Unix
  operating system formerly produced by Hewlett-Packard. The linker combines object
  files into an executable.  A linker script controls how the linker combines object
  files and libraries into an output file, defining the memory layout of the program.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
bugzilla_url: null
date: '2026-04-19'
---

This discussion thread revolves around testsuite failures for the hppa64-hpux target, specifically related to a missing `milli.a` archive and issues with merging `.text` sections during relocatable linking. The thread explores potential causes and solutions for the observed failures, including the linker script and the handling of unique sections. Maciej is double-checking failures between test runs.
