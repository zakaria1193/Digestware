---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- linker
- testsuite
- coff
- windows
commit_hash: 3f8a2c9722b1dcb5525ce3943c5c3f98404ace67
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Add PE COFF weak external symbol tests
tldr: New test suite added for PE COFF weak external symbol resolution.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: 'This commit introduces a new test suite within `ld/testsuite/ld-pe`
  focused on PE COFF weak external symbols. It covers a matrix of weak/strong symbol
  interactions, including archive member resolution and the behavior of weak declarations
  with null fallbacks versus real definitions. The tests are based on work by Martin
  Storsjö and aim to validate correct symbol resolution logic in the PE COFF linker.


  Search context: "binutils ld PE COFF weak external tests archive"'
primer_general: This change enhances the testing for the GNU linker (ld), specifically
  for Windows PE COFF object files. PE COFF files support 'weak external' symbols,
  which are special symbols that can have a fallback definition if no explicit definition
  is found. This commit adds extensive automated tests to ensure the linker correctly
  handles these weak symbols, especially when they are part of archives or when they
  interact with other symbols in complex ways. This improves the reliability of the
  linker for Windows development.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260630234859.06B444BA2E37@sourceware.org
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

A comprehensive set of tests has been added to the linker's test suite to cover weak external symbol behavior in PE COFF files. These tests address various interactions between weak and strong symbols, including those involving archives and specific fallback definitions. This enhancement aims to improve the robustness and correctness of the linker's handling of complex symbol resolution scenarios.
