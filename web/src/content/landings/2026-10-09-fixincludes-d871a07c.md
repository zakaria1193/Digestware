---
project: gcc
subsystem: fixincludes
patch_id: null
tags:
- build
- autoconf
commit_hash: d871a07ca522c4c54139833b9042a662745b7bd8
source_type: github
author: Sam James
headline: 'fixincludes: drop obsolete C functionality test'
tldr: Removes an outdated autoconf macro for checking C 'const' support.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `fixincludes` subsystem is responsible for generating system headers.
  This commit removes the `AC_C_CONST` autoconf macro from `configure.ac`. This macro
  was used to detect if the C compiler correctly supported the `const` keyword. Its
  removal is justified because `AC_C_CONST` was marked as obsolete in Autoconf 2.60,
  and support for `const` is now a baseline requirement for any C compiler capable
  of building GCC.
primer_glossary:
- term: fixincludes
  definition: A GCC build subsystem that generates and installs system-specific header
    files, ensuring compatibility between the compiler and the target operating system's
    C libraries and interfaces.
- term: autoconf
  definition: A tool that automatically configures source code packages to adapt to
    a specific operating system environment. It generates shell scripts to probe system
    characteristics and adapt the build process.
- term: AC_C_CONST
  definition: An Autoconf macro that checks for the presence and correct behavior
    of the `const` keyword in the C language. Its removal indicates that `const` support
    is now considered a standard feature that does not require explicit checking.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d871a07ca522c4c54139833b9042a662745b7bd8
date: '2026-10-09'
is_stub: true
stub_reason: low_score
---

The fixincludes build process no longer needs to check for C's 'const' keyword support using the obsolete AC_C_CONST autoconf macro. This macro was deprecated in autoconf 2.60, and modern C compilers are expected to support 'const'. The change regenerates configuration files.
