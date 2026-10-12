---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- linker
- testing
- cross-compilation
discussion_id: 20261006105101.5720-1-evgeny.karpov@arm.com
source_type: public_inbox
title: '[PATCH v1] aarch64: Expect failures for some tests'
headline: 'aarch64: Expect failures for some tests'
tldr: Marks specific aarch64 PE tests as expected failures because dlltool is not
  built for that target.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Correctly identifies and marks expected test failures.
- Prevents spurious test failures due to toolchain limitations.
exchanges:
- author: Evgeny Karpov <evgeny.karpov@arm.com>
  role: proposer
  position: Submits a patch to mark specific aarch64 PE tests as expected failures
    due to the unavailability of `dlltool`.
  quote: 'Fix the regression in the test configuration for aarch64-*-pe* in

    0bb9902441e417fd43836b0b0fe9466080bb7c43.

    dlltool is not built for that target, and failures are expected for some tests.'
primer_expert: This patch modifies `ld/testsuite/ld-pe/pe.exp` to introduce `XFAIL`
  conditions for `aarch64-*-pe*` targets. This is in response to a regression introduced
  by commit `0bb9902441e417fd43836b0b0fe9466080bb7c43`. The `dlltool` utility, which
  is used in some PE test cases, is not available for the `aarch64-*-pe*` cross-compilation
  targets, hence the need to mark these specific tests as expected failures.
primer_glossary:
- term: aarch64
  definition: A 64-bit ARM architecture, a widely used processor architecture.
- term: PE
  definition: Portable Executable, a file format used for executables and object files
    on Windows systems. Binutils supports building PE targets for cross-compilation.
- term: dlltool
  definition: A utility that creates import libraries for Windows DLLs, used by the
    linker.
- term: test configuration
  definition: The setup and parameters used to run automated tests, ensuring they
    execute correctly in different environments.
- term: regression
  definition: A bug that appears in a new version of software that was not present
    in previous versions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261006105101.5720-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

This patch addresses a regression in the test configuration for aarch64-*-pe* targets. It marks certain tests that rely on `dlltool` as expected failures because `dlltool` is not built for these specific targets. This prevents the test suite from failing due to missing tools rather than actual code defects.
