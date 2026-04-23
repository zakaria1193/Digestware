---
project: glibc
subsystem: advisories
patch_id: null
tags:
- advisories
- security
- NIS+
discussion_id: ef66a476-681a-489e-90c1-78367c277b25@gotplt.org
source_type: public_inbox
title: 'Re: [PATCH 2/2] advisories: Reject GLIBC-SA-2026-0008'
headline: 'Advisories: Reject GLIBC-SA-2026-0008'
tldr: Marks the NIS+ advisory as rejected since the glibc team knows of no open-source
  NIS+ server implementations that work with the API.
stakes: Ensures the glibc security advisories accurately reflect the status of known
  issues.
proposer: Siddhesh Poyarekar <siddhesh@gotplt.org>
consensus: Proposed
outcome: ready
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Siddhesh Poyarekar <siddhesh@gotplt.org>
  role: proposer
  position: Acknowledges LGTM from the previous reviewers.
  quote: LGTM too.
primer_expert: The `advisories/` directory in glibc contains security advisories.
  This patch updates GLIBC-SA-2026-0008 to reflect the lack of known NIS+ server implementations.
  The advisory rejection process involves marking the advisory as rejected and providing
  a reason for the rejection.
primer_general: Glibc maintains a directory of security advisories to inform users
  about potential vulnerabilities. This patch updates an advisory regarding NIS+ (Network
  Information Service Plus) support, which was never fully implemented or officially
  supported in glibc.  The update clarifies that there are no known open-source server
  implementations available for NIS+, advising applications to migrate to modern identity
  and access management services. This change ensures users are not misled into thinking
  NIS+ is a viable option.
series_id: 'glibc:advisories: reject glibc-sa-2026-0008'
series_role: reply
series_parts:
- title: 'advisories: Reject GLIBC-SA-2026-0008'
  url: https://inbox.sourceware.org/libc-alpha/87v7dk6vtr.fsf@mid.deneb.enyo.de
  n: 2
  total: 2
- title: 'advisories: Reject GLIBC-SA-2026-0008'
  url: https://inbox.sourceware.org/libc-alpha/5dcc8de6-2926-41c4-955b-3b752a5805b7@redhat.com
  n: 2
  total: 2
- title: 'advisories: Reject GLIBC-SA-2026-0008'
  url: https://inbox.sourceware.org/libc-alpha/87zf2w6yrm.fsf@mid.deneb.enyo.de
  n: 2
  total: 2
- title: 'advisories: Reject GLIBC-SA-2026-0008'
  url: https://inbox.sourceware.org/libc-alpha/20260421164416.4031726-2-carlos@redhat.com
  n: 2
  total: 2
url: https://inbox.sourceware.org/libc-alpha/ef66a476-681a-489e-90c1-78367c277b25@gotplt.org
bugzilla_url: null
date: '2026-04-21'
---

This patch rejects the GLIBC-SA-2026-0008 advisory related to NIS+ support. The advisory is updated to state that, to the best of the glibc security team's knowledge, no open-source NIS+ server implementations were ever released for use with the API.
