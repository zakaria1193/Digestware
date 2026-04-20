---
project: glibc
subsystem: glibc
patch_id: null
tags:
- contribution guidelines
- git
- automation
- LLM
- code generation
discussion_id: lhutst6t58s.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: Contribution guidelines update regarding tool usage'
headline: Contribution guidelines update regarding tool usage
tldr: The discussion concerns updating glibc's contribution guidelines to include
  an "Assisted-by" Git trailer for auto-generated code.
stakes: Ensures proper attribution for contributions involving auto-generated code,
  improving transparency and maintainability.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Increased complexity in contribution guidelines.
- Potential ambiguity in determining when "Assisted-by" is needed.
primer_expert: The thread discusses adding an "Assisted-by" Git trailer. This would
  apply to contributions that involve auto-generated code.  Examples include Autoconf,
  or potentially LLMs. The goal is to give credit where due and ensure transparency.
  Changes to the contribution guidelines affect all aspects of glibc development from
  syscall wrappers to math functions.
primer_general: Contribution guidelines for large projects like glibc define the process
  and standards for submitting code changes. This ensures consistency, quality, and
  proper attribution. Git trailers are metadata lines added to commit messages that
  provide additional information about the commit.  By adding an "Assisted-by" trailer,
  the guidelines aim to acknowledge the use of automated tools in generating parts
  of a contribution. This enhances transparency and allows reviewers to understand
  the origins of the code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhutst6t58s.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This discussion revolves around updating glibc's contribution guidelines to include an "Assisted-by" Git trailer when parts of a contribution are auto-generated. The example provided includes tools like Autoconf and potentially LLMs. The discussion considers whether a sufficiently open LLM could be mentioned specifically. The thread is currently in the proposal stage.
