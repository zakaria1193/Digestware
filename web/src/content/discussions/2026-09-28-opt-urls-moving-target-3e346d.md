---
project: gcc
subsystem: gcc
patch_id: null
tags:
- build
- regression
- documentation
- avr
- buildbot
discussion_id: 364f55a8-21a5-44a0-b0b1-d1dbd28788ea@gjlay.de
source_type: public_inbox
title: opt.urls moving target
headline: opt.urls moving target
tldr: Buildbot configuration errors indicate the 'opt.urls' file target is unstable.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Georg-Johann Lay
  role: proposer
  position: Reports intermittent buildbot failures related to the 'opt.urls' file
    for the AVR target, where the expected entry for '-moptimize' changes unpredictably.
  quote: 'So I added a new option -moptimize to avr.opt and added a respective entry


    moptimize

    UrlSuffix(gcc/AVR-Options.html#index-moptimize)


    to avr.opt.urls.  Then I got a complaint from buildbot diff, indicating that the
    correct entry should be


    moptimize

    UrlSuffix(gcc/AVR-Options.html#index-moptimize-1)


    which I applied, just to get the next diff complaint that the correct entry should
    be


    moptimize…'
primer_expert: This issue concerns the GCC build system's handling of option documentation
  URLs. The `opt.urls` file maps command-line options to HTML documentation. The problem
  is that the expected URL for the `moptimize` option on the AVR target appears to
  be in flux, causing buildbot diffs to fail inconsistently, suggesting an underlying
  issue with how documentation targets are managed or updated.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers manufactured by Microchip Technology, often
    targeted by embedded systems development.
- term: opt.urls
  definition: A configuration file used by GCC to map compiler options to their corresponding
    online documentation URLs.
- term: buildbot
  definition: An open-source framework for automating software builds, tests, and
    releases, often used by large development projects like GCC.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/364f55a8-21a5-44a0-b0b1-d1dbd28788ea@gjlay.de
bugzilla_url: null
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

Georg-Johann Lay encountered a persistent issue where the buildbot's diff output for the 'opt.urls' file in the GCC AVR target configuration shows conflicting correct entries. After applying a suggested change, the diff complaint reappears, indicating the target URL is unstable or changes unexpectedly, preventing successful buildbot verification.
