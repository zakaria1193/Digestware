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
headline: 'Hppa64-hpux: Create dummy milli.a archives for binutils and ld testsuites
  [v2]'
tldr: Discusses failures in hppa64-hpux and other targets related to missing milli.a
  archives and section merging during relocatable linking.
stakes: This discussion concerns the correctness of the binutils and ld testsuites
  for the HPPA64-HPUX target, affecting developers working on or with that platform.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Creating dummy `milli.a` archives may fix testsuite failures but doesn't address
  the underlying issue.
- Changing linker script behavior may have unintended consequences on existing code.
- Using `UNIQUE`/`NOUNIQUE` output section keywords may provide more control over
  section merging but requires careful consideration of the linker script syntax.
exchanges: []
primer_expert: The discussion touches on HPPA64-HPUX target specifics, linker script
  behavior, and section merging during relocatable links.  The `lang_add_unique` call
  impacts how .text sections are handled.
primer_general: This discussion involves the HPPA64-HPUX port of binutils, specifically
  the linker (`ld`). It addresses issues related to testsuite failures. These failures
  may be caused by missing library archives or unexpected behavior during the linking
  process, for example that `.text` sections are merged when an incremental link is
  performed, contrary to what the testsuite expects.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
bugzilla_url: null
date: '2026-04-19'
---

Maciej Rozycki responds to John David Anglin's patch regarding missing `milli.a` archives in the HPPA64-HPUX testsuite. The discussion covers failures related to section merging during relocatable linking and suggests potential solutions involving linker scripts and `UNIQUE`/`NOUNIQUE` output section keywords.
