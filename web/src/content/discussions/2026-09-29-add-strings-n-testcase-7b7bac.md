---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- strings
- testsuite
- patch
discussion_id: 20260929065048.445169-1-pengxu@kylinos.cn
source_type: public_inbox
title: '[PATCH] Add strings -n testcase '
headline: Add strings -n testcase
tldr: Adds a test case for the binutils 'strings -n' option.
proposer: pengxu@kylinos.cn
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 7
technical_tradeoffs: []
exchanges:
- author: pengxu@kylinos.cn
  role: proposer
  position: Submits a patch adding test cases for the 'strings -n' option, which limits
    symbol length, to binutils.
  quote: This patch adds test cases for the strings -n option in binutils-all/strings.exp.
    The -n option is used to limit the length of displayed symbols, which is default
    4.
- author: Jan Beulich
  role: reviewer
  position: Requests that commit messages include a non-empty description, particularly
    when the subject line is terse.
  quote: Please can we have a non-empty description at least in cases where the subject
    ...
primer_expert: This patch introduces a test case for the `strings` utility in GNU
  Binutils, specifically targeting the `-n` option which controls the maximum length
  of symbols displayed. The addition aims to ensure the correct behavior of this option
  across various string formats and symbol types.
primer_glossary:
- term: strings utility
  definition: A standard Unix utility that scans objects files or (other types of
    files) and prints the printable character sequences that are at least 4 characters
    long (by default).
- term: binutils-all/strings.exp
  definition: A test script file within the Binutils testsuite that specifically exercises
    the 'strings' command.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260929065048.445169-1-pengxu@kylinos.cn
bugzilla_url: null
date: '2026-09-29'
is_stub: false
stub_reason: ''
---

Pengxu submits a patch to add a test case for the `strings -n` option in binutils. This option limits the length of displayed symbols. The patch adds a new test to `binutils-all/strings.exp` and has been verified to pass on the local build.
