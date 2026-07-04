---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- formatting
- ABI
commit_hash: 4fd42fce8d43cefb59c61d2865c198c35c0860be
source_type: github
author: Tomasz Kamiński
headline: 'libstdc++: Provide defined behavior for unrecognized _Pres_type values'
tldr: Ensures that libstdc++'s formatting functions handle unrecognized presentation
  types gracefully, preventing crashes.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change addresses a potential ABI incompatibility and runtime error
  in `libstdc++`'s `<format>` implementation. If a program is compiled with a newer
  GCC that supports new `_Pres_type` values (e.g., for prefixed hex floats) but linked
  against an older libstdc++ that doesn't recognize them, the formatters (`__formatter_int`,
  `__formatter_fp`) would hit `__builtin_unreachable`. This commit modifies the default
  branches of their `format` methods to transition to `_Pres_none` instead, providing
  a safe fallback.
primer_glossary:
- term: _Pres_type
  definition: An internal enumeration or type used by `std::format` in libstdc++ to
    represent the desired presentation format of a value (e.g., decimal, hexadecimal,
    scientific).
- term: ABI incompatibility
  definition: Application Binary Interface incompatibility. Occurs when different
    versions of a library or object files use incompatible data structures or function
    calling conventions, preventing them from working together.
- term: __builtin_unreachable
  definition: A GCC built-in function that informs the compiler that the code path
    reaching it should never be executed. Compilers may optimize more aggressively
    based on this assumption.
- term: _Pres_none
  definition: A specific value within the `_Pres_type` enumeration, likely representing
    the default or most basic presentation format.
- term: TU (Translation Unit)
  definition: A source file after it has been preprocessed and compiled into an intermediate
    object file. Linking multiple TUs forms the final executable or library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4fd42fce8d43cefb59c61d2865c198c35c0860be
date: '2026-06-24'
is_stub: false
stub_reason: ''
---

When new `_Pres_type` values are introduced in `std::format` for future features, linking against older library versions could lead to unrecognized types. Previously, `__formatter_int` and `__formatter_fp` would trigger `__builtin_unreachable` in such cases, causing undefined behavior or crashes. This patch modifies these formatters to fall back to the `_Pres_none` behavior when an unrecognized `_Pres_type` is encountered, ensuring defined and safe operation.
