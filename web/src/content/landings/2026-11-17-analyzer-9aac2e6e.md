---
project: gcc
subsystem: analyzer
patch_id: null
tags:
- analyzer
- diagnostics
- logging
commit_hash: 9aac2e6ea201af2c4435793f3077bb879e1e42cf
source_type: github
author: Oleg Tolmatcev
headline: Analyzer avoids duplicate location prefixes and unsigned comparison warnings
tldr: Fixes duplicate '0x' prefixes in diagnostic output and unsigned comparison warnings
  in the analyzer.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC analyzer's diagnostic output, particularly when using the %wx
  format specifier, was prepending '0x' to hex values, which conflicted with the specifier's
  own prefix. This commit removes the redundant prefix. It also addresses a signed/unsigned
  comparison warning by ensuring loop counters match the type of the value they are
  comparing against, specifically for call-string lengths within the engine.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9aac2e6ea201af2c4435793f3077bb879e1e42cf
date: '2026-11-17'
is_stub: true
stub_reason: low_score
---

The code pretty-printer's %wx directive was causing duplicate '0x' prefixes in the analyzer's logging and DOT output. This has been fixed by removing the redundant prefix at the call sites. Additionally, a signed comparison warning was resolved by making the loop index unsigned when iterating through call-string lengths.
