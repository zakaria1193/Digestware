---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- tls
- pe
- alignment
discussion_id: 10855e94-ce2e-457a-8cb0-9feae17ecda7@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] Write alignment of `.tls` into `_tls_used.Characteristics`'
headline: Write alignment of `.tls` into `_tls_used.Characteristics`
tldr: Debate continues on whether extremely small alignment values for .tls sections
  can break existing code and the interpretation of `_tls_used`.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: under_review
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Potential performance improvements from tighter alignment vs. risk of breaking existing
  code.
- Enforcing stricter interpretation of ABI/file format specifications.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Reiterates concern about small alignment values breaking code, questions
    the author's reasoning on Microsoft CRT and `_tls_used`'s special meaning, and
    points out cosmetic issues with line wrapping.
  quote: 'My concern towards very small ->alignment_power values potentially breaking
    existing code remains. Your latest reply on the v1 thread didn''t help there.
    Apart from that the patch is largely fine, except for two cosmetic issues: There
    are many overlong lines which want splitting. (The description also wants re-wrapping
    to have lines remain within 75 columns.)'
- author: LIU Hao
  role: proposer
  position: Expresses annoyance at the repeated concerns without clear examples, questions
    the impact of under-alignment on EFI and mingw-w64 CRT, and defends the special
    meaning of `_tls_used`.
  quote: 'Please show me how an under-alignment may cause an issue. Apparently this
    doesn''t apply to EFI applications which (so far) make absolutely no use of TLS;
    with mingw-w64 CRT it''s not possible, since tlssup.c defines pointers in .tls
    so alignment is guaranteed;


    And I don''t agree that `_tls_used` might not have a special meaning. As an identifier
    in global scope with external linkage, it''s reserved…'
- author: Jan Beulich
  role: reviewer
  position: Counters the author's arguments, stating that alignment directives matter
    more than pointer presence, and reiterates the lack of specification for `_tls_used`'s
    reserved status.
  quote: 'Having pointers there guarantees nothing. It''s alignment directives which
    matter. Please check what I''ve done, and please in particular point out if you
    see an issue with that.


    As before - you fail to provide a reference to where such reserved-ness is specified
    (for non-Windows uses in particular). I for one to not see why an EFI application
    could not use "_tls_used" for an entirely different pu…'
primer_expert: This discussion revolves around a patch that modifies how the alignment
  of Thread Local Storage (`.tls`) sections is written into the `_tls_used.Characteristics`
  field in PE object files. The core of the debate is Jan Beulich's concern that overly
  aggressive alignment optimization (reducing alignment power) could lead to performance
  degradation or even crashes on some platforms or with certain TLS usage patterns,
  and his questioning of the special significance attributed to the identifier `_tls_used`.
primer_glossary:
- term: .tls
  definition: A section in object files that contains Thread Local Storage data. Each
    thread gets its own copy of this data.
- term: PE
  definition: Portable Executable. The file format used for executables, DLLs, and
    object code in Windows systems.
- term: CRT
  definition: C Runtime. A library providing essential functions for C programs, including
    initialization and support for TLS.
- term: TLS
  definition: Thread Local Storage. A mechanism allowing variables to have thread-specific
    instances.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/10855e94-ce2e-457a-8cb0-9feae17ecda7@suse.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

Jan Beulich expresses ongoing concern that very small alignment values for .tls sections might break existing code, despite the proposed patch. The discussion touches upon the potential issues with Microsoft's CRT and clang/MSVC, and the reservation of the `_tls_used` identifier. The author of the patch has not yet provided a definitive reference to support the claims about under-alignment issues or the reserved nature of `_tls_used`.
