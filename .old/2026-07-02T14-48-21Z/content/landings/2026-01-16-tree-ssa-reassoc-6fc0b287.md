---
project: gcc
subsystem: tree-ssa-reassoc
patch_id: null
tags:
- optimization
- warning
- strict overflow
- SSA
commit_hash: 6fc0b287385d645f122bae89ca20ffb71836a862
source_type: github
author: Daniel Barboza
headline: Remove strict_overflow_p from range_entry
tldr: The strict_overflow_p flag has been removed from range_entry in tree-ssa-reassoc,
  further deprecating the -Wstrict-overflow warning.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the ``strict_overflow_p`` flag from the ``range_entry``
  struct in ``tree-ssa-reassoc.h``, and removes associated uses in ``tree-ssa-reassoc.cc``.  This
  pass reassociates expressions in SSA form to improve code generation; ``range_entry``
  tracks value ranges. The overflow check was used during range test optimization.  This
  is another step in removing ``Wstrict-overflow``.
primer_general: SSA (Static Single Assignment) is a form of intermediate representation
  used by compilers to facilitate optimization. The tree-ssa-reassoc module performs
  reassociation of expressions in SSA form, which can improve code generation. This
  commit removes a flag related to strict overflow checking from a data structure
  used in this module, as part of a larger effort to deprecate the ``-Wstrict-overflow``
  warning.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6fc0b287385d645f122bae89ca20ffb71836a862
date: '2026-01-16'
is_stub: false
---

The ``strict_overflow_p`` flag has been removed from the ``range_entry`` structure in the tree-ssa-reassoc module, along with associated warning calls. This flag was used to track whether strict overflow checking was enabled for a particular range of values.  Removing this simplifies the code and reduces noise, furthering the deprecation of the ``-Wstrict-overflow`` warning.
