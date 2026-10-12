---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- loop optimization
commit_hash: e887376de60a6ae60b81156064cb413db8c90353
source_type: github
author: Alfie Richards
headline: Use LOOP_VINFO_MAIN_EXIT for final IV edge in vectorizer.
tldr: Vectorizer now uses a more appropriate exit condition for final loop invariants.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The vect_set_loop_condition_partial_vectors_avx512 and vect_set_loop_condition_normal
  functions in tree-vect-loop-manip.cc previously used exit_edge for updating the
  final invariant of peeled loops. This commit changes the logic to use LOOP_VINFO_MAIN_EXIT,
  which is a more precise way to denote the main exit of a loop's vector information.
  This change ensures that the loop condition is correctly established for peeled
  iterations, particularly relevant for AVX512 vectorization strategies.
primer_glossary: []
discussion_id_link: github:gcc-mirror/gcc#127805
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e887376de60a6ae60b81156064cb413db8c90353
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

The GCC vectorizer has been updated to use LOOP_VINFO_MAIN_EXIT instead of exit_edge when determining the final invariant for peeled loops. This change corrects how the loop condition is updated, ensuring more accurate vectorization.

This fix addresses a specific issue related to loop peeling and invariant handling within the tree-vectorization pass.
