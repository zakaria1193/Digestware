---
project: binutils
subsystem: binutils/tests
patch_id: null
tags:
- binutils
- strings
- test
- regression
commit_hash: e1a3a5f0b8774dc6bbe177972819efba9d247b57
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: Add strings -n option test case
tldr: Binutils test suite gains tests for the `strings -n` option with various minimum
  lengths.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The binutils test suite is expanded with new `.d` and `.s` files to
  specifically test the functionality of the `strings -n <length>` option. These tests
  ensure that the `strings` utility correctly identifies and outputs only those symbol
  strings that meet or exceed the specified minimum length, including default behavior.
primer_glossary:
- term: strings utility
  definition: A standard Unix utility that scans an object file or text file and extracts
    printable character sequences that are at least a certain length.
- term: Test suite
  definition: A collection of tests designed to verify the correctness and functionality
    of a software project.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261005091655.48FA04BA23E0@sourceware.org
date: '2026-10-05'
is_stub: true
stub_reason: low_score
---

This commit adds new test cases to the binutils test suite for the `strings` command's `-n` option. The tests cover default minimum length (4), and explicit lengths of 5 and 7, verifying that the command correctly filters strings based on the specified minimum length.
