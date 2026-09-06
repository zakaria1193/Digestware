---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- testsuite
- debuginfod
commit_hash: 678e0116c60344c85c976d76e9b9f1dca16803fb
source_type: public_inbox
author: Sam James <sjames@sourceware.org>
headline: Fix debuginfod test cleanup to prevent test suite aborts
tldr: Test cleanup in debuginfod.exp now uses `catch` to prevent `exec kill` failures
  from aborting the entire test file.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The debuginfod test suite uses DejaGnu for test execution. When cleaning
  up the debuginfod server, the test suite previously used `exec kill -INT -[exp_pid]`.
  If this `kill` command returned a non-zero exit code, Tcl's `exec` would raise an
  error, causing DejaGnu to abort the test file. This commit wraps the `kill` commands
  in `catch` to prevent non-zero exit codes from propagating and aborting the test
  file.
primer_glossary:
- term: DejaGnu
  definition: A testing framework that provides a Tcl-based library for building and
    running tests, often used for GNU software.
- term: debuginfod
  definition: A server and client system for distributing debugging information, allowing
    developers to access symbols and other debugging data without needing the full
    source or build artifacts.
- term: Tcl
  definition: Tool Command Language, a scripting language commonly used for testing
    and embedded applications.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260905083534.C05474BB58DB@sourceware.org
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

This commit modifies the debuginfod test suite to use `catch` when executing `kill` commands for server cleanup. Previously, if the `kill` command failed (e.g., the server process had already exited), DejaGnu would abort the entire test file. This change ensures that only the specific test case fails, allowing subsequent tests to run.
