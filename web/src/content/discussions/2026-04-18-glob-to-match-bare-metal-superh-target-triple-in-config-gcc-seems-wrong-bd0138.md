---
project: gcc
subsystem: gcc
patch_id: null
tags:
- configuration
- target triple
- SuperH
discussion_id: 52ebc5da78d98133278410edc5730316be5964e2.camel@gmail.com
source_type: public_inbox
title: 'Re: Glob to match bare-metal SuperH target triple in config.gcc seems wrong
  (sh*-superh-elf)?'
headline: Glob to match bare-metal SuperH target triple in config.gcc seems wrong
tldr: The glob "sh*-superh-elf" in config.gcc may incorrectly identify SuperH bare-metal
  targets.
stakes: Incorrect target triples can lead to build configuration errors.
proposer: Oleg Endo <olegendo1024@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 5
sentiment_rationale: Discussion is neutral, exploring potential issues with a configuration
  glob.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/52ebc5da78d98133278410edc5730316be5964e2.camel@gmail.com
bugzilla_url: null
date: '2026-04-18'
---

A discussion arose about the glob expression "sh*-superh-elf" used in config.gcc to match embedded SuperH targets. The concern is that the "superh" token, which appears to be a manufacturer name, might be causing the glob to miss some valid target triples like "sh-elf". The discussion suggests that the expression is confusing and could benefit from clarification.
