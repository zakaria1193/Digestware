---
project: binutils
subsystem: binutils
patch_id: null
tags:
- testing
- assembly
- disassembly
- nanomips
discussion_id: 20260717103858.199743-7-lei.wang@oss.cipunited.com
source_type: public_inbox
title: '[PATCH 6/6] Add nanoMIPS tests.'
headline: Add nanoMIPS tests.
tldr: Adds test cases for the nanoMIPS architecture to binutils.
proposer: Tsing <lei.wang@oss.cipunited.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Adds test cases for nanoMIPS in binutils. Specifically targets objdump's
  cpus_expected list and gas's various test suites (all, cfi, elf) to verify nanoMIPS
  assembly and disassembly functionalities, noting expected failures for some tests.
primer_glossary: []
series_id: binutils:add nanomips tests
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260717103858.199743-7-lei.wang@oss.cipunited.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch introduces new test cases for the nanoMIPS architecture within the binutils test suite. It modifies objdump and gas test configurations to include specific tests for nanoMIPS, such as debug_ranges, relax, cfi, and groupauto tests, some of which are expected to fail initially.
