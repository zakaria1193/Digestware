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
tldr: Use the new mechanism for setting GLIBC tunables in Makefiles for ELF tests.
stakes: Simplifies setting GLIBC tunables in Makefiles for tests.
proposer: Yury Khrustalev <yury.khrustalev@arm.com>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved readability and maintainability of Makefiles.
- More explicit and consistent way of setting GLIBC tunables for tests.
exchanges: []
primer_expert: This patch updates Makefiles under the `elf` test suite to use the
  new `*TUNABLES` Make variable instead of the older `*ENV` form. The tests here check
  properties of ELF binaries, such as stack execution. This change improves maintainability
  and consistency across the project.
primer_general: The GNU C Library (glibc) provides a way to tune its behavior through
  environment variables called "tunables". These tunables can control aspects like
  memory allocation, threading, and other low-level system behaviors. This patch modifies
  the Makefiles responsible for building and running tests for glibc, specifically
  in the `elf` directory, which relates to the Executable and Linkable Format. It
  changes the way these tunables are set for the tests, moving from a general environment
  variable (`ENV`) to a dedicated `TUNABLES` variable, for clarity and better organization.
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

This patch updates the Makefiles in the elf tests folder to use the new way of handling test tunables, changing from setting tunables in the ENV variable to using the TUNABLES variable.
