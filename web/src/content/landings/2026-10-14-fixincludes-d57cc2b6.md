---
project: gcc
subsystem: fixincludes
patch_id: null
tags:
- build
- c89
- standard
commit_hash: d57cc2b674a38df8f65608f2ca0c9dbd2c3017fa
source_type: github
author: Sam James
headline: 'fixincludes: Assume errno for C89'
tldr: GCC's fixincludes now assumes errno is available for C89.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Modifies fixincludes to remove checks for 'errno', assuming its availability
  for C89 targets as per PR bootstrap/112422. This involves regenerating configure
  scripts and updating system.h by removing the fallback for errno. The change aligns
  the build infrastructure with C89 standard assumptions.
primer_glossary:
- term: errno
  definition: A standard C macro that holds the error code set by certain library
    functions when they fail. It is typically defined in <errno.h>.
- term: fixincludes
  definition: A GCC subsystem responsible for adjusting system header files to be
    compatible with GCC, especially on older or non-standard systems.
- term: C89
  definition: The 1989 version of the ANSI C standard, also known as ANSI C or C90.
    It established a baseline for the C programming language.
- term: configure.ac
  definition: The main input file for autoconf, describing how to configure the build
    environment for a program. It contains macros that generate the configure script.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d57cc2b674a38df8f65608f2ca0c9dbd2c3017fa
date: '2026-10-14'
is_stub: true
stub_reason: low_score
---

This commit updates the fixincludes build process to assume that the 'errno' macro is available for C89 targets. It removes checks for 'errno' in configure.ac and system.h, simplifying the build by relying on the C89 standard's guarantees. This change is part of a larger effort to align GCC's configuration with C89 compliance.
