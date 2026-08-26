---
project: gcc
subsystem: gcc
patch_id: null
tags:
- security
- infrastructure
- traffic analysis
- rate limiting
- evidence
discussion_id: CAJWNc-5n0e_d3ncCpH0vmvKHR8RuRJt5B7RTiF1LAd5cs5xBvw@mail.gmail.com
source_type: public_inbox
title: Concerns about the evidence for the AI scraper problem and the resulting blocking
headline: Concerns about AI scraper problem evidence and blocking measures
tldr: Dispute over evidence for AI scraping as cause of Sourceware load issues and
  the resulting access blocks.
proposer: Kalamatee <kalamatee@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 4
technical_tradeoffs:
- Justifying blocking measures with anecdotal evidence versus requiring rigorous data
  analysis.
- Addressing AI scraping specifically versus securing underlying expensive operations.
exchanges:
- author: Kalamatee <kalamatee@gmail.com>
  role: proposer
  position: Questions the evidence for AI scraping being the cause of Sourceware's
    load issues and criticizes the blocking measures taken without sufficient data.
    Argues that expensive operations being easily abused is the core problem.
  quote: In particular, there seems to be very little evidence beyond assertions that
    the traffic being classified as AI scraping is actually illegitimate traffic,
    rather than simply automated traffic. I haven't seen request statistics, representative
    logs, request patterns, resource-consumption figures, or anything else that would
    allow people outside the infrastructure team to understand what was actual…
- author: Mark Wielaard <mark@klomp.org>
  role: other
  position: Provides a link to an analysis of logs on xeiaso.net as evidence of abusive
    traffic and notes that the problem is ongoing.
  quote: 'It is really abusive. See for example this analysis from our logs: https://xeiaso.net/notes/2026/check-your-smart-tv/

    Note that the article says it is for the last few months, the logs were actually
    for the last few weeks..., so it is way w'
- author: Jonathan Corbet <corbet@lwn.net>
  role: other
  position: Acknowledges the concerns raised about the evidence but notes that LWN
    (Linux Weekly News) may be pulled into the discussion later.
  quote: 'I was going to let this pass, but since you pull LWN in later on...


    > I don''t doubt that Sourceware has seen unusual or excessive traffic, and I

    > don''t think it is unreasonable to investigate whether automated scraping is

    > contributing to load. What I am less convinced about is the ext'
- author: fche@redhat.com
  role: other
  position: Expresses doubt about the precise nomenclature used for the traffic, stating
    that AI tools and automation are acceptable if accessed legitimately.
  quote: I too have doubts about the exact nomenclature. I don't have a problem in
    principle with AI tools or automation accessing our services, in legitimate ways
- author: Jonathan Wakely <jwakely.gcc@gmail.com>
  role: other
  position: Acknowledges Kalamatee's concerns about the evidence for AI scraping and
    its impact.
  quote: 'I have some concerns about the way the current “AI scraper” problem is

    being characterised, and particularly about the measures being taken in

    response to it.


    I don''t doubt that Sourceware has seen unusual or excessive traffic, and I

    don''t think it is unreasonable to investigate whether automated scraping is

    contributing to load. What I am less convinced about is the extent to which

    the public e…'
primer_expert: This discussion continues the thread on Sourceware traffic issues,
  with Kalamatee challenging the evidence for "AI scraping" being the root cause of
  load problems. The debate centers on the lack of concrete data (logs, resource metrics)
  to support the claims and the distinction between automated and illegitimate traffic.
  The underlying technical issue appears to be the susceptibility of expensive operations
  to abuse, regardless of the source's identity.
primer_glossary:
- term: AI scraper
  definition: Automated software that browses websites to collect data, often for
    training artificial intelligence models. In this context, it refers to traffic
    identified as potentially malicious or excessive.
- term: Sourceware
  definition: A web-based infrastructure for open-source projects, providing services
    like Git repositories, bug tracking, and mailing lists.
- term: traffic
  definition: Data sent and received by a computer or network. In this context, it
    refers to the requests made to Sourceware's servers.
- term: resource exhaustion
  definition: A situation where a system runs out of available resources such as CPU
    time, memory, or disk space, leading to degraded performance or system failure.
- term: IP address
  definition: A unique numerical label assigned to each device connected to a computer
    network that uses the Internet Protocol for communication. Used here to discuss
    the source of traffic.
- term: nginx
  definition: A web server that can also act as a reverse proxy, load balancer, and
    HTTP cache. In this context, it is serving the GCC Git web interface and returning
    429 errors.
- term: 429 Too Many Requests
  definition: An HTTP status code indicating that the user has sent too many requests
    in a given amount of time ('rate limiting').
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAJWNc-5n0e_d3ncCpH0vmvKHR8RuRJt5B7RTiF1LAd5cs5xBvw@mail.gmail.com
bugzilla_url: null
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

Kalamatee expresses concerns about the characterization of the "AI scraper" problem and the measures taken, questioning the evidence that traffic is illegitimate rather than merely automated. They highlight a lack of public data such as logs or resource consumption figures, and suggest that expensive operations triggered by unauthenticated requests are the root cause, rather than the specific source of the traffic.
