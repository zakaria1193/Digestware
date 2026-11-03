---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- build
- libtool
- runtime
commit_hash: 06de61c188895df325a4897494f064dbf763eb38
source_type: github
author: Pietro Monteiro
headline: Update obsolete libtool macro for dlopen support
tldr: libgfortran's build configuration updates an obsolete libtool macro for dlopen.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates `libgfortran/configure.ac` to remove the deprecated
  `AC_LIBTOOL_DLOPEN` macro. The functionality is preserved by passing the `dlopen`
  option directly to the `LT_INIT` macro, aligning with current libtool practices
  for enabling dynamic library loading support.
primer_glossary:
- term: libtool
  definition: A script that facilitates the creation of portable shared libraries
    across various operating systems. It abstracts away platform-specific library
    naming and linking conventions.
- term: autoconf
  definition: A tool that automatically configures source code packages to adapt to
    different operating systems and system configurations. It generates shell scripts
    that check for system features and set up build parameters.
- term: configure.ac
  definition: The primary input file for autoconf. It contains macros and directives
    that describe how to configure the package for a specific system.
- term: LT_INIT
  definition: A libtool macro used within `configure.ac` to initialize libtool's build
    environment and options.
- term: dlopen
  definition: A system call that allows a program to load a shared library dynamically
    at runtime. This is useful for modularity and for loading plugins.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/06de61c188895df325a4897494f064dbf763eb38
date: '2026-11-02'
is_stub: true
stub_reason: low_score
---

The build system for libgfortran has been updated to replace the deprecated `AC_LIBTOOL_DLOPEN` macro with the modern approach of passing `dlopen` directly to `LT_INIT`. This change ensures compatibility with newer versions of libtool and maintains correct build configuration for dynamic loading. No functional changes are expected as the macro was called before `LT_INIT`.
