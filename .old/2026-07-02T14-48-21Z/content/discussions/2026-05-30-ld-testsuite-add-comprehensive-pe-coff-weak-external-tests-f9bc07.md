---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- ld
- testsuite
- PE COFF
- weak symbols
discussion_id: 20260530191522.57144-4-peter0x44@disroot.org
source_type: public_inbox
title: '[PATCH 3/3] ld/testsuite: Add comprehensive PE COFF weak external tests'
headline: 'Ld/testsuite: Add comprehensive PE COFF weak external tests'
tldr: Adds a comprehensive test suite for PE COFF weak externals to cover various
  interactions between weak and strong symbols.
proposer: Peter Damianov <peter0x44@disroot.org>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased test coverage vs. increased maintenance burden for new tests.
exchanges:
- author: Peter Damianov <peter0x44@disroot.org>
  role: proposer
  position: Adds tests for PE COFF weak externals covering normal, weak-undef, weak-defined,
    weak-decl-weak-def, weak-use, weak-override, weak-duplicate, weak-def-override,
    and weak-def-use scenarios.
  quote: 'Add tests covering the full matrix of weak/strong symbol interactions

    for PE COFF weak externals, based on testcases by Martin Storsjo.'
primer_expert: Adds ``ld-pe/pe-compile.exp`` which compiles source files, links via
  gcc, and runs the linked binary natively (if possible). Adds new testcases to ``ld-pe``
  to increase test coverage of weak symbols.
primer_general: This patch adds tests for the linker (ld) when handling PE COFF files,
  a common format for executables and object code on Windows.  The tests focus on
  'weak symbols,' which are optional symbol definitions that the linker may or may
  not include in the final executable.  These tests ensure that the linker correctly
  handles different scenarios involving weak symbols, such as when a weak symbol is
  defined, undefined, or overridden by a strong symbol. These tests prevent unexpected
  behavior or errors when linking code that uses weak symbols in PE COFF format.
series_id: 'binutils:ld/testsuite: add comprehensive pe coff weak external tests'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260530191522.57144-4-peter0x44@disroot.org
bugzilla_url: null
date: '2026-05-30'
is_stub: false
---

This patch adds a comprehensive test suite for PE COFF weak externals, covering the matrix of interactions between weak and strong symbols. The tests are based on existing testcases by Martin Storsjo. These tests aim to ensure correct linker behavior when dealing with weak symbols in PE COFF objects.
