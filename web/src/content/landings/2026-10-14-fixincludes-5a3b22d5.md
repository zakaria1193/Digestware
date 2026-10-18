---
project: gcc
subsystem: fixincludes
patch_id: null
tags:
- fixincludes
- c89
- build
commit_hash: 5a3b22d5ea01ee63804bf5a528b3d209fbe6767c
source_type: github
author: Sam James
headline: 'fixincludes: Assume C89 for abort and avoid strings.h search'
tldr: fixincludes now assumes abort is available in C89 and removes unnecessary search
  for strings.h.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the fixincludes subsystem to rely on C89 standards
  for the 'abort' function, removing a fallback check. It also removes the search
  for 'strings.h', as its contents are implicitly available. This is part of a larger
  effort to clean up redundant checks in GCC's configure scripts, specifically targeting
  PR bootstrap/112422.
primer_glossary:
- term: fixincludes
  definition: A GCC subsystem responsible for adjusting header files to work correctly
    with the compiler.
- term: C89
  definition: The 1989 version of the C programming language standard, also known
    as ANSI C.
- term: abort
  definition: A C standard library function that terminates the calling process.
- term: strings.h
  definition: A C standard header file that declares string manipulation functions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5a3b22d5ea01ee63804bf5a528b3d209fbe6767c
date: '2026-10-14'
is_stub: true
stub_reason: low_score
---

The fixincludes subsystem now assumes the abort function is available for C89, eliminating the need to search for it. Additionally, it removes the search for strings.h, as the required functions are already provided by C89. This change simplifies the configuration process and addresses a bootstrap PR.
