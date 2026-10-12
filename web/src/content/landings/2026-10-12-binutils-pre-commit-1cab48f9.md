---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- binutils
- pre-commit
- black
- formatting
- python
commit_hash: 1cab48f975454c2b484a699caa932057adb0a426
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Update black pre-commit hook to version 26.10.1
tldr: The code formatting tool 'black' used by pre-commit has been updated to version
  26.10.1.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `.pre-commit-config.yaml` file, which defines the project's pre-commit
  hook configurations, has been updated. Specifically, the revision for the `black-pre-commit-mirror`
  repository has been changed from `26.10.0` to `26.10.1`. This is a routine update
  to leverage the latest release of the Black formatter.
primer_glossary:
- term: pre-commit
  definition: A framework for managing and automating pre-commit hooks. These are
    scripts that run automatically on code commits, helping to enforce code style,
    detect errors, and ensure code quality before code is committed.
- term: black
  definition: An opinionated Python code formatter that automatically formats Python
    code according to a consistent style guide. It aims to reduce style-related discussions
    in code reviews.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261012061142.970AA4BA23D3@sourceware.org
date: '2026-10-12'
is_stub: true
stub_reason: low_score
---

This commit updates the version of the 'black' Python code formatter used by the project's pre-commit hooks. The update is from version 26.10.0 to 26.10.1, ensuring the project uses the latest minor release for code formatting consistency.
