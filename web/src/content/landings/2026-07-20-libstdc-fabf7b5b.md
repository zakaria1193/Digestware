---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- abi
- backport
commit_hash: fabf7b5b9ac518635dca5233661a84b0f97063be
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Introduce GLIBCXX_3.4.37 version for symbols not backported
  to GCC-16.'
tldr: New ABI version GLIBCXX_3.4.37 added to libstdc++ for symbols not backported
  to GCC 16.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'libstdc++ ABI management: This commit updates the ABI versioning for
  libstdc++ by introducing GLIBCXX_3.4.37. It backports symbols from GCC 17, specifically
  `chrono::__detail::__recent_leap_second_info`, `basic_format_arg` specializations,
  and `basic_string` internal allocation/creation helpers, ensuring compatibility
  for users on older GCCToolchain releases. The `libtool_VERSION` is incremented and
  baseline symbol files are regenerated to reflect these changes.'
primer_glossary:
- term: libstdc++
  definition: The standard C++ library implementation used by GCC. It provides fundamental
    C++ features like containers, algorithms, and I/O streams.
- term: ABI
  definition: Application Binary Interface. Defines how compiled code can interact
    at the binary level, including function calling conventions, data layout, and
    symbol naming. Changes to ABI can break compatibility between different toolchain
    versions.
- term: GLIBCXX_3.4.37
  definition: A specific symbol version marker used by libstdc++ to denote compatibility
    for symbols introduced or changed in that version. This allows older binaries
    to link against newer libraries if the ABI is compatible.
- term: backport
  definition: The process of taking code fixes or features from a newer version of
    a software project and applying them to an older, usually stable, release.
- term: baseline_symbols.txt
  definition: A file used by libstdc++ to track symbols and their ABI versions for
    different target platforms. It's used for ABI compatibility checks and regeneration.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fabf7b5b9ac518635dca5233661a84b0f97063be
date: '2026-07-20'
is_stub: false
stub_reason: ''
---

This change introduces the GLIBCXX_3.4.37 ABI version to libstdc++. It adds specific symbols, related to chrono and format_arg, that were not backported to GCC 16. Additionally, it moves `basic_string`'s `_S_allocate_at_least` and `_M_create_plus` symbols to this new version. The libtool version has been bumped to 3.4.36, and related baseline symbol files and testsuite configurations are updated.
