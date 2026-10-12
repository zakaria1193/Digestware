---
project: binutils
subsystem: binutils
patch_id: null
tags:
- strings
- testing
- binutils
discussion_id: 20261008021533.251211-1-pengxu@kylinos.cn
source_type: public_inbox
title: '[PATCH v4] Add strings -n option test case'
headline: Add strings -n option test case
tldr: Adds test cases for the `strings -n` option and support for it in binutils-common.exp.
proposer: pengxu@kylinos.cn
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Improves test coverage for the `strings` utility.
- Requires careful configuration for different target architectures.
exchanges:
- author: pengxu@kylinos.cn
  role: proposer
  position: Submits a patch to add test cases for the `strings -n` option, including
    adjustments for specific targets.
  quote: 'This patch adds strings -n test case, including n=4(default),5 and 7.

    For example , when n = 5, the "strings -n" result only show symbols whose length
    >= 5.

    At the same time ,add "strings" command support in binutils-common.exp.'
- author: Jan Beulich <jbeulich@suse.com>
  role: contributor
  position: Notes that the patch has already been committed after necessary modifications,
    implying the proposer's updates might be redundant or confirming prior work.
  quote: 'You realize though that I''ve already committed that patch of yours after

    making said changes?'
primer_expert: This patch adds test cases to `binutils/testsuite/binutils-all/` for
  the `strings` utility, specifically targeting the `-n` option which controls the
  minimum length of displayed strings. It also enhances `binutils/testsuite/binutils-common.exp`
  to include support for the `strings` command. The proposer has also made adjustments
  for `mmix`, `tic4x-coff`, and `tic64x-coff` targets to ensure test stability, marking
  some as expected failures.
primer_glossary:
- term: strings
  definition: A command-line utility that displays printable characters in files.
- term: test case
  definition: A set of conditions or variables under which a system or component is
    tested to see whether it behaves as expected.
- term: binutils-common.exp
  definition: A common test script file used by the GNU Binutils test suite, likely
    containing general setup and utility functions for various tests.
- term: XFAIL
  definition: In testing, denotes an 'expected failure', meaning a test is known to
    fail and this is acceptable under certain conditions or for specific targets.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261008021533.251211-1-pengxu@kylinos.cn
bugzilla_url: null
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

This patch introduces test cases for the `strings -n` command-line option, which filters strings based on a minimum length. It specifically adds tests for `n=4` (default), `n=5`, and `n=7`. Additionally, the patch ensures that the `strings` command is supported within the `binutils-common.exp` test suite. The author also notes that specific target configurations (mmix, tic4x-coff, tic64x-coff) have been adjusted to handle expected failures or pass correctly.
