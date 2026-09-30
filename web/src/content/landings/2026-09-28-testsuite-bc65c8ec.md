---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- arm
- compiler
commit_hash: bc65c8ec9113060aba191009f2c23ac8db88ee41
source_type: github
author: Christophe Lyon
headline: 'Arm testsuite: Replace dg-skip-if with dg-require/dg-add-options'
tldr: Arm tests in GCC's testsuite are updated to use more precise directives, enabling
  previously skipped tests.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit cleans up Arm testsuite directives. Specifically, `dg-skip-if`
  is removed in favor of `dg-require-effective-target` and `dg-add-options`. For example,
  `armv6-unaligned-load-ice.c` now correctly uses `arm_arch_v6k` and `arm_arch_v6k_thumb_ok`,
  removing the need for `-mthumb` and `-mfloat-abi=softfp` from `dg-options` as they
  were implicitly handled or unnecessary. This resolves issues where tests failed
  to run due to overly broad skip conditions.
primer_glossary:
- term: dg-skip-if
  definition: A directive used in GCC's testsuite to skip a test case if a certain
    condition is met, preventing the test from running on unsupported configurations.
- term: dg-require-effective-target
  definition: A GCC testsuite directive that specifies the minimum target architecture
    or features required for a test case to be valid and executable.
- term: dg-add-options
  definition: A GCC testsuite directive used to add specific compiler options required
    for a particular test case.
- term: Arm
  definition: A family of reduced instruction set computing (RISC) architectures widely
    used in mobile devices and embedded systems, and increasingly in servers and desktops.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bc65c8ec9113060aba191009f2c23ac8db88ee41
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

Several test cases in GCC's Arm testsuite have been refactored to replace `dg-skip-if` directives with more specific `dg-require-effective-target` and `dg-add-options`. This change allows tests that were previously skipped due to imprecise target requirements to now be executed and pass, improving test coverage.
