---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- vectorization
- loop optimization
- cost model
discussion_id: CAFiYyc0oSQ76NmAYDdcGTqpJcWb=FSV-cTqiXfnDiogaog-E3g@mail.gmail.com
source_type: public_inbox
title: 'Re: Uncounted loop vectorization example doesn''t work with unsigned index'
headline: Uncounted loop vectorization example doesn't work with unsigned index
tldr: Richard Biener investigates why certain seemingly vectorizable loops with unsigned
  indices are not being vectorized by GCC, pointing to cost model issues.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Vectorizing loops can improve performance, but not all loops are suitable for vectorization.
- The compiler's cost model may prevent vectorization if it deems it unprofitable.
- Unsigned loop indices can sometimes hinder the compiler's ability to estimate the
  number of iterations.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: other
  position: Explains that the loop using `unsigned long` does not get vectorized due
    to the cost model, while the loop with `long` does.  Suggests `-fno-vect-cost-model`
    to force vectorization.
  quote: It's a cost model issue.  With 'long' we get an estimate on the number of
    iterations, with 'unsigned long' we don't.
primer_expert: GCC's loop vectorizer uses a cost model to estimate the profitability
  of vectorizing loops. The cost model considers factors like the number of iterations,
  the complexity of the loop body, and the data types involved. This discussion highlights
  how the type of the loop index can affect the cost estimation, specifically how
  unsigned indices can hinder the compiler's ability to predict the number of iterations,
  impacting vectorization decisions.
primer_general: Loop vectorization is a compiler optimization that transforms a loop
  to execute multiple iterations in parallel, using vector instructions. This can
  significantly improve performance on modern CPUs. Compilers use cost models to decide
  whether vectorizing a loop is beneficial, considering factors such as loop complexity
  and data types. The choice of data types in a loop, like using a signed vs. unsigned
  integer for the loop index, can affect whether the compiler can effectively estimate
  the loop's trip count, and thus whether it decides to vectorize the loop.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc0oSQ76NmAYDdcGTqpJcWb=FSV-cTqiXfnDiogaog-E3g@mail.gmail.com
bugzilla_url: null
date: '2026-05-12'
is_stub: false
---

Richard Biener is debugging why a loop using an `unsigned long` index is not being vectorized, while the same loop with a `long` index is. He finds the vectorization is disabled by the cost model.  Using `-fno-vect-cost-model` enables vectorization, but this is not the default, indicating the compiler's cost analysis deems it unprofitable. The discussion highlights the nuances of loop vectorization and the impact of index types on the compiler's cost estimation.
