---
project: gcc
subsystem: gcc
patch_id: null
tags:
- performance
- infrastructure
- security
- DoS
discussion_id: 20260816212922.GA4558@gnu.wildebeest.org
source_type: public_inbox
title: 'Re: gitweb broken?'
headline: gitweb broken?
tldr: Sourceware has lowered the difficulty for its Anubis proof-of-work system to
  address performance issues and slow commit browsing.
proposer: Mark Wielaard <mark@klomp.org>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Lowering proof-of-work difficulty may reduce effectiveness against sophisticated
  botnets.
- Switching challenge types (meta-refresh to JavaScript) might affect users with older
  browsers or specific accessibility needs.
exchanges:
- author: Mark Wielaard
  role: proposer
  position: Announces that the Anubis difficulty has been lowered to 4 to improve
    speed and that challenges for wiki and Bugzilla were updated.
  quote: We lowered the difficulty to 4, which hopefully helps with the speed.
- author: Johann
  role: other
  position: Observes that Anubis remains slow, with commit browsing taking over a
    minute, and notes the fake progress bar behavior.
  quote: null
- author: Georg-Johann Lay
  role: other
  position: Reports that web pages appear normal, but Anubis is still very slow, citing
    a specific commit as an example.
  quote: null
primer_expert: The Sourceware infrastructure team has adjusted the Anubis proof-of-work
  difficulty to level 4 to mitigate performance issues reported by users, such as
  slow access to git commit information. Additionally, they've updated challenge mechanisms
  on other services like Bugzilla and the wiki to counter botnet activity.
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
- term: Proof-of-work
  definition: A system requiring a non-trivial computational effort to deter malicious
    use, often used for spam prevention or access control.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260816212922.GA4558@gnu.wildebeest.org
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Mark Wielaard reports that Sourceware has reduced the difficulty of the Anubis proof-of-work system from 5 to 4, aiming to improve performance for users experiencing slow commit browsing. They also switched the wiki and Bugzilla from meta-refresh to JavaScript challenges to combat scraper attacks.
