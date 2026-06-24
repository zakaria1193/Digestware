---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- pre-commit
- code-quality
- tools
- codespell
commit_hash: 664cc2deff7085b627da58f2d830491df25943d0
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Pre-commit hook now includes GDB files in codespell checks
tldr: Binutils now includes files from the GDB directory in its `codespell` pre-commit
  checks to catch spelling errors.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies the `.pre-commit-config.yaml` to extend the `codespell`
  hook's scope. The `files` regex for the `codespell` hook has been updated to explicitly
  include patterns matching `^gdb/[^/]*$`, thereby ensuring that files directly within
  the top-level `gdb` directory are now subject to spelling checks. This complements
  existing patterns that covered subdirectories, addressing a gap in coverage for
  certain GDB source files.
primer_general: Before code changes are permanently saved (or 'committed') to a project,
  many development teams use automated checks called 'pre-commit hooks' to find common
  mistakes. One such check is `codespell`, which looks for spelling errors. This change
  updates the configuration for these checks in the Binutils project to specifically
  include all the files that belong to the GDB debugger component. Previously, some
  GDB files might have been missed by the spell checker, potentially leading to typos.
  Now, by expanding the files included in the `codespell` check, the project aims
  to improve the overall quality and consistency of the GDB codebase.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260615112447.3F0FE4C3186E@sourceware.org
date: '2026-06-15'
is_stub: true
stub_reason: low-score
---

The Binutils project has expanded its `codespell` pre-commit checks to include files within the `gdb` directory. Previously, these files were not consistently covered by the spelling checker. This update modifies the `.pre-commit-config.yaml` to ensure broader coverage, enhancing code quality by catching typographical errors in the GDB codebase before commits are finalized.
