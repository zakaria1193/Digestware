---
project: glibc
subsystem: glibc
patch_id: null
tags:
- locale
- Hunsrik
- hrx
- i18n
discussion_id: 20260417022155.88363-1-joangarcez2100@gmail.com
source_type: public_inbox
title: '[PATCH v6 0/2] Add Hunsrik locale support (hrx, hrx_BR)'
headline: Add Hunsrik locale support (hrx, hrx_BR)
tldr: This patch adds support for the Hunsrik locale (hrx) and the Hunsrik locale
  for Brazil (hrx_BR) to glibc.
stakes: Adding new locale support increases the usability of glibc for speakers of
  less common languages.
proposer: Garccez <joangarcez2100@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 8
sentiment_rationale: The patch series adds new language support and fixes issues in
  previous versions, suggesting positive progress.
series_id: glibc:add hunsrik locale support (hrx, hrx_br)
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/20260417022155.88363-1-joangarcez2100@gmail.com
bugzilla_url: null
date: '2026-04-17'
---

This patch series adds support for the Hunsrik language (hrx) and the Hunsrik locale for Brazil (hrx_BR) to glibc. The changes include defining Hunsrik in iso-639.def and adding the hrx_BR locale data. This is version 6 of the patch, which fixes a date format escape character and drops the first_weekday setting.
