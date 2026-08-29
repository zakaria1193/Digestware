---
project: binutils
subsystem: lto
patch_id: null
tags:
- lto
- linker
- binutils
- compiler
discussion_id: CAMe9rOooyG9+Uh7Ga=ZiA2nhUzEO8sBZT3vb1Bd5pTMAoxWWag@mail.gmail.com
source_type: public_inbox
title: '[PATCH] lto: Don''t check format of IR dummy file'
headline: 'lto: Skip IR dummy file format check'
tldr: Patch to prevent the linker from checking the format of an IR dummy file during
  LTO processing, fixing PR ld/34572.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Needs Revision
outcome: needs_revision
impact_score: 5
sentiment_score: 4
technical_tradeoffs:
- Removes a potentially unnecessary format check for LTO IR dummy files.
- Increases robustness by allowing empty destination lists in internal functions.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Submits a patch to skip format checks on IR dummy files and handle empty
    DESTLISTs, addressing PR ld/34572.
  quote: '1. Don''t check format of IR dummy file in lang_check.

    2. Allow empty DESTLIST in lang_list_remove_tail.


    PR ld/34572

    * ldlang.c (lang_check): Don''t check format of IR dummy file.

    (debug_file_chain): New.

    (debug_input_files): Use debug_file_chain.

    (lang_list_remove_tail): Also check empty DESTLIST.'
- author: Alan Modra
  role: reviewer
  position: Reports testsuite failures on x86_64-w64-mingw32 after the patch is applied.
  quote: I see testsuite failures on x86_64-w64-mingw32 with this.
- author: H.J. Lu
  role: proposer
  position: States that the patch is being checked after testing on the reported failing
    platform and provides an update on a related PR.
  quote: 'I am checking this patch after testing with x86_64-w64-mingw32.

    Since realdelf is used to check common symbol size in PR ld/34570 tests,

    run PR ld/34570 tests only for ELF targets.


    PR ld/34570

    * testsuite/ld-plugin/lto.exp: Run PR ld/34570 tests only for

    ELF targets.'
- author: Alan Modra
  role: reviewer
  position: Confirms that test failures persist despite the proposed fixes and lists
    specific failing tests.
  quote: 'Fails remain.


    +FAIL: ld-plugin/lto-3r

    +FAIL: ld-plugin/lto-4r-a

    +FAIL: ld-plugin/lto-4r-b

    +FAIL: ld-plugin/lto-4r-c

    +FAIL: ld-plugin/lto-4r-d

    +FAIL: ld-plugin/lto-5r

    +FAIL: ld-plugin/lto-10r

    +FAIL: PR ld/19317 (2)

    +FAIL: LTO 3b

    +FAIL: PR ld/19317 (3)


    ld-plugin/dummy.s: Assembler messages:

    ld-plugin/dummy.s:1: Error: junk at end of line, first unrecognized character
    is `-`'
primer_expert: This patch addresses a problem in the GNU linker's handling of Link-Time
  Optimization (LTO) input, specifically related to intermediate representation (IR)
  files. The linker normally checks the format of input files. However, for LTO, dummy
  IR files are used, and their format check can fail erroneously. This patch modifies
  `ldlang.c` to skip this format check for dummy IR files. It also relaxes a check
  in `lang_list_remove_tail` to handle empty lists. The changes are motivated by a
  specific bug report (PR ld/34572) and associated test failures on platforms like
  MinGW.
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compiler optimization technique where the
    compiler performs optimizations not just within a single source file, but across
    all source files of a program during the linking stage.
- term: IR
  definition: Intermediate Representation. A data structure or code format used internally
    by a compiler or toolchain to represent source code during various stages of translation
    and optimization.
- term: dummy file
  definition: In this context, a placeholder file used during LTO processing that
    may not conform to standard object file formats but serves a specific purpose
    in the toolchain pipeline.
- term: DESTLIST
  definition: Likely refers to a destination list or data structure used within the
    linker's language handling code, possibly for managing output files or symbols.
- term: PR ld/34572
  definition: A bug report filed against the GNU linker (ld), identified by number
    34572.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOooyG9+Uh7Ga=ZiA2nhUzEO8sBZT3vb1Bd5pTMAoxWWag@mail.gmail.com
bugzilla_url: null
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

H.J. Lu submits a patch to address PR ld/34572, which involves Link-Time Optimization (LTO). The patch modifies `ldlang.c` to avoid checking the format of an Intermediate Representation (IR) dummy file within the `lang_check` function. Additionally, it allows for an empty `DESTLIST` in `lang_list_remove_tail`. The changes aim to resolve testsuite failures observed on specific platforms like x86_64-w64-mingw32.
