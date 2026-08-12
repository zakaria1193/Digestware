---
project: binutils
subsystem: binutils
patch_id: null
tags:
- testing
- binutils
- debuginfod
- testsuite
- regression
discussion_id: 20260812013330.3990977-1-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH] binutils: don''t abort debuginfod.exp when the server cleanup kill
  fails'
headline: 'binutils: don''t abort debuginfod.exp when the server cleanup kill fails'
tldr: 'Testsuite: Wrap `kill` commands in `catch` within debuginfod.exp to prevent
  test aborts on cleanup failure.'
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Matt Turner
  role: proposer
  position: Submits a patch to wrap `kill` commands in `catch` within `debuginfod.exp`,
    preventing test aborts when cleanup fails.
  quote: 'Wrap both kills in catch, matching the adjacent cleanup calls. The

    FAIL is still reported; only the spurious abort goes away.'
primer_expert: This patch addresses a robustness issue in the DejaGnu testsuite for
  Binutils, specifically within the `debuginfod.exp` test file. When the `kill` command
  used to clean up the `debuginfod` server process fails (e.g., due to the process
  already having exited), Tcl's `exec` command raises an error. This error propagates
  and causes DejaGnu to abort the test file, preventing subsequent tests from running.
  The fix involves using `catch` around the `exec kill` calls to suppress these errors
  and allow the test suite to continue.
primer_glossary:
- term: debuginfod.exp
  definition: A DejaGnu test script used to verify the functionality of debuginfod,
    a server that provides debugging information.
- term: DejaGnu
  definition: A testing framework that provides support for testing procedures and
    harnesses.
- term: HTTP error 429
  definition: A Too Many Requests error, indicating that the server has received too
    many requests from the client and is rate-limiting the connection.
- term: Tcl
  definition: Tool Command Language. A dynamic programming language often used for
    scripting, rapid prototyping, and testing.
- term: exec
  definition: A Tcl command that executes an external program.
- term: catch
  definition: A Tcl command that executes a script and catches any errors that occur.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260812013330.3990977-1-mattst88@gmail.com
bugzilla_url: null
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

Matt Turner proposes a fix for the binutils testsuite where testcases involving `debuginfod.exp` abort unexpectedly due to `exec kill` commands failing. This patch wraps the `kill` commands in a `catch` block, preventing the DejaGnu test runner from aborting the entire test file when the server cleanup process encounters an error. It also addresses a similar issue in the port-scan timeout path.
