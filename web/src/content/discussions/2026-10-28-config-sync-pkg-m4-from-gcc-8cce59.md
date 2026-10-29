---
project: binutils
subsystem: config
patch_id: null
tags:
- build system
- autoconf
- maintenance
discussion_id: 20261028220341.84076-2-pietro@sociotechnical.xyz
source_type: public_inbox
title: '[PATCH] config: Sync pkg.m4 from GCC'
headline: 'config: Sync pkg.m4 from GCC'
tldr: Updates binutils' `pkg.m4` to use `AC_LINK_IFELSE` instead of the obsolete `AC_TRY_LINK`.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs: []
exchanges:
- author: Pietro Monteiro <pietro@sociotechnical.xyz>
  role: proposer
  position: Submits a patch to sync `pkg.m4` from GCC, updating an obsolete Autoconf
    macro and noting that it does not change generated files.
  quote: 'Sorry I missed this patch had been reviwed: https://inbox.sourceware.org/gcc-patches/20250530213858.59471-1-pietro@sociotechnical.xyz/t/


    I regenerated all autoconf files after applying the patch and there''s no

    changes.'
- author: Pietro Monteiro <pietro@sociotechnical.xyz>
  role: maintainer
  position: Follows up to clarify that the patch should have been marked as committed.
  quote: Sorry, meant to tag this patch as committed.
primer_expert: This patch updates the `PKG_CHECK_MODULES` macro in `config/pkg.m4`
  by replacing `AC_TRY_LINK` with `AC_LINK_IFELSE`. This aligns binutils' build system
  configuration with modern Autoconf practices, as `AC_TRY_LINK` is deprecated. The
  change originates from a corresponding commit in GCC's tree and is a routine maintenance
  update to the build infrastructure, ensuring compatibility and correctness of the
  autoconf-generated scripts.
primer_glossary:
- term: Autoconf
  definition: A tool that automatically configures source code packages to adapt to
    a specific operating system or environment. It generates shell scripts to probe
    the system for required features and libraries.
- term: AC_TRY_LINK
  definition: An obsolete Autoconf macro used to check if a C program can be linked.
    It has been replaced by more specific and robust macros like AC_LINK_IFELSE.
- term: AC_LINK_IFELSE
  definition: An Autoconf macro used to check if a program can be compiled and linked.
    It is the recommended replacement for AC_TRY_LINK.
- term: PKG_CHECK_MODULES
  definition: An Autoconf macro, often provided by pkg-config, used to find and link
    against external libraries.
- term: pkg.m4
  definition: A file containing Autoconf macros related to package checking, often
    used for handling dependencies.
- term: autoconf-archive
  definition: A repository of useful Autoconf macros that are not part of the standard
    Autoconf distribution.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261028220341.84076-2-pietro@sociotechnical.xyz
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch synchronizes the `pkg.m4` file from GCC's repository into binutils. The update replaces the obsolete `AC_TRY_LINK` macro with the recommended `AC_LINK_IFELSE` within the `PKG_CHECK_MODULES` macro. This change is part of ongoing maintenance to keep configuration scripts current with Autoconf best practices. The author confirmed that regenerating autoconf files after applying this patch resulted in no changes to the generated files.
