---
project: glibc
subsystem: advisories
patch_id: null
tags:
- security
- advisory
- iconv
- CVE
discussion_id: 20260417211448.2762539-1-carlos@redhat.com
source_type: public_inbox
title: '[COMMITTED] advisories: Update GLIBC-SA-2026-0007.'
headline: 'advisories: Update GLIBC-SA-2026-0007.'
tldr: Update NEWS and the advisory for GLIBC-SA-2026-0007 to describe an iconv crash.
stakes: Keeps users informed about security vulnerabilities and their fixes.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Committed
outcome: committed
sentiment_score: 10
sentiment_rationale: Necessary update, already committed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260417211448.2762539-1-carlos@redhat.com
bugzilla_url: null
date: '2026-04-17'
---

Carlos O'Donell committed an update to the NEWS file and the GLIBC-SA-2026-0007 advisory. The update includes information about an iconv crash due to an assertion failure with untrusted input (CVE-2026-4046), including the fix commit.
