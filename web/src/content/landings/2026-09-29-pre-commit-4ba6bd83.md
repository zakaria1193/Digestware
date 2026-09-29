---
project: binutils
subsystem: pre-commit
patch_id: null
tags:
- devops
- python
- code style
commit_hash: 4ba6bd8393418b63dc3efa0ec6f934903a10f140
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Update isort to 9.0.2 in binutils-gdb.
tldr: Updates the isort Python code formatter to version 9.0.2 within the binutils-gdb
  project.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `.pre-commit-config.yaml` file, which manages pre-commit hooks
  for the binutils-gdb repository, has been updated. Specifically, the `isort` tool's
  revision has been bumped from `9.0.1` to `9.0.2`. This ensures that the Python code
  formatting applied by `isort` adheres to the latest checks and rules defined in
  this newer version.
primer_glossary:
- term: pre-commit
  definition: A framework for managing and executing pre-commit hooks written in any
    language. It helps automate code style checks, linting, and other code quality
    checks before commits are made.
- term: isort
  definition: A Python utility that sorts the import statements in a Python application
    according to the specified configuration. It helps to keep imports organized and
    consistent.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260929074539.542864BA79A4@sourceware.org
date: '2026-09-29'
is_stub: true
stub_reason: low_score
---

The pre-commit configuration for the binutils-gdb project has been updated to use version 9.0.2 of the isort Python code formatter. This is part of a routine maintenance update, ensuring the project utilizes the latest stable version of its code formatting tools.
