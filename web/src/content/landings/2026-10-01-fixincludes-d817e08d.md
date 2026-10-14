---
project: gcc
subsystem: fixincludes
patch_id: null
tags:
- build
- autoconf
commit_hash: d817e08d9ee56bcf43b43acc9f123b717110c766
source_type: github
author: Simon Marchi
headline: 'fixincludes: Add AC_CONFIG_MACRO_DIRS to configure.ac'
tldr: 'fixincludes: Add AC_CONFIG_MACRO_DIRS to configure.ac to enable autoreconf.'
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies the autotools configuration for the fixincludes
  subsystem. By adding AC_CONFIG_MACRO_DIRS to configure.ac, it ensures that the necessary
  macro directories are recognized when regenerating the configuration. This facilitates
  the use of autoreconf, streamlining the build process and maintenance of generated
  files like aclocal.m4.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d817e08d9ee56bcf43b43acc9f123b717110c766
date: '2026-10-01'
is_stub: true
stub_reason: low_score
---

This change adds the AC_CONFIG_MACRO_DIRS call to configure.ac, mirroring the directories specified in ACLOCAL_AMFLAGS. This allows for the regeneration of aclocal.m4 from scratch using autoreconf, which will simplify the autoregen.py script.
