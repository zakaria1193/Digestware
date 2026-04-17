---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: 20260417022155.88363-1-joangarcez2100@gmail.com
source_type: public_inbox
title: '[PATCH v6 0/2] Add Hunsrik locale support (hrx, hrx_BR)'
proposer: Garccez <joangarcez2100@gmail.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/20260417022155.88363-1-joangarcez2100@gmail.com
bugzilla_url: null
date: '2026-04-17'
---

Changes in v6:
- Fix d_fmt escape character: "%d/%m/%Y" -> "%d//%m//%Y"
- Drop first_weekday since the default is already 1

Garccez (2):
  locale: Define Hunsrik (hrx) in iso-639.def
  localedata: Ad
