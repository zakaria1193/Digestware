---
project: binutils
subsystem: binutils
patch_id: null
tags:
- buildbot
- binutils
- gdb
- compilation failure
- arm64
discussion_id: 20260501215622.969EC43B5538@sourceware.org
source_type: public_inbox
title: '☠ Buildbot (Sourceware): binutils-gdb - failed compile (failure) (master)'
headline: '☠ Buildbot (Sourceware): binutils-gdb - failed compile (failure) (master)'
tldr: Buildbot reports a failed compilation of binutils-gdb on fedora-arm64.
proposer: builder@sourceware.org
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This is a report from the Sourceware buildbot, which continuously builds
  and tests binutils-gdb on various platforms. A failed compile indicates a regression
  in the master branch that needs to be investigated.
primer_general: Buildbots are automated systems that compile and test software projects.
  They are used to detect integration issues early in the development process. This
  report indicates that a recent change to binutils-gdb caused a compilation failure
  on a specific platform (fedora-arm64).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260501215622.969EC43B5538@sourceware.org
bugzilla_url: null
date: '2026-05-01'
---

The Sourceware buildbot detected a failed compilation of binutils-gdb on the binutils-fedora-arm64 builder. The failure occurred during the make stage, after successfully completing the checkout, rm, and configure stages. Full logs are available on the buildbot website.
