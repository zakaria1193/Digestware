---
project: binutils
subsystem: binutils
patch_id: null
tags:
- infrastructure
- security
- funding
- community
discussion_id: 0475bd28feb9f78dcea1c13d6315aac79966ca53.camel@klomp.org
source_type: public_inbox
title: Some good Sourceware Infrastructure news
headline: Sourceware infrastructure updates and news
tldr: Sourceware has successfully mitigated AI scraper bot attacks and is announcing
  increased corporate and individual donations, leading to doubled infrastructure…
proposer: Mark Wielaard <mark@klomp.org>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Mark Wielaard
  role: proposer
  position: Announces successful mitigation of AI scraper bot attacks, increased funding
    through sponsorships and donations, and upcoming conference presentation.
  quote: 'Thanks to Frank Eigler''s work on the nginx limiter, Xe Iaso of Anubis

    fame and advise from our Red Hat Fedora infrastructure friends we have

    been able to catch 90% of the AI scraperbot traffic early at connection

    time. This means you shouldn''t be seeing those 429''s (Too Many

    Requests) reports anymore, even if you aren''t "authenticated".

    Also we are happy to announce our first corporate sponsor at…'
primer_expert: This is an announcement from the Sourceware infrastructure team detailing
  recent improvements and successes. Key points include mitigating large-scale AI
  scraper bot traffic using nginx limiting, which has improved site availability.
  They also highlight significant growth in funding from both corporate sponsorships
  (e.g., Open Source Security, Inc.) and individual donations, leading to a doubled
  budget. The team will present their work on infrastructure automation and resilience
  at the GNU Tools Cauldron.
primer_glossary:
- term: AI scraper bot attacks
  definition: Malicious automated traffic, often from AI services, attempting to scrape
    website content, which can overload servers and disrupt normal operations.
- term: nginx limiter
  definition: A feature of the Nginx web server used to control the rate of incoming
    requests, helping to prevent Denial-of-Service (DoS) attacks or excessive traffic
    from specific sources.
- term: 429 (Too Many Requests)
  definition: An HTTP status code indicating that the server has received too many
    requests from the client in a given amount of time, often used as a rate-limiting
    mechanism.
- term: GNU Tools Cauldron
  definition: An annual conference focused on the GNU toolchain, bringing together
    developers and users to discuss development, maintenance, and future directions
    of tools like GCC, GDB, and Binutils.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/0475bd28feb9f78dcea1c13d6315aac79966ca53.camel@klomp.org
bugzilla_url: null
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

Mark Wielaard shares positive news regarding Sourceware's infrastructure, highlighting the successful defense against AI scraper bots through improved nginx limiting. The announcement also details significant increases in both corporate sponsorships and individual donations, resulting in a doubled budget for 2026/2027. The team plans to present these infrastructure updates and best practices at the upcoming GNU Tools Cauldron conference.
