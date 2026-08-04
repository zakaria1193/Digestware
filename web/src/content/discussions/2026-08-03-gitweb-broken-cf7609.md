---
project: gcc
subsystem: gcc
patch_id: null
tags:
- infrastructure
- web
- gitweb
- anubis
- nginx
discussion_id: 20260803071154.GI13327@gnu.wildebeest.org
source_type: public_inbox
title: 'Re: gitweb broken?'
headline: gitweb broken?
tldr: 'GCC web infrastructure updates: Anubis upgraded to 1.26.1, nginx proxy added
  for performance and security.'
proposer: Mark Wielaard <mark@klomp.org>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Balancing security against bot attacks with performance for legitimate users.
- Implementing a proxy layer (nginx) to manage traffic and potentially improve response
  times.
exchanges:
- author: Mark Wielaard <mark@klomp.org>
  role: proposer
  position: Reports that Anubis was upgraded to 1.26.1 and an nginx proxy was added
    to improve performance and security, asking if issues persist.
  quote: null
- author: Georg-Johann Lay
  role: other
  position: Previously reported extreme slowness and errors with Anubis (1.25.0) and
    gitweb, and that non-external links were also hanging.
  quote: 'It is extremely slow. Takes 1 min until Anubis starts (1.25.0).

    Anubis then takes ca. 2 min and finally denies access with:


    Berechnungsfehler!

    Fehler bei der Berechnung der Prfung: undefined


    https://gcc.gnu.org/git/gitweb.cgi?p=gcc.git


    The gitweb links hangs forever, doesn''t even start to

    render anything.'
primer_expert: This thread discusses recent changes to the gcc.gnu.org web infrastructure,
  primarily involving the Anubis anti-bot/anti-scraping gateway. Issues with performance
  and accessibility were reported after an Anubis upgrade. Subsequent changes include
  a new Anubis version (1.26.1) and an nginx proxy layer designed to improve resilience
  against attacks and speed up access for known users.
primer_glossary:
- term: gitweb
  definition: A web-based interface for browsing Git repositories. It allows users
    to view commit history, file contents, and other repository information through
    a web browser.
- term: Anubis
  definition: A security gateway or anti-bot system used on some web servers to filter
    malicious traffic, particularly from scrapers and bots, before it reaches the
    main web application.
- term: nginx
  definition: A high-performance web server and reverse proxy, commonly used for load
    balancing, HTTP caching, and as a front-end for other web applications to handle
    traffic efficiently and securely.
- term: httpd
  definition: The Apache HTTP Server, a widely used open-source web server software.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/20260803071154.GI13327@gnu.wildebeest.org
bugzilla_url: null
date: '2026-08-03'
is_stub: false
stub_reason: ''
---

This email discusses ongoing issues with the GCC web infrastructure, specifically slow connections and errors encountered with gitweb and other site sections. Mark Wielaard reports that upgrading Anubis to 1.26.1 and adding an nginx proxy in front of httpd are intended to improve performance and prioritize authenticated users, mitigating scraperbot attacks.
