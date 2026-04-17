---
project: glibc
subsystem: glibc
patch_id: null
tags:
- contribution guidelines
- tooling
- LLM
- attribution
discussion_id: lhuh5p992bo.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: Contribution guidelines update regarding tool usage
headline: 'glibc: Update contribution guidelines to mention tool usage and Assisted-by'
tldr: Proposes updating glibc's contribution guidelines to require mentioning tools
  used for code generation and to allow `Assisted-by` trailers.
stakes: Promotes transparency and proper attribution when using code-generating tools,
  including LLMs.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The proposal is generally well-received.
technical_tradeoffs:
- Adding these guidelines increases the burden on contributors slightly.
- More detailed attribution improves transparency and clarifies licensing.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuh5p992bo.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-17'
---

Florian Weimer proposes updating the glibc contribution guidelines to require mentioning tools used to auto-generate code and to allow reviewers to request an "Assisted-by" Git trailer. This aligns with existing practices for tools like autoconf and addresses recent discussions about LLM usage.
