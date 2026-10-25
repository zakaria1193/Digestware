---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- DejaGnu
- pytest
commit_hash: f9c223ae1f57321fbc87722d8cd35ec484739037
source_type: github
author: David Malcolm
headline: 'Testsuite: Fix pytest output parsing in DejaGnu'
tldr: Corrects regexps in DejaGnu test framework to prevent dropping the last character
  of pytest test names.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Several DejaGnu test framework helper procedures (`run-gcov-pytest`,
  `run-sarif-pytest`, `run-html-pytest`) used incorrect regular expressions to parse
  pytest output. Specifically, the pattern `($prefix)[^\r\n]+\r\n` was used to capture
  output, where `$prefix` is a greedy pattern matching any non-line-ending characters.
  The `[^\r\n]+` part following `$prefix` was redundant and caused the last character
  of the test name to be omitted. This patch removes that redundant pattern, ensuring
  the entire test name is captured correctly.
primer_glossary:
- term: DejaGnu
  definition: A testing framework that provides a Tcl-based library for building,
    managing, and running tests. It is commonly used for testing compilers and other
    development tools.
- term: pytest
  definition: A popular Python testing framework that makes it easy to write simple
    to complex tests, supporting TDD, BDD, TPG, and native plugins.
- term: regular expression
  definition: A sequence of characters that defines a search pattern, used for pattern
    matching with strings.
- term: Tcl
  definition: Tool Command Language, a dynamic programming language that is highly
    extensible and commonly used for scripting, GUI development, and testing.
- term: GCC testsuite
  definition: The collection of tests used to verify the correctness and functionality
    of the GNU Compiler Collection (GCC).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f9c223ae1f57321fbc87722d8cd35ec484739037
date: '2026-10-24'
is_stub: true
stub_reason: low_score
---

This commit fixes an issue in the DejaGnu test framework where the last character of pytest test function names was being dropped from output logs. The problem stemmed from overly greedy regular expressions used in test result parsing scripts (e.g., `run-gcov-pytest`, `run-sarif-pytest`). These regexps incorrectly captured parts of the test name, omitting the final character. By removing an extraneous non-newline pattern from these regexps, the test names are now captured completely, ensuring accurate test reporting.
