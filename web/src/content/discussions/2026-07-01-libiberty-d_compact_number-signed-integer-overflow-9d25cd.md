---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- bugfix
- libiberty
- c++
- demangler
discussion_id: akRw-8BLQ-FkUM9O@squeak.grove.modra.org
source_type: public_inbox
title: libiberty d_compact_number signed integer overflow
headline: libiberty d_compact_number signed integer overflow
tldr: Fixes signed integer overflow in `libiberty`'s C++ demangler.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixes a security vulnerability.
- Ensures correct behavior in the C++ demangler.
exchanges:
- author: Alan Modra
  role: proposer
  position: Submits a fix for a signed integer overflow in `libiberty's` C++ demangler,
    applying it to binutils and gcc.
  quote: 'Fix this by doing the addition in unsigned arithmetic.


    Applying to binutils and gcc as obvious.'
primer_expert: A signed integer overflow vulnerability in `libiberty/cp-demangle.c`'s
  `d_compact_number` function is addressed by switching the addition of `1` to unsigned
  arithmetic (`+ 1u`). This prevents the overflow that could occur when `d_number()`
  returns a value close to the maximum for a signed integer, ensuring the demangler
  operates correctly and securely under all valid input conditions.
primer_glossary:
- term: libiberty
  definition: A collection of utility functions used by GCC and other GNU projects,
    providing common routines like string manipulation, memory allocation, and demangling.
- term: C++ demangler
  definition: A tool that converts mangled C++ symbol names (which are made unreadable
    by the compiler for C++ name mangling) back into their original, human-readable
    form.
- term: signed integer overflow
  definition: An error condition that occurs when an arithmetic operation attempts
    to create a value that is too large to be represented by a signed integer type.
    This can lead to unexpected behavior and security vulnerabilities.
- term: unsigned arithmetic
  definition: Arithmetic operations performed on integer types that do not use the
    most significant bit to represent the sign. This allows for a larger positive
    range compared to signed integers of the same size.
- term: compiler
  definition: A program that translates source code written in a high-level programming
    language into a lower-level language, such as machine code or an intermediate
    representation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akRw-8BLQ-FkUM9O@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch addresses a signed integer overflow vulnerability in the `d_compact_number` function within `libiberty/cp-demangle.c`. The overflow occurs during the addition of 1 to a number obtained from `d_number`. The fix converts this addition to use unsigned arithmetic (`+ 1u`), preventing the overflow and ensuring correct behavior for the C++ demangler.
