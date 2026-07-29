---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- testing
- windows
- path length
discussion_id: c1be9231-af55-4293-979f-1c752c63df5c@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld: Skip pr33265-2 and pr33265-3 tests on Windows.'
headline: 'ld: Skip tests on Windows due to path length'
tldr: Two ld test cases (`pr33265-2` and `pr33265-3`) are skipped on Windows due to
  maximum path length limitations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Skipping tests on certain platforms reduces test suite noise but may hide platform-specific
  issues.
- Long path names can be problematic on Windows and require careful handling in test
  case design.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Acknowledged that two linker tests are expected to fail on Windows due
    to path length limits, agreeing to skip them.
  quote: Okay.
- author: Jan Dubiec <jdx@o2.pl>
  role: other
  position: Stated that tests `pr33265-2` and `pr33265-3` are expected to fail on
    Windows due to the default 260-character path length limit.
  quote: 'These test cases are expected to fail on Windows because by default maximum

    path length is only 260 characters.'
primer_expert: This brief exchange relates to test suite maintenance for the `ld`
  linker. Specifically, two tests (`pr33265-2` and `pr33265-3`) are identified as
  problematic on Windows platforms. The root cause is the Windows OS limitation on
  maximum file path lengths (typically 260 characters), which these test cases exceed.
  As a workaround, the tests are being conditionally skipped on Windows to prevent
  build failures in the test suite.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files into executables.
- term: test suite
  definition: A collection of tests designed to verify the correctness of software.
- term: path length limitation
  definition: A restriction on the maximum length of a file path that an operating
    system or filesystem can handle.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/c1be9231-af55-4293-979f-1c752c63df5c@suse.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This discussion confirms that specific linker test cases, `pr33265-2` and `pr33265-3`, are expected to fail on Windows. The reason for the failure is the operating system's default maximum path length limitation of 260 characters, which these tests exceed. Consequently, the tests are skipped on Windows.
