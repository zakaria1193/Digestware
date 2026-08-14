---
project: binutils
subsystem: rfc
patch_id: null
tags:
- security
- ld
- bugfix
- cve
discussion_id: 87zeyq4d2r.fsf@redhat.com
source_type: public_inbox
title: 'RFC: Fix for CVE-2026-19548'
headline: 'RFC: Proposed fix for use-after-free bug in ld/ldmain.c'
tldr: RFC proposes a fix for a use-after-free bug in GNU ld (CVE-2026-19548) by storing
  a copy of a pointer to avoid dereferencing a freed structure.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: under_review
impact_score: 7
sentiment_score: 6
technical_tradeoffs:
- Storing a copy of the pointer vs. refactoring memory management for `symdefs`.
- The proposed fix is simple but might not address the root cause identified by reviewers.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Proposes a fix for a use-after-free bug in GNU ld, suggesting to keep
    a copy of a pointer to avoid dereferencing freed memory.
  quote: CVE-2026-19548 points out a potential use-after-free bug in the add_archive_element()
    function in ld/ldmain.c.  After looking at it it seemed to me that the simplest
    solution was to keep a copy of the my_archive pointer so that there is no need
    to dereference the freed bfd structure.  As is done in the attached, proposed
    patch.  Any comments ?
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Identifies a potential related bug in a previous commit (e34fd4bfa6d7)
    that might be causing the issue addressed by the proposed patch.
  quote: Hmm..  This is likely a bug in e34fd4bfa6d7.  I see a bfd_release in _bfd_compute_and_push_armap
    that will lose the memory for ardata->symdefs set up in _bfd_load_armap.
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: contributor
  position: Suggests an alternative fix using a local `objalloc` structure to manage
    temporary storage, avoiding modifications to the archive BFD and potentially simplifying
    the resolution of the identified issue.
  quote: Good catch!  Since `_bfd_compute_and_push_armap' uses `bfd_alloc' for temporary
    storage only, I think the best way to get this sorted will be just using a local
    objalloc structure rather than attaching it to the archive BFD.  It seems really
    straightforward and will avoid making
primer_expert: A security vulnerability (CVE-2026-19548) has been reported in GNU
  `ld`, specifically a use-after-free in `add_archive_element` within `ld/ldmain.c`.
  The proposed fix involves retaining a pointer to an archive BFD structure to avoid
  dereferencing it after it's freed. Discussion has surfaced a potential underlying
  issue in `_bfd_compute_and_push_armap` related to memory management of `ardata->symdefs`,
  with suggestions for using `objalloc` as an alternative solution.
primer_glossary:
- term: use-after-free
  definition: A memory corruption vulnerability where a program attempts to access
    memory after it has been deallocated, potentially leading to crashes or security
    exploits.
- term: GNU ld
  definition: The GNU linker, a program that combines object files and libraries into
    an executable or another library.
- term: bfd
  definition: Binary File Descriptor library, a GNU library that provides a common
    interface for manipulating various object file formats.
- term: CVE-2026-19548
  definition: A Common Vulnerabilities and Exposures identifier for a specific security
    flaw, in this case, a use-after-free bug in GNU ld.
- term: RFC
  definition: Request For Comments. In this context, it signifies a proposal seeking
    feedback and discussion before potential implementation.
- term: objalloc
  definition: An object allocator, likely a mechanism within BFD for managing memory
    allocations for temporary objects.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87zeyq4d2r.fsf@redhat.com
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

Nick Clifton proposes a fix for a use-after-free vulnerability in the `add_archive_element` function within GNU `ld` (tracked as CVE-2026-19548). The suggested solution involves retaining a copy of the `my_archive` pointer to prevent dereferencing a `bfd` structure after it has been freed. This approach aims to simplify the fix while addressing the reported bug.
