---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- testsuite
- debuginfod
- regression
discussion_id: 87tso4drjo.fsf@gentoo.org
source_type: public_inbox
title: 'Re: [PATCH] binutils: don''t abort debuginfod.exp when the server cleanup
  kill fails'
headline: 'binutils: don''t abort debuginfod.exp when the server cleanup kill fails'
tldr: Fixes a testsuite issue where a failed kill command during debuginfod server
  cleanup caused the entire test file to abort instead of just failing the specific…
proposer: Sam James <sam@gentoo.org>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Masking underlying issues with `kill` success/failure in favor of test case continuity.
exchanges:
- author: Sam James <sam@gentoo.org>
  role: proposer
  position: Submits a patch to wrap `kill` commands in `catch` within the `debuginfod.exp`
    test script.
  quote: 'Wrap both kills in catch, matching the adjacent cleanup calls.  The

    FAIL is still reported; only the spurious abort goes away.'
- author: Matt Turner <mattst88@gmail.com>
  role: contributor
  position: Describes the problem where `exec kill` errors propagate and abort the
    test, explaining it happens when `debuginfod` fails to initialize and the cleanup
    path is taken.
  quote: "Both debuginfod.exp cleanup paths call\n\n  exec kill -INT -[exp_pid]\n\n\
    uncaught, unlike the catch{}-wrapped close/wait that immediately\nfollows.  Tcl's\
    \ exec raises an error when the child exits non-zero, so\nif the kill fails the\
    \ error propagates out of the testcase and DejaGnu\naborts the whole file:\n\n\
    \  ERROR: tcl error sourcing .../debuginfod.exp.\n  ERROR: tcl error code CHILDSTATUS\
    \ 76409 1\n  ERROR…"
primer_expert: This discussion addresses a flaw in the binutils testsuite's `debuginfod.exp`
  script. When the `debuginfod` server fails to start and its cleanup process involves
  killing the server's process, an uncaught exception from the `exec kill` command
  can cause DejaGnu to abort the entire test file. This patch ensures that the `kill`
  command is handled within a `catch` block, preventing the test runner from aborting
  prematurely and allowing other tests to execute.
primer_glossary:
- term: debuginfod
  definition: A server that provides debugging information (like DWARF symbols) over
    the network, used to speed up debugging processes.
- term: dejagnu
  definition: A testing framework used for testing compilers and other tools, which
    relies on Tcl scripting for test case definition and execution.
- term: Tcl
  definition: Tool Command Language, a dynamic scripting language often used for building
    GUIs and test harnesses for software development tools.
- term: UNRESOLVED
  definition: A test result status in DejaGnu indicating that a test case was aborted
    due to an error, preventing its completion.
- term: FAIL
  definition: A test result status in DejaGnu indicating that a test case executed
    but did not produce the expected outcome.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/87tso4drjo.fsf@gentoo.org
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

A patch addresses a bug in the binutils testsuite where a non-zero exit code from the `kill` command during debuginfod server cleanup would cause the DejaGnu test framework to abort the entire test file. This prevented subsequent tests from running. The fix wraps the `kill` commands in `catch` to prevent this spurious abort, allowing the test to report a failure but continue execution.
