---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- pre-commit
- configuration
- tools
- codespell
commit_hash: 0c73540bb80ffb5c88da71e3162b7a01e5b9db61
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Pre-commit hook simplifies codespell configuration in Binutils
tldr: Binutils simplifies its `codespell` configuration by moving file selection from
  `.pre-commit-config.yaml` to `gdb/pyproject.toml`.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the `codespell` pre-commit hook configuration
  within Binutils. Previously, a lengthy regex in `.pre-commit-config.yaml` dictated
  which files the `codespell` hook should apply to. This change delegates the file
  inclusion and exclusion logic to the `gdb/pyproject.toml` file via the `--toml`
  argument. This approach aligns with modern Python project best practices for tool
  configuration, particularly for GDB's extensive Python codebase. The `skip` patterns
  for generated files and ChangeLogs are now managed in a more structured way within
  `pyproject.toml`, reducing clutter in…
primer_general: Open-source projects often use automated tools to maintain code quality.
  One such tool is `codespell`, which checks for common spelling mistakes in code.
  To ensure these checks run before code is submitted, 'pre-commit hooks' are used.
  These are scripts that run automatically when a developer tries to 'commit' their
  changes. This change simplifies how `codespell` is configured in the Binutils project.
  Instead of having a complex rule in the main configuration file that tells `codespell`
  which files to check, that detailed list has been moved to a file specifically for
  the GDB debugger component (`gdb/pyproject.toml`). This makes the configuration
  clearer and easier to understand, especially for developers who focus on GDB, by
  keeping GDB-specific settings in one place.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260615112452.5A29A4B920C6@sourceware.org
date: '2026-06-15'
is_stub: false
---

The Binutils project has streamlined its `codespell` configuration, a tool used for checking common spelling errors. The definition of which files `codespell` should analyze has been moved from the main `.pre-commit-config.yaml` file to `gdb/pyproject.toml`. This change centralizes the file selection and exclusion rules within the GDB specific configuration, making the overall setup cleaner and easier to manage, particularly for developers working on the GDB component.
