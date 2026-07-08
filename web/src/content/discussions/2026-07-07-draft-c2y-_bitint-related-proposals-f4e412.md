---
project: gcc
subsystem: gcc
patch_id: null
tags:
- c
- standardization
- compiler
- language features
discussion_id: ak0RdTxEebAf4T6K@tucnak
source_type: public_inbox
title: Draft C2Y _BitInt related proposals
headline: Draft C2Y _BitInt related proposals
tldr: Proposes additions to C2Y for _BitInt I/O support in printf/scanf and stdbit.h.
proposer: Jakub Jelinek <jakub@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Extending printf/scanf for _BitInt might complicate existing format string parsing
  and argument handling.
- Ensuring _BitInt interoperability with stdbit.h requires careful definition of bit
  manipulation operations for arbitrary widths.
exchanges:
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Proposes C2Y papers for _BitInt I/O support in printf/scanf and stdbit.h,
    seeking comments.
  quote: 'As I wrote earlier, I''d like to see _BitInt I/O support in

    *printf*/*scanf* and extending support of _BitInt in stdbit.h

    in C2Y.


    For those I wrote drafts of possible C2Y papers:

    https://jakubjelinek.github.io/wg14/va_arg_bitint.html

    https://jakubjelinek.github.io/wg14/stdbit_bitint.html'
- author: Joseph Myers <josmyers@redhat.com>
  role: reviewer
  position: Suggests that generic_limb_type should be unsigned, as signed types are
    not compatible with the described formats.
  quote: "generic_limb_type should probably be required to be an unsigned type; the\
    \ \ndescriptions don't work with it as a signed type.  Since the terminology \n\
    was changed so that bool isn't counted as an unsigned"
- author: Jakub Jelinek <jakub@redhat.com>
  role: proposer
  position: Acknowledges Joseph Myers' comment on generic_limb_type and inquires about
    adding an exception for scanf's va_arg usage.
  quote: Would it be ok to add an exception for this in 7.16.2.2?  I
- author: Joseph Myers <josmyers@redhat.com>
  role: reviewer
  position: Responds to Jakub Jelinek's query about va_arg and scanf, referencing
    a specific section.
  quote: null
primer_expert: This discussion concerns proposals for the C2Y (C 202Y) standard, specifically
  integrating support for the `_BitInt` type. It involves standard C language evolution,
  focusing on I/O formatting for `_BitInt` via `printf`/`scanf` and its inclusion
  in the `stdbit.h` header. The core technical challenges likely revolve around type
  promotion, argument passing conventions (especially with `va_arg`), and ensuring
  consistent behavior across implementations.
primer_glossary:
- term: _BitInt
  definition: A C language extension for arbitrary-precision integers, allowing for
    integer types of non-standard bit widths.
- term: C2Y
  definition: Refers to the C language standard targeted for release in or around
    the year 202Y, representing the next iteration after C17/C23.
- term: printf/scanf
  definition: Standard C library functions for formatted input and output. Adding
    support for `_BitInt` would require new format specifiers or extensions.
- term: stdbit.h
  definition: A standard C header providing bit manipulation functions and types.
    Extending it for `_BitInt` would involve defining relevant operations and types.
- term: va_arg
  definition: A macro used in C to access arguments passed to variadic functions (functions
    that accept a variable number of arguments), such as `printf`.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ak0RdTxEebAf4T6K@tucnak
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

Jakub Jelinek has drafted proposals for C2Y, aiming to add support for _BitInt I/O with printf/scanf and extend stdbit.h functionality. The proposals are available as web links for community review and feedback.
