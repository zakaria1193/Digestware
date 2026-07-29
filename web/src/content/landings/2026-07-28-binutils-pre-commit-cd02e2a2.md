---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- binutils
- pre-commit
- python
commit_hash: cd02e2a209482dd9fa06945ffec0675da7dfd74e
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Add 'tomli' dependency for codespell hook.
tldr: Ensures codespell pre-commit hook works on older Python versions by adding 'tomli'
  dependency.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `codespell` pre-commit hook uses `tomllib` (a standard library
  module in Python 3.11+) to parse TOML configuration files. To maintain compatibility
  with older Python versions (pre-3.11), this commit adds `tomli` (a backport of `tomllib`)
  to the `additional_dependencies` for the `codespell` hook in `.pre-commit-config.yaml`.
primer_glossary:
- term: pre-commit hook
  definition: A script that runs automatically before a commit is made. It's used
    to enforce coding standards, check for errors, or perform other quality control
    tasks.
- term: codespell
  definition: A spell checker that detects common misspellings in code and text.
- term: tomllib
  definition: A Python standard library module (available in Python 3.11+) for parsing
    TOML (Tom's Obvious, Minimal Language) files.
- term: tomli
  definition: A third-party Python package that provides a backport of the `tomllib`
    module, allowing TOML parsing on Python versions prior to 3.11.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260728080118.5B7F54B9DB5A@sourceware.org
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

The `codespell` pre-commit hook requires the `tomllib` module to parse `pyproject.toml` files. As `tomllib` is only available in Python 3.11+, this commit adds the `tomli` dependency to the hook configuration. This ensures that `codespell` functions correctly on Python versions 3.10 and older.
