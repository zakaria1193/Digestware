---
project: gcc
subsystem: gcc/wide-int
patch_id: null
tags:
- gcc
- code-cleanup
commit_hash: ccba72f71e192d8448c457e4a469e86c7ed71aac
source_type: github
author: Kael Andrew Franco
headline: Remove unused W_TYPE_SIZE == 32 check.
tldr: GCC's wide-int implementation removes an obsolete check for 32-bit host integer
  sizes.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `gcc/wide-int.cc`, the `W_TYPE_SIZE` macro typically expands to
  `HOST_BITS_PER_WIDE_INT`, which defines the number of bits in GCC's internal wide
  integer type. This commit removes a conditional check `W_TYPE_SIZE == 32`. As `HOST_BITS_PER_WIDE_INT`
  is 64 on the target build platform (x86_64-pc-linux-gnu), this condition was never
  true and is now obsolete.
primer_glossary:
- term: wide-int
  definition: GCC's internal implementation for handling arbitrary-precision integers,
    used for representing large constants or intermediate values during compilation.
- term: HOST_BITS_PER_WIDE_INT
  definition: A preprocessor macro defining the number of bits in GCC's internal word
    size for the host system, used for wide integer operations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ccba72f71e192d8448c457e4a469e86c7ed71aac
date: '2026-11-18'
is_stub: true
stub_reason: low_score
---

The `wide-int` component in GCC contained a check for `W_TYPE_SIZE == 32`. Since `HOST_BITS_PER_WIDE_INT` is consistently 64 on modern systems where GCC is built, this check was always false and has been removed. This simplifies the code and removes dead logic.
