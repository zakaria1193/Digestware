---
project: binutils
subsystem: binutils/build
patch_id: null
tags:
- build
- CI
- refactoring
commit_hash: 2b28c50ecd058b3fe0328d1bf5f7bc06fd8ca41c
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Refine pre-commit configuration
tldr: Pre-commit configuration is updated to reduce duplication and set default file
  paths.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `.pre-commit-config.yaml` is updated to use YAML anchors and aliases
  for the `check-include-guards` hook and a new `python-files` anchor. This reduces
  duplication by allowing reusable configuration blocks. A default `files` setting
  is also introduced, targeting Python files within `gdb/`, `gdbserver/`, and `gdbsupport/`
  directories, and a bug related to duplicate hook definitions is addressed.
primer_glossary:
- term: pre-commit
  definition: A framework that automates the execution of program code quality checks
    before commits are made, ensuring code consistency and preventing common errors.
- term: YAML anchors and aliases
  definition: Features in YAML that allow defining a block of data once (anchor) and
    reusing it elsewhere (alias), reducing redundancy in configuration files.
- term: hook
  definition: A script or program that runs automatically at a specific point in a
    process, such as before a code commit, to perform checks or tasks.
- term: configuration file
  definition: A file that stores settings and parameters for a program or system,
    allowing customization of its behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260713111110.7800D4BA5434@sourceware.org
date: '2026-07-13'
is_stub: false
stub_reason: ''
---

This commit refactors the `.pre-commit-config.yaml` file to reduce duplication by using YAML anchors and aliases for hook configurations. It also sets a default `files` pattern to apply hooks more consistently across Python files in the `gdb`, `gdbserver`, and `gdbsupport` directories. This improves maintainability and reduces redundancy in the pre-commit hook setup.
