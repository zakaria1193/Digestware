---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- binutils
- ld
- testing
- cross-compilation
- testsuite
discussion_id: 20260618075856.2258643-1-chigot@adacore.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld/testsuite: add support for remote testing in ld-cdtest'
headline: 'ld/testsuite: add support for remote testing in ld-cdtest'
tldr: Patch to enable remote testing in ld-cdtest by replacing direct execution with
  'remote_load', improving compatibility with various target environments.
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 8
technical_tradeoffs:
- Using `remote_load` broadens test applicability but adds complexity in managing
  remote execution environments.
- Replacing direct `exec` with `remote_load` requires careful handling of execution
  status and output capture.
- Refining output diffing with `regexp_diff` improves robustness but might require
  more complex regular expressions.
exchanges:
- author: Clément Chigot
  role: proposer
  position: Submits a patch to enable remote testing in ld-cdtest by using 'remote_load'
    for execution.
  quote: null
- author: Maciej W. Rozycki
  role: reviewer
  position: Reviews the patch, confirms its functionality on native and remote targets,
    and suggests a minor improvement for output comparison.
  quote: "I can see this works correctly here with native `powerpc64le-linux-gnu'\
    \ \nsystem as well as remote `mips-linux-gnu' cross target, enabling the tests\
    \ \nin the latter case.  I have looked through the change and it seems good to\
    \ \nme except for one nit across two places; see below."
- author: Clément Chigot
  role: contributor
  position: Responds to Maciej's review, acknowledging the ping and the potential
    issue with email delivery.
  quote: null
primer_expert: This patch enhances the `ld-cdtest` test suite within binutils by enabling
  it to run tests on remote targets. Previously, tests were executed directly on the
  host system. The change introduces `remote_load` to execute binaries on a cross-target
  environment. This is crucial for testing linkers in diverse embedded or cross-compilation
  scenarios where direct execution isn't feasible. The review also touches upon how
  test output differences are handled, suggesting improvements for robustness.
primer_glossary:
- term: ld-cdtest
  definition: A test suite for the GNU linker (ld), likely focusing on code generation
    or specific linking scenarios.
- term: Remote testing
  definition: Executing tests on a different machine or environment than the one initiating
    the test, common in cross-compilation and embedded systems development.
- term: remote_load
  definition: A command or function within a testing framework that loads and executes
    a program on a remote or target system.
- term: regexp_diff
  definition: A utility or function that compares two text files or strings using
    regular expressions to identify differences, often used in test suites to check
    output.
- term: Cross-target
  definition: An environment where the development machine (host) and the execution
    machine (target) have different architectures or operating systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260618075856.2258643-1-chigot@adacore.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

Maciej W. Rozycki reviews a patch by Clément Chigot that adds support for remote testing within the `ld-cdtest` test suite. The patch replaces direct execution of test executables with `remote_load`, allowing tests to run on both native and remote targets. Rozycki confirms the patch works on his `powerpc64le-linux-gnu` native system and a remote `mips-linux-gnu` cross target. He notes a minor nit regarding the handling of differences between output and expected results, suggesting a refinement to the regexp_diff mechanism.
