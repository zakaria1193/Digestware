---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GSoC
- OpenMP
- regression testing
discussion_id: 79f087e8-1881-4c57-b247-286ccf467d70@gmail.com
source_type: public_inbox
title: '[GSoC - OMP/ACC] Question on regression tests'
headline: GSoC student asks about regression tests for OpenMP bug fix
tldr: A GSoC student asks whether regression tests for their OpenMP bug fix should
  target the OG15 branch or trunk/master.
stakes: Ensuring bug fixes have proper regression tests maintains the stability and
  reliability of GCC, especially in actively developed areas like OpenMP.
proposer: Sebastian Galindo <sebastian.galindo143@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Testing against OG15 ensures the fix works in the specific version, but may not
  catch issues that arise in newer versions.
- Testing against trunk/master ensures the fix works in the latest development version,
  potentially catching broader issues, but may not perfectly reflect the OG15 environment.
exchanges: []
primer_expert: This question concerns regression testing within the GCC OpenMP (OG15)
  development branch. The student is unsure whether to run regression tests against
  the specific OG15 branch or the main trunk/master. This relates to the process of
  backporting fixes and ensuring stability across different GCC versions.
primer_general: Regression testing is a crucial part of software development, especially
  for complex projects like GCC. It involves running existing tests after a change
  to ensure that the change hasn't introduced new bugs or broken existing functionality.  This
  is particularly important in areas like OpenMP, which deals with parallel programming
  and can be tricky to get right. The question is whether to test the fix against
  the specific version where the bug was found (OG15) or against the latest development
  version (trunk/master).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/79f087e8-1881-4c57-b247-286ccf467d70@gmail.com
bugzilla_url: null
date: '2026-04-21'
---

Sebastian Galindo, a Google Summer of Code student, has fixed bug 93226 related to OpenMP. They seek guidance on which branch to target for regression testing: the OG15 branch (devel/omp/gcc-15) or trunk/master. They have provided a detailed explanation of the fix in Bugzilla and believe no additional tests are needed.
