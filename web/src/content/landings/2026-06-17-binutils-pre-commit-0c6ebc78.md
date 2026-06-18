---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- configuration
- tooling
- code quality
- refactoring
commit_hash: 0c6ebc781ac79cd64d12d8acc1cb50fd4de2bb3a
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Reorganize .pre-commit-config.yaml
tldr: The pre-commit configuration file for Binutils/GDB has been reorganized for
  improved readability and maintainability.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `.pre-commit-config.yaml` file defines the hooks run by the `pre-commit`
  framework to ensure code quality and consistency before commits are made. This reorganization
  impacts the configuration of various hooks, notably those for Python (like Black
  and Flake8), by centralizing commentary on file selection and clarifying `types_or`
  usage. While not altering core toolchain functionality, these changes streamline
  the pre-commit setup, making it easier for maintainers to understand and modify
  the automated checks.
primer_general: When developers write code, they often use tools to automatically
  check for common errors, style violations, and other issues before submitting their
  changes. These checks are called 'pre-commit hooks' because they run before a code
  change is officially committed. This update reorganizes `pre-commit-config.yaml`,
  which is the configuration file that specifies which checks to run and how to run
  them for the Binutils and GDB projects. The goal is to make this configuration file
  more readable, with consistent formatting and clearer explanations about how different
  checks, such as Python style checkers, apply to various parts of the codebase. This
  helps ensure that the automated quality checks are well-understood and maintained.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617194036.27E744BA2E32@sourceware.org
date: '2026-06-17'
is_stub: false
---

The Binutils and GDB project's `.pre-commit-config.yaml` file has been refactored to unify indentation, group local hooks, and enhance clarity with empty lines and comments. This change also relocates detailed file selection comments to the 'Python hooks' section, providing better explanations for `types_or` settings where needed. Anchors are now used to eliminate repetition within the configuration.
