---
project: glibc
subsystem: tests
patch_id: null
tags:
- glibc
- tests
- elf
- tunables
- makefile
discussion_id: 20260421143804.3933020-3-yury.khrustalev@arm.com
source_type: public_inbox
title: '[PATCH v4 2/8] tests: elf: Use new tunable handling'
headline: 'Tests: Elf: Use new tunable handling'
tldr: Updates the elf tests to use the new tunable handling mechanism.
stakes: Standardizing tunable handling improves test consistency and simplifies maintenance.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Modernizes the tunable handling in the `elf` tests.
- Ensures consistency with other parts of the glibc test suite.
- May require adjustments to test infrastructure if it relies on the old tunable handling
  method.
exchanges: []
primer_expert: This patch updates `elf/Makefile` to use the new tunable handling mechanism.  Specifically,
  it changes how the `GLIBC_TUNABLES` environment variable is set for multiple tests,
  including `tst-execstack-tunable` and `tst-decorate-maps`.  This involves updating
  the way the runtime linker and memory allocation are configured for these tests.  The
  file in question is `elf/Makefile`.
primer_general: The ELF (Executable and Linkable Format) directory in glibc contains
  tests related to dynamic linking and loading. glibc tunables are runtime configuration
  options that allow users to adjust the behavior of the library. Tests often need
  to manipulate these tunables to ensure proper function under different configurations.
  This patch updates the way those tunables are set in the `elf` directory's tests.
series_id: 'glibc:tests: elf: use new tunable handling'
series_role: reply
series_parts:
- title: 'tests: elf: Use new tunable handling'
  url: https://inbox.sourceware.org/libc-alpha/d742aa2d-5be6-45dc-b45f-27d4cf13702b@linaro.org
  n: 2
  total: 8
url: https://inbox.sourceware.org/libc-alpha/20260421143804.3933020-3-yury.khrustalev@arm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch updates the `elf/Makefile` to use the new tunable handling mechanism. It replaces the direct assignment of `GLIBC_TUNABLES` with the `TUNABLES +=` syntax for setting the `glibc.rtld.execstack` and `glibc.mem.decorate_maps` tunables in various tests.
