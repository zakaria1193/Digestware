---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- vulnerability
- bfd
- binutils
- memory corruption
discussion_id: alpine.DEB.2.21.2608142347340.14132@angie.orcam.me.uk
source_type: public_inbox
title: '[to-be-committed v2] PR ld/24600: BFD: Fix use-after-free from `_bfd_load_armap'''
headline: 'BFD: Fix use-after-free from `_bfd_load_armap'''
tldr: Fixes a use-after-free vulnerability in BFD's archive handling related to symbol
  map allocation.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Committed
outcome: committed
impact_score: 7
sentiment_score: 8
technical_tradeoffs:
- Improved memory safety by fixing use-after-free vs. potential minor increase in
  temporary memory usage during archive processing.
exchanges:
- author: Maciej W. Rozycki
  role: proposer
  position: Submitted a revised patch to fix a use-after-free in BFD's archive symbol
    map handling, incorporating Alan Modra's changes and addressing memory release
    upon function failure.
  quote: 'This has passed regression-testing across my usual 263 targets.


    Given the reduction of the change I''ve kept the function result casts in

    this revision.  A separate clean-up with no functional change can be done

    separately.


    I note that the failure of `push_armap'' does not cause the symbol cache

    to be discarded in the `keep_symdefs'' case even though it probably should.

    I''ll offer a separate chang…'
- author: Alan Modra
  role: reviewer
  position: Approved the revised patch, noting that while they preferred the first
    version, this one is also acceptable.
  quote: I was happy with v1, but this is good too.
primer_expert: This patch in binutils/bfd/archive.c resolves a use-after-free vulnerability
  (CVE-2026-19548) related to `_bfd_load_armap` and `_bfd_compute_and_push_armap`.
  The core issue was that memory allocated for a symbol map was freed before it was
  fully processed, particularly when handling mapless archives. The fix ensures that
  local objalloc is used for temporary name pointers within `_bfd_compute_and_push_armap`,
  preventing premature deallocation of essential symbol data.
primer_glossary:
- term: use-after-free
  definition: A memory corruption vulnerability where a program attempts to access
    memory after it has been deallocated, potentially leading to crashes or security
    exploits.
- term: BFD
  definition: Binary File Descriptor library, a low-level interface used by binutils
    to handle various executable and object file formats.
- term: mapless archives
  definition: Archive files that do not contain a symbol map, requiring specific handling
    during loading and processing.
- term: objalloc
  definition: A memory allocation mechanism within BFD that manages memory for specific
    objects, often used for internal data structures.
- term: CVE-2026-19548
  definition: A Common Vulnerabilities and Exposures identifier for a specific security
    flaw in the binutils BFD library related to archive handling.
series_id: PR ld/24600
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2608142347340.14132@angie.orcam.me.uk
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch, a revision of a previous version, addresses a use-after-free vulnerability in the BFD library's handling of archive symbol maps. The issue stems from memory allocated for symbol map entries being prematurely freed. The fix restructures the `_bfd_compute_and_push_armap' function to manage temporary name pointers within local objalloc, ensuring that actual name strings are retained correctly and preventing the use-after-free condition. This addresses CVE-2026-19548.
