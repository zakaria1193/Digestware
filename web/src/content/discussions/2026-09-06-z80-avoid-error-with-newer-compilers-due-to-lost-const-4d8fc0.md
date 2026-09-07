---
project: binutils
subsystem: z80
patch_id: null
tags:
- z80
- build
- const
- compiler
- glibc
discussion_id: 20260906215526.958487-1-hpa@zytor.com
source_type: public_inbox
title: '[PATCH 1/1] z80: avoid error with newer compilers due to lost "const"'
headline: 'z80: avoid error with newer compilers due to lost "const"'
tldr: H. Peter Anvin adds missing 'const' to a pointer in tc-z80.c to fix a build
  error with newer GCC/glibc versions.
proposer: '"H. Peter Anvin" <hpa@zytor.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 9
technical_tradeoffs:
- Strict const correctness vs. historical laxity.
- Minimal code change for build compatibility.
exchanges:
- author: H. Peter Anvin <hpa@zytor.com>
  role: proposer
  position: Submits a patch to add 'const' to a pointer in tc-z80.c to resolve a build
    error caused by newer compiler/glibc versions propagating const-ness.
  quote: The pointer that is missing "const" is ever written to, so simply fix it
    by adding the missing "const".
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch as obvious and states they will apply it.
  quote: Likely counts as obvious. I'll get this in for you in due course.
primer_expert: This patch addresses a build failure in the Z80 assembler configuration
  file (tc-z80.c) when using recent GCC and glibc versions. Newer compilers are stricter
  about 'const' correctness, and a pointer used in `tc-z80.c` was not marked as 'const',
  causing a type mismatch with functions like `bsearch()` that now propagate 'const'-ness.
  The fix involves adding the 'const' qualifier to the pointer declaration, as it
  is never modified.
primer_glossary:
- term: const
  definition: A type qualifier in C that indicates a variable or pointer cannot be
    modified after initialization. Newer compiler versions are more strict about enforcing
    const correctness.
- term: tc-z80.c
  definition: The configuration file for the Z80 target within the GNU Assembler (gas),
    handling target-specific parsing and assembly directives.
- term: bsearch()
  definition: A standard C library function that performs a binary search on a sorted
    array. It requires the array elements to be comparable and the search key to be
    of a compatible type.
series_id: 'binutils:z80: avoid error with newer compilers due to lost "const"'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260906215526.958487-1-hpa@zytor.com
bugzilla_url: null
date: '2026-09-06'
is_stub: false
stub_reason: ''
---

H. Peter Anvin proposes a fix for a build error in tc-z80.c that occurs with newer GCC and glibc versions (16.2.1, 2.43). The error arises because functions like bsearch() now propagate 'const'-ness, and a pointer in tc-z80.c was missing this qualifier. Since the pointer is never written to, adding 'const' resolves the issue without side effects. This bug has been present since the Z80 target was introduced.
