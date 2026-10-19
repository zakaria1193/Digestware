---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- hpux
commit_hash: c7a1a2e21c94d6a6d9af3602d7528db61ae887e4
source_type: github
author: John David Anglin
headline: 'testsuite: Fix regexps in src-loc-1_a.H and src-loc-1_c.C to match on hpux'
tldr: Adjusts test suite regular expressions for HPUX to correctly identify local
  labels.
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
url: https://github.com/gcc-mirror/gcc/commit/c7a1a2e21c94d6a6d9af3602d7528db61ae887e4
date: '2026-10-18'
is_stub: true
stub_reason: low_score
---

This commit modifies regular expressions within two test suite files, src-loc-1_a.H and src-loc-1_c.C, to accommodate the HPUX operating system. On HPUX, local labels are prefixed with 'L$' instead of the typical convention. The changes ensure that the test suite correctly matches these labels across different platforms.
