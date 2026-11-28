---
project: binutils
subsystem: binutils
patch_id: null
tags:
- CTI
- glibc
- git
- infrastructure
- RFC
discussion_id: d9ff2e69-bf44-4a4b-8ed4-f8751e481cce@redhat.com
source_type: public_inbox
title: Meeting Minutes - Office Hours for CTI - 2026-11-27
headline: CTI Office Hours discuss glibc git mirror testing
tldr: CTI Office Hours reviewed RFCs and planned testing for a new read-only glibc
  git mirror with reported speed improvements.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Carlos O'Donell
  role: proposer
  position: Documented the meeting minutes, including discussions on RFCs and the
    new glibc git mirror.
  quote: 'ACTION: Carlos to send out email to libc-alpha to ask to test the mirror.'
primer_expert: These minutes from the Core Toolchain Infrastructure (CTI) project's
  office hours touch upon several RFCs relevant to the GNU Toolchain's development
  workflow, including potential use of bugspray, git-mailbomb, custom DNS endpoints,
  and scaled git mirrors. The primary actionable item involves testing a new read-only
  git mirror for glibc, with early performance data suggesting substantial speedups.
primer_glossary:
- term: CTI
  definition: Core Toolchain Infrastructure, a project focused on improving the development
    and maintenance of core toolchain components.
- term: RFC
  definition: Request for Comments, a type of document used to propose changes or
    new ideas within a project, inviting discussion and feedback.
- term: git mirror
  definition: A copy of a Git repository, often used to provide faster access or redundancy
    for developers.
- term: DNS
  definition: Domain Name System, which translates human-readable domain names into
    machine-readable IP addresses.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/d9ff2e69-bf44-4a4b-8ed4-f8751e481cce@redhat.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

The CTI project's office hours meeting minutes for November 27, 2026, cover ongoing collaborations with glibc and several RFCs related to tooling and infrastructure. A key agenda item was the testing of a new read-only git mirror for glibc, which has shown significant speed improvements in initial reports across different regions.
