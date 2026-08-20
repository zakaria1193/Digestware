---
project: gcc
subsystem: testsuite/arm
patch_id: null
tags:
- testsuite
- arm
commit_hash: f51ab50afb9542d93879e0afcda8e3dbb2f3cd31
source_type: github
author: Torbjörn SVENSSON
headline: 'testsuite: arm: add require effective target for cmse tests'
tldr: Ensures ARM CMSE tests run correctly by setting the effective target appropriately.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: ARM Compliance Mode Security Extension (CMSE) tests in the GCC testsuite
  now explicitly set the effective target using `arm_arch_v8m_main` or `arm_arch_v8_1m_mve`.
  This is necessary to avoid conflicts arising from implicit `-mcpu` settings, which
  can interfere with the specific CPU architecture required for CMSE functionality,
  ensuring test stability.
primer_glossary:
- term: CMSE
  definition: Compliance Mode Security Extension for ARM processors, which enhances
    security by providing isolated execution environments.
- term: effective-target
  definition: In the GCC testsuite, this refers to specifying the exact target architecture
    and features for a test case, overriding or refining default testbed configurations.
- term: -mcpu
  definition: A GCC command-line option to specify the target processor, affecting
    instruction set and optimization choices.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f51ab50afb9542d93879e0afcda8e3dbb2f3cd31
date: '2026-08-07'
is_stub: true
stub_reason: low_score
---

This commit updates ARM compliance tests for CMSE to use the `require effective-target` directive. This prevents conflicts between `-mcpu=unset` and existing `-mcpu` arguments, ensuring the tests accurately reflect the target environment and pass reliably.
