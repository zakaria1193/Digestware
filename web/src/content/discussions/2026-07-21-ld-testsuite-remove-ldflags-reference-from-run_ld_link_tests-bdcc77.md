---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- binutils
- ld
- testsuite
- regression
- patch
discussion_id: alpine.DEB.2.21.2607211442190.14485@angie.orcam.me.uk
source_type: public_inbox
title: '[PATCH] LD/testsuite: Remove $LDFLAGS reference from `run_ld_link_tests'''
headline: 'LD/testsuite: Remove $LDFLAGS reference from `run_ld_link_tests'''
tldr: Patch corrects ld testsuite to avoid double-inclusion of LDFLAGS.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 9
technical_tradeoffs:
- Correctness of test suite execution.
- Avoiding redundant linker flags.
exchanges:
- author: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
  role: proposer
  position: Submits a patch to fix the double-inclusion of LDFLAGS in ld testsuite
    invocations.
  quote: "Fix commit 24602a75d128 (\"ld: Append LDFLAGS to flags variable in \ndefault_ld_link\"\
    ) and prevent $LDFLAGS from being included twice in LD \ninvocations made via\
    \ `run_ld_link_tests', effectively reverting that \npart of commit 740341b9be65\
    \ (\"Provide dummy libraries for alpha-vms\")."
- author: John David Anglin <dave.anglin@bell.net>
  role: reviewer
  position: Acknowledges the patch and confirms no regressions were observed during
    testing.
  quote: Sorry for missing this.  I tested on hppa64-hp-hpux11.11 and saw no regressions.
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Approves the patch for merging.
  quote: Please apply.
primer_expert: This patch targets the `run_ld_link_tests` function within binutils'
  linker test suite. It corrects an issue where the `LDFLAGS` shell variable was being
  appended twice to the `ld` command line, stemming from a combination of commit `24602a75d128`
  and `740341b9be65`. The fix removes a global `LDF` variable reference and ensures
  `LDFLAGS` are correctly handled, preventing redundant flags in test invocations.
primer_glossary:
- term: LDFLAGS
  definition: A common environment variable used to pass flags to the linker during
    the build process.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or library.
- term: testsuite
  definition: A collection of tests designed to verify the correct functionality of
    a software package.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2607211442190.14485@angie.orcam.me.uk
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the binutils linker test suite where the LDFLAGS variable was inadvertently included twice in linker invocations. It corrects a mistake introduced by previous commits and ensures that LDFLAGS are applied only once, preventing regressions and aligning test output with expectations. Testing on hppa64-hp-hpux11.23 showed no regressions.
