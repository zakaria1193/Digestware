---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- errata
- bfd
discussion_id: 20260806054354.27168-1-ktkachov@nvidia.com
source_type: public_inbox
title: '[PATCH] aarch64: ERRAT_NONE is not zero, so test against it'
headline: 'aarch64: ERRAT_NONE is not zero, so test against it'
tldr: A patch corrects a bug in aarch64 code where a workaround was incorrectly enabled
  by default due to a faulty comparison with ERRAT_NONE.
proposer: ktkachov@nvidia.com
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 8
technical_tradeoffs:
- Ensures erratum workarounds are only applied when explicitly requested, avoiding
  unnecessary link-time overhead.
exchanges:
- author: ktkachov@nvidia.com
  role: proposer
  position: Submits a patch to correct a logic error in aarch64 erratum handling where
    a workaround was always enabled due to an incorrect comparison with ERRAT_NONE.
  quote: null
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: reviewer
  position: Acknowledges the patch and its explanation, indicating it addresses the
    described issue.
  quote: null
primer_expert: The aarch64 backend in binutils' BFD library implements workarounds
  for specific hardware errata. This patch corrects a flaw in how these errata workarounds
  are enabled, specifically for `erratum_843419`. Previously, a non-zero `ERRAT_NONE`
  value caused the workaround to be applied even when not requested, impacting link-time
  performance and correctness.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260806054354.27168-1-ktkachov@nvidia.com
bugzilla_url: null
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the aarch64 BFD backend where the `fix_erratum_843419` workaround was being incorrectly enabled by default. The problem stems from `ERRAT_NONE` not being zero, causing a simple boolean test to evaluate as true even when no workaround was explicitly requested. The fix involves changing the comparison to explicitly check against `ERRAT_NONE`, aligning it with other erratum checks in the file.
