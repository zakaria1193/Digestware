---
project: binutils
subsystem: hppa64-hpux
patch_id: null
tags:
- binutils
- hppa
- hpux
- linker
- testsuite
discussion_id: alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [SPAM] Re: [PATCH] hppa64-hpux: Create dummy milli.a archives for binutils
  and ld testsuites [v2]'
headline: 'hppa64-hpux: Create dummy milli.a archives for binutils and ld testsuites
  [v2]'
tldr: Discussion of test failures related to missing milli.a archives for the hppa64-hpux
  target, and issues with section merging in relocatable links.
stakes: Ensuring testsuite passes for the hppa64-hpux target; proper handling of section
  merging impacts the correctness of linking.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Reverting the change that prevents .text section merging might fix the test failures,
  but could break other functionality.
- Modifying the linker script might provide a more targeted solution, but requires
  understanding of linker script syntax.
- Creating dummy milli.a archives is a workaround that allows the testsuite to pass,
  but doesn't address the underlying issue.
exchanges: []
primer_expert: The discussion highlights issues in the HPPA backend related to section
  merging and testsuite execution. The `lang_add_unique (".text")` call prevents merging
  of `.text` sections in relocatable links, impacting test results. The missing `milli.a`
  archive prevents some tests from executing at all. Resolution may involve modifying
  linker scripts or the HPPA backend's section handling.
primer_general: When building software, the linker combines different parts of the
  code into a final executable.  Linker scripts control how these parts are combined,
  including how sections of code (like the `.text` section containing the program's
  instructions) are merged. This discussion addresses problems with the linker's behavior
  when creating relocatable files (files that can be linked into other programs later)
  for the HPPA architecture on HP-UX. The core issues are missing libraries needed
  for testing and unexpected behavior related to how code sections are merged, leading
  to test failures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2604192116310.21647@angie.orcam.me.uk
bugzilla_url: null
date: '2026-04-19'
---

This discussion thread revolves around test failures for the hppa64-hpux target due to missing `milli.a` archives. It also touches on a related issue where `.text` sections are not being merged in relocatable links, causing further test failures.  The lack of section merging is attributed to a change in how the linker handles relocatable links for HPPA, potentially requiring adjustments to linker scripts or syntax.
