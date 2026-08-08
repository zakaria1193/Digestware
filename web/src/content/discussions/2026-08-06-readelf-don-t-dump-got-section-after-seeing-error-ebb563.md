---
project: binutils
subsystem: readelf
patch_id: null
tags:
- binutils
- readelf
- error handling
- GOT
- ELF
discussion_id: a3a94cf9-2c06-49cd-8ab8-7a76a8c706e0@suse.com
source_type: public_inbox
title: 'Re: [PATCH] readelf: Don''t dump GOT section after seeing error'
headline: 'readelf: Don''t dump GOT section after seeing error'
tldr: Suggestion to generalize readelf error handling beyond just the GOT section.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves robustness by preventing `readelf` from producing potentially misleading
  output after encountering errors.
- Generalizing the error handling could increase code complexity but enhance overall
  stability across various object file formats.
exchanges:
- author: H. J. Lu
  role: proposer
  position: Submits a patch to prevent `readelf` from dumping the GOT section after
    encountering errors, citing PR binutils/34473.
  quote: 'Don''t dump GOT section contents after seeing errors in input:


    readelf: Error: Section 10 has invalid sh_entsize of 0

    readelf: Error: (Using the expected size of 18 for the rest of this dump)

    readelf: Error: Too many program headers - 0x3030 - the file is not that big


    PR binutils/34473

    * elfcomm.c (seen_error): New.

    (seen_elf_error): Likewise.

    (clear_elf_error): Likewise.

    (error): Set seen_error…'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Approves the patch for `readelf` but suggests generalizing the error-handling
    approach to other parts of the tool.
  quote: Okay. And this model may want widening to elsewhere, not limited to readelf.
primer_expert: A patch for `readelf` prevents the Global Offset Table (GOT) section
  from being dumped if other errors are encountered during parsing. Reviewer Jan Beulich
  agrees with the change but proposes extending this safer error-handling strategy
  to other parts of `readelf` to improve its robustness when dealing with malformed
  object files.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files, commonly used for inspecting object files and executables.
- term: GOT
  definition: Global Offset Table. A table used in position-independent code (PIC)
    to store addresses of global symbols, allowing them to be resolved at runtime.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: PR binutils/34473
  definition: A specific bug report (Problem Report) filed against the binutils project,
    identified by number 34473.
- term: patch
  definition: A piece of code that modifies existing software to fix bugs, add features,
    or improve performance.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/a3a94cf9-2c06-49cd-8ab8-7a76a8c706e0@suse.com
bugzilla_url: null
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

Jan Beulich reviews a patch for `readelf` that prevents dumping the GOT section after errors occur, acknowledging its usefulness for the specific case. He suggests that this error-handling model might be beneficial to generalize and apply to other sections or contexts within `readelf` as well, improving overall robustness.
