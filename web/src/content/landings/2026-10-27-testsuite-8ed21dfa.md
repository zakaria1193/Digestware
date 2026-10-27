---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- hppa
- openmp
commit_hash: 8ed21dfa6f62b80147fd5f444e9fd0da1ffc5a36
source_type: github
author: John David Anglin
headline: 'testsuite: Fix g++.dg/gomp/deprecate-1.C on hppa targets (v2)'
tldr: Testsuite fix for hppa targets related to OpenMP deprecation warnings.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The g++.dg/gomp/deprecate-1.C test uses a rigid multiline block for
  verification of diagnostic output. On hppa targets, the '#' character, which signifies
  a preprocessor directive and is part of the expected diagnostic output, is being
  stripped. This commit modifies the test to conditionally apply the rigid block only
  on non-hppa targets and uses dg-regexp directives to match the potentially altered
  output on hppa, preserving line indices.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8ed21dfa6f62b80147fd5f444e9fd0da1ffc5a36
date: '2026-10-27'
is_stub: true
stub_reason: low_score
---

This commit addresses a testsuite failure on hppa targets for the g++.dg/gomp/deprecate-1.C test. The issue stemmed from the leading '#' character being stripped from diagnostic source line mirror snippets during metadirective warning expansions. The fix restricts a literal multiline block to non-hppa targets and appends target-specific dg-regexp directives to handle unhashed caret fragments on PA-RISC architectures without altering file line indices.
