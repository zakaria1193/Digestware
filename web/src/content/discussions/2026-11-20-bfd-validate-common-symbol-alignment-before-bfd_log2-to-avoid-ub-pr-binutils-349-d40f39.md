---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- common symbol
- alignment
- undefined behavior
- elf
discussion_id: 04a5d8ff-0b3c-4acf-8377-4996d84e58f5@suse.com
source_type: public_inbox
title: 'Re: [PATCH] bfd: Validate common symbol alignment before bfd_log2 to avoid
  UB [PR binutils/34996]'
headline: 'bfd: Validate common symbol alignment before bfd_log2 to avoid UB [PR binutils/34996]'
tldr: Debate over the correct bounds and handling of common symbol alignment values
  to prevent undefined behavior.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- The patch enforces stricter validation on common symbol alignments.
- The reviewer proposes modifying the shift operation to handle wider alignment values,
  potentially allowing for more flexibility.
- Discussion centers on interpreting the ELF specification for alignment values.
exchanges:
- author: Haolin Xue
  role: contributor
  position: Proposed a patch to validate common symbol alignment to prevent undefined
    behavior in `bfd_log2` and subsequent shifts.
  quote: 'A malformed ELF object with a common symbol whose st_value is not a

    > power of two (e.g., 0xffffff000000ffff) causes bfd_log2 to return 64,

    > which then triggers undefined behavior at the 1 << alignment_power

    > shift (elflink.c:10992).'
- author: Jan Beulich
  role: reviewer
  position: Argues that the proposed bounds for common symbol alignment (power of
    two and < 2^31) are too restrictive and suggests fixing the overflow in the shift
    operation instead.
  quote: 'A value of 0 means "no alignment requirement", just like a value of 1. The

    > spec I''m looking at is explicit about this, be referring to sh_addralign.

    > bfd_log2() also properly deals with an input of 0.


    Limiting to below 2^31 also doesn''t feel right. There''s nothing conceptually

    wrong with bigger values.


    ... this one need adjusting. There''s no good reason to use plain 1 there. Anything
    that fi…'
primer_expert: The issue concerns the handling of common symbols' alignment in binutils'
  BFD library. A malformed ELF object can provide an `st_value` for a common symbol
  that is not a power of two. This leads `bfd_log2` to return an incorrect value (e.g.,
  64), causing undefined behavior in `elf_link_add_object_symbols` due to a bit shift
  (`1 << alignment_power`). The patch proposes validating `st_value` to be zero, a
  power of two, and less than 2^31. Reviewer Jan Beulich contests these limits, arguing
  that the spec allows for values of 0 and 1 to mean no alignment requirement, and
  larger powers of two are…
primer_glossary:
- term: Common symbol
  definition: A type of symbol in object files that represents a variable that has
    been declared but not yet defined. Multiple definitions are merged during linking.
- term: Alignment
  definition: The requirement that data be stored at memory addresses that are multiples
    of a specific power of two.
- term: bfd_log2
  definition: A function within the BFD library that calculates the base-2 logarithm
    of a number, typically used for alignment calculations.
- term: Undefined behavior (UB)
  definition: Behavior that occurs when a program attempts an operation that is not
    specified by the C or C++ standards, leading to unpredictable results.
- term: ELF
  definition: Executable and Linkable Format.
- term: PR binutils/34996
  definition: A bug report filed against the binutils project, specifically bug number
    34996.
- term: st_value
  definition: A field in the ELF symbol table entry that stores the symbol's value
    or offset.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/04a5d8ff-0b3c-4acf-8377-4996d84e58f5@suse.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This discussion addresses a potential undefined behavior in binutils' BFD library when handling common symbol alignments. The proposed patch suggested validating the `st_value` to be a power of two and less than 2^31. Reviewer Jan Beulich argues against these specific bounds, stating that 0 and 1 are valid alignment values, and larger powers of two are conceptually permissible. He suggests adjusting the UB-causing shift operation instead of imposing arbitrary limits on the alignment value.
