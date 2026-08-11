---
project: gcc
subsystem: gcc
patch_id: null
tags: []
discussion_id: 720c60d9-0453-4ee2-9ba1-11a41f397e06@gjlay.de
source_type: public_inbox
title: 'Re: gitweb broken?'
headline: gitweb broken?
tldr: Web interface performance issues persist for Georg-Johann Lay, although general
  site access seems normal.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Georg-Johann Lay
  role: proposer
  position: Reports that Anubis is still very slow for web interface operations, citing
    a specific commit URL as an example.
  quote: "For the web page, all seems normal by now.\n\nBut Anubis is still very slow,\
    \ for example at \nhttps://gcc.gnu.org/cgit/gcc/commit/?id=f3f8bb6afbcdc8a9dc5e633"
- author: Mark Wielaard
  role: reviewer
  position: Informs Georg-Johann Lay about upgrades to Anubis and nginx proxy to address
    scraper bot attacks and improve performance.
  quote: 'We upgraded Anubis again to 1.26.1 which has various challenge page

    robustness fixes:

    https://github.com/TecharoHQ/anubis/releases#release-v1.26.1


    That is odd, because neither of those page are behind Anubis.

    Maybe that was just caused be the general AI scraperbot attacks.


    We have added an nginx proxy in front of httpd which does the initial

    tls handshake and gives priority to connections from…'
primer_expert: null
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/720c60d9-0453-4ee2-9ba1-11a41f397e06@gjlay.de
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

Georg-Johann Lay reports continued slowness with the Anubis interface for gitweb, specifically when accessing commit details. While general website access appears normal, the performance issues with Anubis persist, making operations like viewing commits very slow.
