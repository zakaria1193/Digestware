---
project: gcc
subsystem: testsuite/arm
patch_id: null
tags:
- testsuite
- arm
- embedded
commit_hash: 8a5c76ca173f25012ab9ba21fed11eb598bf777a
source_type: github
author: Torbjörn SVENSSON
headline: 'testsuite: arm: Set tuning for MVE FP intrinsic tests'
tldr: ARM MVE FP intrinsic tests now use a fixed tuning to ensure stable assembly
  output.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ARM MVE testsuite requires stable assembly output for its FP intrinsic
  tests. This commit forces a specific tuning (`-mtune=cortex-m55`) to prevent variations
  caused by DejaGNU's default tuning settings, ensuring test consistency.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8a5c76ca173f25012ab9ba21fed11eb598bf777a
date: '2026-10-04'
is_stub: true
stub_reason: low_score
---

The ARM MVE floating-point intrinsic tests now explicitly set the -mtune=cortex-m55 flag. This overrides any default tuning provided by DejaGNU, guaranteeing that the generated assembly is stable and predictable for testing purposes. Several intrinsic test files have been updated to incorporate this change.
