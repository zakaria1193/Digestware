---
project: gcc
subsystem: ada
patch_id: null
tags:
- ada
- compiler
- bugfix
- optimization
commit_hash: debafaf88c2a32b12a09ed6779b2c669eb886c01
source_type: github
author: Marc Poulhiès
headline: 'Ada: Drop renamings when dropping an unused subprogram.'
tldr: The Ada compiler ensures that renamings of unused subprograms are also dropped
  during unnesting, preventing potential issues.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `exp_unst.adb` to handle subprogram renamings
  during unnesting. The compiler may drop subprograms deemed unreachable by reachability
  analysis. The change ensures that any renamings associated with these dropped subprograms
  are also removed.  New functions `Nullify_Renamings` and `Move_Pending_Renamings`
  are introduced, and the `Subp_Entry` record in `exp_unst.ads` is extended with a
  `Renamings` component.
primer_general: Compilers often perform optimizations to remove unused code. This
  commit addresses a specific scenario in the Ada compiler where a subprogram (similar
  to a function) is removed because it's never called. If a subprogram is renamed,
  the compiler must also remove the renaming when the original subprogram is removed
  to avoid errors.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/debafaf88c2a32b12a09ed6779b2c669eb886c01
date: '2025-12-05'
is_stub: false
---

The Ada compiler now tracks subprogram renamings during unnesting and ensures that these renamings are dropped when the subprogram is determined to be unused. This change prevents potential issues related to dangling references to renamed subprograms that are no longer reachable.
