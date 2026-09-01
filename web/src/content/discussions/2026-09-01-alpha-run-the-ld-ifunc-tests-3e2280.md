---
project: binutils
subsystem: alpha
patch_id: null
tags:
- binutils
- alpha
- linker
- IFUNC
- testsuite
discussion_id: 20260901023318.3503991-11-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 11/11] alpha: run the ld-ifunc tests'
headline: 'alpha: run the ld-ifunc tests'
tldr: Enables ld-ifunc tests for the alpha target.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Enables more comprehensive testing for IFUNC support on Alpha.
- Acknowledges and documents a known failing test case.
exchanges: []
primer_expert: This patch enables the `ld-ifunc` test suite for the alpha target by
  removing it from the `skip_target_list` in `ld/testsuite/ld-ifunc/ifunc.exp`. It
  also updates `ld/NEWS` to document alpha's support for IFUNC symbols and the new
  `R_ALPHA_IRELATIVE` relocation. The patch notes that `ifunc-26` remains an expected
  failure because the test's use of `.set` is misinterpreted by the alpha assembler,
  which is a known issue.
primer_glossary:
- term: IFUNC
  definition: Indirect Function. A mechanism allowing functions to be resolved at
    runtime, often used for performance optimization or selecting architecture-specific
    implementations.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: R_ALPHA_IRELATIVE
  definition: A dynamic relocation type specific to the Alpha architecture, used for
    resolving indirect function addresses at runtime.
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and run at any memory
    address without modification.
- term: dynamic linker
  definition: A system component that resolves dynamic dependencies (shared libraries)
    when a program is loaded into memory or during runtime.
- term: C library startup code
  definition: The initial code executed when a program starts, responsible for setting
    up the environment before the main function is called. This includes handling
    dynamic linking.
series_id: 'binutils:alpha: reject a non-zero addend on a reference to an ifunc'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-11-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch removes the alpha target from the skip list in `ld-ifunc/ifunc.exp`, thereby enabling the indirect function (IFUNC) tests for alpha. The tests were run using an alpha-linux-gnu cross toolchain, and only the linker tests were supported in that configuration. One test, `ifunc-26`, is expected to continue failing due to known limitations related to `.set` directives and assembly modes.
