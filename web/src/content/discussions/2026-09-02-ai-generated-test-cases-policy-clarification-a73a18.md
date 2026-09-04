---
project: binutils
subsystem: binutils
patch_id: null
tags:
- ai
- testing
- policy
- contribution
discussion_id: 76b4bcbd-ab3c-4dc0-961d-3107370391d9@redhat.com
source_type: public_inbox
title: 'Re: ping regarding an earlier question'
headline: AI-generated test cases policy clarification
tldr: Binutils may accept AI-generated test cases if 'assisted by' is meant, aligning
  with other projects.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Potential for decreased code quality or maintainability if AI-generated tests are
  not rigorously reviewed.
- Aligning with industry trends for AI adoption in software development.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: maintainer
  position: Clarifies that AI-assisted test cases are acceptable if 'assisted by'
    is the interpretation, and is open to formalizing this policy.
  quote: 'Yes, if Sam had really meant "assisted by" rather than "partially created
    by" then I think that it is OK to accept the patch.


    There also seems to a trend for other projects to accept AI generated test

    cases.  Whilst we do not have that for the binutils, I am open to making

    such a change if it is the way to go.'
primer_expert: This discussion concerns the binutils project's policy on accepting
  patches generated or assisted by Artificial Intelligence. Specifically, it addresses
  whether AI-generated test cases are permissible, focusing on the interpretation
  of contributor attribution and the project's stance on adopting such tools.
primer_glossary:
- term: AI-generated test cases
  definition: Test code that has been created with the assistance of artificial intelligence
    tools, such as large language models.
- term: AI rule
  definition: A project-specific policy or guideline that governs the acceptance and
    attribution of code generated or assisted by artificial intelligence.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/76b4bcbd-ab3c-4dc0-961d-3107370391d9@redhat.com
bugzilla_url: null
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

Nick Clifton clarifies the policy on AI-generated code within binutils, responding to a query about a previous patch. He indicates that if 'assisted by' is interpreted as the intent for AI-generated test cases, then accepting them is permissible, aligning with practices seen in other projects. This suggests a willingness to adopt AI tools for test case generation under specific conditions.
