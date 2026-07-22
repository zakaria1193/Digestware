---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- testsuite
- integer overflow
- c
discussion_id: 9c15be6c-77a8-4817-9fa7-7c88e9f638eb@suse.com
source_type: public_inbox
title: 'Re: [PATCH] ld: testsuite: Fix integer overflow in ld/testsuite/ld-elf/init-mixed.c.'
headline: 'ld: testsuite: Fix integer overflow in ld/testsuite/ld-elf/init-mixed.c.'
tldr: Jan Beulich agrees with a patch fixing an integer overflow in a binutils linker
  test case, noting such assumptions are common.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Correctness of test cases.
- Portability and robustness of code relying on assumed integer sizes.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Agrees with the patch fixing an integer overflow in a test case, acknowledging
    that assumptions about 'int' size are widespread in binutils.
  quote: 'In general I agree, yet I''m certain there are many instances of this assumption

    throughout binutils sources.'
- author: Jan Dubiec
  role: contributor
  position: Submitted the original patch identifying the integer overflow issue.
  quote: 'The code assumes that int is 32 bits wide (see e.g. line 97), which is

    not necessarily true.'
primer_expert: This discussion concerns a test case within the binutils linker (`ld`)
  test suite, specifically `ld/testsuite/ld-elf/init-mixed.c`. A patch was submitted
  to address an integer overflow bug caused by the test code assuming `int` is always
  32 bits. Jan Beulich, a reviewer, agreed with the fix but noted that this assumption
  is a common pattern across the binutils codebase, implying that more systemic fixes
  might be necessary.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or library.
- term: testsuite
  definition: A collection of tests designed to verify the correct functionality of
    a software package.
- term: integer overflow
  definition: A condition that occurs when an arithmetic operation produces a result
    that exceeds the maximum value that can be stored in a variable of a fixed size.
- term: int
  definition: A fundamental integer data type in C and C++. Its size (e.g., 16, 32,
    or 64 bits) is platform-dependent, though often 32 bits on common systems.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/9c15be6c-77a8-4817-9fa7-7c88e9f638eb@suse.com
bugzilla_url: null
date: '2026-07-20'
is_stub: false
stub_reason: ''
---

Jan Beulich acknowledges a patch intended to fix an integer overflow in a binutils linker test case (`ld/testsuite/ld-elf/init-mixed.c`). The original patch noted that the code assumed `int` was 32 bits, which isn't always true. Beulich agrees with the problem but points out that similar assumptions about `int` size are prevalent throughout the binutils source code.
