---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- c++
- testsuite
- portability
commit_hash: 2bb0802bf844915658a87595aaa186d2ed787006
source_type: github
author: Patrick Palka
headline: 'c++: Fix portability of initlist135.C testcase'
tldr: C++ testsuite fix replaces inline initializer_list definition with standard
  include.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test case `g++.dg/cpp0x/initlist135.C` previously contained an
  inline definition of `std::initializer_list`. This was found to be problematic on
  certain architectures (specifically i686) due to how the compiler's reduction passes
  interacted with the user-defined type. Including the standard header `<initializer_list>`
  provides the correct definition and avoids these interactions, making the test more
  robust and portable across different compiler internal behaviors.
primer_glossary:
- term: std::initializer_list
  definition: A C++ standard library class that provides a convenient way to create
    and pass lists of values to functions or constructors.
- term: i686
  definition: A common 32-bit x86 processor architecture, widely used in older personal
    computers.
- term: over-reduction
  definition: A compiler optimization pass that may simplify or transform code too
    aggressively, sometimes leading to incorrect or unexpected behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2bb0802bf844915658a87595aaa186d2ed787006
date: '2026-08-21'
is_stub: true
stub_reason: low_score
---

A C++ test case (`cpp0x/initlist135.C`) that defined `std::initializer_list` inline has been fixed. This inline definition caused issues on the i686 architecture due to over-reduction of the original test case. The fix replaces the inline definition with a standard `#include <initializer_list>`, ensuring portability and correct behavior.
