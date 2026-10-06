---
project: binutils
subsystem: pre-commit
patch_id: null
tags:
- devops
- code formatting
- binutils
commit_hash: 6abebae506b9df22bf9463c232b2b7b33ab3a229
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Binutils-gdb project updates Black formatter to version 26.10.0
tldr: The pre-commit configuration for the binutils-gdb repository has been updated
  to use Black version 26.10.0.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `.pre-commit-config.yaml` file in the binutils-gdb repository specifies
  the tools used for pre-commit code reviews. This commit updates the `rev` field
  for the Black formatter repository from `26.5.1` to `26.10.0`. This action is typically
  performed using the `pre-commit.py --autoupdate` script to ensure consistency across
  the project's development workflow.
primer_glossary:
- term: pre-commit
  definition: A framework for managing and maintaining multi-language pre-commit hooks.
    It helps automate the process of checking code style and quality before committing
    changes.
- term: Black formatter
  definition: An opinionated Python code formatter that automatically reformats Python
    code to adhere to a consistent style, reducing debates about code style.
- term: .pre-commit-config.yaml
  definition: A YAML configuration file that defines the pre-commit hooks to be run
    for a repository, including the repositories, revisions, and hooks themselves.
- term: binutils-gdb
  definition: The repository containing the GNU Binary Utilities (Binutils) and the
    GNU Debugger (GDB), essential tools for software development.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261006060525.41A964BA23DD@sourceware.org
date: '2026-10-06'
is_stub: true
stub_reason: low_score
---

The pre-commit configuration for the binutils-gdb project has been updated to use a newer version of the Black code formatter. The revision for Black has been advanced from 26.5.1 to 26.10.0, ensuring that code formatting checks adhere to the latest standards of the Black tool.
