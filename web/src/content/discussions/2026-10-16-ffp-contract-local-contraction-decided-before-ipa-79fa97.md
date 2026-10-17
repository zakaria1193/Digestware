---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- floating-point
- determinism
- compiler
discussion_id: CAMDxqyYZjS5kNzw6O6mFccgtwcLaOHnG9_wn8o-WH3L5sSArMQ@mail.gmail.com
source_type: public_inbox
title: '[RFC] -ffp-contract=local: contraction decided before IPA'
headline: 'ffp-contract=local: contraction decided before IPA'
tldr: Proposal for a new GCC flag -ffp-contract=local to deterministically control
  floating-point contraction before inter-procedural analysis.
proposer: paavan kumar <paavan.kumar@gravitontrading.com>
consensus: Proposed
outcome: under_review
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Potential performance impact if the local pass is not aggressive enough or if target-specific
  FMA optimizations are missed.
- Introduces a new compiler flag, increasing complexity for users.
- Aims to improve build reproducibility at the cost of potentially less aggressive
  FMA optimization in some scenarios compared to -ffp-contract=fast.
exchanges:
- author: paavan kumar <paavan.kumar@gravitontrading.com>
  role: proposer
  position: Proposes an opt-in mode -ffp-contract=local to achieve deterministic floating-point
    contraction by performing fusion before inter-procedural analysis.
  quote: With -ffp-contract=fast, whether a * b + c gets fused depends on IPA inlining,
    so unrelated code can change the result of a function that didn't change.
- author: Richard Biener <rguenther@suse.de>
  role: reviewer
  position: Agrees that the contraction pass must occur after IPA to correctly use
    target-specific information for offloaded functions.
  quote: It must be after IPA since it otherwise may use the wrong target when optimizing
    functions marked for offloading.
- author: Paavan Indela <indela.paavankumar@gmail.com>
  role: contributor
  position: Clarifies that the revised proposal places contraction after IPA and vectorization,
    and suggests that achieving FMA across calls might require annotations like __builtin_assoc_barrier.
  quote: 'Agreed. The revised version keeps contraction in widening_mul, after IPA
    and vectorization.


    Also allowing early inlining but not IPA is odd and feels like a heuristic specifically
    tuned to the problem. As you do want to form FMA across calls I don''t think the
    issue can be solved without annotation with for example __builtin_assoc_barrier'
primer_expert: This proposal addresses non-determinism in floating-point code generation
  related to fused multiply-add (FMA) operations. When -ffp-contract=fast is used,
  the decision to fuse multiplication and addition into a single FMA instruction can
  depend on inter-procedural analysis (IPA) and subsequent inlining. This RFC suggests
  -ffp-contract=local to perform fusion in an earlier pass, before IPA, making the
  outcome more predictable and independent of unrelated code changes, thereby fixing
  issues like PR106902 and PR126195.
primer_glossary:
- term: IPA
  definition: Inter-Procedural Analysis. A compiler analysis that examines relationships
    between different functions in a program, often used for optimizations like inlining.
- term: FMA
  definition: Fused Multiply-Add. A single floating-point instruction that computes
    (a * b) + c, often providing higher precision and performance than separate multiply
    and add operations.
- term: FP-contract
  definition: Floating-point contraction. Refers to the compiler's ability to fuse
    floating-point operations like multiplication and addition.
- term: non-deterministic
  definition: An outcome that can vary even with the same input, often due to factors
    like code layout, compiler heuristics, or optimization choices that change between
    builds.
- term: build reproducibility
  definition: The property of a build system or compiler that ensures identical output
    is produced every time a program is compiled, even if intermediate optimization
    choices vary.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAMDxqyYZjS5kNzw6O6mFccgtwcLaOHnG9_wn8o-WH3L5sSArMQ@mail.gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

Paavan Kumar proposes adding a new GCC option, -ffp-contract=local, to address non-deterministic floating-point contraction (FMA) behavior caused by inter-procedural analysis (IPA) and inlining. This option would perform FMA fusion in an early optimization pass, making contraction decisions independent of later inlining, thus improving build reproducibility. The goal is to prevent unrelated code changes from affecting floating-point results in functions that have not themselves changed.
