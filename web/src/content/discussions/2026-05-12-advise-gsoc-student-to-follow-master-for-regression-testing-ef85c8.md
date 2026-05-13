---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- gsoc
- regression testing
- openmp
- branches
discussion_id: 79f087e8-1881-4c57-b247-286ccf467d70@gmail.com
source_type: public_inbox
title: 'Re: [GSoC - OMP/ACC] Question on regression tests'
headline: Advise GSoC student to follow master for regression testing.
tldr: Martin Jambor advises a GSoC student to generally follow master for regression
  testing unless an issue is specific to a release branch.
proposer: Martin Jambor <mjambor@suse.cz>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 7
technical_tradeoffs: []
exchanges:
- author: Martin Jambor <mjambor@suse.cz>
  role: reviewer
  position: Recommends following the master branch for regression testing unless the
    issue is specific to a release branch.
  quote: I would always recommend following master fairly closely unless you have
    a specific reason not to
- author: Sebastian Galindo <sebastian.galindo143@gmail.com>
  role: other
  position: Acknowledges the advice to compare regression test results with and without
    the patch on the branch if necessary.
  quote: Sounds good! Thanks for your response.
primer_expert: This concerns the process of testing GCC patches, specifically OpenMP/ACC
  related fixes from GSoC students. Regression testing ensures that changes don't
  introduce new bugs or break existing functionality. Release branches (OG15) maintain
  older GCC versions.
primer_general: When fixing bugs in software like GCC, it's important to test the
  fix to ensure it doesn't create new problems. This is called regression testing.  GCC
  has a main development version (master) and stable release versions.  This discussion
  clarifies which version to use when regression testing a specific bug fix.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ri61pfgti1m.fsf@virgil.suse.cz
bugzilla_url: null
date: '2026-05-12'
is_stub: false
---

Sebastian Galindo asked about which branch to target for regression testing a fix in the OG15 branch (devel/omp/gcc-15). Martin Jambor recommends generally following master unless the issue only manifests on the release branch, in which case testing on that branch is necessary.
