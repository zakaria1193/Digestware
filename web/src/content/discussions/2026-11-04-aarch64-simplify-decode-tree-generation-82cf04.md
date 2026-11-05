---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- disassembler
- code generation
- refactoring
discussion_id: af546ddb-7221-843f-e17d-4b619ce4bceb@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 22/28] aarch64: Simplify decode tree generation'
headline: 'aarch64: Simplify decode tree generation'
tldr: Simplifies AArch64 decode tree generation by printing the tree on-the-fly.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Simplifies code by removing intermediate data structures, potentially at the cost
  of some flexibility for future complex tree manipulations.
exchanges: []
primer_expert: Refactors `opcodes/aarch64-gen.c` to simplify the decode tree generation
  process. Instead of building an intermediate `bittree` data structure and then processing
  it, this change generates the decision tree code directly into the output file.
  This removes the need for intermediate storage and simplifies the overall code flow,
  as the tree is now constructed and output in a single pass.
primer_glossary: []
series_id: 'binutils:aarch64: simplify decode tree generation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/af546ddb-7221-843f-e17d-4b619ce4bceb@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch refactors the AArch64 decode tree generation in `opcodes/aarch64-gen.c`. It eliminates the need to store the computed tree for multiple users by printing the generated decision tree directly. This change streamlines the code and results in no modification to the generated output, simplifying maintenance.
