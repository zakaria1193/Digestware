---
project: binutils
subsystem: elf
patch_id: null
tags:
- linker
- bugfix
- x86
- ELF
discussion_id: CAMe9rOrbnsbN5dYb17PZdHvoXY+03X5WsuBfHuTmHMATwA53qA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] elf: Avoid relocating non-allocated code sections'
headline: 'elf: Avoid relocating non-allocated code sections'
tldr: Fixes binutils linker to correctly handle non-allocated code sections, preventing
  crashes.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Needs Revision
outcome: needs_revision
impact_score: 5
sentiment_score: 4
technical_tradeoffs:
- Moving the fix to the backend complicates the overall linker logic.
- The initial approach of disallowing non-allocated code sections was a simpler workaround
  but deemed incorrect.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Proposes to issue an error when encountering a non-allocated code section,
    as they cannot be properly relocated.
  quote: Since non-allocated code sections can't be properly relocated, issue an error
    on such input.
- author: Alan Modra
  role: reviewer
  position: Argues that the proposed error is not a proper fix, as the root cause
    is a relocation offset out of range, and the weird flags are secondary. Suggests
    the fix should address the underlying issue.
  quote: This is not a proper fix for the bug, which is caused by a reloc offset out
    of range. The weird flags are just something you see with fuzzed object files.
- author: H.J. Lu
  role: proposer
  position: Explains that non-allocated code sections using GOT or PLT can lead to
    an abort in the x86 backend's relocation logic. Proposes to move the check to
    the x86 backend.
  quote: "If input code section doesn't have SEC_ALLOC, x86-64 linker may abort at\n\
    \n          if (off >= (bfd_vma) -2)\n            abort ();\n\nin elf_x86_64_relocate_section\
    \ since x86-64 linker has\n\n  if ((input_section->flags & SEC_ALLOC) != 0\n...\n\
    \  if ((input_section->flags & SEC_ALLOC) == 0)\n\nI will move the check to x86\
    \ backend."
- author: Jan Beulich
  role: reviewer
  position: Questions why text sections are treated specially and points out that
    the issue might be with the GOT/PLT usage in non-alloced sections.
  quote: In addition to what Alan said - why would text sections be different here?
    Iirc this isn't the first time that you want to treat them specially when there's
    no provision for that in the spec.
- author: Alan Modra
  role: reviewer
  position: Agrees that a correction might be needed where the non-alloced sections
    use GOT or PLT.
  quote: So that may be where a correction is needed then.
primer_expert: The binutils ELF linker (`elflink.c`) has logic to handle relocations.
  A bug was found where non-allocated code sections (those without the `SEC_ALLOC`
  flag) could cause the linker to abort, particularly in the x86 backend when using
  GOT/PLT for resolution. The initial approach was to disallow these sections, but
  it's recognized as a workaround. The discussion moves towards addressing the issue
  within the x86 backend where the problematic relocation logic resides.
primer_glossary:
- term: relocation
  definition: The process of updating symbolic references in relocatable object code
    to absolute symbols, typically done by the linker.
- term: non-allocated section
  definition: An object file section that is not intended to be loaded into memory
    at runtime (e.g., debug sections).
- term: SEC_ALLOC
  definition: A flag indicating that a section should be allocated memory when the
    program is loaded.
- term: GOT
  definition: Global Offset Table, a data structure used by position-independent code
    to indirectly access global variables and functions.
- term: PLT
  definition: Procedure Linkage Table, a table used in position-independent code to
    dynamically resolve function calls.
- term: PR ld/34444
  definition: A bug report filed against the GNU ld linker, identified by the number
    34444.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOqXoU7=Cx8MkN5NpZXfL8JVZOC9DQJu9Sn-LGGP5CAiHQ@mail.gmail.com
bugzilla_url: null
date: '2026-07-30'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the binutils linker where it would abort when attempting to relocate non-allocated code sections. The original fix proposed to issue an error, but was deemed insufficient. The discussion clarifies that the issue stems from the x86 backend's handling of such sections when using GOT or PLT, and the fix is being moved to the backend to properly manage these cases, resolving PR ld/34444.
