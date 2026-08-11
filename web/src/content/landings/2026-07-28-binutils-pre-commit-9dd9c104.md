---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- binutils
- pre-commit
- linting
- yaml
commit_hash: 9dd9c10463a561aaeb7de78bdc8a8b4ad0138352
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Fix yamllint errors in pre-commit configuration.
tldr: Corrects YAML formatting issues in `.pre-commit-config.yaml` to comply with
  yamllint rules.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit cleans up the `.pre-commit-config.yaml` file by resolving
  issues reported by `yamllint`. The changes involve correcting indentation, ensuring
  proper document start markers (`---`), and fixing whitespace errors, which are crucial
  for maintaining the readability and correct parsing of the pre-commit configuration.
primer_glossary:
- term: pre-commit hook
  definition: A script that runs automatically before a commit is made. It's used
    to enforce coding standards, check for errors, or perform other quality control
    tasks.
- term: yamllint
  definition: A linter for YAML files that checks for syntax errors, best practices,
    and potential issues.
- term: YAML
  definition: A human-readable data-serialization standard. Commonly used for configuration
    files.
- term: .pre-commit-config.yaml
  definition: The main configuration file for the pre-commit framework, specifying
    which hooks to run and their settings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260728074356.86A004BB1C26@sourceware.org
date: '2026-07-28'
is_stub: true
stub_reason: low-score
---

This commit addresses several YAML formatting errors detected by `yamllint` within the `.pre-commit-config.yaml` file. The fixes include adding a missing document start marker, correcting indentation, and resolving whitespace issues, ensuring the configuration file is properly formatted and lintable.
