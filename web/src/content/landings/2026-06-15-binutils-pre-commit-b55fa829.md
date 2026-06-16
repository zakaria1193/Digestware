---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- pre-commit
- file-permissions
- code-hygiene
- tools
commit_hash: b55fa8294aebd5e9587169f3c74decea7fec5c33
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Pre-commit hook now checks for incorrect file modes in Binutils
tldr: Binutils has added a pre-commit hook to detect and prevent incorrect file permissions,
  specifically executable modes on non-executable source files.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit integrates `check-file-mode.sh` as a new pre-commit hook
  within `binutils-gdb`. The hook, residing in `gdb/contrib`, uses `git ls-files -s`
  to enumerate staged files and filters them to identify files marked as executable
  (mode `100755`) that should, by convention, only have read/write permissions (e.g.,
  `100644`). This hook directly addresses a scenario where source files acquire executable
  bits, which, while not functionally critical for compilation, indicates a deviation
  from standard repository hygiene and can sometimes interfere with build environments
  or package managers. Th…
primer_general: In software projects, every file has 'permissions' that control who
  can read, write, or execute it. For example, a program needs 'execute' permission
  to run, but a simple text file with source code usually only needs 'read' and 'write'
  permissions. Sometimes, due to development tools or how code changes are managed,
  source code files can accidentally get marked as 'executable'. This doesn't usually
  break the program, but it's not correct and can sometimes cause minor issues or
  confusion. This change adds a new automated check, called a 'pre-commit hook,' to
  the Binutils project. This check runs automatically before new code is saved and
  specifically looks for source code files that have been incorrectly marked as executable.
  If it finds any, it will alert the developer, helping to keep file permissions consistent
  and correct across the entire project.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260615081649.C70464B99F68@sourceware.org
date: '2026-06-15'
is_stub: false
---

A new pre-commit hook has been introduced to the Binutils project to verify file permissions. This `check-file-mode` hook identifies source files that have been mistakenly marked as executable, which can happen during development or merging processes. By automatically flagging these discrepancies, the hook prevents incorrect file modes from being committed, ensuring consistency and preventing potential issues with build systems or deployment.
