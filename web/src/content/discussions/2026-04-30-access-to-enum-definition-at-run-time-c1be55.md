---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- plugin
- enum
- reflection
discussion_id: 5C269ABF-5ACA-40F2-AA40-AE3CC06A7AF6@gmail.com
source_type: public_inbox
title: 'Re: Access to enum definition at run time'
headline: Access to enum definition at run time
tldr: Yair Lenga acknowledges David Malcolm's suggestion of ref-track plugins and
  will investigate them.
proposer: Yair Lenga <yair.lenga@gmail.com>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Yair Lenga
  role: proposer
  position: Acknowledges the suggestion to look at ref-track plugins and will investigate
    them for potential similarities.
  quote: Thanks for sharing! I found the ref-track plugins at the bottom of- on surface
    - doing something similar (in terms of injecting code based on objects). I will
    dig further to learn understand.
primer_expert: This is a follow-up to a discussion about a GCC plugin for enum reflection.  The
  author is responding to a suggestion to look at ref-track plugins, which are example
  plugins that track references to variables.
primer_general: This email is part of a thread discussing a GCC plugin to provide
  runtime access to enum names.  The author is acknowledging a suggestion to investigate
  "ref-track plugins," which are existing GCC plugins that might offer insights into
  how to inject code based on program objects.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/5C269ABF-5ACA-40F2-AA40-AE3CC06A7AF6@gmail.com
bugzilla_url: null
date: '2026-04-30'
---

Yair Lenga thanks David Malcolm for pointing out the ref-track plugins and indicates that he will investigate them further. These plugins might offer similar functionality in terms of injecting code based on objects.
