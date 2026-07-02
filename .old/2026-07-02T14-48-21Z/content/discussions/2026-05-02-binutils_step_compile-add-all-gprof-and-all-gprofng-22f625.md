---
project: binutils
subsystem: binutils_step_compile
patch_id: null
tags:
- binutils
- gprof
- build system
- buildbot
discussion_id: 20260502152257.2758088-1-mark@klomp.org
source_type: public_inbox
title: '[COMMITTED] binutils_step_compile: Add all-gprof and all-gprofng'
headline: 'Binutils_step_compile: Add all-gprof and all-gprofng.'
tldr: The build system now builds gprof in binutils_step_compile to avoid check failures
  in binutils_step_check.
proposer: Mark Wielaard <mark@klomp.org>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Building gprof in the standard compile step increases the build time slightly.
- The change simplifies the build configuration by ensuring that gprof is always available
  for testing.
- The gprofng target remains a no-op on non-Linux systems, minimizing the impact on
  other platforms.
exchanges:
- author: Mark Wielaard <mark@klomp.org>
  role: proposer
  position: Proposes to modify the binutils build configuration to build `gprof` in
    `binutils_step_compile` to avoid check failures.
  quote: 'make check-gprof was added to binutils_step_check, but only build for

    binutils_step_compile_minimal. While binutils_step_check_minimal does

    check gprof. Switch things around so that binutils_step_compile does

    also build gprog so binutils_step_check doesn''t fail because gprof

    isn''t build.'
primer_expert: '`binutils_step_compile` and `binutils_step_check` are steps in the
  buildbot configuration for building and testing binutils.  This change ensures that
  the `gprof` and `gprofng` build targets are included in the main compile step, rather
  than only in the minimal compile step. The `all-gprofng` target is a no-op on non-Linux
  systems.'
primer_general: Build systems automate the process of compiling and linking software.
  Binutils uses a build system with separate steps for compiling and checking.  `gprof`
  is a profiling tool, and this change makes sure that it's built as part of the standard
  compile step. By building `gprof` during the compile step, the check step can run
  tests that depend on `gprof` without failing.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260502152257.2758088-1-mark@klomp.org
bugzilla_url: null
date: '2026-05-02'
---

The build system's configuration is updated so that `binutils_step_compile` now builds `gprof` and `gprofng`. Previously, `make check-gprof` was added to `binutils_step_check`, but `gprof` was only built for `binutils_step_compile_minimal`. This change ensures that `gprof` is built before the checks are run, preventing failures due to missing binaries.
