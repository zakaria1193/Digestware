---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- freestanding
- headers
- C++
- ranges
commit_hash: d4ca6c0d87626c0e065525a87ea278bedfceb68d
source_type: github
author: Felix Morgner
headline: 'libstdc++: Add <bits/binders.h> to freestanding headers [PR125112]'
tldr: Fixes freestanding builds of libstdc++ by including <bits/binders.h>.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The libstdc++ build system distinguishes between "hosted" and "freestanding"
  environments. Freestanding environments, indicated by `--disable-libstdcxx-hosted`,
  target systems without an operating system, like embedded systems.  The `<ranges>`
  header, introduced in r16-3575-g1a41e52d7ecb58, depends on `<bits/binders.h>`.  This
  commit updates `include/Makefile.am` to move `<bits/binders.h>` from `bits_headers`
  to `bits_freestanding`, correcting the build configuration and enabling `<ranges>`
  in freestanding mode. This resolves PR125112.
primer_general: The C++ standard library (libstdc++ in GCC) provides a wide range
  of functions and data structures.  Some parts of the library are designed to work
  in any environment, including those without an operating system (so-called "freestanding"
  environments, often used in embedded systems development).  This commit fixes an
  issue where a header file (`<bits/binders.h>`) required by a newer feature (`<ranges>`)
  was not correctly included in the set of headers available in freestanding environments.
  This change ensures that the `<ranges>` feature can be used in these environments,
  expanding the capabilities of C++ for bare-metal and embedded development.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d4ca6c0d87626c0e065525a87ea278bedfceb68d
date: '2026-04-30'
---

This commit fixes a build issue in libstdc++ when using the `--disable-libstdcxx-hosted` option, which configures the library for freestanding environments. The `<ranges>` header, recently added to the freestanding headers, depends on `<bits/binders.h>`.  This commit moves `<bits/binders.h>` to the freestanding headers, resolving the dependency and allowing `<ranges>` to be used in freestanding builds.
