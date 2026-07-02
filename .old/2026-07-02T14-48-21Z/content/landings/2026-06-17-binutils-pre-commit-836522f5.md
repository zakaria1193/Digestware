---
project: binutils
subsystem: binutils/pre-commit
patch_id: null
tags:
- configuration
- tooling
- refactoring
commit_hash: 836522f582b848831e310cfcdcec078ea61436dd
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Drop types_or filtering for tclint
tldr: 'The superfluous `types_or: [file]` setting has been removed from the `tclint`
  pre-commit hook.'
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'The `types_or` setting in `pre-commit` configurations overrides a
  hook''s default file type detection, useful for hooks that implicitly exclude certain
  file kinds. For `tclint`, a linter for Tcl scripts, `types_or: [file]` was redundant
  because `tclint` lacks an inherent default file type that needs overriding. This
  removal eliminates an unnecessary filter, which simplifies the hook''s execution
  logic by avoiding a superfluous type-checking step.'
primer_general: 'When developers check their code, they often use automated tools
  called ''pre-commit hooks'' to run checks before saving changes. These checks are
  configured in a file named `.pre-commit-config.yaml`. This change removes a setting
  called `types_or: [file]` from the `tclint` hook, which is used to check Tcl language
  files for errors. The `types_or` setting is normally used to tell a tool to treat
  certain files as generic ''files'' even if it has a specific default file type.
  However, for `tclint`, there was no default type to override, making this setting
  unnecessary. Removing it streamlines the configuration and prevents the tool from
  doing extra, pointless filtering.'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617194010.9AD034BA2E11@sourceware.org
date: '2026-06-17'
is_stub: true
stub_reason: low-score
---

This change removes the `types_or: [file]` setting from the `tclint` pre-commit hook in `.pre-commit-config.yaml`. This filter was unnecessary because `tclint` does not have a default file type that `types_or` needed to override. Removing this redundant setting makes the configuration more precise and avoids performing additional, unneeded filtering.
