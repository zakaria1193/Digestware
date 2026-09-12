---
project: gcc
subsystem: backthreader
patch_id: null
tags:
- debugging
commit_hash: b2ccf81fa3097eab7ee3f96243004236d077d962
source_type: github
author: Aldy Hernandez
headline: Backthreader corrects dump messages in adjust_one_path.
tldr: Cleans up and corrects diagnostic messages in the backthreader's adjust_one_path
  function for better clarity.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The dump messages from `back_jt_path_registry::adjust_one_path` were
  misleading. This commit corrects them to accurately reflect the conditions under
  which candidates are cancelled (e.g., being a prefix), why rewiring might fail (e.g.,
  `rewire_first_differing_edge` failure), and when candidates are dropped due to structural
  limitations (e.g., not being able to chop to a one-edge candidate).
primer_glossary:
- term: backthreader
  definition: A GCC pass that optimizes control flow by identifying and threading
    common execution paths, aiming to reduce execution time and improve instruction
    cache locality.
- term: adjust_one_path
  definition: A function within the GCC backthreader responsible for adjusting a single
    candidate path to align with the main threaded path.
- term: candidate path
  definition: A potential control flow path that the backthreader is considering for
    optimization or integration with the main execution flow.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b2ccf81fa3097eab7ee3f96243004236d077d962
date: '2026-09-10'
is_stub: true
stub_reason: low_score
---

This commit refactors diagnostic messages within the `adjust_one_path` function of the backthreader. It clarifies messages related to candidates being prefixes of the threaded path, failures in rewiring, and the dropping of ill-formed candidates, improving the interpretability of compiler dumps.
