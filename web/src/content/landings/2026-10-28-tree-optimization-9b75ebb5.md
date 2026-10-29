---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- exception handling
commit_hash: 9b75ebb5068abcf009dd1f7f8014c3b535b9042e
source_type: github
author: Richard Biener
headline: Avoid fixing up removed statements during DOM cleanup
tldr: Ensures that statements removed during EH cleanup are not processed further
  during DOM cleanup.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `tree-ssa-dom.cc`, this commit modifies `pass_dominator::execute`
  to guard against operating on statements that have been previously removed during
  EH cleanup. Specifically, it adds a check to verify if a `stmt` is still present
  in the IL before calling `fixup_noreturn_call`. This addresses PR tree-optimization/128172,
  ensuring that the dominator tree construction remains sound even when EH-related
  statement removals occur.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9b75ebb5068abcf009dd1f7f8014c3b535b9042e
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit prevents the dominator pass from attempting to fix up statements that have already been removed as part of exception handling (EH) cleanup. By adding a check to ensure a statement still exists in the intermediate language (IL) before processing it, the compiler avoids potential errors and ensures the integrity of the control flow graph during dominator analysis. A new test case is provided for verification.
