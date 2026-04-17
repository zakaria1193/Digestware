---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- abi
- compatibility
commit_hash: 9bb30cff1a251f037f420e82ff23b8dcc16e1d72
source_type: github
author: Jakub Jelinek
headline: 'libstdc++: Further baseline symbols updates'
tldr: The libstdc++ ABI baseline symbols are updated for several architectures by
  applying informed guesses based on prior analysis.
why_it_matters: Maintaining accurate ABI baselines ensures binary compatibility across
  different compiler versions and distributions, avoiding unexpected runtime issues.
impact_score: 7
impact_rationale: Updates to ABI baseline symbols affect binary compatibility and
  are important for library maintenance.
performance_win: false
breaking_change: false
outcome: committed
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9bb30cff1a251f037f420e82ff23b8dcc16e1d72
date: '2026-04-17'
---

This commit updates the ``baseline_symbols.txt`` files for several architectures in libstdc++. The updates are based on change analysis from a previous patch and applying the aarch64-linux-gnu baseline symbols patch for targets using m size_t mangling and i486-linux-gnu baseline symbols patch for targets using j size_t mangling. Targets not updated in GCC 15 and hppa-linux-gnu were skipped.
