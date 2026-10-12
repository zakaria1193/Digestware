---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- testing
- PE/COFF
- XCOFF
discussion_id: 20261008121221.1662355-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH] ld: add PE/COFF and XCOFF64 aux symbol overrun tests'
headline: 'ld: add PE/COFF and XCOFF64 aux symbol overrun tests'
tldr: Adds tests for linker symbol table bounds checking in PE/COFF and XCOFF64 formats.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increases test suite size and execution time.
- Ensures robustness by adding coverage for edge cases and malformed inputs.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes adding new test cases to cover PE/COFF and XCOFF64 aux symbol
    overrun scenarios, building upon previous work for 32-bit XCOFF.
  quote: 'This patch adds regression test coverage for commit 335d76afde5.

    Commit 335d76afde5 validates symbol table bounds before the linker

    walks symbols in cofflink.c and xcofflink.c. The original commit

    added regression tests for 32-bit XCOFF only.


    This change adds 9 new tests (6 malformed and 3 positive controls),

    bringing the xcoff-aux and coff-aux tests to 16 in total:'
primer_expert: This patch adds test cases to ld/testsuite/ld-pe/coff-aux.exp and ld/testsuite/ld-powerpc/xcoff-aux.exp.
  It specifically targets the `cofflink.c` and `xcofflink.c` files within the linker,
  focusing on the validation of `n_numaux` fields in symbol table entries for PE/COFF
  and XCOFF64 object formats. The goal is to ensure that malformed symbol table data
  does not lead to crashes or incorrect linker behavior, as was addressed in commit
  335d76afde5.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, a file format used for
    executables, object code, and DLLs on 32-bit and 64-bit versions of Windows.
- term: XCOFF
  definition: Extended Common Object File Format, an object file format used on AIX
    systems.
- term: symbol table
  definition: A data structure used by a linker or debugger to store information about
    symbols (e.g., function names, variable names) defined in an object file or executable.
- term: n_numaux
  definition: A field in the XCOFF symbol table entry that indicates the number of
    auxiliary entries associated with the symbol.
- term: linker
  definition: A program that combines various pieces of code and data from object
    files into a single executable program.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261008121221.1662355-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

This patch introduces new regression tests for linker symbol table bounds checking, specifically for PE/COFF and XCOFF64 formats. The tests cover malformed inputs that previously caused crashes or incorrect exits, as well as positive control cases. This work follows up on a previous commit that added similar tests for 32-bit XCOFF.
