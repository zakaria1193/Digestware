---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- error handling
- binutils
discussion_id: CAMe9rOqjBsX-4MkE0bonCMmj0Qyvxpd3cTZa9qq65vz7vtmsjw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] ld: Don''t ignore bfd_gc_sections failure'
headline: 'ld: Don''t ignore bfd_gc_sections failure'
tldr: Report bfd_gc_sections failures as fatal errors instead of warnings to prevent
  potential issues in the linker.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Ensures critical errors are not silently ignored.
- Slightly increases verbosity if `bfd_gc_sections` fails, but improves robustness.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Proposes to issue a fatal error when bfd_gc_sections fails instead of
    treating it as a warning.
  quote: If bfd_gc_sections fails, issue a fatal error and change fatal to pass false
    as the is_warning argument to vfinfo so that the fatal isn't treated as a warning
    by vfinfo.
- author: Jan Beulich
  role: reviewer
  position: Agrees with the change but suggests splitting it into two separate commits
    for better clarity.
  quote: Okay, albeit I think the two would better have been separate changes.
primer_expert: This patch addresses an issue in binutils/ld where a failure in `bfd_gc_sections`
  might not be escalated to a fatal error. The change modifies how the `fatal` function
  is invoked to ensure such failures are treated with the appropriate severity, preventing
  them from being masked as warnings.
primer_glossary:
- term: bfd_gc_sections
  definition: A function within the Binary File Descriptor (BFD) library used by the
    linker to garbage collect unused sections in an object file.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: vfinfo
  definition: A function likely used for verbose informational output within the linker,
    which differentiates between fatal errors and warnings.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqjBsX-4MkE0bonCMmj0Qyvxpd3cTZa9qq65vz7vtmsjw@mail.gmail.com
bugzilla_url: null
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

This patch modifies the linker (ld) to treat failures in bfd_gc_sections as fatal errors. Previously, these failures were sometimes treated as warnings. The change ensures that the `fatal` function is called with correct arguments to prevent the failure from being misinterpreted. This addresses an issue where linker warnings might mask critical errors, potentially leading to incorrect output.
