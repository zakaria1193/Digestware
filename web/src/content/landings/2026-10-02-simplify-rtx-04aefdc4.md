---
project: gcc
subsystem: simplify-rtx
patch_id: null
tags:
- compiler
- warning
- bootstrap
commit_hash: 04aefdc47fd6baeff572f5087d6c30f5d7c2a575
source_type: github
author: Tamar Christina
headline: 'simplify-rtx: Avoid -Wuninitialized false positive'
tldr: Fixes a false positive -Wuninitialized warning during profiled bootstraps by
  improving analysis of conditional initializations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `simplify-context::simplify_subreg`, a `is_a<..>(&foo)` check was
  triggering a false positive for `-Wuninitialized`. The analyzer could not deduce
  that `foo` would be initialized post-check. The fix avoids passing `foo` by reference
  to `is_a`, removing the problematic aliasing that confused the analyzer.
primer_glossary:
- term: simplify-rtx
  definition: A GCC optimization pass that simplifies the compiler's internal representation
    (RTX) to facilitate further optimizations and code generation.
- term: profiled bootstrap
  definition: A multi-stage compilation process where the compiler's performance is
    measured and used to optimize subsequent compilation stages, often used to improve
    overall compiler speed.
- term: -Wuninitialized
  definition: A compiler warning flag that detects the use of uninitialized variables,
    helping to prevent bugs and undefined behavior.
- term: RTX
  definition: Representation of intermediate code in GCC, used after the front-end
    parses the source code and before code generation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/04aefdc47fd6baeff572f5087d6c30f5d7c2a575
date: '2026-10-02'
is_stub: false
stub_reason: ''
---

This commit resolves a false positive -Wuninitialized warning that occurred during profiled bootstraps in GCC's `simplify-rtx` pass. The warning stemmed from the compiler's analyzer failing to recognize that a variable `foo` would be initialized if a specific condition (`is_a <.., &foo>`) passed. The fix rewrites the check to avoid an out-parameter, thus eliminating the spurious warning.
