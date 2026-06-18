---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- configuration
- tooling
- refactoring
commit_hash: 8cf82b58d73d28f3732b8a652d4c69fa6c02bd58
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Drop always_run setting for codespell-log
tldr: The redundant `always_run` setting has been removed from the `codespell-log`
  pre-commit hook configuration.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'In the context of `pre-commit` configurations, the `always_run` flag
  dictates whether a hook executes regardless of staged file changes. For `commit-msg`
  hooks, which operate on the commit message rather than file content, `always_run:
  true` is implicitly handled and therefore redundant. This commit specifically addresses
  the `codespell-log` hook, responsible for scanning commit messages for spelling
  errors, by removing this unnecessary setting, streamlining the definition without
  affecting its function.'
primer_general: 'Before a developer''s code changes are officially saved, a system
  of automated checks known as ''pre-commit hooks'' runs to catch potential issues.
  These hooks are configured in a file called `.pre-commit-config.yaml`. One such
  check, `codespell-log`, is designed to scan the commit message itself for spelling
  errors. This change removes a setting called `always_run: true` from the `codespell-log`
  configuration. This setting was redundant because commit message checks naturally
  always run when a commit message is provided, so explicitly stating `always_run`
  did not add any value. Removing it makes the configuration cleaner without changing
  how the spelling check operates.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617194031.0CC924BA2E11@sourceware.org
date: '2026-06-17'
is_stub: false
---

This change removes the `always_run: true` setting from the `codespell-log` hook definition within the `.pre-commit-config.yaml` file. Since `codespell-log` is configured to run during the `commit-msg` stage, enforcing `always_run` is unnecessary. Removing this superfluous setting simplifies the pre-commit configuration without altering its behavior.
