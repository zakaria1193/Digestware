---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- linker
- PE COFF
- weak symbols
- test suite
- binutils
discussion_id: akRWucmJ5Ih535lU@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH 3/3] ld/testsuite: Add comprehensive PE COFF weak external tests'
headline: 'ld/testsuite: Add comprehensive PE COFF weak external tests'
tldr: Tests for PE COFF weak externals have been applied upstream after fixing a build
  configuration issue.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased test coverage for a specific linker feature.
- Ensuring tests correctly target the intended linker version.
- Addressing potential pre-existing issues in object file parsing.
exchanges:
- author: Peter Damianov
  role: proposer
  position: Submitted tests for PE COFF weak externals.
  quote: Add tests covering the full matrix of weak/strong symbol interactions for
    PE COFF weak externals, based on testcases by Martin Storsjo.
- author: Alan Modra
  role: reviewer
  position: Reported test failures on a cross-build environment, specifically around
    duplicate weak definitions and undefined strong symbols with weak definitions.
  quote: 'On a cross build of x86_64-w64-mingw32 from x86_64-linux with gcc 13.2.0-6ubuntu1+26.1
    installed, I see x86_64-w64-mingw32 +FAIL: weak external: strong undef + weak
    def (link) x86_64-w64-mingw32 +FAIL: weak external: duplicate weak defs (link)'
- author: Peter Damianov
  role: contributor
  position: Identified that the reported failures were likely due to the test environment
    using the system's default linker instead of the new one, due to GCC configuration.
  quote: 'ERROR: Your compiler apparently ignores -B when choosing ld. ERROR: Hint:
    don''t configure gcc using --with-ld (or --with-as) ERROR: You will not be testing
    the new ld in many of the following tests. ERROR: It seems you will be testing
    /usr/bin/x86_64-w64-mingw32-ld instead.'
- author: Alan Modra
  role: maintainer
  position: Confirmed reproduction of failures after addressing the build configuration
    issue via symlinks and committed the patchset, noting potential pre-existing buffer
    overflow issues.
  quote: 'Right, I should have checked that before I tried your patch set, and worked
    around the compiler config problem by installing sym-links.


    I have committed your v3 patchset upstream.  I think there are some

    potential buffer overflow problems reading aux entries from fuzzed

    object files, but at least some of those are pre-existing.'
primer_expert: This thread tracks the integration of new test cases for weak external
  symbols in PE COFF object files into the GNU linker's test suite. The tests, originally
  developed by Martin Storsjo, aim to cover the complex interactions of weak and strong
  symbols in this object file format. A key challenge encountered was ensuring the
  test suite actually invoked the newly built linker rather than a system default,
  which required workarounds related to GCC's linker configuration.
primer_glossary:
- term: PE COFF
  definition: Portable Executable Common Object File Format, the executable file format
    used by Microsoft Windows.
- term: Weak External
  definition: A symbol with a special linkage that allows it to be defined in multiple
    places, or not at all, with specific rules for resolving conflicts during linking.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component.
series_id: 'binutils:ld/testsuite: add comprehensive pe coff weak external tests'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/akRWucmJ5Ih535lU@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This discussion covers the addition of comprehensive tests for PE COFF weak external symbols in the GNU linker's test suite. Initial test failures were reported, but later diagnosed as stemming from an incorrect GCC configuration that bypassed the new linker. After resolving this configuration issue, the patch series was committed upstream. Potential pre-existing buffer overflow issues in handling fuzzed object files were also noted.
