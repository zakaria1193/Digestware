---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- i386
- solaris
- assembler
commit_hash: aef738b4a47e6dcf6242485a3f2c1bf4bbad0bdd
source_type: github
author: Rainer Orth
headline: Fix i386 testsuite pattern for Solaris assembler syntax
tldr: Adjusted assembler pattern in an i386 test case to accommodate Solaris syntax.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `scan-assembler-times` pattern in `gcc.target/i386/bt-cmov-1.c`
  was failing on Solaris because its assembler uses `cmovcc.c` syntax, whereas the
  test expected `cmovc`. This commit updates the pattern to be more flexible, allowing
  for both `cmovc` and `cmovl.c` forms, and uses brace quoting for cleaner pattern
  matching. This resolves a test failure specific to Solaris's assembler dialect.
primer_glossary:
- term: testsuite
  definition: A collection of test programs and scripts used to verify the correctness
    of a compiler or other software component.
- term: i386
  definition: The architecture designation for Intel's 32-bit x86 processors. GCC
    supports compiling for this widely used architecture.
- term: scan-assembler-times
  definition: A function within GCC's testsuite that checks if a specific pattern
    appears in the output of the assembler, often used to verify instruction emission.
- term: Solaris assembler
  definition: The assembler program used on the Solaris operating system. It may have
    slight syntax variations compared to the GNU assembler (GAS).
- term: cmovcc
  definition: Conditional move instructions (e.g., cmovc, cmovnc) that conditionally
    transfer data from one register to another based on the processor's condition
    flags.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aef738b4a47e6dcf6242485a3f2c1bf4bbad0bdd
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

A test case in the GCC testsuite (`gcc.target/i386/bt-cmov-1.c`) failed on Solaris due to differences in assembler syntax for conditional move instructions. This patch modifies the `scan-assembler-times` pattern to accept both the standard GCC syntax and the Solaris assembler's dialect, ensuring test compatibility across different environments. Brace quoting is also used to simplify patterns.
