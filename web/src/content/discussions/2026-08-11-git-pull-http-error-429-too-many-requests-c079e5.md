---
project: gcc
subsystem: gcc
patch_id: null
tags:
- git
- access
- http
- protocol
discussion_id: eebaaeff-0e89-405b-9b43-e787d11c6b6f@gjlay.de
source_type: public_inbox
title: git pull -> HTTP error 429 (too many requests)
headline: git pull -> HTTP error 429 (too many requests)
tldr: git pull fails with HTTP 429; using 'git://' instead of 'https://' resolves
  the issue.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 8
technical_tradeoffs: []
exchanges:
- author: Georg-Johann Lay
  role: proposer
  position: Reported an HTTP 429 error when attempting to `git pull` the GCC repository.
  quote: "fatal: unable to access 'https://gcc.gnu.org/git/gcc.git/': The \nrequested\
    \ URL returned error: 429"
- author: Josef Melcr
  role: contributor
  position: Suggested using the `git://` protocol as an alternative to `https://`
    to bypass the HTTP 429 error.
  quote: Try 'git://' instead of 'https://'.
- author: Georg-Johann Lay
  role: proposer
  position: Confirmed that switching to the `git://` protocol resolved the `git pull`
    issue.
  quote: null
primer_expert: This discussion concerns a git access issue for the GCC source repository.
  The user encountered HTTP 429 errors when using HTTPS, a common rate-limiting response
  from web servers. Switching to the git protocol (git://) bypasses the web server's
  rate limiting.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/eebaaeff-0e89-405b-9b43-e787d11c6b6f@gjlay.de
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Georg-Johann Lay reported receiving an HTTP 429 error when trying to `git pull` the GCC repository. Josef Melcr suggested using the `git://` protocol instead of `https://`, which resolved the problem for Lay.
