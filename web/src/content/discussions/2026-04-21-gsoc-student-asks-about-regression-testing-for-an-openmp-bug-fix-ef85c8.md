---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GSoC
- OpenMP
- OpenACC
- regression testing
- bug fix
discussion_id: 79f087e8-1881-4c57-b247-286ccf467d70@gmail.com
source_type: public_inbox
title: '[GSoC - OMP/ACC] Question on regression tests'
headline: GSoC student asks about regression testing for an OpenMP bug fix.
tldr: Sebastian Galindo asks whether to run regression tests against the development
  branch or trunk/master after fixing a bug in OG15.
stakes: Ensuring proper regression testing is crucial for maintaining the stability
  and correctness of GCC, especially in the context of GSoC contributions.
proposer: Sebastian Galindo <sebastian.galindo143@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Testing against the development branch provides isolation but may miss interactions
  with other changes.
- Testing against trunk/master tests integration but can introduce unrelated failures.
exchanges:
- author: Sebastian Galindo <sebastian.galindo143@gmail.com>
  role: proposer
  position: Asks whether to run regression tests against the development branch or
    trunk/master after fixing a bug in OG15.
  quote: Since the bug is in OG15 (i.e., devel/omp/gcc-15, if I am understanding correctly),
    should I run the regression tests against that branch, or against trunk/master?
primer_expert: The student is working on OpenMP/ACC features within GCC.  OG15 likely
  refers to a specific development branch for GCC version 15, focusing on OpenMP and
  potentially OpenACC extensions.  The question is whether regression tests should
  be run against the specific development branch where the fix was made, or against
  the main development branch (trunk/master).  This decision impacts whether the fix
  is tested in isolation or in the context of more recent changes.
primer_general: Regression tests are automated tests designed to ensure that new code
  changes do not introduce new bugs or break existing functionality. In GCC development,
  regression testing is a crucial step before a patch is accepted.  The student is
  working on a bug fix related to OpenMP (a parallel programming API) and OpenACC
  (a directive-based programming model for accelerators) within the GCC compiler.
  The question is about which version of the GCC source code should be used to run
  these tests.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/79f087e8-1881-4c57-b247-286ccf467d70@gmail.com
bugzilla_url: null
date: '2026-04-21'
---

Sebastian Galindo, a GSoC student working on OpenMP/ACC, seeks guidance on the correct procedure for regression testing a bug fix. Having fixed bug 93226 in OG15, Galindo is unsure whether to run regression tests against the devel/omp/gcc-15 branch or the trunk/master branch.
