---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- binutils
- pre-commit
- linting
commit_hash: fc3afcdce4245d5a084bc84b8f048c7c610b0d8d
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Add yamllint hook to pre-commit configuration.
tldr: Introduces yamllint as a pre-commit hook to lint the configuration file itself.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit adds a new repository entry in `.pre-commit-config.yaml`
  for `yamllint`. The hook is configured to target only the `.pre-commit-config.yaml`
  file itself, creating a self-linting mechanism for the pre-commit setup. This helps
  maintain the integrity and readability of the configuration file.
primer_glossary:
- term: pre-commit hook
  definition: A script that runs automatically before a commit is made. It's used
    to enforce coding standards, check for errors, or perform other quality control
    tasks.
- term: yamllint
  definition: A linter for YAML files that checks for syntax errors, best practices,
    and potential issues.
- term: TOML
  definition: Tom's Obvious, Minimal Language. A configuration file format that aims
    to be easy to read due to obvious semantics.
- term: .pre-commit-config.yaml
  definition: The main configuration file for the pre-commit framework, specifying
    which hooks to run and their settings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260728074401.A073D4BB24EE@sourceware.org
date: '2026-07-28'
is_stub: true
stub_reason: low_score
---

A new pre-commit hook using `yamllint` has been added to the `.pre-commit-config.yaml` file. This hook is specifically configured to lint the `.pre-commit-config.yaml` file itself, ensuring that the configuration for pre-commit hooks remains well-formatted and adheres to YAML standards.
