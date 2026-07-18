---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- testing
- Windows
- portability
discussion_id: 20260717101723.1022175-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] ld: testsuite: Fix a few backslash-related issues on MinGW.'
headline: 'ld: testsuite: Fix a few backslash-related issues on MinGW.'
tldr: Fixes ld test cases on MinGW that fail due to incorrect use of backslashes in
  file paths.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Fixing test cases to use platform-specific path separators maintains strict adherence
  to OS conventions but increases test complexity.
- Modifying `ld` to always use forward slashes would simplify path handling but might
  deviate from native Windows conventions.
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Submits a patch to fix test case failures on MinGW related to backslash
    usage in file paths.
  quote: 'Several relatively new test cases fail on MinGW: [...] This is because on
    Windows ld uses "\" instead of "/" to create full file names as shown in the log
    below:'
- author: Jan Beulich
  role: reviewer
  position: Questions if `ld` could use forward slashes consistently, even on Windows,
    to avoid such issues.
  quote: 'Yet: Does it need to? If slashes work, can''t ld simply use slashes?'
- author: Maciej W. Rozycki
  role: reviewer
  position: Seconded Jan Beulich's question about the root cause of the backslash
    usage.
  quote: 'Seconded: what''s the root cause, i.e. where does the backslash exactly

    come from?'
- author: Jan Dubiec
  role: proposer
  position: Explains that the backslash originates from the linker's construction
    of file names.
  quote: "From the linker. It is invoked as follows:\n/d/Works/xcomp/build-binutils-h8300-mingw/ld/ld-new\
    \    -o tmpdir/absc \n-L/d/Works/binutils/ld/testsuite/ld-archive -e ff tmpdir/abc.o\
    \ \n/d/Works/binutils/ld/testsuite/ld-archive/ab.t --verbose --print-map\n\nFor\
    \ each library listed in ld/testsuite/ld-archive/ab.t, the linker \ntakes the\
    \ library name, prepends the libr"
- author: Jan Dubiec
  role: proposer
  position: Clarifies that the tools built with MinGW are native Windows executables
    and use the WinAPI, which can behave differently depending on the shell.
  quote: "Don't ask me — I wasn't involved in porting the GNU tools to \nWindows/MinGW.\
    \ :-) \n\nIn any case, the tools built with MinGW are native Windows executables.\
    \ \nThey use the WinAPI directly, without a compatibility layer such as \nCygwin.\
    \ As a result, they can be invoked either from a Unix-like shell \nor from the\
    \ rather crappy native"
primer_expert: This patch addresses a cross-platform compatibility issue in the `ld`
  test suite, specifically on the MinGW (Minimalist GNU for Windows) environment.
  Native Windows executables, like those built by MinGW, often use backslashes (`\`)
  as path separators, whereas Unix-like systems and consequently many test scripts
  use forward slashes (`/`). The test cases in `ld/testsuite/ld-archive/archive.exp`
  were failing because `ld` was generating paths with backslashes, which the test
  harness did not expect. The discussion revolves around whether `ld` should be modified
  to always use forward slashes or if…
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component.
- term: MinGW
  definition: Minimalist GNU for Windows, a software development environment that
    allows the development of native Windows applications using the GNU Compiler Collection.
- term: backslash
  definition: The '\' character, commonly used as a path separator in Windows file
    systems.
- term: forward slash
  definition: The '/' character, commonly used as a path separator in Unix-like file
    systems.
- term: WinAPI
  definition: The Windows API (Application Programming Interface), a collection of
    functions and data structures used by Windows applications to interact with the
    operating system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260717101723.1022175-1-jdx@o2.pl
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

Several test cases in the `ld` test suite are failing on MinGW due to incorrect path handling. On Windows, paths are typically constructed using backslashes (`\`). The test cases, however, are expecting forward slashes (`/`). The patch aims to correct this by ensuring that file paths are generated in a way that is compatible with MinGW's environment. The discussion involves questions about whether `ld` could simply use forward slashes universally, even on Windows, to simplify path handling.
