---
project: gcc
subsystem: unknown
patch_id: null
commit_hash: 9dbf90fc0876b6b33dbe695fd1ab62976cc7178b
source_type: github
author: Gaius Mulley
impact_score: 5
performance_win: false
breaking_change: false
discussion_id_link: null
bugzilla_pr: null
url: https://github.com/gcc-mirror/gcc/commit/9dbf90fc0876b6b33dbe695fd1ab62976cc7178b
date: '2026-04-15'
---

PR modula2/124081 Bugfix ICE in expand_expr_real_2 with a record

This patch fixes an ICE which occurs when attempting to create a
set using a subrange from a record field.  The fix ensures that the
r
