---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- linker
- testsuite
- symbol visibility
discussion_id: 20260525083249.11857-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Remove local hidden symbols testscase'
headline: 'LoongArch: Remove local hidden symbols testcase'
tldr: This patch removes hidden visibility for local symbols in LoongArch linker test
  cases, as it's meaningless and causes errors.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: zhaozhou
  role: proposer
  position: Proposes to remove local hidden symbol definitions from LoongArch test
    cases because they are meaningless and cause errors.
  quote: 'Remove the local symbol ldh definitions with hidden visibility from the

    relax-call36-*.s tests.  The hidden visibility is meaningless for local

    defined symbols and makes the test cases error.'
primer_expert: This patch modifies the LoongArch linker testsuite by removing `.hidden`
  directives applied to local symbols within `relax-call36-*.s` tests. This is because
  the hidden visibility attribute is intended for global symbols to control dynamic
  linking visibility, not for local symbols within a compilation unit. Applying it
  to local symbols can lead to unexpected linker behavior or errors.
primer_general: When building software, symbols are used to represent functions and
  variables.  Visibility attributes control how these symbols are accessed and linked
  between different parts of the code. This patch addresses an issue in the LoongArch
  architecture's linker tests where the `hidden` visibility attribute was incorrectly
  applied to local symbols, which are only meant to be used within a single file.
  Removing this incorrect attribute fixes errors in the testsuite.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260525083249.11857-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-05-25'
is_stub: false
---

This patch removes the definition of local symbols with hidden visibility in the `relax-call36-*.s` tests for the LoongArch architecture. The author states that hidden visibility is not meaningful for local symbols and is causing the test cases to fail.
