---
project: binutils
subsystem: binutils/configure
patch_id: null
tags:
- build
- configure
- msgpack
- library
discussion_id: c7c689e7-fb1d-4087-af0e-621009ef6642@efficios.com
source_type: public_inbox
title: 'Re: [PATCH] binutils/configure: look for msgpack-c.pc (in addition to msgpack.pc)'
headline: Confirms fix for msgpack configure script
tldr: Simon Marchi confirms that a patch addressing msgpack detection in binutils
  configure script has fixed the issue.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: other
  position: Confirms that the patch fixing msgpack detection has resolved the issue.
  quote: null
primer_expert: This thread confirms a fix in the binutils configure script (`configure.ac`)
  related to detecting the `msgpack` library. The `PKG_CHECK_MODULES` macro is used
  to locate the library's pkg-config file (`.pc`), which provides necessary compiler
  and linker flags. The patch ensures that both the old and new names (`msgpack.pc`
  and `msgpack-c.pc`) are checked, avoiding build failures when `msgpack` is present.
primer_general: When building software, configure scripts are used to check for the
  presence of required libraries and set up the build environment. This discussion
  concerns a fix to the binutils configure script that ensures it can correctly find
  the `msgpack` library. The fix addresses a change in the library's packaging, ensuring
  that binutils can be built with `msgpack` support when it is available on the system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c7c689e7-fb1d-4087-af0e-621009ef6642@efficios.com
bugzilla_url: null
date: '2026-05-18'
is_stub: false
---

Simon Marchi confirms that a patch addressing the detection of the `msgpack` library in the binutils configure script has resolved the reported issue. The patch modifies the `configure.ac` file to check for both `msgpack-c.pc` and `msgpack.pc`, accommodating a renaming that occurred in the library's packaging. This ensures that the build process can correctly identify and utilize the `msgpack` library when it is available.
