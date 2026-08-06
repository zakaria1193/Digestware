---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- error-handling
- diagnostics
discussion_id: CAMe9rOo_ayYvJ=YOH9BFGB-j96g7p+GOV=N7Pgsqpguzpqh+SA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] ld: Don''t treated the fatal error as warning'
headline: 'ld: Don''t treat fatal error as warning'
tldr: A patch has been applied to ensure fatal errors reported by the linker are not
  treated as warnings.
proposer: H.J. Lu
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: H.J. Lu
  role: proposer
  position: Announces that the patch to prevent fatal errors from being treated as
    warnings has been checked in.
  quote: I am checking it in.
primer_expert: The linker (`ld`) has been updated to correctly distinguish between
  fatal errors and warnings. A prior patch modified the `fatal` function to pass `false`
  for the `is_warning` argument to `vfinfo`. This ensures that messages identified
  as fatal errors are not subsequently processed or displayed as mere warnings, leading
  to clearer diagnostics for build failures.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into executable files or shared libraries.
- term: vfinfo
  definition: Likely a function within the linker or a related library used for reporting
    information or errors to the user.
- term: is_warning
  definition: A flag or parameter indicating whether a reported message is a warning
    or a more severe error.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOo_ayYvJ=YOH9BFGB-j96g7p+GOV=N7Pgsqpguzpqh+SA@mail.gmail.com
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

This discussion confirms that a patch has been applied to the linker (`ld`) to correct its error handling. Previously, fatal errors might have been misinterpreted as warnings due to how they were passed to the `vfinfo` function. The change ensures that fatal errors are consistently reported as such, aligning with expected behavior and improving diagnostic clarity.
