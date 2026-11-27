---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c++
- compiler
- extension
- compatibility
discussion_id: CAMwLgFpTDYVvwi68RX2EhrJ+BwiXTa2W=MQ9O24Kncb8Mh8EkA@mail.gmail.com
source_type: public_inbox
title: Supporting __typeof_unqual__ in the C++ front end
headline: Support __typeof_unqual__ in C++ front end
tldr: Proposes adding __typeof_unqual__ as a GNU extension to g++ to improve compatibility
  with shared C/C++ headers.
proposer: Richard <richard.qin.x@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds a new GNU extension to the C++ front end, potentially increasing maintenance
  burden.
- Aims to improve compatibility with widely used C/C++ headers, reducing build issues.
exchanges:
- author: Richard <richard.qin.x@gmail.com>
  role: proposer
  position: Proposes adding __typeof_unqual__ as a GNU extension to the C++ front
    end to resolve compatibility issues with shared C/C++ headers that use this construct.
  quote: 'Because shared C/C++ headers (such as kernel, system, and low-level utility
    macros) increasingly use __typeof_unqual__ to strip top-level cvr-qualifiers when
    declaring temporary variables, C++ code including those headers compiles cleanly
    under Clang but fails under g++.


    Would there be interest in supporting __typeof_unqual__ as a GNU extension in
    the C++ front end as well, keeping unprefixed ty…'
primer_expert: This proposal addresses a compatibility gap between GCC's C and C++
  front ends regarding the __typeof_unqual__ extension. While the C front end supports
  it (following C23), the C++ front end (g++) does not, leading to build failures
  when C++ code includes headers using this construct, which Clang supports in both
  C and C++ modes. The goal is to add it as a GNU extension to g++.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAMwLgFpTDYVvwi68RX2EhrJ+BwiXTa2W=MQ9O24Kncb8Mh8EkA@mail.gmail.com
bugzilla_url: null
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

GCC 14 added C23's typeof_unqual and __typeof_unqual__ to the C front end, but g++ currently rejects __typeof_unqual__. This extension is used in shared headers to strip qualifiers, causing compilation failures in g++ while working in Clang. This proposal aims to add __typeof_unqual__ support to g++ as a GNU extension, preserving the C23-only status of typeof_unqual.
