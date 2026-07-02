---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- x86
- darwin
- mach-o
- testsuite
commit_hash: 9e6ce124e2fcf08e395196590b2952e410227473
source_type: github
author: Iain Sandoe
headline: Amend fabsneg-2.c for Mach-O
tldr: A GCC test for x86 Darwin was updated to correctly handle constant labels in
  Mach-O executables, allowing `fabsneg-2.c` to pass.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In GCC's testsuite, `scan-assembler` directives are used to verify
  the generated assembly output. This particular issue involves the Mach-O object
  file format used on Darwin (macOS) systems. Mach-O linkers often introduce special
  prefixes for symbols, particularly for constant data, which can take the form of
  `lC` followed by additional characters. The existing `gcc.target/i386/fabsneg-2.c`
  test's assembly matching pattern was too strict, requiring constant labels to be
  directly linker-visible without such prefixes. This commit broadens the `scan-assembler`
  pattern to accept `lC*` variants, t…
primer_general: Compilers like GCC create executable files by first turning your code
  into assembly language, then into an 'object file,' and finally linking it into
  an executable. On Apple's macOS operating system (which uses the Darwin kernel),
  a special format called Mach-O is used for these object files. When GCC writes assembly
  code for constants, the Mach-O format might add special prefixes to their labels,
  like `lC`. GCC has a suite of tests to ensure it generates correct assembly. One
  such test, `fabsneg-2.c`, was failing on macOS because it wasn't expecting these
  `lC` prefixes for constant labels. This commit updates the test to recognize these
  Mach-O-specific labels, so the test now passes correctly, confirming GCC is generating
  proper code for macOS.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9e6ce124e2fcf08e395196590b2952e410227473
date: '2026-06-16'
is_stub: false
---

A GCC test case, `fabsneg-2.c`, was failing on Darwin systems because its assembly output scanner did not correctly account for how Mach-O object files generate constant labels. On Mach-O, constant labels can be introduced with `lC` prefixes, which the test's regular expression did not recognize, causing it to incorrectly report a failure. The test has been amended to permit `lC*` in its matching pattern, ensuring it now passes correctly on Darwin x86 targets.
