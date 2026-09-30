---
project: gcc
subsystem: testsuite/powerpc64
patch_id: null
tags:
- testsuite
- powerpc64
- altivec
commit_hash: 73ae58ac01fcfad105d4d28f906839137847717c
source_type: github
author: Stefan Schulze Frielinghaus
headline: 'testsuite: powerpc64: Fix asm-hard-reg-5.c'
tldr: Skips a test case on powerpc64 if altivec is not supported.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The gcc.dg/asm-hard-reg-5.c test case relies on specific register constraints
  for inline assembly that may not be universally available on powerpc64 without explicitly
  enabling altivec. The test is now guarded to ensure it only runs when altivec is
  supported, preventing spurious failures on powerpc64 systems where it's not implicitly
  enabled.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/73ae58ac01fcfad105d4d28f906839137847717c
date: '2026-09-30'
is_stub: true
stub_reason: low_score
---

The test gcc.dg/asm-hard-reg-5.c might fail on powerpc64 due to missing altivec support. This commit modifies the test to either explicitly enable altivec or skip the test case when altivec is unavailable. This ensures the test suite functions correctly across different powerpc64 configurations.
