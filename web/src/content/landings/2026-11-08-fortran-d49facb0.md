---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- gfortran
- standard
- attribute
commit_hash: d49facb09dfc467069b71a24b8a1de470dc472d1
source_type: github
author: Jerry DeLisle
headline: 'Fortran: Correctly handle attributes for associate names'
tldr: Fixes incorrect POINTER and ALLOCATABLE attributes for Fortran associate names,
  aligning with F2023 standard.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Fortran's `ASSOCIATE` construct allows local names to refer to selected
  components or variables. According to F2023 11.1.3.3, an associate name does not
  inherently have POINTER or ALLOCATABLE attributes. This patch corrects gfortran's
  behavior, which previously assigned the POINTER attribute to polymorphic associate
  names based on their class container, leading to incorrect behavior in pointer assignment
  and within `TYPE IS` blocks. The `TARGET` attribute is now sourced from the `SELECT
  TYPE` selector itself, not its data component.
primer_glossary:
- term: ASSOCIATE construct
  definition: A Fortran construct that allows defining local names that refer to selected
    components or variables within a specific scope.
- term: POINTER attribute
  definition: In Fortran, this attribute declares a variable as a pointer, which can
    be associated with a target variable or memory location.
- term: ALLOCATABLE attribute
  definition: In Fortran, this attribute declares a variable whose storage can be
    dynamically allocated and deallocated during program execution.
- term: TARGET attribute
  definition: In Fortran, this attribute indicates that a variable can be pointed
    to by a pointer.
- term: gfortran
  definition: The GNU Fortran compiler, part of the GCC compiler suite.
- term: Polymorphic
  definition: In Fortran, a variable is polymorphic if it can hold values of different
    intrinsic types or derived types, typically used with `SELECT TYPE`.
- term: SELECT TYPE construct
  definition: A Fortran construct that allows conditional execution based on the dynamic
    type of a variable, often used with polymorphic variables.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d49facb09dfc467069b71a24b8a1de470dc472d1
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This change corrects how Fortran associate names handle POINTER, ALLOCATABLE, and TARGET attributes, adhering to the F2023 standard. Previously, gfortran incorrectly granted polymorphic associate names the POINTER attribute of their class container, enabling invalid pointer assignments. The fix ensures associate names (except for SELECT RANK) do not inherit POINTER or ALLOCATABLE attributes and correctly derive TARGET from SELECT TYPE selectors.
