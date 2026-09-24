---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- testsuite
- microblaze
- regression
discussion_id: 20260924015023.36799-2-thesamprice@gmail.com
source_type: public_inbox
title: '[PATCH v3 3/4] gas: testsuite: exclude microblazeel from the diff1 and end
  tests'
headline: 'gas: testsuite: exclude microblazeel from the diff1 and end tests'
tldr: Corrects MicroBlaze test exclusions in `gas.exp` to include both endiannesses,
  resolving test failures on little-endian builds.
proposer: Sam Price <thesamprice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Expands a test exclusion pattern to cover both endiannesses of MicroBlaze.
- Resolves specific test failures on little-endian MicroBlaze builds.
exchanges: []
primer_expert: The `gas.exp` test runner script has guards to skip specific tests
  on certain architectures. For MicroBlaze, tests `diff1.s` (dealing with symbol differences
  and relaxation) and `end.s` (related to the `.end` directive's meaning) are excluded
  using `microblaze-*-*`. However, the little-endian variant, `microblazeel-*-*`,
  was not matched by this glob. This patch widens the glob to `microblaze*-*-*`, aligning
  with the pattern used for other architectures like `avr`, `rl78`, and `rx`, ensuring
  correct test exclusion for both MicroBlaze endiannesses and resolving previously
  reported failures on `…
primer_glossary:
- term: gas.exp
  definition: A DejaGnu test suite script used by the GNU Assembler (gas) to run and
    verify its test cases across different configurations.
- term: microblazeel
  definition: The little-endian variant of the MicroBlaze processor architecture.
- term: diff1.s
  definition: A gas test file that checks the handling of differences between two
    undefined symbols, often related to relaxation.
- term: end.s
  definition: A gas test file that checks the behavior of the `.end` directive, which
    can signify the end of assembly or a function endpoint depending on the architecture.
- term: Glob
  definition: A pattern used for matching filenames or strings, often containing wildcards
    like '*'.
series_id: 'binutils:gas: testsuite: exclude microblazeel from the diff1 and end tests'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260924015023.36799-2-thesamprice@gmail.com
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This patch updates the MicroBlaze test exclusion logic in `gas/testsuite/gas/all/gas.exp`. Previously, the exclusion glob `microblaze-*-*` only matched the big-endian MicroBlaze triplet, causing the `diff1.s` and `end.s` tests to incorrectly run and fail on the little-endian `microblazeel-*-*` triplet. By changing the glob to `microblaze*-*-*`, both endiannesses are now correctly excluded from these tests. This resolves two pre-existing unexpected failures on `microblazeel-elf` without affecting the `microblaze-elf` count, bringing the test suite to zero unexpected failures on both configurations.
