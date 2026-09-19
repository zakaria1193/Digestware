---
project: binutils
subsystem: binutils
patch_id: null
tags:
- strings
- testsuite
- binutils
discussion_id: 47260f4e-6024-436a-ac5a-458836df5bed@suse.com
source_type: public_inbox
title: 'Re: [PATCH] Add strings -f testcase'
headline: Add strings -f testcase
tldr: Adds a new test case for the `strings -f` option.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves test coverage for the `strings` utility.
- Minimal impact on existing functionality.
exchanges:
- author: pengxu
  role: proposer
  position: Submits a patch to add a test case for `strings -f`.
  quote: "--- \n binutils/testsuite/binutils-all/strings.exp | 17 +++++++++++++++++\n\
    \ 1 file changed, 17 insertions(+)"
- author: Jan Beulich
  role: reviewer
  position: Acknowledges and approves the submitted patch.
  quote: Okay.
primer_expert: This change adds a test case to the `binutils` test suite, specifically
  for the `strings -f` option. The `strings` utility is used to extract printable
  strings from binary files. The `-f` option likely relates to specifying a file or
  a format for string extraction, and this patch ensures its correct behavior is tested.
primer_glossary:
- term: strings utility
  definition: A command-line utility that scans an object file or executable and prints
    the printable character sequences that are at least a minimum length (defaulting
    to 4).
- term: test case
  definition: A specific set of conditions or variables under which a tester will
    determine whether a system under test satisfies requirements or works correctly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/47260f4e-6024-436a-ac5a-458836df5bed@suse.com
bugzilla_url: null
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

This patch introduces a new test case for the `strings -f` option in the `binutils` test suite. The change involves adding 17 lines of code to the `strings.exp` file to cover this specific functionality.
