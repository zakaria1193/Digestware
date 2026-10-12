---
project: gcc
subsystem: libdecnumber
patch_id: null
tags:
- libdecnumber
- build
- configure
- cleanup
commit_hash: c6522f8bd570250f49c2c7f9bf9b8e213cabc7c0
source_type: github
author: Sam James
headline: Drop unused configure checks for standard headers from libdecnumber
tldr: Unused checks for standard C89 headers removed from libdecnumber's configure
  script, simplifying the build.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `configure.ac` for libdecnumber has been simplified by removing
  checks for `<ctype.h>`, `<stddef.h>`, and `<stdio.h>`. These headers are part of
  the C89 standard, making explicit checks unnecessary for a C compiler. Furthermore,
  the results of these checks were not being used in the build process.
primer_glossary:
- term: C89
  definition: The 1989 ANSI standard for the C programming language, also known as
    ANSI C or C'90.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c6522f8bd570250f49c2c7f9bf9b8e213cabc7c0
date: '2026-10-09'
is_stub: true
stub_reason: low_score
---

This commit removes configuration checks for standard C89 headers like `<ctype.h>`, `<stddef.h>`, and `<stdio.h>` from the libdecnumber build process. Since these are standard headers guaranteed by C89 and their results were not used, their removal simplifies the configuration script without impacting functionality.
