---
project: binutils
subsystem: gas/testsuite
patch_id: null
tags:
- gas
- testsuite
- Windows
- regression
commit_hash: 63f5af1fe20bb56c4bd798abd62667af8eff9561
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: 'gas/testsuite: Fix multibyte3 test cases on Windows'
tldr: Corrects regular expressions in gas testsuite to pass on Windows.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `multibyte3.l` test case in `gas/testsuite/gas/all/` uses `run_list_test`
  and had incorrect regular expressions that caused failures on Windows. This commit
  modifies the regex to align with how `run_list_test` processes output, specifically
  addressing the start-of-line matching behavior difference from `run_dump_test`.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the binutils package. It translates assembly
    language into machine code.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component or system.
- term: multibyte character
  definition: A character represented by more than one byte in a character encoding,
    commonly used for non-ASCII characters.
- term: regular expression
  definition: A sequence of characters that defines a search pattern, used for matching
    character combinations in strings.
- term: run_list_test
  definition: A test runner utility within the binutils testsuite, likely used for
    specific types of output verification.
- term: run_dump_test
  definition: Another test runner utility within the binutils testsuite, potentially
    differing in how it interprets or processes test output compared to run_list_test.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260911120146.6525040AC6E8@sourceware.org
date: '2026-09-11'
is_stub: true
stub_reason: low_score
---

The gas testsuite's `multibyte3.l` file has been updated to fix issues on Windows. The regular expressions were modified to correctly match expected output when the test is run using `run_list_test`, ensuring consistent test results across platforms.
