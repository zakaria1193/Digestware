---
project: gcc
subsystem: gsoc
patch_id: null
tags:
- gcc
- gsoc
- optimization
- ipa
- correctness
discussion_id: 20261031153633.27477-1-kapellirohith@gmail.com
source_type: public_inbox
title: 'Re: GSoC: possible IPA-ICF project direction'
headline: 'GSoC: possible IPA-ICF project direction'
tldr: Student proposes comparing more function attributes in IPA-ICF to fix a correctness
  bug.
proposer: Rohith Kapelli <kapellirohith@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Expanding attribute comparison in IPA-ICF could increase compile times.
- Deciding which attributes must be identical for equivalence is complex; differing
  attributes might not always affect correctness but could limit optimization.
exchanges:
- author: Rohith Kapelli <kapellirohith@gmail.com>
  role: proposer
  position: Proposes a direction for a GSoC project to enhance IPA-ICF by comparing
    more function properties, specifically focusing on function attributes in call
    types that were previously ignored, potentially causing correctness issues.
  quote: 'One case looks particularly concerning. It''s related to PR123227, but this
    time the attribute is on a call''s function type: [...] The likely issue is in
    compare_gimple_call (ipa-icf-gimple.cc:729). It uses comp_type_attributes, whose
    ordinary attribute comparison ignores attributes that don''t affect type identity,
    and nonnull is one of them.'
primer_expert: This GSoC proposal for GCC's IPA-ICF pass targets improving function
  equivalence checking. The core issue lies in `ipa-icf-gimple.cc` and `sem_function::equals_wpa`,
  where function attributes on call types (like `__attribute__((nonnull))`) are not
  fully compared, leading to incorrect merging of seemingly equivalent functions.
  This can break optimizations like VRP by propagating incorrect assumptions across
  merged calls, as demonstrated by a test case where null checks are erroneously eliminated.
primer_glossary:
- term: IPA
  definition: Inter-Procedural Analysis. A compiler optimization technique that analyzes
    code across function calls, rather than just within individual functions, to enable
    more aggressive optimizations.
- term: ICF
  definition: Inter-procedural Constant Folding. A compiler optimization that evaluates
    expressions involving constants across function calls.
- term: GSoC
  definition: Google Summer of Code. A global program where Google funds student developers
    to spend the summer contributing to various open-source projects.
- term: nonnull attribute
  definition: A function attribute that informs the compiler that a specific pointer
    argument will never be NULL. This can enable optimizations that assume the pointer
    is valid.
- term: VRP
  definition: Value Range Propagation. A compiler optimization pass that determines
    the possible range of values for variables, which can help in simplifying expressions
    and eliminating code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20261031153633.27477-1-kapellirohith@gmail.com
bugzilla_url: null
date: '2026-10-31'
is_stub: false
stub_reason: ''
---

A Google Summer of Code student is investigating Inter-Procedural Analysis (IPA) and Inter-procedural Constant Folding (ICF) to identify more properties that could be compared between functions. A specific concern is the handling of function attributes on call types, which in one case led to incorrect null pointer elimination when IPA-ICF merged functions. The student suggests directly comparing these attributes to address the issue, similar to a previous bug fix.
