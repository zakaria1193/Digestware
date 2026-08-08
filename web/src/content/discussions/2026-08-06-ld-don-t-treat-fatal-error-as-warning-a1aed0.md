---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- error handling
- patch
discussion_id: alpine.DEB.2.21.2608060446450.55540@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH] ld: Don''t treated the fatal error as warning'
headline: 'ld: Don''t treat fatal error as warning'
tldr: Disagreement over whether a fatal linker error should be treated as a warning.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- The patch aims to improve error reporting accuracy by distinguishing fatal errors
  from warnings.
- The objection raises concerns about the potential side effects or correctness of
  this change in the `ld` tool.
exchanges:
- author: H. J. Lu
  role: reviewer
  position: Indicates intent to apply a patch that modifies error handling in `ld`.
  quote: If there is no objection, I will check it in next week.
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: proposer
  position: Objects to the patch, stating that his objection was previously made.
  quote: I did object, didn't I?
primer_expert: A disagreement on the `ld` mailing list regarding a patch that alters
  error reporting. The patch intends to prevent `vfinfo` from treating a fatal linker
  error as a warning. One reviewer indicated they would apply it, but another explicitly
  voiced an objection, creating a stall.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or other binary.
- term: vfinfo
  definition: Likely a function within binutils related to reporting information or
    errors, possibly during the linking process.
- term: fatal error
  definition: An error condition that is severe enough to halt the program's execution
    immediately.
- term: warning
  definition: A message indicating a potential problem or non-critical issue that
    does not necessarily stop program execution.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2608060446450.55540@angie.orcam.me.uk
bugzilla_url: null
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

Maciej W. Rozycki objects to a patch that changes how the linker (`ld`) handles fatal errors, specifically concerning the `vfinfo` function. H.J. Lu had previously indicated intent to check in the patch, but Rozycki explicitly states he objected. The core issue is whether `vfinfo` should continue to treat a fatal error as a warning.
