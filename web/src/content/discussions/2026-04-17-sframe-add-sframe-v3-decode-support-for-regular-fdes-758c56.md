---
project: glibc
subsystem: sframe
patch_id: null
tags:
- sframe
- backtracing
- debugging
- FDE
- v3
discussion_id: 755f5dfe-fb19-4888-b778-9ec4449e6822@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] sframe: Add SFrame v3 decode support for regular FDEs'
headline: 'sframe: Add SFrame v3 decode support for regular FDEs'
tldr: This patch adds support for decoding SFrame v3 format, which includes changes
  to function descriptor layouts and stack trace backtracing.
stakes: This update enables glibc to work with newer SFrame formats, which are used
  for stack unwinding and debugging, potentially improving application debugging and
  performance analysis.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
sentiment_score: 9
sentiment_rationale: The patch receives positive feedback and addresses an important
  feature, suggesting strong approval.
technical_tradeoffs:
- Adds complexity to the sframe decoding logic.
- Requires careful handling of different SFrame versions.
- May introduce performance overhead due to additional checks and processing.
- Needs to maintain compatibility with existing SFrame v2 implementations.
series_id: 'glibc:sframe: add sframe v3 decode support for regular fdes'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/755f5dfe-fb19-4888-b778-9ec4449e6822@linux.ibm.com
bugzilla_url: null
date: '2026-04-17'
---

This patch adds SFrame v3 format definitions and updates backtrace routines to handle both v2 and v3 function descriptor layouts. The updated stack trace backtracer detects the outermost frame, reads v3 index/attribute records, performs bounds checks, and uses int64_t PC/start-address handling. The patch looks good, with a minor indentation nit.
