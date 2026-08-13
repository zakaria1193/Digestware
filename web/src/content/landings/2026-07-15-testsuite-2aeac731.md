---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- aarch64
- abi
commit_hash: 2aeac7315ee65fd3829fddd4835bb549c69dbda9
source_type: github
author: Iain Sandoe
headline: 'aarch64: Add `dg-requires` for `mabi=ilp32`.'
tldr: aarch64 test suite now gates tests requiring the ilp32 ABI with `dg-requires`
  directives.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit (2aeac7315ee65fd3829fddd4835bb549c69dbda9) enhances the
  GCC testsuite for aarch64 by introducing `dg-requires` directives for tests targeting
  the ILP32 ABI. Previously, tests that depended on this ABI might fail spuriously
  on systems not configured for it. By adding `dg-requires` and a corresponding entry
  in `lib/target-supports.exp`, these tests are now correctly skipped when the target
  does not support `mabi=ilp32`, improving test suite robustness and accuracy.
primer_glossary:
- term: mabi=ilp32
  definition: A compiler flag for the aarch64 architecture that specifies the ILP32
    (Integer, Long, 32-bit) Application Binary Interface, where pointers and `long`
    types are 32 bits, while `int` is also 32 bits.
- term: ABI
  definition: Application Binary Interface. Defines how compiled code is translated
    into instructions and how software components interact at the binary level, including
    function call conventions and data type sizes.
- term: dg-requires
  definition: A directive used in GCC's testsuite to specify prerequisites or target
    capabilities that must be met for a test to be executed.
- term: aarch64
  definition: A 64-bit ARM architecture, widely used in mobile devices and increasingly
    in servers and desktops.
- term: target-supports.exp
  definition: An internal GCC testsuite support file that defines and manages target-specific
    capabilities and features required for test execution.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/2aeac7315ee65fd3829fddd4835bb549c69dbda9
date: '2026-07-15'
is_stub: false
stub_reason: ''
---

Several test cases for the aarch64 architecture in the GCC testsuite have been updated to include a `dg-requires` directive for the `mabi=ilp32` setting. This ensures that these tests are only executed on configurations that support this specific Application Binary Interface (ABI), preventing test failures on unsupported targets. A new target support entry for `mabi=ilp32` has also been added to `lib/target-supports.exp`.
