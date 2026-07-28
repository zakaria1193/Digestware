---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- parser
- refactor
commit_hash: bdcc2f7fd6fc0ef6b9b892d5e39d7848f977a94d
source_type: github
author: James K. Lowden
headline: Resume COBOL source format after copybook ends.
tldr: COBOL parser correctly resumes source format after processing copybooks.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Refactors COBOL's lexer to properly manage source format state across
  copybook inclusions. Changes to SOURCE FORMAT directives within copybooks are now
  correctly discarded upon exiting the copybook, ensuring consistent parsing of the
  main source file.
primer_glossary:
- term: copybook
  definition: A file containing COBOL structures and definitions that can be included
    in multiple programs. It promotes code reuse and consistency.
- term: SOURCE FORMAT
  definition: A COBOL directive that specifies the syntax rules for interpreting the
    source code, such as fixed or free format.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/bdcc2f7fd6fc0ef6b9b892d5e39d7848f977a94d
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

The COBOL front-end now correctly resumes the source format after a copybook file has been processed. Previously, changes to the source format directive within a copybook were not properly discarded upon exiting the copybook, leading to incorrect parsing.
