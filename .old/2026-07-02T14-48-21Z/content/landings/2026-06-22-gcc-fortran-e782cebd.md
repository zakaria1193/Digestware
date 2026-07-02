---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- c-interoperability
- abi
- prototypes
commit_hash: e782cebd83be590090216ce3642318f9121991ce
source_type: github
author: Harald Anlauf
headline: 'Fortran: Improve -fc-prototypes for deferred shape/length dummies'
tldr: The Fortran frontend now uses `CFI_cdesc_t` for C prototypes of deferred shape
  and deferred length dummy arguments.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refines the handling of Fortran's C interoperability (`-fc-prototypes`)
  for deferred-shape and deferred-length dummy arguments. Specifically, in `get_c_type_name`
  within `dump-parse-tree.cc`, the type selected for the C prototype of these arguments
  is now consistently `CFI_cdesc_t`. This change unifies the representation of Fortran's
  dynamic array and string arguments in C, aligning it with the existing handling
  for assumed-length scalar character dummies. This ensures that the generated C prototypes
  accurately reflect the Fortran argument passing mechanism, particularly for descr…
primer_general: When you write programs that mix Fortran and C, the Fortran compiler
  can generate C-style function definitions (called "prototypes") so that the C code
  can correctly call Fortran functions. This update improves how the Fortran compiler
  creates these C prototypes for certain types of Fortran arguments. Specifically,
  it affects arguments where the array's size or string's length isn't known until
  the program runs (called "deferred shape" and "deferred length"). The compiler now
  uses a special C type, `CFI_cdesc_t`, which is designed to help C and Fortran share
  information about these dynamic arguments. This makes it easier and more reliable
  to write programs that combine Fortran and C, as the compiler handles the complex
  details of passing these dynamic data structures correctly between the two languages.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e782cebd83be590090216ce3642318f9121991ce
date: '2026-06-22'
is_stub: false
---

This update to the Fortran frontend improves the generation of C prototypes for Fortran procedures, particularly when dealing with deferred-shape and deferred-length dummy arguments. The compiler now consistently uses the `CFI_cdesc_t` C interoperability type for these arguments, aligning their representation with how assumed-length scalar character dummies are handled. This enhancement ensures more correct and robust C interface generation, which is crucial for mixed-language programming with Fortran and C.
