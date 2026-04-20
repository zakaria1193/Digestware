---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- contribution guidelines
- git
- autoconf
- llm
discussion_id: lhutst6t58s.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: Contribution guidelines update regarding tool usage'
headline: Contribution guidelines update regarding tool usage
tldr: Discussion on whether to include a specific LLM or just Autoconf in the contribution
  guidelines regarding "Assisted-by" Git trailers for auto-generated contrib…
stakes: Ensuring clear guidelines for contributors regarding the use of automated
  tools like LLMs and Autoconf in generating code.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
primer: The GNU C Library (glibc) has established contribution guidelines to ensure
  code quality, consistency, and maintainability. These guidelines cover various aspects
  of the development process, including coding style, testing, and commit message
  formatting.  Git trailers are structured metadata lines in commit messages that
  provide additional information about the commit, such as authorship or assistance
  from tools.  Autoconf is a tool for producing source code configuration scripts.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhutst6t58s.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This discussion revolves around updating the glibc contribution guidelines to clarify when an "Assisted-by" Git trailer should be added for auto-generated contributions.  The point of contention is whether to mention a specific open LLM as an example, or to simply refer to Autoconf. The goal is to provide helpful guidance to reviewers and contributors on acknowledging the use of automated tools in the development process.
