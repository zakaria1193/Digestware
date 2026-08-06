---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- error-handling
- BFD
discussion_id: CAMe9rOo4GC_Lkw6PYA78CnR5gWsy6T1nYGW+hvdq9DXMeA2YLg@mail.gmail.com
source_type: public_inbox
title: '[PATCH] ld: Check bfd_gc_sections return'
headline: 'ld: Check bfd_gc_sections return'
tldr: Ensures the linker (`ld`) properly handles errors returned by `bfd_gc_sections`,
  specifically when `bfd_error_bad_value` is set.
proposer: H.J. Lu
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 5
technical_tradeoffs: []
exchanges:
- author: H.J. Lu
  role: proposer
  position: Submits a patch to make the linker check the return value of `bfd_gc_sections`
    and handle `bfd_error_bad_value` as a fatal error.
  quote: 'bfd_gc_sections may return false on invalid input:


    ld: pr34448-bug_18.o: bad reloc symbol index (0xf2000005 >= 0x13) for

    offset 0x4 in section `.text.get_tls[get_tls]''


    and set the BFD error to bfd_error_bad_value.  Check bfd_gc_sections

    return and report the fatal error if the BFD error is bfd_error_bad_value.'
- author: Jan Beulich
  role: reviewer
  position: Questions the guarantee that `bfd_error_bad_value` is only set for the
    specific error condition being addressed.
  quote: 'And what guarantees that bfd_error_bad_value isn''t also set for other kinds

    of errors, from about anywhere in the library? Does bfd_gc_'
- author: H.J. Lu
  role: proposer
  position: Responds to Jan Beulich's concern, indicating further discussion or clarification
    is needed.
  quote: And what guarantees that bfd_error_bad_value i
- author: Jan Beulich
  role: reviewer
  position: Continues the discussion about the scope of `bfd_error_bad_value`.
  quote: 'And '
- author: H.J. Lu
  role: proposer
  position: Continues to engage in the discussion about error handling.
  quote: And
- author: Alan Modra
  role: contributor
  position: Weighs in on the discussion, likely providing context or further questions
    about error handling.
  quote: null
primer_expert: This patch addresses error handling within the GNU linker (`ld`) related
  to garbage collection of sections. The `bfd_gc_sections` function, which is responsible
  for this, can fail and report `bfd_error_bad_value` for various reasons, including
  invalid relocation symbol indices. The proposed change ensures that `ld` treats
  this specific error as fatal, preventing it from proceeding with potentially corrupt
  link results. The discussion involves clarifying whether `bfd_error_bad_value` might
  be set for other, non-fatal errors, which could impact the robustness of this fix.
primer_glossary:
- term: ld
  definition: The GNU linker, which combines object files and libraries into an executable
    or another object file.
- term: bfd_gc_sections
  definition: A function within the BFD library that performs garbage collection on
    sections, removing unreferenced ones.
- term: bfd_error_bad_value
  definition: An error code from the BFD library indicating that a value encountered
    is invalid or out of range.
- term: relocation
  definition: Information in an object file that specifies how to modify code or data
    addresses when the file is linked or loaded.
- term: reloc symbol index
  definition: The index of a symbol within the symbol table, used in relocation entries.
- term: PR ld/34448
  definition: Problem Report number 34448 in the binutils linker component, likely
    referencing the bug this patch aims to fix.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOo4GC_Lkw6PYA78CnR5gWsy6T1nYGW+hvdq9DXMeA2YLg@mail.gmail.com
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

This patch for the GNU linker (`ld`) improves error handling by checking the return value of `bfd_gc_sections`. This function can return `false` and set `bfd_error_bad_value` on invalid input, as seen in a reloc symbol index error. The change ensures that `ld` reports a fatal error in such cases, preventing potentially misleading or incomplete diagnostics. This addresses a specific bug report (PR ld/34448).
