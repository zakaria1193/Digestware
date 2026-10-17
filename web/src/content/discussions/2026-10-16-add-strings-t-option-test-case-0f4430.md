---
project: binutils
subsystem: binutils
patch_id: null
tags:
- strings
- testsuite
- binutils
- regression-testing
discussion_id: af6eebcd-f1d6-4320-a217-1f861556690e@suse.com
source_type: public_inbox
title: 'Re: [PATCH] Add strings -t option test case'
headline: Add strings -t option test case
tldr: Reviewer suggests minor tidying for a new test case for the `strings -t` option.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Adds a test case to improve confidence in the `strings -t` option's functionality.
- Minor code style adjustments requested for consistency with existing code.
exchanges:
- author: pengxu
  role: proposer
  position: Submitted a patch to add a test case for the `strings -t` option.
  quote: 'This patch adds strings -t test case , which is used to show related

    location information.

    For example , the command "strings -t o"  prints the location of the string in
    base 8.


    Signed-off-by: pengxu <pengxu@kylinos.cn>'
- author: Jan Beulich
  role: reviewer
  position: Approves the patch but requests minor tidying, aligning it with previous
    adjustments made to the author's other contributions.
  quote: 'This is okay, albeit preferably with a little bit of tidying (along the

    lines of what I did with your earlier patch).'
primer_expert: This discussion concerns a new test case for the `strings` utility
  within binutils. The `strings` command extracts printable strings from object files.
  The `-t` option specifies the output format for the string's offset (e.g., octal,
  decimal, hexadecimal). The submitted patch adds a test to ensure this functionality
  works correctly. A reviewer has accepted the patch conceptually but requests minor
  code style adjustments.
primer_glossary:
- term: strings utility
  definition: A command-line program that scans an object file or executable and extracts
    sequences of printable characters, often used to find embedded messages or configuration
    strings.
- term: test case
  definition: A set of conditions or inputs used to verify that a specific feature
    or functionality of a program works as expected. In software development, test
    cases are crucial for regression testing and ensuring code quality.
- term: offset
  definition: The position of a string or data within a file, usually measured in
    bytes from the beginning of the file or a specific section.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/af6eebcd-f1d6-4320-a217-1f861556690e@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

A patch was submitted to add a test case for the `strings -t` option, which displays the location of strings in various formats (like octal). The reviewer finds the patch acceptable but suggests minor tidying, similar to adjustments made on a previous patch from the same author. This indicates a minor refinement is needed before the test case can be fully integrated.
