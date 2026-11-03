---
project: gcc
subsystem: libsanitizer
patch_id: null
tags:
- build
- libtool
commit_hash: 9b2bfc93a2d6d82594785818a41b1d37f8be40ef
source_type: github
author: Pietro Monteiro
headline: libsanitizer updates obsolete libtool macro
tldr: libsanitizer's configure script replaces a deprecated libtool macro with the
  current standard, with no functional changes.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Similar to other components, libsanitizer's build scripts are updated
  to replace AC_LIBTOOL_DLOPEN with LT_INIT([dlopen]). This is a routine maintenance
  change for the build system, ensuring it works with current versions of Autoconf
  and Libtool.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9b2bfc93a2d6d82594785818a41b1d37f8be40ef
date: '2026-11-02'
is_stub: true
stub_reason: low_score
---

The libsanitizer build process now uses the current standard for dynamic library loading by replacing the deprecated AC_LIBTOOL_DLOPEN macro with LT_INIT([dlopen]) in configure.ac, addressing PR103459. This change ensures that the build system remains up-to-date with libtool practices. As the obsolete macro was called prior to LT_INIT, its replacement has no functional effect on the library's behavior.
