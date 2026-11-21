---
project: gcc
subsystem: libgfortran
patch_id: null
tags:
- libgfortran
- locale
- windows
- bugfix
commit_hash: 4ab39ca82231997cd925d4c4e04995e22836119e
source_type: github
author: Julien Marrec
headline: Improve locale handling in libgfortran's formatted I/O for non-POSIX locales
tldr: ' libgfortran now copies the LC_NUMERIC locale name before switching to ''C''
  to prevent issues on platforms without POSIX locales.'
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: For targets without full POSIX 2008 locale support, libgfortran's `data_transfer_init_worker`
  and `finalize_transfer` routines historically relied on `setlocale(LC_NUMERIC, NULL)`
  to retrieve the current locale name. This pointer was then used for restoration
  after a temporary `setlocale(LC_NUMERIC, "C")` call. However, C runtimes on Windows
  (MSVCRT, UCRT) can invalidate this pointer or its buffer. This commit changes the
  approach to instead save a copy of the locale name string. It also optimizes by
  skipping the `setlocale(LC_NUMERIC, "C")` and subsequent restoration if the locale
  is already…
primer_glossary:
- term: LC_NUMERIC
  definition: A locale category that affects the formatting of numeric and string
    conversions.
- term: setlocale
  definition: A C standard library function used to query and set the program's locale.
- term: POSIX locales
  definition: Standards-defined sets of locale-specific information, providing consistent
    internationalization and localization behavior across systems.
- term: MinGW-w64
  definition: A development environment for Windows that includes GCC toolchains,
    often lacking full POSIX compliance.
- term: MSVCRT
  definition: Microsoft Visual C++ Runtime; the runtime library for Microsoft's C/C++
    compilers.
- term: UCRT
  definition: Universal C Runtime; a newer C runtime library developed by Microsoft.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4ab39ca82231997cd925d4c4e04995e22836119e
date: '2026-10-26'
is_stub: false
stub_reason: ''
---

On systems lacking POSIX 2008 locales, such as MinGW-w64, libgfortran's formatted I/O faced issues with locale handling. Previously, it saved a pointer to the locale name and restored it after temporarily setting the locale to 'C'. This approach could lead to memory corruption or performance degradation due to incorrect handling of the locale string by Windows C runtimes. The fix involves copying the locale name and only switching to 'C' if necessary, improving robustness and performance.
