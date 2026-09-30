---
project: binutils
subsystem: binutils
patch_id: null
tags:
- strings
- testsuite
- binutils
discussion_id: 20260929095225.773309-1-pengxu@kylinos.cn
source_type: public_inbox
title: '[PATCH v3] Add strings -n option test case'
headline: Add strings -n option test case
tldr: Adds test cases for the `strings -n` option to verify minimum string length
  filtering.
proposer: pengxu@kylinos.cn
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: pengxu@kylinos.cn
  role: proposer
  position: Submits a v3 patch series to add test cases for the `strings -n` option.
  quote: 'This patch adds strings -n test case, including n=4(default),5 and 7.

    For example , when n = 5, the "strings -n" result only show symbols whose length
    >= 5.

    At the same time ,add "strings" command support in binutils-common.exp.'
primer_expert: This patch adds test cases to the `strings` command's test suite to
  cover the `-n` option, which filters strings based on a minimum length. The tests
  include default behavior (n=4) and specific values like n=5 and n=7, ensuring that
  the length filtering works as expected. It also integrates the `strings` command
  into the `binutils-common.exp` framework for broader test coverage.
primer_glossary:
- term: strings command
  definition: A Unix utility that scans an object file or executable and prints the
    printable character sequences that are at least a certain length. It's useful
    for finding embedded text strings in binary files.
- term: test case
  definition: A set of conditions or variables under which a tester will determine
    whether a system under test satisfies requirements or works correctly. In this
    context, it involves input files and expected output for the `strings` command.
- term: binutils-common.exp
  definition: A file in the binutils test suite that likely contains common setup
    or utility functions used by multiple test scripts, ensuring consistency across
    different parts of the test suite.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260929095225.773309-1-pengxu@kylinos.cn
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch introduces new test cases for the `strings` command's `-n` option, which specifies the minimum length of strings to be displayed. The tests cover the default length (n=4), as well as n=5 and n=7. Additionally, the patch ensures that the `strings` command itself is supported within the `binutils-common.exp` test suite, allowing for comprehensive testing of this functionality.
