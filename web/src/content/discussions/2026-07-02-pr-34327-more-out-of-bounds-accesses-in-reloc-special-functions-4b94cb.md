---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- bugfix
- elf
- relocations
- coff
discussion_id: akXWTenS9zB13ypw@squeak.grove.modra.org
source_type: public_inbox
title: PR 34327 More out of bounds accesses in reloc special functions
headline: PR 34327 More out of bounds accesses in reloc special functions
tldr: Addresses more instances of out-of-bounds reads in relocation functions across
  various targets.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases robustness by adding checks, potentially rejecting more malformed object
  files.
- Improves security by preventing out-of-bounds reads.
exchanges:
- author: Alan Modra
  role: proposer
  position: Submits a follow-up patch to fix more instances of out-of-bounds reads
    in relocation special functions, expressing hope that no new issues are introduced.
  quote: 'I don''t claim to have caught all places where reloc special functions

    don''t sanity check input, but this should be most of them.  Hopefully

    this does not expose odd reloc howto entries like the mmix one in the

    previous patch.'
primer_expert: Following up on a prior fix, this patch series continues to identify
  and rectify instances of out-of-bounds reads within binutils' BFD library, specifically
  in relocation handling code. The fixes involve adding robust sanity checks for relocation
  offsets across multiple ELF and COFF targets, aiming to prevent memory corruption
  and crashes originating from malformed input object files.
primer_glossary:
- term: relocation
  definition: A directive that describes how to modify code or data when an object
    file is linked. Relocations typically specify an address and the type of modification
    needed, such as patching in an offset or a symbol address.
- term: out-of-bounds access
  definition: An error where a program attempts to read from or write to a memory
    location that is outside the allocated bounds of an array or buffer, potentially
    leading to data corruption or crashes.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: COFF
  definition: Common Object File Format, an older object file format used on some
    Unix systems, and also the basis for the PE format used on Windows.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akXWTenS9zB13ypw@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

This patch series extends the bug fixes from a previous submission, addressing additional locations within relocation special functions that were susceptible to out-of-bounds reads. It applies sanity checks for relocation offsets and performs cleanup, such as removing unnecessary casts, across a range of architectures including ARM, MIPS, SPARC, and others.
