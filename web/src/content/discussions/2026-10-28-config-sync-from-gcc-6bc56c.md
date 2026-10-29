---
project: binutils
subsystem: config
patch_id: null
tags:
- build system
- autoconf
- maintenance
- lto
discussion_id: 20261028220548.84273-2-pietro@sociotechnical.xyz
source_type: public_inbox
title: '[COMMITTED] config: Sync from GCC'
headline: 'config: Sync from GCC'
tldr: Updates binutils configuration files by syncing recent changes from GCC's repository.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Proposed
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Pietro Monteiro <pietro@sociotechnical.xyz>
  role: proposer
  position: Commits updates to binutils' configuration files by syncing multiple changes
    from GCC, including autoconf macros and LTO-related flags.
  quote: "Sync the following changes from GCC and regenerate all autoconf files.\n\
    \ncommit 3d61ec632f9292fb7642865d8b588bb82d51d466\nAuthor: Sam James <sam@gentoo.org>\n\
    Date:   Sun Oct 11 20:15:54 2026 +0100\n\n    config: sync ax_check_define.m4\
    \ from autoconf-archive\n\n    config/ChangeLog:\n\n    \t* ax_check_define.m4:\
    \ Update to serial 12.\n\ncommit 9d3338579f6448dcffa6f0b818c45374f925f3d5\nAuthor:\
    \ Zhongteng Gui <dr…"
primer_expert: This commit integrates several updates from GCC's configuration system
  into binutils. It synchronizes `ax_check_define.m4` to its latest version from the
  autoconf-archive, updates build flags for mingw targets related to LTO (`-ffat-lto-objects`),
  and modifies `hwcaps.m4` to use `LT_PATH_LD` instead of `AC_PROG_LD`. These are
  routine maintenance actions for build system components shared between GCC and binutils.
primer_glossary:
- term: LTO
  definition: Link Time Optimization. A compiler optimization technique that allows
    optimizations to be performed across multiple translation units during the linking
    phase, potentially leading to significant performance improvements.
- term: mingw
  definition: Minimalist GNU for Windows. A development environment and set of tools
    that allow the creation of native Windows applications using the GNU Compiler
    Collection.
- term: autoconf-archive
  definition: A repository of useful Autoconf macros that are not part of the standard
    Autoconf distribution, providing reusable snippets for common build system tasks.
- term: AC_PROG_LD
  definition: An Autoconf macro used to find the system's linker. It is often superseded
    by other macros depending on the specific requirements.
- term: LT_PATH_LD
  definition: A macro used in build systems, often related to libtool, to determine
    the path to the linker.
- term: build system
  definition: The collection of tools and processes used to transform source code
    into executable programs or libraries. This includes compilers, linkers, and build
    automation tools like Make or Autoconf.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261028220548.84273-2-pietro@sociotechnical.xyz
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit brings several updates to binutils' configuration system by synchronizing changes from GCC. Notable updates include syncing `ax_check_define.m4` from the autoconf-archive, adding `-ffat-lto-objects` for mingw targets in `bootstrap-lto-lean.mk`, and updating `AC_PROG_LD` to `LT_PATH_LD` in `hwcaps.m4`. These changes ensure binutils' build environment remains current with related projects and addresses specific build-related issues.
