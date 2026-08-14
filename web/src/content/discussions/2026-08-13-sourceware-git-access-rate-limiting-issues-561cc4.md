---
project: binutils
subsystem: binutils
patch_id: null
tags:
- infrastructure
- git
- access
- rate limiting
discussion_id: alpine.DEB.2.21.2608131847110.48788@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: binutils git: error 429 (too many requests)'
headline: Sourceware git access rate limiting issues
tldr: Discussion continues on 'error 429' git fetch issues on Sourceware, possibly
  related to recent Anubis updates or scraper bots, with a pointer to a related GCC…
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: under_review
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Aggressive rate limiting to deter bots might impact legitimate user access.
- Investigating and mitigating bot traffic requires developer resources.
exchanges:
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: contributor
  position: Responds to a git fetch '429 error' report by referencing a similar issue
    on the GCC mailing list, suggesting a potential common cause.
  quote: "Cf. \n<https://inbox.sourceware.org/gcc/SJ5PPF77D28E3C266CFBC1F2644FD5E8B82ECD32@SJ5PPF77D28E3C2.namprd11.prod.outlook.com/>."
primer_expert: Users are encountering HTTP 429 'Too Many Requests' errors when fetching
  from Sourceware git repositories, specifically `binutils-gdb.git`. This is impacting
  build systems like `cfarm121`. The issue is suspected to be related to automated
  traffic (scraper bots) or recent infrastructure changes (Anubis update). A similar
  problem is being discussed on the GCC mailing list.
primer_glossary:
- term: git fetch
  definition: A Git command used to download objects and refs from another repository,
    updating the local repository's state.
- term: 429 error
  definition: An HTTP status code indicating 'Too Many Requests', typically returned
    by a server when the client has exceeded its allowed request rate.
- term: Sourceware
  definition: A platform providing hosting and infrastructure for various open-source
    projects, including GNU toolchains like binutils, GCC, and glibc.
- term: Anubis
  definition: Likely refers to a system or service within Sourceware's infrastructure,
    possibly related to repository access or security, whose recent update may have
    affected request rates.
- term: scraper bots
  definition: Automated programs that systematically browse the web, often to extract
    data. In this context, they are suspected of overloading Sourceware's git services.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2608131847110.48788@angie.orcam.me.uk
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This email follows up on an earlier report of 'error 429 (too many requests)' when fetching from the binutils git repository on Sourceware. The issue is suspected to be related to recent Anubis updates or increased bot activity. The sender provides a link to a similar discussion happening on the GCC mailing list, indicating a potential wider impact.
