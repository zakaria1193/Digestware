---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- i386
- maintenance
commit_hash: 4cb3ad46e761c62e51084ba4dac083edb8f1034e
source_type: github
author: Haochen Jiang
headline: 'testsuite: Fix include in PR128221-2.c.'
tldr: Corrected test case include directive in the GCC testsuite.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gcc/testsuite/gcc.target/i386/pr128221-2.c` file had an incorrect
  include statement, referencing `pr128221-1a.c` instead of the correct `pr128221-1.c`.
  This commit corrects that specific include directive. The change is a straightforward
  fix to ensure test case integrity within the GCC testsuite infrastructure.
primer_glossary:
- term: testsuite
  definition: A collection of test programs and scripts used to verify the correctness
    and functionality of a software project, such as the GCC compiler.
- term: i386
  definition: Refers to the x86 instruction set architecture, commonly used in Intel
    and AMD processors.
- term: PR128221-2.c
  definition: The filename of a specific test case within the GCC testsuite, likely
    related to bug report 128221.
- term: Include directive
  definition: A preprocessor directive (e.g., `#include` in C/C++) that tells the
    compiler to insert the contents of another file at that location.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4cb3ad46e761c62e51084ba4dac083edb8f1034e
date: '2026-11-04'
is_stub: true
stub_reason: low_score
---

This commit corrects a minor error in the GCC testsuite by fixing an include directive within the `pr128221-2.c` test file. The test case should have included `pr128221-1a.c` but was incorrectly including `pr128221-1.c`. This change ensures the test suite functions as intended.
