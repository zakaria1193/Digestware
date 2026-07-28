---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- attribute
- union
- static-analysis
- diagnostics
discussion_id: amfnO5MFDRqr39k0@thesun
source_type: public_inbox
title: 'Re: [RFC] Proposal for tagged_by attribute to describe union discriminators'
headline: Proposal for tagged_by attribute to describe union discriminators
tldr: Proposes a GCC attribute to explicitly link enum discriminators to union members
  for improved static analysis.
proposer: Ashton Warner <drflamemontgomery@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds a new language extension for improved type safety.
- Requires front-end changes to parse and interpret the attribute.
- No runtime performance impact.
exchanges:
- author: Ashton Warner <drflamemontgomery@gmail.com>
  role: proposer
  position: Proposes a new `tagged_by` GCC attribute to explicitly describe tagged
    unions by mapping enum discriminators to union members. The goal is to enhance
    static analysis and diagnostics without affecting runtime behavior.
  quote: "I propose the GCC attribute __attribute__((tagged_by(...))) with the following\
    \ syntax:\n\ntagged_by(discriminator, mapping-list) \n\nwhere:\n\n- discriminator\
    \ is an identifier\n- mapping-list is a comma-separated list of one or more mappings.\n\
    - Each mapping has the form:\n    (enumerator, union-member)\n\nFor example:\n\
    \nstruct number {\n  enum num_type type;\n\n  union { int ival; float fval; }\
    \ __attribute__((…"
- author: Martin Uecker
  role: reviewer
  position: Asks for clarification on the implications of the proposed attribute,
    specifically regarding potential changes to the C standard or compiler behavior.
  quote: "Am Donnerstag, dem 16.07.2026 um 09:17 +1200 schrieb Ashton Warner via Gcc:\n\
    > Hello, \n> \n> I would like to discuss the possibility of adding a GCC attribute\
    \ for\n> describing tagged unions (discriminated unions) to improve static\n>\
    \ analysis diagnostics."
primer_expert: This proposal introduces a new GCC extension attribute, `tagged_by`,
  for tagged unions. It aims to provide explicit semantic information for analyzing
  the relationship between an enum discriminator and union members, enabling improved
  compiler diagnostics for type safety. The attribute would reside within the C front-end,
  processed during semantic analysis.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/amfnO5MFDRqr39k0@thesun
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

Ashton Warner proposes a new GCC attribute `tagged_by` to associate enum discriminators with specific union members. This attribute would provide additional information for static analysis tools, enabling them to issue diagnostics when a union is accessed with an incorrect member for its current discriminator value. The attribute is explicit and does not alter runtime behavior.
