---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- testsuite
- elf
- integer-overflow
discussion_id: alyKoJflxVaaOlLY@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] ld: testsuite: Fix integer overflow in ld/testsuite/ld-elf/init-mixed.c.'
headline: 'ld testsuite: Fix integer overflow in init-mixed.c'
tldr: Alan Modra commits a fix to an ld testsuite file, renaming a variable and using
  smaller values to avoid integer overflows.
proposer: Alan Modra <amodra@gmail.com>
consensus: Committed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Choosing between using a wider integer type (`int32_t`) to directly accommodate
  larger values and resizing the variable and its test values to be safe across different
  `int` widths.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Submitted a patch to fix an integer overflow in a testsuite file by using
    `int32_t` to ensure correct behavior across different `int` sizes.
  quote: The code assumes that int is 32 bits wide (see e.g. line 97), which is not
    necessarily true.
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Accepted a different fix by renaming the variable to `order` and using
    small values to avoid overflow on 16-bit `int` targets, aligning with past commits.
  quote: 'Fair enough, but I''m going to commit the following instead.


    The variable isn''t a counter so rename it, and use small values that won''t overflow
    a target with 16-bit int.'
primer_expert: '`ld/testsuite/ld-elf/init-mixed.c` tests the interaction of sections
  like `.init_array` and `.fini_array` across different object files. The fix addresses
  an integer overflow in a variable used to check the initialization/finalization
  order, ensuring correctness on platforms where `int` might be smaller than 32 bits,
  a scenario enabled by a prior commit.'
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files into executables
    or libraries.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of the software.
- term: integer overflow
  definition: A condition that occurs when an arithmetic operation produces a result
    that exceeds the maximum representable value for the given integer type.
- term: .init_array and .fini_array
  definition: ELF sections used to store pointers to C++ global constructors and destructors,
    respectively, executed before and after main().
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alyKoJflxVaaOlLY@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

This discussion resolves a potential integer overflow issue in an `ld` testsuite file. While the original patch proposed using `int32_t`, the maintainer opted for a different fix: renaming the `count` variable to `order` and using small values (0-6) to prevent overflow, even on targets with 16-bit integers. This change accounts for prior commits that enabled testing on such targets.
