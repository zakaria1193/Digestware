---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- compiler
commit_hash: 1dec3355162851ab3cf991fbf8c7fa9cd08331f3
source_type: github
author: Richard Biener
headline: Fix vector boolean type precision in pattern recognition
tldr: Corrects mask precision calculation for vector boolean types to enable proper
  vectorization.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: When VECTOR_BOOLEAN_TYPE_P uses an integer mode, the original scalar
  type is needed to determine the mask precision. Previously, `build_mask_conversion`
  and `vect_convert_mask_for_vectype` lacked this information, leading to incorrect
  `mask_precision` values and hindering vectorization. This change passes the `scalar_type_for_mask`
  parameter to these functions to rectify this.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/1dec3355162851ab3cf991fbf8c7fa9cd08331f3
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

This commit addresses an issue where the mask precision for vector boolean types was incorrectly calculated, leading to failed vectorization. By ensuring the original scalar type is used to determine precision, the fix enables correct pattern recognition and improves vectorization for specific operations.
