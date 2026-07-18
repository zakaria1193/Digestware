---
project: binutils
subsystem: binutils/gdb
patch_id: null
tags:
- binutils
- gdb
- pre-commit
- hooks
- testing
commit_hash: 0cdde1399d2d453569fe91c55b34b4879f8a6501
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Fix pre-commit hook for commit messages
tldr: Corrects the pre-commit hook configuration to ensure the codespell-log hook
  correctly processes commit messages.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The pre-commit hook configuration in `.pre-commit-config.yaml` was
  updated to resolve a regression where the `codespell-log` commit-msg hook was bypassed.
  The previous `files` directive, intended for repository files, incorrectly filtered
  out `.git/COMMIT_EDITMSG`. This change modifies the `files` pattern to include `.git/COMMIT_EDITMSG`,
  ensuring commit-msg hooks are invoked correctly. The test case in `gdb/testsuite/gdb.src/pre-commit.exp`
  was also adjusted to properly trigger and detect this behavior during regression
  testing.
primer_glossary:
- term: pre-commit hook
  definition: A script that runs automatically before a commit is created (or during
    other Git operations), used for tasks like linting, formatting, and spell-checking
    code and commit messages.
- term: commit-msg hook
  definition: A specific type of Git hook that runs after a commit message has been
    written but before the commit is finalized, allowing for validation or modification
    of the message.
- term: codespell-log
  definition: A pre-commit hook that checks for common spelling errors in code and
    commit messages.
- term: .git/COMMIT_EDITMSG
  definition: A temporary file in the `.git` directory that stores the commit message
    during the commit process.
- term: regression test
  definition: A test designed to ensure that a previously fixed bug does not reappear
    or that a new change does not break existing functionality.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260717111833.3714F4BA5439@sourceware.org
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This commit addresses an issue where the `codespell-log` pre-commit hook was not being triggered for commit messages. A recent change to the `files` filter in `.pre-commit-config.yaml` inadvertently excluded the `.git/COMMIT_EDITMSG` file, which is used by commit-msg hooks. The fix updates the configuration to include `.git/COMMIT_EDITMSG` in the filter, ensuring the hook properly analyzes commit messages, and also adjusts the associated regression test to accurately detect the issue.
