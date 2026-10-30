---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- build
- python
- linting
commit_hash: 928fa285bf87cddb0a2e88d74237d8db73e18340
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Update flake8 to version 7.5.0
tldr: The project's pre-commit hooks are updated to use flake8 version 7.5.0.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `.pre-commit-config.yaml` file specifies the versions of various
  pre-commit hooks used to maintain code quality. This change updates the `flake8`
  hook's revision from `7.4.1` to `7.5.0`, likely incorporating bug fixes or new checks
  from the upstream flake8 project.
primer_glossary:
- term: flake8
  definition: A Python linter that combines PyFlakes, pycodestyle, and McCabe complexity
    analysis to check Python code quality and style.
- term: pre-commit hook
  definition: A script that runs automatically before each commit, used to enforce
    code style, detect errors, and ensure code quality across the project.
- term: autoupdate
  definition: A feature of the pre-commit framework that automatically updates hook
    revisions to their latest versions.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261029083442.6C53A4BA2E05@sourceware.org
date: '2026-10-29'
is_stub: true
stub_reason: low_score
---

This commit updates the flake8 linter used by the project's pre-commit hooks from version 7.4.1 to 7.5.0. The update was performed automatically by running the `pre-commit.py --autoupdate` script, ensuring the codebase adheres to the latest linting rules and best practices.
