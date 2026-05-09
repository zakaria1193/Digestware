---
project: binutils
subsystem: binutils
patch_id: null
tags:
- buildbot
- binutils
- gdb
- git
- failure
discussion_id: 20260508101800.301DB4BA2E27@sourceware.org
source_type: public_inbox
title: '☝ Buildbot (Sourceware): binutils-gdb - retry lost connection update (exception)
  (master)'
headline: '☝ Buildbot (Sourceware): binutils-gdb - retry lost connection update (exception)
  (master)'
tldr: The binutils-gdb buildbot on fedora-arm64 experienced a 'retry lost connection
  update (exception)' during git checkout.
proposer: builder@sourceware.org
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This message indicates a failure in the Sourceware buildbot infrastructure
  while building binutils-gdb. The failure occurred during the `git checkout` phase,
  suggesting a problem with accessing or updating the source code repository. This
  could be due to network issues, repository problems, or buildbot configuration errors.
primer_general: Buildbots are automated systems that compile and test software projects
  to ensure code quality and identify potential issues. This message reports an error
  that occurred during the build process for binutils-gdb, specifically during the
  step where the source code is retrieved from the Git repository. The error suggests
  a problem with the connection to the repository or the repository itself.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260508101800.301DB4BA2E27@sourceware.org
bugzilla_url: null
date: '2026-05-08'
---

The Sourceware buildbot for binutils-gdb on fedora-arm64 encountered a "retry lost connection update (exception)" during the `git checkout` step. The build is being retried. The blamelist includes Jan Beulich and Simon Marchi.
