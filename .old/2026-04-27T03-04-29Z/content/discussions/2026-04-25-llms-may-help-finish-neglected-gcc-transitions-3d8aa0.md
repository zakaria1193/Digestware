---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- LLM
- AI
- refactoring
- code review
discussion_id: 45953524-39c8-4046-a805-698e3c8b243e@netcologne.de
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: LLMs may help finish neglected GCC transitions.
tldr: Richard Biener suggests that LLMs might be useful for completing long-neglected
  partial transitions in GCC, but not for designing new features.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Under Review
outcome: under_review
sentiment_score: 6
technical_tradeoffs:
- Balancing the potential for increased development speed with the risk of introducing
  errors or unmaintainable code.
- Determining the appropriate level of human oversight for LLM-generated code.
- Choosing between using LLMs for small, incremental changes versus larger, more complex
  tasks.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: other
  position: Suggests that LLMs could be useful for finishing long-neglected partial
    transitions in GCC, but not for implementing new compiler features.
  quote: I’d also not accept big infrastructure designed by LLMs.  I still hope for
    sensible use of LLMs for GCC, like finishing long neglected partial transitions.  I
    do not think LLMs are ready to implement new compiler features.
- author: Eric Botcazou <ebotcazou@libertysurf.fr>
  role: contributor
  position: Agrees with limiting changes to the local "scope" to minimize potential
    mistakes.
  quote: "Yes, that seems to be a safe and sensible middle ground, in other words\
    \ to \nlimit changes to the local \"scope\" so that any mistakes made are also\
    \ local.\nSomething (slightly) above mechanical, but certainly nowhere near global."
- author: Thomas Koenig <tkoenig@netcologne.de>
  role: contributor
  position: Suggests that patches containing LLM-generated code need special care
    from reviewers.
  quote: 'I think that patches which contain LLM-generated code need to receive

    special care from *reviewers*, as well (to be formalized how?)'
- author: Giacomo Tesio <giacomo@tesio.it>
  role: contributor
  position: Describes his corporate policy of including prompts in commits containing
    LLM output.
  quote: 'To this aim, our corporate policy mandates inclusion of prompts in

    commits containing LLM output (together with tool name and version).'
- author: Thomas Koenig <tkoenig@netcologne.de>
  role: contributor
  position: Expresses concerns about cluttering up commits with prompts and the relevance
    of prompts in the long term.
  quote: 'That may be a good thing, or not.  Cluttering up commits is one concern

    that I have. Also, for r'
- author: Eric Botcazou <ebotcazou@libertysurf.fr>
  role: contributor
  position: Emphasizes the need for human-readable descriptions of changes in commit
    logs, rather than just LLM prompts.
  quote: "That certainly should not preempt the need to provide a description, detailed\
    \ \nfor complex changes if need be, of the change in the commit log, written for\
    \ \nhuman beings, instead of only a prompt jargon that will become obsolete in\
    \ a \nfew months."
primer_expert: The discussion concerns the practical application of LLMs to GCC development,
  specifically targeting legacy code and refactoring tasks.  The debate centers on
  the level of autonomy granted to LLMs and the required level of human oversight.
  This touches on compiler internals and refactoring strategies.
primer_general: This thread discusses how AI tools (LLMs) can be used to improve GCC,
  the GNU Compiler Collection.  The main idea is to use LLMs for smaller, well-defined
  tasks like finishing partially completed features, rather than letting them design
  entire new systems.  The discussion also covers the importance of human review and
  clear explanations of changes, even when AI is involved.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/7D76F825-E65A-4218-9CFF-27CDE39211DF@gmail.com
bugzilla_url: null
date: '2026-04-25'
---

Richard Biener suggests a sensible middle ground for using LLMs in GCC development: using them to complete long-neglected partial transitions, but not for designing major new features. He cautions against accepting large infrastructure changes designed by LLMs.  The discussion highlights concerns about LLMs producing unmaintainable code or making poor architectural decisions.
