---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- testsuite
- strings
commit_hash: 5e7a2992024c2918023f2dd64362bf6aaadcef6d
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: Add test case for strings -f option
tldr: New test verifies `strings -f` prints the filename prefix.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: A new test case is added to binutils/testsuite/binutils-all/strings.exp
  to specifically exercise the `strings -f` option. This option is intended to prepend
  the filename to each extracted string. The test checks that the output format matches
  the expected pattern, including the filename prefix.
primer_glossary:
- term: strings
  definition: A command-line utility that displays printable strings from binary files.
- term: -f option
  definition: An option for the 'strings' command that causes it to print the filename
    prefix before each string it finds.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260925121742.219184BB3BE6@sourceware.org
date: '2026-09-25'
is_stub: true
stub_reason: low_score
---

A new test case has been added to the `strings` utility's test suite. This test specifically verifies that the `-f` option correctly prints the filename prefix before each string found in the input file.
