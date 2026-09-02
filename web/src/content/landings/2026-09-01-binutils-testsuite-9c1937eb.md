---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- binutils
- objdump
- testsuite
- regression
commit_hash: 9c1937eb7103bee8c329b9c4f5137fcd1726b23d
source_type: public_inbox
author: Nick Clifton <nickc@sourceware.org>
headline: Add missing files for objdump --map-global-vars test
tldr: Adds necessary files to the testsuite for objdump's --map-global-vars option.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `binutils/testsuite/binutils-all/` directory houses tests for various
  binutils utilities. This change adds `objdump-map-global-vars.c` and `objdump.map-global-vars`.
  The C file defines various global variables (simple types, pointers, enums, structs,
  unions, arrays, function pointers) to be inspected. The `.map-global-vars` file
  contains a regular expression pattern that `objdump --map-global-vars` is expected
  to output when processing the compiled C code. This completes the setup for testing
  the `--map-global-vars` functionality, which lists global symbols and their properties.
primer_glossary:
- term: objdump
  definition: A standard Unix utility that displays information from object files.
    It can show section contents, symbol tables, disassembly, and more.
- term: testsuite
  definition: A collection of tests used to verify the correctness of a software project,
    in this case, the Binutils suite.
- term: global variables
  definition: Variables declared outside of any function, accessible from any part
    of the program.
- term: regular expression
  definition: A sequence of characters that specifies a search pattern. Used here
    for matching the output of objdump.
- term: BZ 34577
  definition: Bugzilla ID 34577, referring to a specific issue tracker entry that
    this commit resolves.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260901104620.1D3424BA23C1@sourceware.org
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This commit introduces two new files to the Binutils testsuite to properly test the `objdump --map-global-vars` option. The files `objdump-map-global-vars.c` and `objdump.map-global-vars` provide the source code for a test program and the expected output, respectively, ensuring this functionality can be verified.
