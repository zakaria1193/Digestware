---
project: gcc
subsystem: gcc
patch_id: null
tags:
- security
- performance
- infrastructure
- DoS
discussion_id: 20260816221211.GB4558@gnu.wildebeest.org
source_type: public_inbox
title: 'Re: Anubis check stuck?'
headline: Anubis check stuck?
tldr: Sourceware's Anubis proof-of-work system is facing persistent scraper attacks,
  leading to rate limiting and slow performance.
proposer: Mark Wielaard <mark@klomp.org>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Implementing IP allow-listing may inconvenience users with dynamic IP addresses
  or those behind CGNAT.
- Balancing security against user accessibility is a constant challenge with bot mitigation
  strategies.
exchanges:
- author: Mark Wielaard
  role: proposer
  position: Explains that Anubis and other services are under heavy scraper attack,
    making rate limiting challenging.
  quote: We should add authentication through patchwork and wiki. And add some way
    to manually authenticate an ip address. If nothing works please email admin-requests@
    to get yours added.
- author: Jonathan Wakely
  role: other
  position: Reports experiencing 429 errors when trying to access cgit, indicating
    the rate limiting is affecting users.
  quote: I've been unable to access any cgit links for at least a week, I get the
    429 error every single time.
primer_expert: Sourceware's infrastructure, including gitweb and Anubis (a proof-of-work
  system for access control), is experiencing denial-of-service attacks from scrapers.
  The current rate-limiting mechanisms are struggling to differentiate legitimate
  user traffic from malicious bot activity, prompting discussions on enhanced IP authentication
  strategies.
primer_glossary:
- term: Anubis
  definition: A proof-of-work system used by Sourceware to mitigate automated access
    and bot traffic. Users must solve a computational challenge to gain access.
- term: gitweb
  definition: A web-based interface for browsing Git repositories, commonly used by
    open-source projects for code repository access.
- term: cgit
  definition: An alternative web-based interface for Git repositories, often considered
    more efficient than gitweb.
- term: 429 error
  definition: An HTTP status code indicating 'Too Many Requests,' used for rate limiting
    to prevent abuse.
- term: Nginx
  definition: A popular web server and reverse proxy that can be configured with rate-limiting
    modules.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260816221211.GB4558@gnu.wildebeest.org
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Mark Wielaard discusses ongoing scraper attacks targeting Sourceware, causing rate limiting and impacting services like gitweb and Anubis. A proposed solution involves an IP allow-list for authenticated users, with ongoing efforts to add support for more services and manual IP authentication.
