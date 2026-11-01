---
project: gcc
subsystem: testsuite/jit
patch_id: null
tags:
- testsuite
- jit
- darwin
commit_hash: f1114bb0f3ec67f2fb6bee88f22e148c3d7dedf4
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
url: https://github.com/gcc-mirror/gcc/commit/f1114bb0f3ec67f2fb6bee88f22e148c3d7dedf4
date: '2026-10-28'
is_stub: true
stub_reason: low_score
---

This commit adjusts GCC's Just-In-Time (JIT) compilation test suite for Darwin to correctly handle differences in assembly syntax between Mach-O and ELF object file formats. It also removes GDB-based debuginfo checks that are no longer supported on modern Darwin systems.
