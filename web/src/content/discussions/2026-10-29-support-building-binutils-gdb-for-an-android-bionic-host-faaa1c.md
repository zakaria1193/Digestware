---
project: binutils
subsystem: binutils/gdbserver
patch_id: null
tags:
- binutils
- gdb
- android
- bionic
- cross-compilation
discussion_id: 20261029124117.13519-1-oyzawqgcfc@gmail.com
source_type: public_inbox
title: Support building binutils-gdb for an Android (bionic) host
headline: Support building binutils-gdb for an Android (bionic) host
tldr: Enables building binutils-gdb, specifically binutils-gdbserver, for Android
  (bionic) as a host system.
proposer: trcrsired <oyzawqgcfc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Modifies gnulib and libiberty headers, which are often updated as a batch. If these
  changes need to go through the `update-gnulib.sh` script, the approach may need
  to be reworked.
- Introduces platform-specific conditional code to handle differences between Bionic
  and glibc.
exchanges:
- author: trcrsired
  role: proposer
  position: Submits a patch series to support building binutils-gdb for an Android
    (bionic) host, detailing several necessary adjustments.
  quote: 'This patch makes binutils-gdb build with --host=aarch64-linux-android30

    against bionic: PATH_MAX is taken from <linux/limits.h>, UINTPTR_WIDTH no

    longer relies on __UINTPTR_WIDTH__, _FORTIFY_SOURCE is not enabled for

    C++, gdbserver auto-detects the auxv types, and gprofng is skipped on

    Android.'
- author: trcrsired
  role: proposer
  position: Further explains the specific build failures encountered with bionic due
    to its differences from glibc and outlines the solutions implemented in the patch.
  quote: "Building with --host=aarch64-linux-android30 failed because bionic is not\n\
    glibc:\n\n- The compiler's <limits.h> does not expose PATH_MAX (bionic defines\
    \ it in\n  <linux/limits.h>), while <sys/param.h> defines MAXPATHLEN as PATH_MAX.\n\
    \  Make PATH_MAX available from libiberty.h and gnulib's pathmax.h for\n  __ANDROID__.\n\
    - bionic's <stdint.h> defines UINTPTR_WIDTH in terms of\n  __UINTPTR_WIDTH__,\
    \ which G…"
primer_expert: 'This patch series targets the build system integration of binutils-gdb
  (specifically gdbserver) for Android''s Bionic libc. It addresses several platform-specific
  differences: `PATH_MAX` is exposed via `<linux/limits.h>` on Bionic, requiring a
  change in libiberty and gnulib; `UINTPTR_WIDTH` derivation needed adjustment as
  Bionic''s `<stdint.h>` has a different dependency; and `_FORTIFY_SOURCE` behavior
  for C++ differs. It also makes gdbserver detect auxv types correctly and skips `gprofng`
  on Android.'
primer_glossary:
- term: binutils-gdb
  definition: A combined package that includes the GNU Project Debugger (GDB) and
    related binary utilities like gdbserver. GDB is a debugger, and gdbserver is a
    program that allows remote debugging.
- term: Android (bionic)
  definition: Android's C standard library, which is a fork of BSD libc. It differs
    in some aspects from the more common glibc used on Linux systems.
- term: Host system
  definition: The system on which a program is compiled and executed. In cross-compilation,
    the host system is different from the target system where the final executable
    will run.
- term: PATH_MAX
  definition: A system limit on the maximum length of a pathname that can be used.
    Its definition can vary between operating systems and C libraries.
- term: UINTPTR_WIDTH
  definition: A macro that defines the bit width of the `uintptr_t` type, which is
    an unsigned integer type capable of holding a pointer. Its definition can depend
    on the C library and compiler.
- term: libiberty
  definition: A library of C routines used by various GNU projects, including GCC
    and Binutils, often providing common utility functions not available in standard
    C libraries or specific to the build environment.
- term: gnulib
  definition: A GNU project that aims to provide a portable library of C routines
    and macros, helping to make software behave consistently across different operating
    systems.
series_id: binutils:support building binutils-gdb for an android (bionic) host
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029124117.13519-1-oyzawqgcfc@gmail.com
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch series aims to enable the building of binutils-gdb, particularly the gdbserver component, for an Android (bionic) host system. It addresses several issues related to bionic's differences from glibc, such as the location of `PATH_MAX`, the definition of `UINTPTR_WIDTH`, and the behavior of `_FORTIFY_SOURCE` for C++ builds, and ensures gdbserver correctly detects auxiliary vector types.
