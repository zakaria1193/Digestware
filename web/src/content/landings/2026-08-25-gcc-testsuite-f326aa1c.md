---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- Darwin
- Mach-O
- testsuite
commit_hash: f326aa1ca5697e1923f43c701b1f53b3e609c1f5
source_type: github
author: Iain Sandoe
headline: 'Darwin: Port ssp-global-hidden tests to Mach-O'
tldr: Fortran tests for ssp-global-hidden now correctly run on Darwin by accounting
  for Mach-O differences.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ssp-global-hidden tests have been adapted for Darwin's Mach-O object
  file format. This was necessary because Mach-O's handling of tentative symbols and
  its PIC mechanisms differ from ELF, leading to test failures. The changes modify
  test cases to align with Mach-O's specific behavior for these scenarios.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/f326aa1ca5697e1923f43c701b1f53b3e609c1f5
date: '2026-08-25'
is_stub: true
stub_reason: low_score
---

Tests for ssp-global-hidden in C and C++ on Darwin have been ported to account for differences between ELF and Mach-O object file formats. Mach-O does not provide extra markup for tentative symbols and uses different mechanisms for PIC code on m32, which caused these tests to fail previously. The port ensures these tests function correctly on the Darwin platform.
