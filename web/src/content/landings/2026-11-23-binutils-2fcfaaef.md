---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gdb
- branching
commit_hash: 2fcfaaefd029a597646f9740e2c0686b0cc9810f
source_type: public_inbox
author: Andrew Burgess <aburgess@sourceware.org>
headline: Create gdb-tracking-multi-loc branch
tldr: New branch 'gdb-tracking-multi-loc' created in binutils-gdb repository.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit simply creates a new git branch in the binutils-gdb repository.
  The branch name suggests it's for tracking multi-location breakpoints or watchpoints
  in GDB, and it's based on a commit that modifies symbol table parsing related to
  GDB locations. No core toolchain logic is changed here, only repository organization.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261123225723.0D93C43F0ABC@sourceware.org
date: '2026-11-23'
is_stub: true
stub_reason: low_score
---

A new branch named 'gdb-tracking-multi-loc' has been created in the binutils-gdb repository. This branch is based on an existing commit that refines how GDB handles breakpoint and watchpoint locations during symbol table parsing.
