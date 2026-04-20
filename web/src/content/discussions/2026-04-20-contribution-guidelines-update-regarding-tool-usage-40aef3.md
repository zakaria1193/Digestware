---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- contribution guidelines
- llm
- autoconf
- code generation
discussion_id: lhutst6t58s.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: Contribution guidelines update regarding tool usage'
headline: Contribution guidelines update regarding tool usage
tldr: Discussion on whether to include a reference to an open LLM in the contribution
  guidelines for auto-generated code.
stakes: Clarifies guidelines for contributors using automated tools, ensuring transparency
  and proper attribution.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Including a specific LLM might become outdated if the tool is no longer relevant
  or widely used.
- A more generic guideline might be less clear for new contributors.
primer_expert: This concerns glibc's contribution guidelines, specifically regarding
  the use of auto-generation tools. The 'Assisted-by' tag is a way to attribute parts
  of the code to these tools. The discussion touches on whether to mention specific
  LLMs.
primer_general: Contribution guidelines in large projects like glibc ensure consistent
  code quality and transparency. When automated tools like Autoconf or LLMs are used
  to generate parts of a contribution, it's important to acknowledge their role.  This
  is often done using special tags in the commit message. This proposal aims to clarify
  how to properly attribute contributions made with the help of such tools.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhutst6t58s.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This discussion revolves around updating the glibc contribution guidelines to include a recommendation that reviewers may request an “Assisted-by” tag in commit messages when parts of the contribution have been auto-generated. The discussion focuses on whether to provide an example of a specific LLM or just mention Autoconf. The thread is ongoing.
