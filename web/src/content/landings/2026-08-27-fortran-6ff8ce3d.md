---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- refactor
- debug info
commit_hash: 6ff8ce3db86e53775e6cc10e5eadfc62fb6ec39f
source_type: github
author: Mikael Morin
headline: 'fortran: Move rank offset construction for array descriptors'
tldr: Fortran array descriptor rank offset construction moved to trans-descriptor.cc.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Moves the rank offset calculation logic from `gfc_get_array_descr_info`
  in `fortran/trans-types.cc` to `gfc_get_descriptor_offsets_for_info` in `fortran/trans-descriptor.cc`.
  This change localizes the understanding of the GFC_DTYPE_RANK field's position and
  size within the descriptor structure.
primer_glossary:
- term: array descriptor
  definition: A data structure that describes an array, typically including its base
    address, element type, shape, and strides. In Fortran, these are used extensively
    to pass arrays between procedures and to manage multidimensional arrays.
- term: rank offset
  definition: In the context of array descriptors, this refers to the specific memory
    location or calculation required to access the 'rank' (number of dimensions) field
    within the descriptor structure.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6ff8ce3db86e53775e6cc10e5eadfc62fb6ec39f
date: '2026-08-27'
is_stub: true
stub_reason: low_score
---

This commit moves the construction of rank offset information for array descriptor debug info from `trans-types.cc` to `trans-descriptor.cc`. This change encapsulates the knowledge of the rank field's layout within `trans-descriptor.cc`, improving modularity and reducing dependencies.
