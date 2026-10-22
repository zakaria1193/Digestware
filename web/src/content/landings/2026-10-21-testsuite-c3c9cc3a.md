---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- arm
- testsuite
commit_hash: c3c9cc3a6a7c198af801fa6dd1474ea7111a2071
source_type: github
author: Torbjörn SVENSSON
headline: 'arm: Remove unused arm_v8_1m_lob-related target checks'
tldr: Removes obsolete test suite checks for ARM architecture.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ARM architecture's support for the v8.1m_lob (lower-order bits)
  feature has evolved, rendering certain specific target checks in the GCC test suite
  obsolete. This commit removes `check_effective_target_arm_thumb2_no_arm_v8_1m_lob`
  and `check_effective_target_arm_thumb2_ok_no_arm_v8_1m_lob` from `lib/target-supports.exp`
  that are no longer relevant due to prior code changes (r16-7929-ge1077ad5753148).
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c3c9cc3a6a7c198af801fa6dd1474ea7111a2071
date: '2026-10-21'
is_stub: true
stub_reason: low_score
---

Unused target checks related to arm_v8_1m_lob have been removed from the GCC test suite. These checks were identified as obsolete following earlier code modifications. Their removal cleans up the test suite without affecting current functionality.
