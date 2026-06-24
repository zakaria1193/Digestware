---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- configuration
- tooling
- refactoring
commit_hash: caefce72351daf3d249eb93397bf66a02a802736
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Drop require_serial for pre-commit-setup
tldr: The redundant `require_serial` setting has been removed from the `pre-commit-setup`
  hook configuration.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `pre-commit` framework generally attempts to run hooks in parallel
  for efficiency. The `require_serial: true` flag forces a hook to run sequentially
  relative to other hooks, often used when a hook modifies staged files or depends
  on specific ordering. For the `pre-commit-setup` hook, its `pass_filenames` setting
  being `false` implies it does not process individual files, negating the original
  justification for `require_serial`. This removal is a clean-up, aligning the configuration
  with the hook''s actual behavior.'
primer_general: 'When developers prepare code changes, automated checks run through
  a system called ''pre-commit hooks,'' configured in `.pre-commit-config.yaml`. Normally,
  these checks can run simultaneously to save time. However, some checks need to run
  one after another, which is enforced by a setting called `require_serial: true`.
  The `pre-commit-setup` hook used to have this setting. This change removes it because
  the hook no longer processes individual files (it has `pass_filenames: false`),
  which was the primary reason for `require_serial`. Without needing to process files
  in a specific order, there''s no need to force it to run sequentially, making the
  configuration simpler.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617194015.B1D8C4BA23C3@sourceware.org
date: '2026-06-17'
is_stub: true
stub_reason: low-score
---

This change removes the `require_serial: true` setting from the `pre-commit-setup` hook definition in `.pre-commit-config.yaml`. This setting was previously necessary when `pass_filenames` was enabled, which required hooks to run sequentially. Now that `pass_filenames` is disabled for `pre-commit-setup` and files are not passed individually, `require_serial` is no longer needed, simplifying the configuration.
