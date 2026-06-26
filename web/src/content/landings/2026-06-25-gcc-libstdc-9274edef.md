---
project: gcc
subsystem: gcc/libstdc++
patch_id: null
tags:
- c++
- modules
- libstdc++
- build-system
- bugfix
commit_hash: 9274edef95ab1b74b82f4a9cf14baa9004e03c0d
source_type: github
author: Jakub Jelinek
headline: Libstdc++ corrects symlink installation for bits/std.cc module
tldr: GCC's libstdc++ build process now correctly installs the `std.cc` symlink within
  the `bits` directory, fixing module test failures.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change addresses a build system regression in `libstdc++` related
  to C++23 modules. Specifically, the `stamp-modules-bits` target in `src/c++23/Makefile.am`
  was using `abs_srcdir` to create a symlink for `std.cc` within the `$(top_builddir)/include/bits`
  directory. The `std.cc` file is generated from `std.cc.in` during the build process
  and resides in the build directory, not the source directory. This led to broken
  symlinks and subsequent failures in module tests. The fix replaces `abs_srcdir`
  with `abs_builddir` to ensure the symlink correctly points to the generated `std.cc`
  in the bu…
primer_general: When you compile C++ code that uses standard library features (like
  `std::vector`), it often relies on the `libstdc++` library. Modern C++ also includes
  "modules," which are a new way to organize and compile code more efficiently than
  traditional header files. This commit fixes a problem in how GCC's `libstdc++` is
  built, specifically concerning these C++ modules. During the build process, a special
  link (called a symlink) that pointed to a file named `std.cc` was being created
  incorrectly. Instead of pointing to the version of `std.cc` that was actually created
  during the build, it was pointing to a non-existent file, causing various C++ module
  tests to fail. The fix ensures that this link points to the correct, generated file,
  which means the C++ modules can now be used and tested properly.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9274edef95ab1b74b82f4a9cf14baa9004e03c0d
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This commit fixes an issue in the libstdc++ build process where the `std.cc` symlink was incorrectly generated, causing C++ module tests to fail. Previously, the symlink pointed to a non-existent source directory within the build tree. The corrected build now ensures the symlink points to the properly generated `std.cc` file in the build directory, resolving failures related to C++23 modules.
