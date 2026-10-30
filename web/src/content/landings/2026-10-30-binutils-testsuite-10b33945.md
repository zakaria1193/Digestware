---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- binutils
- strings
- testsuite
- regression
commit_hash: 10b339451bf55dcd9a0a631bc71925a4223fb8b1
source_type: public_inbox
author: pengxu <pengxu@kylinos.cn>
headline: Add test case for strings -t option
tldr: New test case validates the `strings -t` option for displaying string locations
  in various bases.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces a new test case, `strings-location.d` and `strings.exp`,
  to the binutils testsuite. The test specifically targets the `-t` option of the
  `strings` utility, which outputs the offset of found strings. The test verifies
  that the offset is correctly reported in different bases (e.g., octal, decimal,
  hexadecimal), ensuring the `strings` utility adheres to its specified behavior for
  reporting string locations.
primer_glossary:
- term: strings utility
  definition: A command-line program that displays the printable character sequences
    from files. It is often used to extract human-readable strings from binary files.
- term: offset
  definition: A numerical value representing the distance in bytes from the beginning
    of a file or memory region to a specific location.
- term: test suite
  definition: A collection of test cases used to verify the correctness of a software
    program or library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261030072519.85C704BA900B@sourceware.org
date: '2026-10-30'
is_stub: true
stub_reason: low_score
---

A new test case has been added to verify the functionality of the `strings` utility's `-t` option. This option is used to display the location of strings within a file, and the test covers different base formats (e.g., octal) for these locations. The addition improves test coverage for the `strings` command.
