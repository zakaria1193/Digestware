---
project: binutils
subsystem: binutils
patch_id: null
tags:
- infrastructure
- security
- bots
- fundraising
discussion_id: 20260816210001.GB5585@gnu.wildebeest.org
source_type: public_inbox
title: 'Re: Sourceware Open Office, Fri 14, 15:00 UTC'
headline: Sourceware Open Office, Fri 14, 15:00 UTC
tldr: Sourceware is implementing new strategies to combat AI scraper bots, including
  rate limiting non-approved IPs and improving user authentication, while also see…
proposer: Mark Wielaard <mark@klomp.org>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased rate limiting and challenges can negatively impact legitimate users and
  accessibility.
- IP-based allow-listing strategies can be complicated by dynamic IPs and CGNAT.
- Disabling Anubis honeypot ingestion saves memory but might reduce visibility into
  attack patterns.
exchanges:
- author: Mark Wielaard
  role: proposer
  position: Summarizes discussion points, including bot mitigation strategies, Anubis
    performance, and fundraising updates.
  quote: "nginx rate limits non \"goodguy\" addresses\n  - goodguys are people that\
    \ log into the services, so it's an\n    incentive to contribute"
primer_expert: Sourceware is discussing its ongoing battle against AI scraper bots
  and other automated traffic. Mitigation efforts include refining Nginx rate limiting
  to favor authenticated users ('goodguys'), exploring new authentication methods,
  and adjusting the Anubis proof-of-work system's challenges. Fundraising is also
  progressing positively.
primer_glossary:
- term: AI scraper bot
  definition: Automated software designed to crawl websites and extract data, often
    used for malicious purposes or to overload servers.
- term: Nginx
  definition: A popular web server and reverse proxy that can be configured with rate-limiting
    modules.
- term: Anubis
  definition: A proof-of-work system used by Sourceware to mitigate automated access
    and bot traffic. Users must solve a computational challenge to gain access.
- term: CGNAT
  definition: Carrier-Grade Network Address Translation, a method used by ISPs to
    share public IP addresses among multiple customers, which can complicate IP-based
    allow-listing.
- term: Fail2ban
  definition: A security software framework that protects computer servers from brute-force
    attacks by monitoring log files and banning malicious IPs.
- term: FOSSY
  definition: Free and Open Source Software Young Developers Conference, a conference
    where various FOSS projects discuss infrastructure and development.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260816210001.GB5585@gnu.wildebeest.org
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Discussion notes from the Sourceware Open Office reveal ongoing efforts to mitigate AI scraper bots through improved Nginx rate limiting and a 'goodguy' IP list incentivizing user contributions. They also discuss disabling Anubis honeypot ingestion due to memory issues and the impact of Anubis's JavaScript challenge on mobile devices. Fundraising updates show a significant increase in donations.
