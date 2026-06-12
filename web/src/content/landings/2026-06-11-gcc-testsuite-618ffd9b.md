---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- c++
- darwin
- portability
- weak-symbols
commit_hash: 618ffd9be9129adaf2d5d8fcbe934084c2c45fe9
source_type: github
author: Iain Sandoe
headline: Test suite uses portable weak symbol scanning for Darwin C++ tests.
tldr: GCC's C++ test suite now employs portable `scan-weak` and `scan-not-weak` directives
  for weak symbol checks, especially on Darwin.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Weak symbols are linker features that allow multiple definitions of
  a symbol, with the linker choosing one (usually the non-weak one) or allowing a
  default if no strong definition exists. On Darwin (macOS), the behavior and representation
  of weak symbols in object files can differ from other Unix-like systems. This commit
  updates a C++ test for reflection and visibility (`g++.dg/reflect/visibility1.C`)
  to use `scan-weak` and `scan-not-weak` directives. These abstract the low-level
  details of checking for weak symbol presence, making the test robust to platform
  differences and the various `mac…
primer_general: In computer programming, a \"symbol\" is like a name for a function
  or a variable. Sometimes, a program might have multiple versions of the same symbol,
  and the system needs to decide which one to use. \"Weak symbols\" are a way to tell
  the system that a particular version of a symbol can be overridden by another, stronger
  one if it exists. This update to GCC's automated tests makes it easier to check
  how these weak symbols behave across different operating systems, especially on
  Apple's macOS (Darwin). By using special commands that automatically adapt to the
  system's specifics, the tests become more reliable and easier to maintain, ensuring
  that programs using weak symbols work correctly on various platforms.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/618ffd9be9129adaf2d5d8fcbe934084c2c45fe9
date: '2026-06-11'
is_stub: false
---

This commit refactors a C++ test in GCC's test suite to use the `scan-weak` and `scan-not-weak` directives, improving its portability, particularly for Darwin targets. Previously, the test `g++.dg/reflect/visibility1.C` might have required extensive modifications to function correctly on Darwin due to differences in how weak symbols are handled. By leveraging these portability helpers, the test suite can now reliably verify weak symbol behavior across different operating systems, reducing maintenance overhead and ensuring consistent testing results.
