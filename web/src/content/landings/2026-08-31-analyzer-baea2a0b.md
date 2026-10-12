---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- c
commit_hash: baea2a0be30d843febce3b40543aa93f91018444
source_type: github
author: Torbjörn SVENSSON
headline: Analyzer follows macro aliases for named constants
tldr: Analyzer now correctly handles macro aliases for named constants, fixing test
  failures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The analyzer's redundant flag detection in r17-177-g9a5f89005dc49d
  required named constants to resolve to numerical values. This commit extends that
  capability to handle macro aliases, such as `O_CREAT` being an alias for `_FCREAT`.
  A depth limit for alias resolution is configurable via `analyzer-max-macro-alias-depth`.
  This addresses issues in `mkostemp` and `mkostemps` test cases.
primer_glossary:
- term: static analyzer
  definition: A tool within the compiler that analyzes code without executing it to
    find potential errors, such as logic flaws or memory leaks. It operates on an
    intermediate representation of the code.
- term: macro alias
  definition: A macro definition that simply renames another macro or a constant value.
    For example, `#define NEW_NAME OLD_NAME`.
- term: named constant
  definition: A symbolic name given to a fixed value, typically defined using `#define`
    in C/C++ or `const`.
- term: libc
  definition: The standard C library, providing fundamental functions for input/output,
    memory management, string manipulation, and more. Examples include glibc, newlib,
    and picolibc.
- term: ODR
  definition: One Definition Rule. A C++ rule stating that non-inline functions and
    variables must have exactly one definition in the program.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/baea2a0be30d843febce3b40543aa93f91018444
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

The static analyzer can now follow macro aliases when evaluating named constants. This change improves the analyzer's ability to detect redundant flags by allowing it to resolve constants defined through macros like O_CREAT _FCREAT, which are used in libc implementations. This fix resolves several test failures related to macro aliasing.
