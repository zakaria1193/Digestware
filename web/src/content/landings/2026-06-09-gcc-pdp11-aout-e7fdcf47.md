---
project: gcc
subsystem: gcc/pdp11-aout
patch_id: null
tags:
- pdp11
- build-fix
- cross-compilation
commit_hash: e7fdcf4738f4e4699022e8ea72776cbc5989de8e
source_type: github
author: Martin Jambor
headline: 'Pdp11-aout: Remove invalid conversion and restore build'
tldr: This patch fixes a build error when cross-compiling GCC for pdp11-aout by correcting
  a type mismatch.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The pdp11-aout port of GCC's backend (`gcc/config/pdp11/pdp11.cc`)
  encountered a type mismatch in the `pdp11_conditional_register_usage` function.
  This function likely deals with the specific register allocation or usage conventions
  for the PDP-11 architecture. The fix involves correcting a pointer type to resolve
  a build-time error related to implicit conversions, ensuring the AOUT object file
  format generation for PDP-11 remains consistent.
primer_general: Compilers like GCC translate human-readable code into machine instructions.
  This process is complex and often involves specific configurations for different
  computer architectures and operating systems, known as 'targets'. When GCC is compiled
  to run on one system but generate code for a different system (called 'cross-compiling'),
  it needs to understand the target's unique characteristics. This commit addresses
  a situation where GCC was failing to build itself for a specific, older target (pdp11-aout,
  referring to the PDP-11 computer architecture and the AOUT executable format). The
  problem was a type mismatch in the compiler's internal code, where an `int` pointer
  was being incorrectly converted to an `unsigned int` pointer, leading to a build
  error. This fix simply corrects that type, allowing the cross-compilation process
  for pdp11-aout to complete successfully.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e7fdcf4738f4e4699022e8ea72776cbc5989de8e
date: '2026-06-09'
is_stub: false
---

When cross-compiling GCC for the pdp11-aout target, a recent change introduced a build failure due to an invalid conversion from `int*` to `unsigned int*`. This patch addresses the issue by changing the type of the variable in `pdp11_conditional_register_usage` from `int` to `unsigned int`, restoring the build functionality for this specific target.
