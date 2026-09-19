---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- shared-libraries
- testing
- portability
commit_hash: db54bfba3a0afb93257b9e30ff7fa70207367045
source_type: github
author: Robert Dubner
headline: 'cobol: Change policy for finding shared object files'
tldr: Cobol compiler updates policy for finding .so files and fixes character encoding
  issues in tests.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libgcobol` library now implements a new policy for finding shared
  object (.so) files using `do_the_dl_thing`, `find_in_dirs`, and `__gg__function_handle_from_cobpath`.
  This replaces the previous implicit search mechanism. The DejaGNU tests are updated
  to use 'ibm1140' instead of 'cp1140' for EBCDIC character set tests, as 'ibm1140'
  is more widely supported across different POSIX systems (glibc, FreeBSD, NetBSD).
  Minor fixes in `symbols.cc` and `parse.y` also address corner cases in picture string
  handling and data capacity tests.
primer_glossary:
- term: Cobol
  definition: A compiled programming language designed for business applications.
    GCC includes a front-end for Cobol.
- term: Shared Object (.so)
  definition: A type of library file that contains compiled code and data which can
    be loaded and linked by multiple programs at runtime. Used on Unix-like systems.
- term: Symbol resolution
  definition: The process by which the compiler or linker determines the memory address
    of a symbol (like a function or variable name) that is referenced in the code.
- term: DejaGNU
  definition: A testing framework used by GCC and other GNU projects to test their
    software across various configurations and platforms.
- term: EBCDIC
  definition: Extended Binary Coded Decimal Interchange Code. An older character encoding
    standard used primarily on IBM mainframe and midrange systems.
- term: Character encoding
  definition: A system that assigns a unique number to each character, allowing computers
    to store and process text. Examples include ASCII, UTF-8, and EBCDIC variants
    like cp1140 and ibm1140.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/db54bfba3a0afb93257b9e30ff7fa70207367045
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

The GCC Cobol compiler has updated its policy for searching for shared object (.so) files containing specific symbols. This change aims to improve symbol resolution across different systems, including FreeBSD and NetBSD, by recognizing the 'ibm1140' character encoding instead of 'cp1140'. Additionally, several DejaGNU tests have been updated to reflect this change and fix minor logic or data capacity issues.
