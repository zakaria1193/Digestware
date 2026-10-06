---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- analyzer
commit_hash: d5cdcaaf9a8800900f60dd7f8894f12cbcab11d3
source_type: github
author: linden
headline: 'gcc, analyzer: drop std::move calls that have no effect'
tldr: Remove redundant std::move calls in GCC's analyzer and XML processing.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit cleans up unnecessary std::move operations in the GCC analyzer
  and its XML output generation. Specifically, it targets calls where the argument
  is taken by const reference or where std::string::operator+=(std::string&&) is not
  applicable, effectively making the std::move a no-op. The changes are in gcc/xml.cc
  and gcc/analyzer/access-diagram.cc/engine.cc.
primer_glossary:
- term: std::move
  definition: A standard library function that unconditionally converts its argument
    into an rvalue reference, typically used to enable move semantics for resources
    like memory or file handles. It signals that the source object can be left in
    a valid but unspecified state after the move.
- term: GCC analyzer
  definition: A static analysis pass within GCC that detects potential runtime errors
    and undefined behavior by examining code without executing it. It operates on
    GCC's intermediate representation.
- term: rvalue reference
  definition: A reference that can bind to temporary objects (rvalues). It's a key
    mechanism for implementing move semantics and perfect forwarding in C++.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d5cdcaaf9a8800900f60dd7f8894f12cbcab11d3
date: '2026-09-26'
is_stub: true
stub_reason: low_score
---

Three call sites in GCC's analyzer and XML processing incorrectly used std::move on arguments that could not be moved. These redundant std::move calls have been removed, ensuring no change in behavior while slightly cleaning up the code.
