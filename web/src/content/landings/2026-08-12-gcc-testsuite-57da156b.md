---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- x86
- testsuite
- tuning
commit_hash: 57da156bfc01865c716112e5582c39cd551e8b7a
source_type: github
author: Iain Sandoe
headline: X86 testsuite uses generic tuning when needed.
tldr: X86 testsuite explicitly uses generic tuning to ensure reliability.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `scan-asm` tests for X86 were sensitive to the default CPU tuning
  set by `--with-cpu`. To make these tests deterministic, the commit explicitly adds
  `-mtune=generic` to the test cases that require it, ensuring they run with a consistent
  tuning profile.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/57da156bfc01865c716112e5582c39cd551e8b7a
date: '2026-08-12'
is_stub: true
stub_reason: low_score
---

Several X86 testsuite cases that previously passed or failed based on the platform's default tuning have been updated to explicitly use '-mtune=generic'. This change ensures that these tests, which rely on generic tuning for reliable operation, behave consistently regardless of the host system's CPU configuration.
