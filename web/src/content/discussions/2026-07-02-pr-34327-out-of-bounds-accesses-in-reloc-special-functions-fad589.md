---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- bugfix
- elf
- relocations
discussion_id: akXVE3vcyZt4qhY-@squeak.grove.modra.org
source_type: public_inbox
title: PR 34327 Out of bounds accesses in reloc special functions.
headline: PR 34327 Out of bounds accesses in reloc special functions
tldr: Fixes out-of-bounds access in relocation functions and corrects a long-standing
  bug in the mmix howto table.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Enforces stricter bounds checking, potentially rejecting malformed object files
  that may have previously been processed partially.
- Corrects a historical inaccuracy in a specific architecture's relocation handling.
exchanges:
- author: Alan Modra
  role: proposer
  position: Proposes fixes for out-of-bounds accesses in relocation functions and
    corrects an error in the mmix howto table.
  quote: 'As per the PR, s12z lacked any reloc offset sanity checking, the

    others all just checked that the offset started within the section

    rather than checking the field was contained in the section.


    Using the proper check for mmix exposed a problem in the howto table,

    present since the initial mmix commit.  The R_MMIX_BASE_PLUS_OFFSET

    field is actually two bytes, located at the reloc address.  Making…'
- author: Hans-Peter Nilsson
  role: reviewer
  position: Agrees with the proposed fix for the mmix howto table and notes that the
    problem has existed since the initial commit.
  quote: "Looks like it; R_MMIX_BASE_PLUS_OFFSET was there originally, but \nmost\
    \ of the implementation came later."
- author: Alan Modra
  role: proposer
  position: Clarifies that the overflow reporting was handled by `complain_on_overflow`
    and that the change to `complain_overflow_dont` is correct, despite potential
    initial confusion.
  quote: I meant, presu
primer_expert: This patch series addresses security vulnerabilities and correctness
  issues in binutils' BFD library related to ELF relocations. Specifically, it fixes
  several functions that perform out-of-bounds reads by not properly checking if the
  relocation offset falls within the bounds of the target section. An additional fix
  targets a long-standing bug in the mmix ELF target's howto table, correcting the
  size and overflow reporting for the R_MMIX_BASE_PLUS_OFFSET relocation.
primer_glossary:
- term: relocation
  definition: A directive that describes how to modify code or data when an object
    file is linked. Relocations typically specify an address and the type of modification
    needed, such as patching in an offset or a symbol address.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: howto table
  definition: A data structure within BFD that describes how to perform specific relocation
    types for a given architecture. It maps relocation types (e.g., R_MMIX_BASE_PLUS_OFFSET)
    to operations and checks.
- term: out-of-bounds access
  definition: An error where a program attempts to read from or write to a memory
    location that is outside the allocated bounds of an array or buffer, potentially
    leading to data corruption or crashes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akXVE3vcyZt4qhY-@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

This patch addresses out-of-bounds read accesses in relocation functions across various ELF targets by implementing proper sanity checks for relocation offsets. It also corrects an issue in the mmix howto table that has persisted since its initial commit, specifically concerning the size and interpretation of the R_MMIX_BASE_PLUS_OFFSET field, which was incorrectly defined as an eight-byte field.
