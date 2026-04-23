---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GSoC
- OpenMP
- regression testing
- bug fix
discussion_id: 79f087e8-1881-4c57-b247-286ccf467d70@gmail.com
source_type: public_inbox
title: '[GSoC - OMP/ACC] Question on regression tests'
headline: GSoC student asks about running regression tests for bug fix
tldr: A GSoC student asks which branch to target for regression tests after fixing
  a bug in the OpenMP/ACC component.
stakes: Proper regression testing ensures bug fixes don't introduce regressions, maintaining
  code quality and stability.
proposer: Sebastian Galindo <sebastian.galindo143@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Testing against the older branch ensures the fix works in the specific release,
  but might miss issues in newer code.
- Testing against trunk/master tests the fix against the latest code, but might not
  accurately reflect the state of the older release.
exchanges: []
primer_expert: The student is working on a bug fix in the OpenMP/ACC component of
  GCC, specifically targeting the OG15 branch (likely referring to a GCC 15 development
  branch). The question concerns the correct branch to use for regression testing
  to validate the fix.
primer_general: This email is from a student participating in the Google Summer of
  Code (GSoC) program, contributing to the GNU Compiler Collection (GCC). GCC is a
  suite of programming language compilers. Regression testing is a process of re-running
  tests after a code change to ensure that the change hasn't introduced new bugs or
  broken existing functionality. The student's question concerns the specific version
  of GCC they should use to run these tests.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/79f087e8-1881-4c57-b247-286ccf467d70@gmail.com
bugzilla_url: null
date: '2026-04-21'
---

Sebastian Galindo, a GSoC student, fixed a bug (93226) related to debugging in the OpenMP/ACC component.  Having tested the fix and added a detailed explanation to Bugzilla, Galindo asks whether to run regression tests against the OG15 branch or the trunk/master branch.
