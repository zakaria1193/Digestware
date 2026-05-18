---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gitignore
- build system
- cleanup
discussion_id: 20260518024527.177251-1-rsaxvc@gmail.com
source_type: public_inbox
title: '[PATCH] .gitignore .dirstamp files'
headline: Add .dirstamp to .gitignore
tldr: Adds the `.dirstamp` file to `.gitignore` to prevent it from being tracked in
  the repository.
proposer: Richard Allen <rsaxvc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Minor change with no significant tradeoffs.
exchanges: []
primer_expert: The patch adds `.dirstamp` to the `.gitignore` file.  This prevents
  autotools-generated timestamp files from being added to the repository.
primer_general: '`.gitignore` is a file that specifies intentionally untracked files
  that Git should ignore. This patch updates the `.gitignore` file to exclude `.dirstamp`
  files, which are created by the build system. This prevents these automatically
  generated files from cluttering the repository.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260518024527.177251-1-rsaxvc@gmail.com
bugzilla_url: null
date: '2026-05-18'
is_stub: false
---

This patch adds `.dirstamp` to the `.gitignore` file in the binutils repository. This prevents the file from being inadvertently tracked by Git.  This is a minor cleanup that improves the overall hygiene of the repository.
