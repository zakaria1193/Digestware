---
project: binutils
subsystem: binutils
patch_id: null
tags:
- CTI
- glibc
- infrastructure
- meeting minutes
- DNS
discussion_id: bd2ff3e3-29f8-4889-91bd-b62b02ffafb0@redhat.com
source_type: public_inbox
title: Meeting Minutes - Office Hours for CTI - 2026-09-18
headline: Meeting Minutes - Office Hours for CTI - 2026-09-18
tldr: Minutes from CTI project office hours cover community items, VCS to email output,
  bug text to Bugzilla, and DNS/service naming for glibc.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 5
technical_tradeoffs:
- Centralizing infrastructure services (DNS, Git) can simplify management but may
  introduce single points of failure.
- Standardizing output formats improves consistency but requires buy-in and potential
  tooling changes.
exchanges:
- author: Carlos O'Donell <carlos@redhat.com>
  role: proposer
  position: Posted meeting minutes from CTI project office hours, outlining discussions
    on community items and glibc infrastructure.
  quote: 'CTI: https://cti.coretoolchain.dev/


    The CTI project holds Office Hours every Friday, these are the minutes for this
    Friday''s meeting.


    The CTI project in collaboration with glibc is working on: https://cti.coretoolchain.dev/projects/glibc.html


    Posting across the project mailing lists since some developers had questions and
    are only subscribed on some lists.'
- author: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Questions the assumption of consensus on moving services, as stated in
    the minutes.
  quote: This assumes that there is consensus on mov
- author: DJ Delorie <dj@redhat.com>
  role: other
  position: Inquires about the rationale for having three distinct Git URLs for glibc.
  quote: What is the rationale for having 3 different URLs?
primer_expert: This discussion centers around the Core Toolchain Infrastructure (CTI)
  project's collaboration with glibc. Topics include standardizing output formats
  for development workflows (VCS to email, bug reporting), and rationalizing DNS and
  Git repository naming conventions for improved service isolation and developer access.
  The minutes reflect ongoing efforts to streamline toolchain development processes.
primer_glossary:
- term: CTI
  definition: Core Toolchain Infrastructure, a project focused on improving the development
    infrastructure for core toolchain components like GCC and glibc.
- term: VCS
  definition: Version Control System, such as Git, used for tracking changes in source
    code.
- term: DNS
  definition: Domain Name System, which translates human-readable domain names into
    IP addresses.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/bd2ff3e3-29f8-4889-91bd-b62b02ffafb0@redhat.com
bugzilla_url: null
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

Minutes from the CTI project's office hours detail discussions on community items, including the format for VCS-to-email and bug-text-to-Bugzilla outputs, which will be posted to libc-alpha. Also discussed were strategies for service isolation using DNS names and finalizing Git URLs and mailing list naming conventions for glibc infrastructure.
