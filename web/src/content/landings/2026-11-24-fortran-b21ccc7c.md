---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- type checking
- pointer
commit_hash: b21ccc7c211e6a4a5e77f20fd05d65c378f583df
source_type: github
author: Jerry DeLisle
headline: 'fortran: Fixes INTENT(IN) error for POINTER selector in CLASS IS'
tldr: Corrects a false INTENT(IN) error when a POINTER dummy argument is used as a
  selector in a CLASS IS block.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gfc_check_vardef_context` in Fortran's `expr.cc` was misinterpreting
  the INTENT(IN) constraint when applied to a CLASS IS block whose selector is a POINTER
  dummy. Due to a fix for PR54322, it incorrectly rejected constructs where the associate
  name inherited the POINTER attribute from its class container. This commit modifies
  the check to examine the POINTER attribute of the dummy argument itself, rather
  than the associate name, resolving the incorrect rejection.
primer_glossary:
- term: INTENT(IN)
  definition: An attribute in Fortran that specifies a dummy argument must not be
    modified by the procedure.
- term: POINTER
  definition: A Fortran attribute that designates a variable as a pointer, capable
    of target association.
- term: CLASS IS block
  definition: A Fortran construct used for type discrimination, selecting code paths
    based on the dynamic type of an object.
- term: selector
  definition: In a CLASS IS block, the expression whose dynamic type determines which
    branch is taken.
- term: associate name
  definition: A temporary name introduced within a SELECT TYPE or CLASS IS construct
    to refer to the selector.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b21ccc7c211e6a4a5e77f20fd05d65c378f583df
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This change fixes a bug where the Fortran compiler incorrectly issued an INTENT(IN) error for POINTER dummy arguments used as selectors in CLASS IS blocks. The compiler was checking the associate name's POINTER attribute instead of the dummy argument's, leading to this false positive. The fix ensures the check correctly targets the dummy argument, resolving the issue for polymorphic POINTER INTENT(IN) arrays as well.
