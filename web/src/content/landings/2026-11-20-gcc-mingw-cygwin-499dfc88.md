---
project: gcc
subsystem: gcc/mingw/cygwin
patch_id: null
tags:
- mingw
- cygwin
- specs
- simplification
commit_hash: 499dfc880d45fe0a04ef1f7986871f661ef131b2
source_type: github
author: Zhongteng Gui
headline: Simplify SHARED_LIBGCC_SPEC for mingw/cygwin targets
tldr: Streamline SHARED_LIBGCC_SPEC for mingw and cygwin using GCC's conditional spec
  syntax.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the `SHARED_LIBGCC_SPEC` in `config/i386/cygwin.h`
  and `config/mingw/mingw32.h` by leveraging the conditional clauses feature of GCC's
  spec language. Instead of multiple separate entries, a single line using `%{S:X;T:Y;:D}`
  syntax now handles shared library selection more compactly. The author also observes
  that mingw's default `SHARED_LIBGCC_SPEC` uses static libgcc, which contradicts
  the 'shared' naming and cygwin's equivalent.
primer_glossary:
- term: SHARED_LIBGCC_SPEC
  definition: A GCC spec string that determines which version of libgcc (shared or
    static) is linked when building shared objects.
- term: spec syntax
  definition: The syntax used in GCC's spec files to define how the compiler driver
    constructs command lines for various stages of compilation and linking.
- term: mingw
  definition: Minimalist GNU for Windows; a set of tools enabling the use of GNU compiler
    tools on Windows.
- term: cygwin
  definition: A POSIX-compatible environment for Windows, providing a Linux-like API
    and tools.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/499dfc880d45fe0a04ef1f7986871f661ef131b2
date: '2026-11-20'
is_stub: true
stub_reason: low_score
---

The SHARED_LIBGCC_SPEC for mingw and cygwin targets has been simplified using GCC's conditional spec syntax (`%{S:X;T:Y;:D}`). This allows for a more concise definition that achieves the same functionality as the previous, more verbose implementation. The change aims to improve readability without altering the functional behavior. It also notes that mingw's default static libgcc for shared builds may be inconsistent with its name and cygwin's behavior.
