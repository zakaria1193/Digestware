---
project: glibc
subsystem: glibc
patch_id: null
tags:
- contribution guidelines
- git
- LLM
- tooling
- collaboration
discussion_id: lhuh5p992bo.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: Contribution guidelines update regarding tool usage'
headline: Contribution guidelines update regarding tool usage
tldr: Discussion on updating glibc contribution guidelines to include "Assisted-by"
  Git trailers for auto-generated code; considering open LLMs.
stakes: Impacts contribution process by clarifying guidelines on acknowledging AI/tool
  assistance, potentially affecting transparency.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Including a specific LLM might be seen as endorsing it, but ensures the examples
  are realistic.
- Omitting LLMs keeps the guidelines general but might limit clarity for contributors
  using such tools.
- Mentioning only Autoconf is safe, but excludes modern AI-assisted development.
exchanges:
- author: Florian Weimer
  role: proposer
  position: Suggests updating contribution guidelines to include an "Assisted-by"
    Git trailer for auto-generated code.
  quote: Reviewers may request that you add an “Assisted-by” Git trailer if parts
    of the contribution have been auto-generated.
- author: Paul Eggert
  role: contributor
  position: Suggests providing an example for the "Assisted-by" Git trailer.
  quote: It would be helpful to give an example, as we can't assume that every new
    contributor is up to speed on what to put into "Assisted-by".
- author: Florian Weimer
  role: proposer
  position: Asks if there's an open LLM to mention rather than a closed one (like
    Claude), or whether to just mention Autoconf.
  quote: Is there a sufficiently open LLM we could mention instead? Otherwise I would
    go with just mentioning Autoconf.
- author: Paul Eggert
  role: contributor
  position: Suggests OLMo as it's free.
  quote: Sure, something like OLMo. Admittedly fewer users than the big guys but it
    is free
primer_expert: This discussion concerns glibc's contribution guidelines, specifically
  regarding the use of tools like Autoconf or LLMs in generating code.  The "Assisted-by"
  Git trailer is a way to acknowledge such tool usage. The core issue is whether to
  recommend specific tools in the guidelines, particularly open vs. closed LLMs. It
  touches on transparency and reproducibility in the build process.
primer_general: Contributing to a software project like glibc involves following specific
  guidelines to ensure code quality and consistency.  These guidelines often cover
  aspects like code style, testing, and commit message formatting.  A Git trailer
  is a line added to a commit message to provide extra information.  This discussion
  is about adding a guideline to acknowledge when automated tools (like AI-powered
  code generators) have been used to help create a contribution, and whether to suggest
  specific tools.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhutst6t58s.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Florian Weimer proposes clarifying the contribution guidelines to include an "Assisted-by" Git trailer when parts of a contribution are auto-generated. Paul Eggert suggests including an example. Florian then questions whether they should suggest a sufficiently open LLM (like OLMo) in the example, instead of a closed one.
