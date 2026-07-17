---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- solaris
- sparc
- bitint
commit_hash: 1731ba6e70ff806c209ab4d73c402257afd41768
source_type: github
author: Rainer Orth
headline: Add _BitInt support requirement to torture test case
tldr: New torture test case now correctly requires _BitInt support, fixing Solaris/SPARC
  failures.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gcc.dg/torture/bitint-101.c` test case, which exercises `_BitInt`
  functionality, was failing on Solaris/SPARC due to the target lacking support for
  this feature. The test has been updated to include `dg-require-bitint` to prevent
  it from running on unsupported platforms, thus resolving the failures.
primer_glossary:
- term: _BitInt
  definition: A built-in integer type in GCC that allows for arbitrary bit widths,
    offering more flexibility than standard integer types like int or long.
- term: torture test
  definition: A category of GCC test cases designed to stress-test specific language
    features or compiler optimizations with complex or edge-case scenarios.
- term: Solaris/SPARC
  definition: A combination of the Solaris operating system and Sun Microsystems'
    SPARC processor architecture, a common target for GCC.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1731ba6e70ff806c209ab4d73c402257afd41768
date: '2026-07-16'
is_stub: true
stub_reason: low_score
---

A new torture test case, `bitint-101.c`, failed on Solaris/SPARC due to lack of `_BitInt(2)` support. This commit modifies the test to explicitly require `bitint` support, ensuring it only runs on the intended architectures and passes.
