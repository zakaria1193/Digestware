---
project: gcc
subsystem: gcc/fortran
patch_id: null
tags:
- fortran
- c-interop
- bugfix
commit_hash: fdffb66e398d4440116a7d7834aae11053973ffe
source_type: github
author: Harald Anlauf
headline: Fortran -fc-prototypes consistently includes ISO_Fortran_binding.h for deferred
  dummies
tldr: GCC Fortran now consistently includes `ISO_Fortran_binding.h` when generating
  C prototypes for deferred shape and length dummy arguments.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The Fortran frontend in GCC generates C prototypes for Fortran procedures
  when the `-fc-prototypes` option is used, particularly for interoperability. This
  change in `dump-parse-tree.cc` introduces `needs_CFI_cdesc`, a new helper function
  that determines when the `struct CFI_cdesc_t` from `ISO_Fortran_binding.h` is required
  for deferred shape and deferred length dummy arguments. This ensures consistent
  inclusion of the necessary C interoperability header, which was previously sometimes
  missed in complex cases involving procedure interfaces.
primer_general: Fortran and C are two different programming languages, but sometimes
  you need them to work together in the same program. GCC, the GNU Compiler Collection,
  can help with this, especially when generating 'C prototypes' for Fortran functions,
  which are like blueprints that tell C code how to call a Fortran function. This
  commit fixes an issue in the Fortran part of GCC related to `-fc-prototypes`, an
  option that helps with this interoperability. Specifically, when Fortran functions
  have certain types of arguments (called 'deferred shape' or 'deferred length' dummies,
  which are arrays or strings whose sizes aren't fixed until runtime), the generated
  C prototype needs to include a special header file (`ISO_Fortran_binding.h`). This
  update ensures that GCC consistently includes this header, preventing errors and
  making it easier to mix Fortran and C code correctly for these kinds of flexible
  arguments.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fdffb66e398d4440116a7d7834aae11053973ffe
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This commit improves the Fortran frontend's `-fc-prototypes` option by ensuring `ISO_Fortran_binding.h` is consistently included when generating C prototypes for procedure interfaces with deferred shape and deferred length dummy arguments. Previously, a fix for this issue did not always detect when the include was necessary. A new helper function, `needs_CFI_cdesc`, centralizes this logic, preventing missing includes and improving interoperability between Fortran and C for such arguments.
