---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- testsuite
- windows
- bugfix
commit_hash: 02ae79131475402a83bfdd0794cf23ea4c3868a0
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: Fix addr2line test cases on Windows
tldr: Addr2line test cases now pass on Windows, resolving path and symbol issues.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The binutils test suite's `addr2line` tests failed on Windows due to
  discrepancies in path formatting between the test suite's UNIX-style paths and Windows
  `nm`'s DOS-style paths. Additionally, targets like H8/300 that prefix symbols with
  an underscore required special handling. This patch normalizes paths and accounts
  for symbol mangling to ensure test stability.
primer_glossary:
- term: addr2line
  definition: A command-line utility that translates object code addresses into line
    numbers and function names, aiding in debugging.
- term: nm
  definition: A command-line utility that lists symbols from object files.
- term: H8/300
  definition: A specific microcontroller architecture for which binutils provides
    support.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260925121752.55A5D4BB3BAA@sourceware.org
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

Two test cases for `addr2line` were failing on Windows. This commit resolves issues with Windows path formats used by `nm` and the handling of prefixed symbol names by GCC on certain targets. The test suite now correctly accounts for these platform-specific behaviors.
