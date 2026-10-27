---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- gfortran
- floating-point
- x86
commit_hash: 1c3be8e0d429c25c888de298f3de7f14694fd458
source_type: github
author: Harald Anlauf
headline: 'testsuite: Adjust numerical thresholds for gfortran.dg/trigd_1.f90 [PR127063]'
tldr: Adjusts floating-point comparison thresholds for a Fortran test on 32-bit x86.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gfortran.dg/trigd_1.f90` test involves floating-point calculations,
  the results of which are compared against expected values. On 32-bit x86 platforms,
  compiler flags related to floating-point precision and optimization can lead to
  minor variations in results. This commit modifies the test to use adjusted numerical
  comparison thresholds, ensuring that these acceptable variations do not cause the
  test to fail, thereby improving its robustness across different build configurations.
primer_glossary:
- term: gfortran
  definition: The GNU Fortran compiler.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a program
    or system. In GCC, the testsuite contains numerous small programs and scripts
    to check compiler behavior.
- term: floating-point arithmetic
  definition: Arithmetic operations performed on numbers that have a fractional part,
    represented in a format that approximates real numbers.
- term: thresholds
  definition: In the context of numerical tests, specific values that define acceptable
    ranges or limits for results. If a result falls outside these thresholds, the
    test is considered to have failed.
- term: x86
  definition: A family of instruction set architectures developed by Intel and widely
    used in personal computers and servers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1c3be8e0d429c25c888de298f3de7f14694fd458
date: '2026-10-26'
is_stub: true
stub_reason: low_score
---

This commit adjusts the numerical thresholds for the gfortran.dg/trigd_1.f90 test case. Floating-point arithmetic in numerical tests can be sensitive to compile flags, particularly on 32-bit x86 platforms. By setting suitable thresholds, this change ensures the test's reliability and accuracy across different compilation environments, addressing issues reported in PRs 121366 and 127063.
