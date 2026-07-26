---
project: gcc
subsystem: rfc
patch_id: null
tags:
- preprocessor
- extension
- macros
- ergonomics
- RFC
discussion_id: CALzUo856qtVxh8PobEG7Qkf8pp3JkxCeunx7ASbDkmKSeifxbg@mail.gmail.com
source_type: public_inbox
title: 'RFC: C preprocessor extension: Multiline/block macro definition'
headline: 'RFC: C preprocessor extension: Multiline/block macro definition'
tldr: Proposal for a new C preprocessor directive to define multiline macros without
  backslashes.
proposer: NomagnoIsNotDead <alvarosaez316@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 7
technical_tradeoffs:
- Adds a new directive, potentially increasing preprocessor complexity.
- Improves ergonomics for writing multiline macros, avoiding backslash escapes.
- Requires careful integration into existing preprocessor parsing logic.
exchanges:
- author: Joseph Myers <josmyers@redhat.com>
  role: reviewer
  position: Suggests the author consult an existing proposal for similar functionality
    (#def/#enddef, N3531).
  quote: 'You should be talking to Alejandro about his #def/#enddef proposal

    (N3531).'
- author: NomagnoIsNotDead <alvarosaez316@gmail.com>
  role: proposer
  position: Introduces an RFC for a new preprocessor directive to simplify multiline
    macro definitions.
  quote: "I have an idea to extend the GNU C preprocessor with a new kind of\ndirective.\
    \ Its behaviour should be sufficiently encapsulated by the\nfollowing simple example:\n\
    \n#startdef MACRO_NAME\n    You may define multiline macros here.\n    No backslashes\
    \ are needed.\n#enddef"
primer_expert: This RFC proposes an extension to the GNU C preprocessor (libcpp) to
  simplify the definition of multiline macros. Instead of using backslashes to escape
  newlines, this proposal introduces `#startdef` and `#enddef` directives to delimit
  macro definitions that can span multiple lines naturally. The goal is to improve
  readability and maintainability of complex macros.
primer_glossary:
- term: libcpp
  definition: The C preprocessor library used by GCC. It handles preprocessor directives,
    macro expansion, and source file inclusion.
- term: RFC
  definition: Request For Comments. A type of document that proposes a change or idea
    and solicits feedback from the community before implementation.
- term: macro definition
  definition: A preprocessor directive (`#define`) that associates a name with a sequence
    of replacement text, allowing for code reuse and conditional compilation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CALzUo856qtVxh8PobEG7Qkf8pp3JkxCeunx7ASbDkmKSeifxbg@mail.gmail.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

A proposal outlines a new GNU C preprocessor directive, `#startdef`/`#enddef`, to enable multiline macro definitions without requiring trailing backslashes. This ergonomic feature aims to simplify the writing of large, multi-line macros. The author has a prototype and seeks community feedback before developing a full implementation for libcpp, acknowledging the contribution guidelines for GCC frontends.
