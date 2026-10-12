---
project: gcc
subsystem: libdecnumber
patch_id: null
tags:
- libdecnumber
- build
- autoconf
- cleanup
commit_hash: 15e4a5a52e100408b859f44465165ff47078d84f
source_type: github
author: Sam James
headline: Drop obsolete C functionality and unused checks from libdecnumber configuration
tldr: Obsolete Autoconf macro AC_C_CONST and unused configuration checks removed from
  libdecnumber build setup.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `configure.ac` for libdecnumber has been cleaned up by removing
  `AC_C_CONST`, an obsolescent Autoconf macro. Additionally, checks for `off_t` and
  various `sizeof` operations were removed because they are not utilized by the library,
  simplifying the build configuration.
primer_glossary:
- term: AC_C_CONST
  definition: An Autoconf macro used to check for the availability and correct behavior
    of the C `const` keyword.
- term: off_t
  definition: A data type typically used to represent file offsets, often defined
    in `<sys/types.h>`.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/15e4a5a52e100408b859f44465165ff47078d84f
date: '2026-10-09'
is_stub: true
stub_reason: low_score
---

This commit streamlines the libdecnumber build configuration by removing the obsolete Autoconf macro AC_C_CONST and several unused `sizeof` checks. It also removes a search for `off_t` as it is not used within the library. These changes simplify the configuration process and remove unnecessary code.
