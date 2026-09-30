---
project: binutils
subsystem: binutils
patch_id: null
tags:
- strings
- testsuite
- binutils
discussion_id: 3da15824-06d2-4398-8733-b315fd9f78bf@suse.com
source_type: public_inbox
title: '[PATCH] Add strings -n option test case'
headline: Add strings -n option test case
tldr: Adds test cases for the `strings -n` option, improving test coverage for string
  length filtering.
proposer: pengxu@kylinos.cn
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 7
technical_tradeoffs: []
exchanges:
- author: pengxu@kylinos.cn
  role: proposer
  position: Submits a patch to add test cases for the `strings -n` option.
  quote: 'This patch adds strings -n test case, including n=4(default),5 and 7.

    For example , when n = 5, the "strings -n" result only show symbols whose length
    >= 5.

    At the same time ,add "strings" command support in binutils-common.exp.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Requests that new patch versions be submitted as distinct threads for
    clearer version tracking.
  quote: 'Also, please sen new versions as distinct new threads, not as replies

    to earlier versions. See how the versioning isn''t possible to determine

    at https://sourceware.org/pipermail/binutils/2026-September/thread.html.

    The sole thing tagged V2 is _not_ this new patch version.'
- author: pengxu@kylinos.cn
  role: proposer
  position: Provides an update to the patch, clarifying its purpose and changes.
  quote: 'I have updated the patch:

    1.Add some description for this patch

    2.Correct changed files list

    3.This case is for "string -n", I used "string -d -n" to avoid non-data

    symbols, only show data symbols

    4.Change dirctives format

    5.I used loop to test 3 cases

    6.Correct STRINGS in binutils-common.exp'
primer_expert: This patch adds comprehensive test cases for the `strings -n` option,
  ensuring that the minimum string length filtering functionality works correctly.
  It covers default behavior and custom length specifications, and integrates the
  `strings` command into the `binutils-common.exp` test harness for improved test
  suite management.
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
url: https://inbox.sourceware.org/binutils/20260929085421.654372-1-pengxu@kylinos.cn
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

This patch introduces test cases for the `strings -n` option, which allows users to specify a minimum string length for output. It includes tests for the default length (n=4) and custom lengths (n=5, n=7), verifying that the command correctly filters strings based on their length. The patch also integrates support for the `strings` command into the `binutils-common.exp` test suite.
