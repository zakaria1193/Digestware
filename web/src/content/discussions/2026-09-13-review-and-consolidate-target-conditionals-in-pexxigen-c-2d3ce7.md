---
project: binutils
subsystem: binutils
patch_id: null
tags:
- bfd
- pe
- refactoring
- maintainability
- code quality
discussion_id: 20260913123323.9734-1-jon.turney@dronecode.org.uk
source_type: public_inbox
title: '[PATCH 0/4] Review and consolidate target conditionals in peXXigen.c'
headline: Review and consolidate target conditionals in peXXigen.c
tldr: Consolidate and clean up PE target conditional logic in BFD.
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves code clarity and reduces maintenance overhead.
- Removes support for obsolete targets, potentially simplifying the codebase.
exchanges:
- author: Jon Turney <jon.turney@dronecode.org.uk>
  role: proposer
  position: Proposes a series of patches to consolidate and clean up target-specific
    conditional logic in `bfd/peXXigen.c`, removing obsolete MIPS support and simplifying
    PE32/PE32+ format distinctions.
  quote: 'As suggested back at [1], I reviewed the target conditional in peXXigen.c.


    This discards some historical cruft for PE32 MIPS and then consolidates the

    "is this target PE32 or PE32+" logic in one place.'
primer_expert: This is a series of patches focused on improving the maintainability
  of `bfd/peXXigen.c` by cleaning up conditional compilation directives. It addresses
  outdated MIPS support and refactors the way PE32 vs. PE32+ (64-bit) targets are
  distinguished, aiming for clearer, more robust code. The changes are primarily code
  hygiene and consolidation efforts.
primer_glossary:
- term: target conditional
  definition: Code that is conditionally compiled based on the target architecture
    or system being built for.
- term: peXXigen.c
  definition: A C source file within the binutils BFD library that handles PE (Portable
    Executable) file format specifics for various architectures.
- term: historical cruft
  definition: Code or design elements that are outdated, no longer relevant, or have
    become cumbersome due to the evolution of the software.
series_id: binutils:review and consolidate target conditionals in pexxigen.c
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260913123323.9734-1-jon.turney@dronecode.org.uk
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This patch series reviews and refactors target conditional logic within `bfd/peXXigen.c`. It aims to discard historical cruft, such as obsolete PE MIPS support, and consolidate the logic for distinguishing PE32 and PE32+ formats. The changes improve code maintainability and reduce the potential for errors by simplifying how different PE targets are handled.
