---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- testsuite
- dejagnu
- bug
- testing
discussion_id: 8259bf0c-ea86-4c9d-a4fb-e8d135470edc@o2.pl
source_type: public_inbox
title: A bug in get_board_flags fin ld/testsuite/lib/ld-lib.exp
headline: Bug in get_board_flags for ld testsuite
tldr: Bug in DejaGnu testsuite helper for ld, where get_board_flags incorrectly returns
  empty flags due to an empty target_info name.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Testsuite configuration is broken for certain targets.
- Fix requires understanding DejaGnu's internal state management.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Reports a bug in `get_board_flags` where it returns empty CFLAGS/LDFLAGS
    because `[target_info name]` is empty during test execution. Seeks assistance
    to fix the DejaGnu logic.
  quote: 'What is the get_board_flags procedure in ld/testsuite/lib/ld-lib.exp supposed
    to do? Return the cflags and ldflags defined in the board description file, right?
    But it doesn''t seem to do that.


    Unfortunately, I don''t know enough about DejaGnu''s target/board handling to
    figure out how this should be fixed, so I''d appreciate some help from someone
    more experienced. Some information is provided belo…'
primer_expert: This discussion highlights a problem in the DejaGnu testsuite for the
  GNU linker (`ld`). Specifically, the `get_board_flags` helper function, responsible
  for setting up target-specific CFLAGS and LDFLAGS from board configurations, fails.
  The root cause appears to be that `[target_info name]` is evaluating to an empty
  string within the test context, preventing `board_info` from correctly retrieving
  the flags. The contributor has added diagnostic `verbose` statements to illustrate
  the issue.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or library.
- term: DejaGnu
  definition: A testing framework for C programs, often used for toolchains. It provides
    a high-level interface for running tests and examining results.
- term: ld/testsuite/lib/ld-lib.exp
  definition: A Tcl script file within the binutils source tree that contains helper
    procedures and configurations for testing the GNU linker.
- term: get_board_flags
  definition: A function within the DejaGnu test framework that retrieves board-specific
    compiler and linker flags.
- term: target_info name
  definition: A DejaGnu Tcl variable or command that should hold the name of the current
    target system being tested.
- term: board_info
  definition: A DejaGnu function that accesses configuration information for a specific
    target board.
- term: CFLAGS
  definition: Compiler flags passed to the C compiler.
- term: LDFLAGS
  definition: Linker flags passed to the linker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8259bf0c-ea86-4c9d-a4fb-e8d135470edc@o2.pl
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Jan Dubiec identified a bug in the `get_board_flags` procedure within binutils' ld testsuite (`ld/testsuite/lib/ld-lib.exp`). The procedure is intended to retrieve compiler and linker flags from board descriptions but fails because `[target_info name]` returns an empty string, causing it to incorrectly return empty flags. The author seeks help to fix this DejaGnu-related issue.
