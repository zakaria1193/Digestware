---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- alpha
- security
commit_hash: 6dad587cb3342289387b454ee3d8e230066dbf80
source_type: github
author: Matt Turner
headline: Require stack protector support for attr test on Alpha
tldr: A test for stack protector attributes now correctly requires target support,
  fixing failures on Alpha.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test `g++.dg/no-stack-protector-attr.C` previously used an `x86`
  specific `dg-do compile` directive, which was later superseded by an explicit exclusion
  for `hppa`. DejaGnu's logic favored the latter, causing the test to run on unintended
  targets like Alpha. The commit replaces these directives with `require fstack_protector`,
  ensuring the test is only executed on architectures supporting stack protectors.
  Alpha, which lacks this support and warns about `-fstack-protector`, now correctly
  skips the test, and the `hppa` exclusion becomes redundant as `check_effective_target_fstack_protector…
primer_glossary:
- term: stack protector
  definition: A security feature that helps detect buffer overflows by placing a special
    value (canary) on the stack before a function's return address. If the canary
    is overwritten, a buffer overflow is detected.
- term: -fstack-protector
  definition: A GCC compiler flag that enables stack smashing protection.
- term: dg-do compile
  definition: A DejaGnu test directive that specifies the actions to be performed
    for a test case, such as compiling, assembling, or running.
- term: canary
  definition: A random value placed on the stack by stack protectors to detect buffer
    overflows. If this value is modified, it indicates a potential overflow.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:testsuite: require stack protector support in no-stack-protector-attr.c'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6dad587cb3342289387b454ee3d8e230066dbf80
date: '2026-08-18'
is_stub: true
stub_reason: low_score
---

The test `no-stack-protector-attr.C` previously had a restrictive `dg-do compile` directive for x86 and an exclusion for HPPA. This led to it running on unsupported targets like Alpha. This commit removes the outdated directives and instead requires `-fstack-protector` support, ensuring the test only runs on platforms where stack protection is available. This resolves failures on Alpha, which warns about the unsupported option.
