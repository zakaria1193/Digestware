---
project: gcc
subsystem: ifcvt
patch_id: null
tags:
- ifcvt
- aarch64
- optimization
- gcc
commit_hash: 35decdaff05d720dc143d2877d8233178fce7212
source_type: github
author: Kyrylo Tkachov
headline: 'ifcvt, aarch64: Make the outside-loop profitability rule work'
tldr: AArch64 if-conversion now correctly applies profitability rules to code outside
  loops.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The AArch64 `if_convert` pass in GCC has a profitability heuristic
  (`aarch64_noce_conversion_profitable_p`) intended to apply less strict cost limits
  to code outside of loops, assuming poorer branch predictor performance in such scenarios.
  However, this rule never fired due to issues with loop tree management. In `ce1`,
  blocks outside loops were still part of the root loop, and in `ce2`/`ce3`, the loop
  tree was freed prematurely. This patch modifies `ifcvt.cc` to record natural loop
  membership (`in_loop` flag in `noce_if_info`) before the loop tree is freed. The
  AArch64 target hook then uses…
primer_glossary:
- term: if-conversion
  definition: A compiler optimization technique that transforms conditional control
    flow (like if-else statements) into data flow using conditional instructions (like
    conditional selects) to potentially improve performance by reducing branch prediction
    misses.
- term: AArch64
  definition: A 64-bit ARM architecture, commonly used in mobile devices and servers.
- term: profitability rule
  definition: A heuristic used by compilers to decide whether applying an optimization
    is likely to improve performance or code size.
- term: loop tree
  definition: A data structure used by the compiler to represent the hierarchical
    structure of loops within the code.
- term: natural loop
  definition: A loop in control flow graphs that has a single entry point (header).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/35decdaff05d720dc143d2877d8233178fce7212
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This commit fixes an issue where GCC's AArch64 if-conversion optimization incorrectly applied its cost limit to code blocks residing outside of loops. The original logic failed to identify these blocks as candidates for conversion because the loop tree was either still present or already freed by the time the check occurred. The patch records natural loop membership before loop tree finalization and passes this information to the target hook, allowing the AArch64 profitability rule to be applied only when optimizing for speed and when the code is indeed outside a loop, thus enabling more effective if-conversion in non-loop contexts.
