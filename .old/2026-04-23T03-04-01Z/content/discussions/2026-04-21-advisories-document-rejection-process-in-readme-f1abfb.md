---
project: glibc
subsystem: advisories
patch_id: null
tags:
- advisories
- documentation
- security
discussion_id: a07f4b38-bee2-4163-b758-0c993d340dd7@gotplt.org
source_type: public_inbox
title: 'Re: [PATCH 1/2] advisories: Document rejection process in README.'
headline: 'Advisories: Document rejection process in README'
tldr: Documents the process for rejecting advisories in the advisories/README file.
stakes: Improves clarity and maintainability of glibc security advisories by documenting
  the rejection process.
proposer: Siddhesh Poyarekar <siddhesh@gotplt.org>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Siddhesh Poyarekar <siddhesh@gotplt.org>
  role: proposer
  position: Acknowledges LGTM from the previous reviewer.
  quote: LGTM.
primer_expert: 'The `advisories/` directory in glibc contains security advisories.  This
  patch documents the process for marking an advisory as rejected, including adding
  the "REJECTED: " prefix to the description and a `Rejected-Date` tag. This is purely
  documentation; no code changes are involved.'
primer_general: 'Glibc maintains a directory of security advisories to inform users
  about potential vulnerabilities. This patch enhances the documentation for the advisory
  process, specifically detailing how to reject an advisory. This includes adding
  a "REJECTED: " prefix to the advisory''s description, explaining the reason for
  rejection, and adding a `Rejected-Date` tag, thereby clarifying the process for
  contributors.'
series_id: 'glibc:advisories: document rejection process in readme'
series_role: reply
series_parts:
- title: 'advisories: Document rejection process in README.'
  url: https://inbox.sourceware.org/libc-alpha/20260421164416.4031726-1-carlos@redhat.com
  n: 1
  total: 2
url: https://inbox.sourceware.org/libc-alpha/a07f4b38-bee2-4163-b758-0c993d340dd7@gotplt.org
bugzilla_url: null
date: '2026-04-21'
---

This patch adds documentation to the advisories/README file outlining the process for rejecting an advisory. The documentation details how to mark an advisory as rejected, including adding "REJECTED: " prefixes and a Rejected-Date tag.
