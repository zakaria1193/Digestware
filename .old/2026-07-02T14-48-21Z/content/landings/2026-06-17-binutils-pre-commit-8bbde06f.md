---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- configuration
- tooling
- refactoring
commit_hash: 8bbde06fa2a0ac754e6e8e2354e59721ee2c81b3
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Remove pass_filenames setting for check-whitespace
tldr: 'The redundant `pass_filenames: true` setting was removed from the `check-whitespace`
  pre-commit hook.'
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'Within the `pre-commit` framework, the `pass_filenames` flag determines
  whether the paths of staged files are passed as arguments to the hook''s script.
  For the `check-whitespace` hook, designed to examine file content, this behavior
  is a default. Removing `pass_filenames: true` merely eliminates a redundant configuration
  entry, which is a common cleanup for `pre-commit` hooks that rely on default behaviors.'
primer_general: 'Before code changes are saved, automated checks run to ensure code
  quality. These checks are configured in a file called `.pre-commit-config.yaml`.
  One of these checks, `check-whitespace`, looks for improper spacing in code files.
  This change removes a setting called `pass_filenames: true` from the `check-whitespace`
  hook. This setting tells the hook to receive a list of the files that have changed.
  Since this is the default behavior for such checks, explicitly stating `true` was
  unnecessary. Removing it makes the configuration cleaner without altering how the
  whitespace check works.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617194020.CA4EC4BA2E1E@sourceware.org
date: '2026-06-17'
is_stub: true
stub_reason: low-score
---

This commit eliminates the `pass_filenames: true` setting for the `check-whitespace` pre-commit hook in the `.pre-commit-config.yaml` file. Because `true` is the default value for `pass_filenames`, explicitly stating it is unnecessary. This change simplifies the configuration without affecting the hook's operation.
