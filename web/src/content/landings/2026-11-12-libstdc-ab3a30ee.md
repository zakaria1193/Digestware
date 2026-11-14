---
project: gcc
subsystem: libstdc++
patch_id: null
tags: []
commit_hash: ab3a30eeb2f70baf07f5710b529d5103b0541dd6
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Avoid ''_T'' in comment for template argument'
tldr: Avoids a forbidden name in a comment to prevent false positives in code searches.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: ''
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab3a30eeb2f70baf07f5710b529d5103b0541dd6
date: '2026-11-12'
is_stub: true
stub_reason: low_score
---

This change modifies a comment in libstdc++'s regex header to use 'T' instead of '_T' as a template argument. This prevents a false positive when searching for uses of '_T', improving code analysis tool usability.
