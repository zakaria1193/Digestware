---
project: glibc
subsystem: glibc
patch_id: null
tags:
- linker
- separate-code
- security
- build
discussion_id: CAMe9rOqdkoLnOsgRnUw_-5aA0ta+DW0kaNmhGYJNf3gRc_gbQw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2 1/2] Check if linker supports -z separate-code'
headline: Check if linker supports -z separate-code
tldr: This patch checks if the linker supports the -z separate-code option.
stakes: Enables use of -z separate-code if supported by the linker, which can improve
  security by separating code and data.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: The author indicates this was the wrong patch.
series_id: glibc:check if linker supports -z separate-code
series_role: reply
series_parts:
- title: Check if linker supports -z separate-code
  url: https://inbox.sourceware.org/libc-alpha/CAMe9rOrrpvo_DDK6DQZUBycRTV=ciDw9f5EFTUS+ko=Ano=KbQ@mail.gmail.com
  n: 1
  total: 2
- title: Check if linker supports -z separate-code
  url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982730779AD584441D08A7783202@PAWPR08MB8982.eurprd08.prod.outlook.com
  n: 1
  total: 2
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqdkoLnOsgRnUw_-5aA0ta+DW0kaNmhGYJNf3gRc_gbQw@mail.gmail.com
bugzilla_url: null
date: '2026-04-17'
---

The patch checks if the linker supports the `-z separate-code` option. The author retracts a previous statement about the patch being unchanged, suggesting it was a mistake.
