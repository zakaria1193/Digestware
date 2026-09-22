---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- Windows
- portability
- testsuite
- file handling
discussion_id: bca8c37d-95a0-4c6a-87e7-b97241a34c4b@o2.pl
source_type: public_inbox
title: '[RFC] gas: testsuite: How to fix gas/all/pr27381 on Windows?'
headline: 'gas: testsuite: How to fix gas/all/pr27381 on Windows?'
tldr: Discussion on how to fix a failing gas testcase (pr27381) on Windows due to
  differences in `fopen` and `fstat` behavior compared to POSIX systems.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- XFAILing the test sacrifices correctness verification on Windows.
- Modifying the regex is a minimal change but might mask other issues.
- Adding a `stat` check before `fopen` increases code complexity but improves cross-platform
  robustness.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Asks for community advice on fixing a failing gas testcase on Windows,
    presenting three potential solutions.
  quote: 'This test case fails on Windows because the following code from gas/read.c:


    [...] FILE * f = fopen (filename, FOPEN_RB); [...] returns NULL on Windows and
    non-NULL value on POSIX-compliant systems (assuming that filename exists and refers
    to a directory).'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the problem description regarding `fopen` and `fstat` behavior
    differences on Windows.
  quote: "On 21.09.2026 14:53, Jan Dubiec wrote:\n> This test case fails on Windows\
    \ because the following code from gas/read.c:\n> \n> [...] FILE *\n> search_and_open\
    \ (const char *filename, char *path)\n> {\n>    FILE *f = fopen (filename, FOPEN_RB);\n\
    > [...] \n> \n> returns NULL on Windows and non-NULL value on POSIX-compliant\
    \ systems \n> (assuming that filename exists and refers to a directory)."
primer_expert: The `gas/all/pr27381` test case in Binutils is failing on Windows due
  to differences in how `fopen` and `fstat` interact with directory paths across platforms.
  On POSIX systems, `fopen` might return a valid file pointer for a directory, which
  `fstat` then correctly identifies as non-regular. On Windows, `fopen` is more restrictive
  and returns `NULL` for directories, leading to a different error path. The core
  of the issue is platform-specific file handling in `search_and_open` and subsequent
  validation in `s_incbin`. The RFC explores options ranging from simply marking the
  test as expected to…
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, which translates
    assembly language into object files.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of software.
- term: pr27381
  definition: A specific problem report (likely from a bug tracking system) number
    27381, which this test case aims to address or verify.
- term: Windows
  definition: Microsoft's proprietary graphical operating system.
- term: POSIX
  definition: Portable Operating System Interface, a family of standards specified
    by the IEEE for maintaining compatibility between operating systems.
- term: fopen
  definition: A C standard library function that opens a file stream.
- term: fstat
  definition: A C standard library function that retrieves file status information.
- term: S_ISREG
  definition: A macro that checks if a stat structure's mode indicates a regular file.
- term: S_ISDIR
  definition: A macro that checks if a stat structure's mode indicates a directory.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/bca8c37d-95a0-4c6a-87e7-b97241a34c4b@o2.pl
bugzilla_url: null
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

Jan Dubiec is seeking community input on how to fix the `gas/all/pr27381` test case, which fails on Windows. The failure stems from platform-specific behavior of `fopen` and subsequent `fstat` calls when handling file paths, leading to different error messages and control flow than on POSIX systems. Three potential solutions are proposed: XFAILing the test on Windows, adjusting the expected regular expression, or adopting a more involved approach by checking file types with `stat` before opening.
