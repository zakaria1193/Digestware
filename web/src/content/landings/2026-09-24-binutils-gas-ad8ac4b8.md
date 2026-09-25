---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- gas
- microblaze
- testsuite
- bugfix
commit_hash: ad8ac4b8993e14160dfe2f365d646d52afc5ecd8
source_type: public_inbox
author: Michael Eager <eager@sourceware.org>
headline: Exclude MicroBlaze little-endian from specific gas testsuite tests
tldr: Gas testsuite exclusion for MicroBlaze little-endian prevents false failures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The glob pattern in `gas/testsuite/gas/all/gas.exp` for excluding MicroBlaze
  from the `diff1.s` and `end.s` tests has been broadened from `microblaze-*-*` to
  `microblaze*-*-*`. This change ensures that the little-endian `microblazeel` architecture
  is also correctly excluded from these tests, preventing spurious failures. The change
  aligns the MicroBlaze exclusion pattern with those used for other architectures
  like AVR and RL78.
primer_glossary:
- term: gas.exp
  definition: A test suite file for the GNU Assembler (gas) that uses DejaGnu and
    Expect to automate testing across various architectures and configurations.
- term: MicroBlaze
  definition: A soft processor core from Xilinx, commonly used in FPGAs. It supports
    both big-endian and little-endian configurations.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    system. For compilers and assemblers, this typically includes compiling and assembling
    a wide range of source code examples.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260924153102.D9F8C48A0810@sourceware.org
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

The GNU Assembler's testsuite now correctly excludes the MicroBlaze little-endian architecture ('microblazeel-*-*') from two specific tests: 'diff1.s' and 'end.s'. Previously, the test guards only matched the big-endian 'microblaze-*-*' triplet, causing these tests to run and fail on the little-endian variant despite the assembler functioning correctly for that configuration.
