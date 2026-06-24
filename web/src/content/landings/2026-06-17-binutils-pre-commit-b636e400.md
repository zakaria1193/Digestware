---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- configuration
- tooling
- refactoring
commit_hash: b636e400028ea7928c1cd280121422bb9f42a0b1
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Remove stages setting for two hooks
tldr: Redundant `stages` settings were removed from two pre-commit hooks as they matched
  the default configuration.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In the `pre-commit` framework, hooks can specify which `stages` they
  operate in (e.g., `pre-commit`, `commit-msg`). If a hook's `stages` entry matches
  the globally defined `default_stages`, it becomes superfluous. This commit targets
  `check-license` and `check-whitespace`, two local hooks, removing their identical
  `pre-commit` stage declarations. This is a configuration simplification that has
  no functional impact on the hooks' execution.
primer_general: 'When developers make changes to code, automated checks run at different
  points in their workflow. These points are called ''stages,'' and for Binutils and
  GDB, most checks run during the ''pre-commit'' stage, which happens just before
  code is saved. The overall configuration for these checks sets a ''default stage''
  of ''pre-commit.'' This change removes redundant ''stages: [pre-commit]'' settings
  from two specific checks, `check-license` and `check-whitespace`, because they were
  already covered by the global default. This makes the configuration file tidier
  without changing how or when these checks actually run.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617194025.E31B54BA2E3E@sourceware.org
date: '2026-06-17'
is_stub: true
stub_reason: low-score
---

This commit removes the explicit `stages: [pre-commit]` setting from `check-license` and `check-whitespace` pre-commit hooks in `.pre-commit-config.yaml`.  Since the global `default_stages` is also set to `[pre-commit]`, these individual settings were entirely redundant and their removal streamlines the configuration without altering hook behavior.
