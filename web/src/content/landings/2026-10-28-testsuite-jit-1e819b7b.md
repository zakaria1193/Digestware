---
project: gcc
subsystem: testsuite/jit
patch_id: null
tags:
- testsuite
- jit
- darwin
commit_hash: 1e819b7b7ec9ad53b274acbe0f6bb55d0da1afec
source_type: github
author: Iain Sandoe
headline: Darwin JIT tests adapt to Mach-O assembly syntax and skip GDB checks.
tldr: JIT tests on Darwin now handle Mach-O differences and avoid unsupported GDB
  debuginfo checks.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The JIT testsuite on Darwin previously assumed ELF assembly syntax
  and GDB for debuginfo verification. This patch updates scan-asm directives to use
  Mach-O syntax where necessary and skips GDB tests because modern Darwin versions
  lack a compatible GDB. This ensures test stability on the target platform.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1e819b7b7ec9ad53b274acbe0f6bb55d0da1afec
date: '2026-10-28'
is_stub: true
stub_reason: low_score
---

This commit adjusts GCC's Just-In-Time (JIT) compilation test suite for Darwin to correctly handle differences in assembly syntax between Mach-O and ELF object file formats. It also removes GDB-based debuginfo checks that are no longer supported on modern Darwin systems.
