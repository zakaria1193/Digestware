---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- binutils
- testing
- debuginfod
- bugfix
commit_hash: 53d5835004594105265fd4657bb69c5943588af3
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'binutils: Prevent test suite abort on debuginfod cleanup failure'
tldr: Test suite no longer aborts when debuginfod server cleanup fails.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `debuginfod.exp` test suite file contains cleanup paths that execute
  `exec kill -INT -[exp_pid]` without error handling. When the `kill` command fails
  (e.g., exits non-zero), Tcl's `exec` raises an error, causing DejaGnu to abort the
  test file. This commit wraps the `kill` calls in `catch` blocks within `debuginfod.exp`
  to prevent test file abortion due to non-zero exit statuses from `kill`, ensuring
  that subsequent tests can still run and that failures are reported correctly.
primer_glossary:
- term: debuginfod
  definition: A server that provides debugging information files to clients, allowing
    for faster debugging of applications without needing local debug symbols.
- term: test suite
  definition: A collection of automated tests designed to verify the correct functionality
    of a software project.
- term: Tcl
  definition: Tool Command Language. A dynamic programming language often used for
    scripting, testing, and rapid prototyping, particularly within the GNU toolchain.
- term: DejaGnu
  definition: A testing framework that provides a consistent environment for testing
    all kinds of programs, regardless of the language they are written in or the platform
    they are running on.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261111024127.2436D4BA2E14@sourceware.org
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

Previously, the binutils test suite could abort entirely if the cleanup process for the `debuginfod` server encountered an error. This was because Tcl's `exec` command would raise an error, halting the test run and causing subsequent tests to be skipped. This change wraps the kill commands in a `catch` block, allowing the test to fail gracefully without aborting the entire test file.
