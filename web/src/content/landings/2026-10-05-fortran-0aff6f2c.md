---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- gfortran
- contiguous
commit_hash: 0aff6f2c1b145e6d35b8ece3da4a7e32dfc74719
source_type: github
author: Mikael Morin
headline: Fortran compiler fixes simply contiguous property for associate subreferences
tldr: Corrects the GFortran compiler's handling of the 'simply contiguous' property
  for associate names referencing array components or sections.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `fortran/expr.cc`, the `gfc_is_simply_contiguous` function has been
  modified to accurately handle associate name references. Previously, it forwarded
  queries to the associate target for any full array reference, including array components.
  This commit adds a check to ensure no component reference occurred before forwarding.
  Additionally, it now forwards queries for non-full array sections, correcting the
  behavior for associate names tied to non-contiguous targets and ensuring array section
  checks continue even if the associate target is contiguous.
primer_glossary:
- term: Simply contiguous
  definition: A Fortran language property that specifies whether an array or array
    section has its elements stored contiguously in memory, similar to C's arrays.
    This is important for interoperability and certain performance optimizations.
- term: Associate name
  definition: A Fortran construct that creates a temporary name (an alias) for a variable
    or expression, often used to simplify complex code or refer to parts of data structures.
- term: GFortran
  definition: The Fortran compiler provided by the GCC toolchain.
- term: Array component
  definition: A field within a Fortran derived type that is an array.
- term: Array section
  definition: A subset of an array defined by specifying ranges for one or more dimensions.
    For example, `array(1:5:2)` is an array section.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0aff6f2c1b145e6d35b8ece3da4a7e32dfc74719
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

The GFortran compiler has been updated to correctly determine the 'simply contiguous' property for associate names in Fortran. This commit fixes issues where the property was incorrectly forwarded to an associate target, even when the reference involved subcomponents or non-full array sections. The changes ensure that the compiler accurately checks the contiguity of array components and handles non-contiguous sections of associate names associated with contiguous targets.
