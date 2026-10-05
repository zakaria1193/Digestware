---
project: gcc
subsystem: fortran
patch_id: null
tags:
- fortran
- compiler
- language-compliance
commit_hash: d745dfbe669d71061dbd5fbb3d5d0dce6432621c
source_type: github
author: Mikael Morin
headline: Fortran enforces restrictions on polymorphic volatile array arguments
tldr: Fortran compiler now correctly checks restrictions on polymorphic volatile array
  arguments.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The fortran/interface.cc compare_parameter function previously had
  incomplete checks for VOLATILE and ASYNCHRONOUS array arguments when the dummy argument
  was polymorphic. This commit updates the checks to use CLASS_DATA, ensuring the
  correct attributes and fields are examined for polymorphic dummies, aligning with
  language rules.
primer_glossary:
- term: polymorphic
  definition: In Fortran, a polymorphic entity can have dynamic type, meaning its
    type can change during execution. This allows for more flexible programming, particularly
    with inheritance and dynamic dispatch.
- term: volatile
  definition: The VOLATILE attribute in Fortran specifies that a variable's value
    may be altered by external means (e.g., hardware or another process) at any time.
    The compiler must not optimize away accesses to volatile variables.
- term: CLASS_DATA
  definition: A macro or internal representation used in the Fortran front-end to
    access data members of polymorphic variables, ensuring correct handling of dynamic
    typing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d745dfbe669d71061dbd5fbb3d5d0dce6432621c
date: '2026-10-04'
is_stub: false
stub_reason: ''
---

The Fortran compiler now correctly enforces restrictions on polymorphic volatile array arguments. Previously, checks for forbidden cases involving polymorphic arrays were insufficient. This change updates the comparison logic to correctly identify and reject invalid arguments, ensuring stricter adherence to language standards.
