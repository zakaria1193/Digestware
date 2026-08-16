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
discussion_id: alpine.DEB.2.21.2608141637320.14132@angie.orcam.me.uk
source_type: public_inbox
title: '[to-be-committed] PR ld/24600: BFD: Fix use-after-free from `_bfd_load_armap'''
headline: 'BFD: Fix use-after-free from `_bfd_load_armap'''
tldr: Fixes a use-after-free vulnerability in BFD's archive handling related to symbol
  map allocation.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Committed
outcome: committed
impact_score: 7
sentiment_score: 9
technical_tradeoffs:
- Improved memory safety by fixing use-after-free vs. using local objalloc for temporary
  allocations, potentially increasing peak memory usage during archive processing.
exchanges:
- author: Maciej W. Rozycki
  role: proposer
  position: Submitted a patch to fix a use-after-free vulnerability in BFD's archive
    symbol map handling by refactoring memory management for symbol names.
  quote: "An observation here is that `_bfd_compute_and_push_armap' only makes\ntemporary\
    \ use of its allocations, so there's no point in attaching them\nto the archive\
    \ BFD.  Switch to using local objalloc then, the release of\nwhich does not affect\
    \ allocations made by `_bfd_load_armap'.\n\n NB this code dates back to commit\
    \ 5ee3886b48fb from 1994."
- author: Maciej W. Rozycki
  role: contributor
  position: Followed up on the patch, noting that a previous version had already addressed
    function result casts and that a separate change could handle the symbol cache
    discarding issue.
  quote: 'I saw Alan''s fix which takes a different approach and makes temporary

    allocations from `_bfd_compute_and_push_armap'' permanent, however at the

    cost of keeping intermediate pointer allocations forever.  This variant

    discards them after use at the cost of temporary higher memory usage in

    `_bfd_load_armap''.  I''m happy to discuss pros and cons.'
- author: Maciej W. Rozycki
  role: maintainer
  position: Self-corrected on the technical approach, concluding that a combination
    of strategies could yield the best result without the downsides of either individual
    approach.
  quote: 'On second thoughts I concluded we can have the pros of both changes and

    the cons of neither,'
primer_expert: This patch in binutils/bfd/archive.c addresses a use-after-free vulnerability
  (CVE-2026-19548) in the handling of archive symbol maps. The function `_bfd_compute_and_push_armap`
  was prematurely freeing memory that was still needed by `_bfd_load_armap`. The proposed
  solution involves refactoring `_bfd_compute_and_push_armap` to use local objalloc
  for temporary symbol name allocations. This ensures that memory essential for symbol
  map processing is retained, resolving the use-after-free condition without impacting
  the data loaded by `_bfd_load_armap`.
primer_glossary:
- term: use-after-free
  definition: A memory corruption vulnerability where a program attempts to access
    memory after it has been deallocated, potentially leading to crashes or security
    exploits.
- term: BFD
  definition: Binary File Descriptor library, a low-level interface used by binutils
    to handle various executable and object file formats.
- term: objalloc
  definition: A memory allocation mechanism within BFD that manages memory for specific
    objects, often used for internal data structures.
- term: CVE-2026-19548
  definition: A Common Vulnerabilities and Exposures identifier for a specific security
    flaw in the binutils BFD library related to archive handling.
- term: symbol map
  definition: A data structure within an archive file that lists the symbols contained
    within its member object files, facilitating symbol resolution.
series_id: PR ld/24600
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2608141637320.14132@angie.orcam.me.uk
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch addresses a use-after-free vulnerability in the BFD library concerning archive symbol map handling. The issue arose from memory allocated for symbol map entries being freed prematurely. The proposed solution utilizes local objalloc within `_bfd_compute_and_push_armap` for temporary symbol name pointers, ensuring that permanent name strings are correctly retained and preventing the memory corruption. This fix targets CVE-2026-19548 and is a refactoring of existing code that dates back to 1994.
