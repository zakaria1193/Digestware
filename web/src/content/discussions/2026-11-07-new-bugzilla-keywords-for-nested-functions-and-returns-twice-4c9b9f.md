---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GCC
- bugzilla
- keywords
- LLM
discussion_id: 2a662600-db06-41c0-948c-2fa025467825@gmail.com
source_type: public_inbox
title: 'Re: FYI New keywords in bugzilla'
headline: New bugzilla keywords for nested functions and returns-twice
tldr: Reviewer agrees with new bugzilla keywords for nested functions and returns-twice,
  and suggests considering a tag for LLM-found bugs.
proposer: Jeff Law <jeffreyalaw@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adding new keywords aids bug triage but increases the management overhead of the
  bug tracking system.
- A specific tag for LLM-generated bugs could improve tracking but might stigmatize
  certain bug reports or introduce noise.
exchanges:
- author: Andrea Pinski via Gcc
  role: contributor
  position: Introduced new Bugzilla keywords 'nested-func' and 'returns-twice' to
    categorize specific types of bugs, including those found by LLMs.
  quote: 'With the recent influx of LLM based wrong code and ICE on valid fuzzers
    in a few areas, I added a few keywords for bugzilla.


    nested-func - to cover issues relating to the nested function extension in C but
    also covers nested functions as used by both the Ada and Fortran front-end since
    they use the same mechanism in the middle-end too


    returns-twice - to cover issues relating to the returns_twic…'
- author: Jeff Law
  role: reviewer
  position: Agrees with the proposed keywords and suggests considering a tag for LLM-discovered
    bugs.
  quote: "All seems sensible to me.\n\nAs you've undoubtedly noticed Andrea I've got\
    \ LLMs chewing through \nruntime data on spec looking for missed optimizations\
    \ (focused on \nRISC-V).   The cases posted so far as just a subset of what it's\
    \ found \non x264.  Undoubtedly when I start sorting through the findings in the\
    \ \nrest of the benchmarks more cases will come to light.\n\nWhile I try to always\
    \ mention that iss…"
primer_expert: This thread discusses additions to GCC's Bugzilla for categorizing
  issues related to nested functions (used across C, Ada, Fortran frontends via shared
  middle-end mechanisms) and the `returns_twice` attribute, which often intersects
  with `fork`/`setjmp` and `-Wclobber` warnings. The conversation also touches on
  the potential need for a dedicated tag for bugs identified by Large Language Models
  (LLMs), distinguishing between ICEs on valid code versus invalid input.
primer_glossary:
- term: Bugzilla
  definition: A popular open-source bug-tracking system used by many projects, including
    GCC, to manage defects and feature requests.
- term: keyword
  definition: In Bugzilla, a keyword is a tag that can be added to a bug report to
    provide additional categorization or context.
- term: nested function
  definition: A function defined inside another function. GCC supports this as a C
    extension and it's also used internally by Ada and Fortran frontends.
- term: returns_twice
  definition: An attribute in GCC that indicates a function may return twice, typically
    associated with functions like `fork()` or `setjmp()`.
- term: ICE
  definition: Internal Compiler Error, a severe error where the compiler itself crashes
    during the compilation process.
- term: LLM
  definition: Large Language Model, an AI model trained on vast amounts of text data,
    capable of generating human-like text and code.
- term: DFP
  definition: Decimal Floating Point, a data type for representing decimal numbers
    with floating-point precision, distinct from binary floating-point types.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/2a662600-db06-41c0-948c-2fa025467825@gmail.com
bugzilla_url: null
date: '2026-11-07'
is_stub: false
stub_reason: ''
---

Jeff Law responds to Andrea Pinski's introduction of new Bugzilla keywords for 'nested-func' and 'returns-twice'. Law expresses agreement with these additions, noting their relevance to recent issues found with LLM-generated code. He also raises the question of whether a dedicated tag for bugs discovered by LLMs might be beneficial, while acknowledging the ongoing debate about categorizing such bugs, particularly differentiating between incorrect code and internal compiler errors (ICEs) on valid code versus invalid input.
