---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- format
- abi
- compatibility
commit_hash: 50cbacfaa1e776b7ab36070f7f61873b092fd71f
source_type: github
author: Tomasz Kamiński
headline: libstdc++ safely handles unrecognized format_arg types
tldr: Format library now uses a fallback mechanism for unrecognized argument types,
  preventing UB and improving compatibility.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'libstdc++ `<format>` ABI evolution: `basic_format_arg` specializations
  for `format_context` and `wformat_context` now export `_M_handle_unrecognized` to
  cope with future `_Arg_t` extensions. This avoids UB from unrecognized values when
  a newer `libstdc++.so` is used with an older executable. This mechanism becomes
  crucial for `visit_format_arg` on newer types. The `__type` parameter is removed
  from `_M_visit` helpers, relying on `_M_type` for consistency.'
primer_glossary:
- term: libstdc++
  definition: The GNU Standard C++ Library, a fundamental component of GCC that provides
    the C++ standard library implementation.
- term: basic_format_arg
  definition: An internal representation within the C++ `<format>` library that holds
    a formatted argument, capable of deferring its actual type.
- term: _Arg_t
  definition: An enumeration type used internally by the C++ `<format>` library to
    distinguish between different kinds of arguments that can be formatted.
- term: UB
  definition: Undefined Behavior. Situations in code where the C++ standard does not
    specify the outcome, leading to unpredictable program behavior, crashes, or security
    vulnerabilities.
- term: ABI
  definition: Application Binary Interface. Defines how compiled code is linked and
    executed, including function calling conventions, data layout, and system call
    interfaces.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/50cbacfaa1e776b7ab36070f7f61873b092fd71f
date: '2026-06-23'
is_stub: false
stub_reason: ''
---

The C++ format library in libstdc++ now gracefully handles unrecognized `_Arg_t` values in `basic_format_arg`. Instead of calling `__builtin_unreachable` which can lead to undefined behavior, a new `_M_handle_unrecognized` method is invoked. This ensures backward compatibility when newer library versions are used with older binaries, preventing crashes and providing better runtime robustness.
