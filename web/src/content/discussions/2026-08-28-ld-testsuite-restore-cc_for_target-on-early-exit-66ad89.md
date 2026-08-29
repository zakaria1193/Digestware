---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- testsuite
- CI
- LTO
- binutils
discussion_id: a376c787f1417abedb3c51516942c0077892313c.1787909218.git.sam@gentoo.org
source_type: public_inbox
title: '[COMMITTED] ld: restore CC_FOR_TARGET if bailing out early for LTO tests'
headline: 'ld testsuite: Restore CC_FOR_TARGET on early exit'
tldr: Fix committed to ld testsuite to restore the CC_FOR_TARGET variable when exiting
  early during LTO tests, preventing potential issues if a non-Clang compiler wa…
proposer: Sam James <sam@gentoo.org>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures test environment consistency by properly restoring compiler variables.
- Prevents potential test failures caused by lingering compiler settings.
exchanges:
- author: Sam James
  role: proposer
  position: Announces the commitment of a fixup to restore CC_FOR_TARGET in the ld
    testsuite's LTO tests.
  quote: "Fixup c562e4ffa94c50ee974200a7457e435cec411a43 as we need to restore\nCC_FOR_TARGET\
    \ which may not be Clang if we return early because of missing\nobjects.\n\n\t\
    PR ld/34576\n\t* testsuite/ld-plugin/lto.exp (llvm_lto_tests): Restore\n\tCC_FOR_TARGET\
    \ on return."
primer_expert: This is a notification about a committed fix to the `binutils` testsuite,
  specifically within the `ld/testsuite/ld-plugin/lto.exp` file. The change addresses
  a subtle issue in the `llvm_lto_tests` procedure. If this procedure returns early
  because required objects are missing, it must restore the `CC_FOR_TARGET` variable
  to its saved state (`CC_FOR_TARGET_saved`). Failure to do so could leave `CC_FOR_TARGET`
  pointing to Clang even if it was not the intended compiler for subsequent tests,
  potentially causing cascading failures. This fix ensures proper environment cleanup
  during test execution.
primer_glossary:
- term: CC_FOR_TARGET
  definition: A variable, typically used in build systems or test suites, that specifies
    the C compiler to be used for cross-compilation or for building tools for a target
    system.
- term: LTO
  definition: Link-Time Optimization. A compiler optimization technique where optimizations
    are performed across multiple source files during the linking phase.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    program or component.
- term: PR ld/34576
  definition: A specific bug report (Problem Report) filed against the GNU linker
    (ld), identified by number 34576.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/a376c787f1417abedb3c51516942c0077892313c.1787909218.git.sam@gentoo.org
bugzilla_url: null
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

Sam James reports the commitment of a fixup for a previous change in the GNU linker's testsuite. The change ensures that the `CC_FOR_TARGET` variable is correctly restored to its saved value (`CC_FOR_TARGET_saved`) when the `llvm_lto_tests` procedure exits early due to missing objects. This prevents potential issues where `CC_FOR_TARGET` might incorrectly remain set to Clang if it was previously configured that way, even if a different compiler is intended for subsequent tests.
