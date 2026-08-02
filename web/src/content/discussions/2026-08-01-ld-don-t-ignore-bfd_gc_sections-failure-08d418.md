---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- bugfix
- patch
discussion_id: CAMe9rOpUPG-XS=XThOx1SbzP96kCumDaMVmBzgxZCZBenJOJLQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] ld: Don''t ignore bfd_gc_sections failure'
headline: 'ld: Don''t ignore bfd_gc_sections failure'
tldr: The author withdraws a patch that would make bfd_gc_sections failures fatal,
  planning a different fix.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Deciding whether linker section garbage collection failures should be fatal or recoverable.
- Ensuring that bug fixes do not introduce regressions or unintended side effects.
- Revising the approach to fixing PR ld/34448 based on feedback or further analysis.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Withdraws a previously submitted patch that aimed to make `bfd_gc_sections`
    failures fatal, indicating a new approach will be taken.
  quote: I withdrew this patch.  I will post a different fix.
primer_expert: 'A patch was proposed to change the behavior of the `ld` linker: instead
  of ignoring failures from `bfd_gc_sections` (a function related to garbage collection
  of sections), it would issue a fatal error. This was intended to address PR ld/34448.
  However, the author has withdrawn this specific patch and intends to submit an alternative
  fix.'
primer_glossary:
- term: bfd_gc_sections
  definition: A function within the BFD (Binary Descriptor Format) library that performs
    garbage collection on sections, removing unused ones.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: fatal error
  definition: An error that causes the program (in this case, the linker) to terminate
    immediately.
- term: PR ld/34448
  definition: Problem Report number 34448 filed against the GNU linker (ld), indicating
    a specific bug or issue that needs to be addressed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpUPG-XS=XThOx1SbzP96kCumDaMVmBzgxZCZBenJOJLQ@mail.gmail.com
bugzilla_url: null
date: '2026-08-01'
is_stub: false
stub_reason: ''
---

H.J. Lu withdraws a patch intended to make failures in `bfd_gc_sections` fatal for the linker. He states that he will post a different fix for the underlying issue (PR ld/34448), without elaborating on the reasons for withdrawal or the nature of the new fix.
