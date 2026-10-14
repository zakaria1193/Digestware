---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- bugzilla
- usability
- spam
- community
discussion_id: CAH6eHdRicyXRmZsudHoqW6D7NGi34=tygm-WafRQgY9a3Me8Ww@mail.gmail.com
source_type: public_inbox
title: 'Re: Re-enabling account signup on Bugzilla'
headline: Re-enabling account signup on Bugzilla
tldr: Discussion on re-enabling self-service account creation for the GCC Bugzilla
  to improve bug reporting accessibility.
proposer: Jonathan Wakely <jwakely.gcc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ease of use for legitimate reporters vs. vulnerability to spam.
- Manual moderation overhead vs. automated filtering effectiveness.
- Potential for lost bug reports due to complex signup vs. risk of overwhelming the
  system with spam.
exchanges:
- author: Jonathan Wakely
  role: proposer
  position: Supports re-enabling Bugzilla account signups if a moderation extension
    to ban URLs for new accounts for 24 hours is implemented.
  quote: If we had that extension than I'd be happy to re-enable account registration.
    I don't think spammers would bother waiting 24h and coming back to post their
    links.
- author: Sam James
  role: contributor
  position: Advocates for re-enabling self-account signup on Bugzilla, noting that
    the current process deters users from filing bugs.
  quote: 'I think we should re-enable self-account signup on Bugzilla.


    Andrea and I at least have seen people put off by having to email to get an account
    and they end up just not filing a bug at all and only complaining on social media,
    or not even that.'
- author: Jonathan Wakely
  role: contributor
  position: Highlights that past attacks involved hundreds of bugs filed per minute
    with SEO spam, necessitating restrictions.
  quote: The reason we put the restrictions in place was that the attacks we got were
    too large and too fast for humans to handle. Hundreds of new bugs filed per minute,
    full of SEO spam.
- author: Sam James
  role: contributor
  position: Mentions Gentoo's experience with a Bugzilla extension that bans URLs
    for new accounts for 24 hours and suggests porting it to GCC.
  quote: 'On the Gentoo side, we have had similar problems but it''s not too bad.
    We have a Bugzilla extension [0] which bans URLs from new accounts for 24 hours:
    we could possibly bring that over here but exempt some sites like stackoverflow,
    standard reference sites, and godbolt.'
primer_expert: The GCC Bugzilla currently requires users to email for account creation,
  which discourages bug reporting and can lead to requests being lost due to spam
  filters. The community is debating re-enabling self-signup, considering past large-scale
  spam attacks that overwhelmed manual moderation.
primer_glossary:
- term: Bugzilla
  definition: An open-source bug tracking system used by many software projects, including
    GCC, to manage reported issues.
- term: SEO spam
  definition: Unsolicited messages or content posted to websites with the primary
    goal of increasing search engine rankings, often including irrelevant links.
- term: IRC
  definition: Internet Relay Chat, an early form of real-time text messaging used
    by many open-source communities for communication.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAH6eHdRicyXRmZsudHoqW6D7NGi34=tygm-WafRQgY9a3Me8Ww@mail.gmail.com
bugzilla_url: null
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

Jonathan Wakely and Sam James discuss the implications of re-enabling self-service account creation on the GCC Bugzilla. While re-enabling would reduce friction for users who are deterred by the current email-request process, concerns remain about potential spam and abuse, as experienced in the past.
