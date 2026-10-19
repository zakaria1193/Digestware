---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- hppa
commit_hash: ff0b2fe58c2531d58e609e84d2277c7f5dd7bbb1
source_type: github
author: John David Anglin
headline: 'testsuite: Fix g++.dg/opt/mem-notrap-load-builtin.C on hppa*64*-*-*'
tldr: Disable scan-rtl-dump for mem-notrap-load-builtin test on PA-RISC.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test g++.dg/opt/mem-notrap-load-builtin.C fails on hppa*64*-*-*
  due to address splitting in the expand pass. This commit disables scan-rtl-dump
  for this testcase on the affected targets, as the splitting of the 'this' pointer
  attribute from the memory expression interferes with the expected RTL dump analysis.
primer_glossary:
- term: scan-rtl-dump
  definition: A debugging tool that outputs Register Transfer Language (RTL) for analysis
    during compiler optimization passes. It helps in understanding the intermediate
    representation of the code.
- term: address splitting
  definition: A compiler optimization technique where an address calculation is broken
    down into smaller parts. This can sometimes affect how other compiler analyses
    perceive the relationship between different parts of an expression.
- term: PA-RISC
  definition: A family of RISC computer architectures developed by Hewlett-Packard.
    The 'hppa' targets in GCC refer to these architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ff0b2fe58c2531d58e609e84d2277c7f5dd7bbb1
date: '2026-10-18'
is_stub: true
stub_reason: low_score
---

This commit disables the scan-rtl-dump for a specific test case on 64-bit PA-RISC systems. Address splitting in the compiler separates the 'this' pointer from the memory expression during expand, causing the test to fail. Disabling the dump prevents this failure.
