---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- regression testing
- OpenACC
- OpenMP
- bug fix
discussion_id: 87a4u3zb0l.fsf@euler.schwinge.ddns.net
source_type: public_inbox
title: 'Re: [GSoC - OMP/ACC] Question on regression tests'
headline: Question on regression tests
tldr: Discussion about which branch to target for regression tests related to an OpenACC
  bug fix.
proposer: Thomas Schwinge <tschwinge@baylibre.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Thomas Schwinge
  role: other
  position: Acknowledges the response and appreciates the detailed explanation regarding
    regression testing.
  quote: 'No worries; appreciate any such "verboseness".  As you say, it helps

    us/me check that you''re on the right track.'
primer_expert: This thread discusses regression testing in the context of GCC's OpenACC
  implementation.  The specific bug (93226) resides in the OG15 branch, which is the
  development branch for GCC 15's OpenMP/OpenACC features. The discussion revolves
  around whether to target the master branch or the OG15 branch for regression testing
  the fix.
primer_general: Regression testing is a crucial part of software development where
  existing tests are rerun after changes to ensure that new code doesn't break existing
  functionality.  In complex projects like GCC, multiple branches exist for different
  stages of development and maintenance. OpenACC is a programming standard for parallel
  computing that allows developers to offload computations to accelerators like GPUs.
  OpenMP is another API for shared-memory multiprocessing.  This discussion pertains
  to the correct procedure for validating a bug fix in a specific development branch
  of GCC using regression tests.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/87a4u3zb0l.fsf@euler.schwinge.ddns.net
bugzilla_url: null
date: '2026-05-13'
is_stub: false
---

This thread discusses which branch to use for regression testing a fix for bug 93226, which is in OG15 (devel/omp/gcc-15). Martin Jambor recommends following master closely unless there's a specific reason not to.  If the issue only manifests on the OG15 branch, then the regression test results should be compared with and without the fix on that branch.
