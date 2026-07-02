---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- buildbot
- test failure
discussion_id: 20260502091657.1E8634A9E063@sourceware.org
source_type: public_inbox
title: '☠ Buildbot (Sourceware): binutils-gdb - failed test (failure) (master)'
headline: 'Buildbot (Sourceware): binutils-gdb - failed test (failure) (master).'
tldr: The binutils-gdb build on binutils-debian-amd64 (master) failed a test.
proposer: builder@sourceware.org
consensus: NACK'd
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Buildbot reports the status of the binutils-gdb build. Details include
  the revision number and links to logs for each step. A failed test indicates a regression
  and needs investigation.
primer_general: Buildbots automate building/testing software. A failed test means
  code changes introduced an issue. The logs need to be analyzed to identify the cause
  and restore functionality.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260502091657.1E8634A9E063@sourceware.org
bugzilla_url: null
date: '2026-05-02'
is_stub: true
---

The buildbot reports a failed test for binutils-gdb on the binutils-debian-amd64 builder, triggered by commit 65cd0d66a647f14719e69bd19f34dc98bdb7e635. The `make check` step resulted in a failure.  The logs should be reviewed to determine the cause of the test failure and address the underlying issue. This failure blocks further integration.
