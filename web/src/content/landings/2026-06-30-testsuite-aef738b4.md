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
headline: 'testsuite: i386: Fix bt-cmov-1.c on Solaris'
tldr: i386 test case for conditional moves now works on Solaris.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `i386/bt-cmov-1.c` test case failed on Solaris due to differences
  in assembler syntax for conditional move instructions; Solaris uses suffixes like
  `.c` (e.g., `cmovl.c`) where standard gas uses the condition code directly (e.g.,
  `cmovc`). This commit modifies the `scan-assembler-times` section to accept both
  syntaxes, using brace quoting to handle variations and removing redundant escapes.
  This resolves failing tests in `i386-pc-solaris2.11` environments and ensures the
  test suite's robustness across different assembler implementations.
primer_general: A test designed to verify the functionality of conditional move instructions
  on Intel processors (i386) failed when run on the Solaris operating system. This
  failure was due to differences in how the assembler, the program that translates
  assembly code into machine code, interprets these instructions. The test has been
  updated to understand both the standard syntax and the Solaris-specific syntax for
  these instructions. This fix ensures that the compiler's tests are more reliable
  across different operating systems and assembler versions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/aef738b4a47e6dcf6242485a3f2c1bf4bbad0bdd
date: '2026-06-30'
is_stub: true
stub_reason: low_score
---

A gcc test case (`bt-cmov-1.c`) for the i386 architecture's conditional move instructions has been fixed to work correctly on Solaris. The issue arose because the Solaris assembler uses a slightly different syntax for conditional moves (e.g., `cmovl.c` instead of `cmovc`). The test case has been updated to accept both syntaxes, improving cross-platform compatibility of the test suite. It also simplifies patterns and avoids unnecessary escaping, ensuring broader test coverage.
