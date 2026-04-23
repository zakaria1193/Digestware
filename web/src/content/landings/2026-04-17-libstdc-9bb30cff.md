---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- ABI
- baseline symbols
- Linux
commit_hash: 9bb30cff1a251f037f420e82ff23b8dcc16e1d72
source_type: github
author: Jakub Jelinek
headline: 'Libstdc++: Update baseline symbols for various Linux architectures.'
tldr: Updates baseline symbols for several Linux architectures in libstdc++, mainly
  based on Fedora package builds and analysis of GCC 15 changes.
impact_score: 6
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

This commit updates the baseline_symbols.txt files for several Linux architectures, including ia64, m68k, powerpc64, sparc64, and x86_64. The updates are largely based on Fedora package builds and informed by the change analysis performed in previous patches for GCC 15. Some manual adjustments were made for powerpc64.
