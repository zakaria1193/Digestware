---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- contribution guidelines
- git
- llm
- autoconf
discussion_id: lhuh5p992bo.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: Contribution guidelines update regarding tool usage'
headline: Contribution guidelines update regarding tool usage
tldr: Discusses updating glibc contribution guidelines to include an "Assisted-by"
  Git trailer for auto-generated contributions, considering mentioning LLMs.
stakes: Clear guidelines help ensure code quality and proper attribution when using
  AI or other automated tools.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Under Review
outcome: proposed
sentiment_score: 7
sentiment_rationale: The discussion is collaborative and aims to improve clarity in
  the contribution guidelines.
technical_tradeoffs:
- Balancing clarity with overly prescriptive guidelines.
- Choosing appropriate examples that are both helpful and widely applicable.
- Staying current with the evolving landscape of AI-assisted development.
exchanges:
- author: Florian Weimer <fweimer@redhat.com>
  role: proposer
  position: Discusses adding an “Assisted-by” Git trailer if parts of the contribution
    have been auto-generated.
  quote: "* Reviewers may request that you add an “Assisted-by” Git trailer if\n \
    \  parts of the contribution have been auto-generated."
- author: Paul Eggert <eggert@cs.ucla.edu>
  role: contributor
  position: Suggests providing an example for the "Assisted-by" trailer.
  quote: 'It would be helpful to give an example, as we can''t assume that every

    new contributor is up to speed on what to put into

    "Assisted-by".'
- author: Florian Weimer <fweimer@redhat.com>
  role: contributor
  position: Asks if there's an open LLM to mention instead of a closed-source one,
    otherwise suggesting to only mention Autoconf.
  quote: 'Is there a sufficiently open LLM we could mention instead?  Otherwise I

    would go with just mentioning Autoconf.'
- author: Paul Eggert <eggert@cs.ucla.edu>
  role: contributor
  position: Suggests OLMo as an open LLM.
  quote: "Sure, something like OLMo. Admittedly fewer users than the big guys but\
    \ \nit is free"
primer_expert: This discussion concerns updating the glibc contribution guidelines
  to reflect the use of automated tools like LLMs and Autoconf. The "Assisted-by"
  Git trailer is meant to provide attribution for code that's not entirely human-authored.
  The discussion highlights the need for clear examples and the preference for mentioning
  open-source tools.
primer_general: This discussion revolves around updating the rules for contributing
  to glibc, the standard C library used in many Linux systems.  The update focuses
  on how to acknowledge the use of automated tools, like AI-powered code generators
  or tools like Autoconf, in creating contributions. The goal is to ensure proper
  credit and transparency when code is not entirely written by a human.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhutst6t58s.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Florian Weimer and Paul Eggert discuss updating glibc's contribution guidelines to encourage the use of an "Assisted-by" Git trailer when contributions are auto-generated.  They consider providing an example and discuss whether to mention a specific LLM, favoring Autoconf for clarity and avoiding closed-source tools.
