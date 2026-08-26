---
project: gcc
subsystem: gcc
patch_id: null
tags:
- security
- infrastructure
- traffic analysis
- rate limiting
discussion_id: bfc07bf2-d422-4409-8e61-a30ab2bd5ce8@xeiaso.net
source_type: public_inbox
title: Concerns about the evidence for the AI scraper problem and the resulting blocking
headline: Concerns about AI scraper problem evidence and blocking measures
tldr: Dispute over evidence for AI scraping as cause of Sourceware load issues and
  the resulting access blocks.
proposer: Xe Iaso <me@xeiaso.net>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 4
technical_tradeoffs:
- Blocking potentially malicious AI scrapers versus inconveniencing legitimate users.
- Resource exhaustion due to inefficient operations versus proactive security measures.
exchanges:
- author: Xe Iaso <me@xeiaso.net>
  role: proposer
  position: Asserts that the AI scraper problem is real and corroborated by multiple
    organizations, defending the necessity of blocking measures.
  quote: 'As a rule of thumb: if multiple organizations are all coming to the same
    conclusions without colluding, it''s probably because a thing is actually happening.'
- author: Kalamatee <kalamatee@gmail.com>
  role: other
  position: Questions the evidence presented for the AI scraper problem, arguing that
    traffic is not definitively proven to be illegitimate or the sole cause of resource
    exhaustion.
  quote: I don't doubt that Sourceware has seen unusual or excessive traffic, and
    I don't think it is unreasonable to investigate whether automated scraping is
    contributing to load. What I am less convinced about is the extent to which the
    public evidence actually supports the conclusions being drawn from that traffic.
- author: fche@redhat.com
  role: other
  position: Agrees that the underlying issue is expensive operations being triggered
    by unauthenticated requests, suggesting that securing these operations is more
    important than identifying the requester as AI.
  quote: If the expensive operations are made difficult to abuse, it matters much
    less whether the requester is an AI scraper, CI, curl or a human.
- author: Mark Wielaard <mark@klomp.org>
  role: other
  position: States that `git blame` has been disabled in cgit and gitweb, implying
    a mitigation measure has already been taken.
  quote: git blame has been disabled in cgit (and gitweb).
primer_expert: The discussion revolves around unusual traffic patterns observed on
  Sourceware, suspected to be from AI scrapers. The core of the debate is whether
  the evidence for this being malicious AI scraping is sufficient to justify blocking
  measures, which are causing access issues for legitimate users. The impact on `git
  blame` queries and other resource-intensive operations is a key concern.
primer_glossary:
- term: AI scraper
  definition: Automated software that browses websites to collect data, often for
    training artificial intelligence models. In this context, it refers to traffic
    identified as potentially malicious or excessive.
- term: Sourceware
  definition: A web-based infrastructure for open-source projects, providing services
    like Git repositories, bug tracking, and mailing lists.
- term: RFC 9309
  definition: A Request for Comments document that specifies internet standards. The
    specific content of RFC 9309 is not detailed here but is mentioned as being disrespected.
- term: git blame
  definition: A Git command that shows what revision and author last modified each
    line of a file, often used for understanding code history.
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
url: https://inbox.sourceware.org/gcc/5f838205-c889-410e-bef8-78e0e2b81828@xeiaso.net
bugzilla_url: null
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

Xe Iaso, creator of the Anubis project, defends the characterization of an AI scraper problem impacting Sourceware, citing multiple organizations reaching similar conclusions. This follows concerns raised by Kalamatee regarding the sufficiency of public evidence linking traffic to AI scraping and resource exhaustion. The discussion touches on the nature of the traffic, whether it's illegitimate or merely automated, and the potential for expensive operations to be abused by unauthenticated requests.
