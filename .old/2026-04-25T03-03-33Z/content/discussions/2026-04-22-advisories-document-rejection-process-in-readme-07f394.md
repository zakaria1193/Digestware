---
project: glibc
subsystem: advisories
patch_id: null
tags:
- glibc
- advisory
- security
- documentation
- CVE
discussion_id: 5e42e0f0-354c-4909-8e7e-b6f5e0fa7b14@redhat.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] advisories: Document rejection process in README.'
headline: 'advisories: Document rejection process in README'
tldr: Documents the process for rejecting advisories in the glibc advisories README.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Committed
outcome: committed
sentiment_score: null
technical_tradeoffs:
- Improved documentation clarifies the process for rejecting advisories.
- Ensures a consistent approach to handling invalid or retracted security information.
exchanges:
- author: Carlos O'Donell <carlos@redhat.com>
  role: maintainer
  position: Pushed the patch documenting the advisory rejection process after receiving
    a LGTM.
  quote: null
- author: Siddhesh Poyarekar
  role: reviewer
  position: Reviewed and approved the patch.
  quote: LGTM.
primer_expert: This patch updates the `advisories/README` file in glibc. This directory
  contains information about security vulnerabilities (CVEs) affecting glibc.  The
  patch documents the process for formally rejecting an advisory, clarifying the workflow
  for retracting incorrect or irrelevant security claims. This process involves marking
  the advisory as rejected with a reason and a rejection date.
primer_general: Glibc maintains a set of advisories that document known security vulnerabilities.
  These advisories help users understand and mitigate potential risks. This patch
  adds documentation to the `README` file in the `advisories` directory, explaining
  how to properly reject an advisory if it turns out to be invalid or not applicable.
  This ensures a clear and consistent process for managing security information in
  glibc.
series_id: 'glibc:advisories: document rejection process in readme'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/5e42e0f0-354c-4909-8e7e-b6f5e0fa7b14@redhat.com
bugzilla_url: null
date: '2026-04-22'
---

Carlos O'Donell pushed a patch that documents the process for rejecting security advisories in the `advisories/README` file within the glibc repository. The documentation outlines how to mark an advisory as rejected, including adding a "REJECTED: " prefix to the description, providing a justification for the rejection, and adding a `Rejected-Date` tag. This clarifies the procedure for handling invalid or retracted advisories.
