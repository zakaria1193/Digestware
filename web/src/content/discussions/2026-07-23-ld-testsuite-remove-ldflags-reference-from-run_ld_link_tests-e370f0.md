---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- binutils
- linker
- testsuite
- regression
- LDFLAGS
discussion_id: alpine.DEB.2.21.2607232004200.14485@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH] LD/testsuite: Remove $LDFLAGS reference from `run_ld_link_tests'''
headline: 'LD/testsuite: Remove $LDFLAGS reference from `run_ld_link_tests'''
tldr: Patch removes $LDFLAGS from linker test suite invocations, correcting a regression
  that caused flags to be duplicated.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- 'Test Correctness: Ensuring the test suite accurately reflects linker behavior without
  unintended side effects from its own configuration.'
- 'Regression Fix: Reverting an undesirable side effect of a previous commit to maintain
  expected functionality.'
- 'Cross-Target Consistency: Maintaining correct test behavior across various architecture
  targets.'
exchanges:
- author: Maciej W. Rozycki
  role: proposer
  position: Submits a patch to remove `$LDFLAGS` from `run_ld_link_tests` to fix a
    duplication bug, and has applied it after positive review.
  quote: "Fix commit 24602a75d128 (\"ld: Append LDFLAGS to flags variable in \ndefault_ld_link\"\
    ) and prevent $LDFLAGS from being included twice in LD \ninvocations made via\
    \ `run_ld_link_tests', effectively reverting that \npart of commit 740341b9be65\
    \ (\"Provide dummy libraries for alpha-vms\").\n\nI have pushed this change now,\
    \ thank you for your review."
- author: John David Anglin
  role: reviewer
  position: Apologizes for a missed aspect of the change during review, confirming
    no regressions on hppa64-hp-hpux11.11.
  quote: "Sorry for missing this. I tested on hppa64-hp-hpux11.11 and saw no \nregressions."
- author: Alan Modra
  role: reviewer
  position: Requests the patch be applied.
  quote: null
primer_expert: This patch cleans up the binutils linker test suite by removing an
  erroneous reference to `$LDFLAGS` in the `run_ld_link_tests` script. A previous
  commit intended to set default linker flags but inadvertently caused `$LDFLAGS`
  to be appended twice to test invocations. This change reverts that specific behavior,
  addressing potential test inaccuracies and ensuring consistency across different
  target architectures. The issue was validated on hppa64-hp-hpux.
primer_glossary:
- term: LD
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or another object file.
- term: testsuite
  definition: A collection of automated tests designed to verify the correct functionality
    of a software system, in this case, the binutils linker.
- term: LDFLAGS
  definition: An environment variable commonly used to pass options to the linker
    during the build process.
- term: regression
  definition: The reintroduction of a bug or defect in a software system that was
    previously fixed, or the introduction of a new bug caused by a change.
- term: AR
  definition: The GNU archiver, used to combine multiple object files into a single
    archive file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2607232004200.14485@angie.orcam.me.uk
bugzilla_url: null
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

This discussion confirms and accepts a patch that removes the `$LDFLAGS` variable reference from the `run_ld_link_tests` function in binutils' testsuite. This corrects a regression introduced by a previous commit (740341b9be65) which caused link flags to be unintentionally duplicated, affecting tests on specific architectures like hppa64-hp-hpux. The change ensures test suite consistency and correctness.
