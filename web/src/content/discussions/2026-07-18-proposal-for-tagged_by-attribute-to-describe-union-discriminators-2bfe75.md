---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- attribute
- union
- type system
- debug info
discussion_id: 2417780.ElGaqSPkdT@fomalhaut
source_type: public_inbox
title: 'Re: [RFC] Proposal for tagged_by attribute to describe union discriminators'
headline: Proposal for tagged_by attribute to describe union discriminators
tldr: Introduce tagged_by attribute for discriminated unions, impacting layout and
  debug info.
proposer: Eric Botcazou <botcazou@adacore.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enables better code generation and debugging for discriminated unions at the cost
  of increased compiler complexity.
exchanges:
- author: Eric Botcazou <botcazou@adacore.com>
  role: proposer
  position: Explains that QUAL_UNION_TYPE, unlike UNION_TYPE, has dynamic size and
    is used for layout and debug info generation. The 'tagged_by' attribute's predicate
    references the discriminant via PLACEHOLDER_EXPRs.
  quote: null
primer_expert: This RFC introduces a new GCC attribute, likely `__attribute__((tagged_by(...)))`,
  to annotate discriminated unions. This mechanism, used in Ada, allows the compiler
  to track which member of a union is active based on a separate discriminant field.
  This affects code generation for memory layout (stor-layout.cc) and debugging information
  (dwarf2out.cc), with QUAL_UNION_TYPE implying dynamic sizing.
primer_glossary:
- term: discriminated union
  definition: A union where a separate field, the discriminant, indicates which member
    of the union is currently active. This allows for type safety and specific access
    patterns.
- term: QUAL_UNION_TYPE
  definition: A GCC internal type representing a discriminated union with dynamic
    size, whose active member can be determined at runtime. This contrasts with UNION_TYPE,
    which has a fixed size.
- term: stor-layout.cc
  definition: A GCC source file responsible for determining the memory layout of language
    constructs, including unions and their members.
- term: dwarf2out.cc
  definition: A GCC source file involved in generating DWARF debugging information,
    which describes the compiled program's structure to debuggers.
- term: PLACEHOLDER_EXPRs
  definition: An internal GCC expression type used to represent references to declarations
    that might not yet be fully resolved or that are used in specific contexts like
    attribute qualifiers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/2417780.ElGaqSPkdT@fomalhaut
bugzilla_url: null
date: '2026-07-18'
is_stub: false
stub_reason: ''
---

Eric Botcazou proposes the 'tagged_by' attribute to describe union discriminators in GCC. This attribute is used for driving layout and debug info generation, and it differs from UNION_TYPE by enabling runtime checks and having a dynamic size based on the active member. The predicate for this attribute references the tag via PLACEHOLDER_EXPRs.
