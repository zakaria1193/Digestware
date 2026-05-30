---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- linker
- testing
- remote
- testsuite
discussion_id: 20260529135252.2094804-1-chigot@adacore.com
source_type: public_inbox
title: '[PATCH] ld/testsuite: add support for remote testing in ld-cdtest'
headline: ld-cdtest Supports Remote Testing
tldr: The ld-cdtest testsuite now supports remote testing by using remote_load and
  regexp_diff.
proposer: Clément Chigot <chigot@adacore.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Using regexp_diff may make the tests more brittle to minor output changes.
- Remote testing adds complexity to the test setup, but improves coverage.
exchanges: []
primer_expert: This patch modifies the linker's `cdtest` testsuite to enable execution
  on remote targets.  The core change involves using `remote_load` instead of relying
  on native execution. The testsuite compares the output of the linker against expected
  results; this patch updates the diffing mechanism to use regular expressions (`regexp_diff`)
  for more robust comparisons, especially when dealing with remote execution environments.
primer_general: This patch improves the testing process for the `ld` (linker) program
  within the Binutils project.  It allows the tests to be run not only on the machine
  where the code is being developed (native), but also on other machines or simulated
  environments (remote).  This is achieved by using a tool called `remote_load` to
  execute the tests remotely and using regular expressions to compare the results,
  ensuring that the tests are accurate even when run in different environments.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260529135252.2094804-1-chigot@adacore.com
bugzilla_url: null
date: '2026-05-29'
is_stub: false
---

The ld-cdtest testsuite is updated to use `remote_load`, allowing execution on both native and remote targets. The diff between the output and expected result is transformed to the usual `regexp_diff` format. This avoids issues with newline variations that arose when using `remote_exec build diff`.
