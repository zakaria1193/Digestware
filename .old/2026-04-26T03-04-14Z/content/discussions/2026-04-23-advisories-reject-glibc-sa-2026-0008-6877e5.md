---
project: glibc
subsystem: advisories
patch_id: null
tags:
- glibc
- advisories
- security
- NIS+
discussion_id: 2eb7cde7-b096-4359-9f29-7e97dbe2dbe1@redhat.com
source_type: public_inbox
title: 'Re: [PATCH 2/2] advisories: Reject GLIBC-SA-2026-0008'
headline: 'advisories: Reject GLIBC-SA-2026-0008'
tldr: Glibc is rejecting CVE-2026-5358, an advisory related to the never-fully-supported
  NIS+ APIs, due to the lack of available server implementations.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: ready
sentiment_score: null
technical_tradeoffs:
- Rejecting the CVE clarifies the status of NIS+ in glibc.
- Users relying on NIS+ APIs are advised to migrate to modern solutions.
exchanges:
- author: Carlos O'Donell <carlos@redhat.com>
  role: proposer
  position: Pushed the updated advisory after receiving LGTMs, and the CVE is now
    marked as rejected with MITRE.
  quote: Thanks. Pushed. CVE is now marked as rejected with MITRE.
- author: Siddhesh Poyarekar
  role: reviewer
  position: Gave the advisory a "Looks Good To Me."
  quote: 'LGTM too.


    Reviewed-by: Siddhesh Poyarekar <siddhesh@gotplt.org>'
- author: Florian Weimer
  role: contributor
  position: Suggested clarifying that there are no known server implementations available
    for the NIS+ code.
  quote: Maybe also mention that there to the glibc team's knowledge, there are no
    server implementations available that this code could interact with?
primer_expert: This thread concerns the advisories in glibc, specifically CVE-2026-5358
  related to NIS+ APIs. The glibc team maintains advisories to inform users of potential
  security issues. NIS+ was an incomplete implementation and the team is clarifying
  its stance since there are no known server implementations to interact with this
  API.
primer_general: The GNU C Library (glibc) project maintains a set of advisories to
  inform users about potential security issues and recommended actions.  This discussion
  concerns a specific advisory (CVE-2026-5358) related to Network Information Service
  Plus (NIS+), a directory service. Although glibc included NIS+ APIs, the implementation
  was incomplete, and more importantly, there aren't any readily available server
  implementations to connect to.  As a result, the advisory is being rejected, and
  users are urged to use modern alternatives.
series_id: 'glibc:advisories: reject glibc-sa-2026-0008'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/2eb7cde7-b096-4359-9f29-7e97dbe2dbe1@redhat.com
bugzilla_url: null
date: '2026-04-23'
---

Glibc is rejecting CVE-2026-5358, which concerned potential vulnerabilities in the NIS+ APIs. According to the glibc team, NIS+ was never fully supported, and there are no known open-source server implementations available. The advisory has been updated to reflect this, advising users to migrate to modern identity and access management services instead. The CVE is now marked as rejected with MITRE.
