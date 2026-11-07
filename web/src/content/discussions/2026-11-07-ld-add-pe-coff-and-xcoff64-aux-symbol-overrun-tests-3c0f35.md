---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- binutils
- testing
- coff
- xcoff
discussion_id: CAOX--DR=vD-=ueXr-a=fLHMX59WqGZBtehGM++eUpb9K7DnORQ@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] ld: add PE/COFF and XCOFF64 aux symbol overrun tests'
headline: 'ld: add PE/COFF and XCOFF64 aux symbol overrun tests'
tldr: Follow-up on a patch adding tests for PE/COFF and XCOFF64 aux symbol overrun
  issues in the linker.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Seeks confirmation on a patch adding PE/COFF and XCOFF64 aux symbol overrun
    tests for the linker, referencing a previous commit.
  quote: 'It adds i386 PE/COFF (ld-pe/coff-aux.exp) and 64-bit AIX

    (xcoff64_aux_test) aux-symbol overrun tests for 335d76afde5. It still

    applies cleanly to master.'
primer_expert: This discussion is a follow-up to a patch that adds test cases to the
  GNU linker (`ld`) to verify its robustness against malformed auxiliary symbol entries
  in PE/COFF (Windows) and XCOFF64 (AIX) object files. The tests specifically target
  an overflow condition identified in commit 335d76afde5, which had previously only
  included tests for 32-bit XCOFF. The author is checking if the new tests are still
  relevant.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the standard file format
    for executables, object code, and DLLs used in 32-bit and 64-bit versions of Windows.
- term: XCOFF
  definition: Extended Common Object File Format, an object file format used on AIX
    systems. XCOFF64 refers to its 64-bit variant.
- term: aux symbol
  definition: Auxiliary symbol entries in an object file's symbol table, which provide
    additional information about a symbol, such as its storage class or type.
- term: overrun
  definition: A vulnerability or bug where a program writes data beyond the allocated
    buffer boundaries, potentially leading to memory corruption or crashes.
- term: linker
  definition: A program that combines various object files and libraries into a single
    executable file, resolving symbol references between them.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAOX--DR=vD-=ueXr-a=fLHMX59WqGZBtehGM++eUpb9K7DnORQ@mail.gmail.com
bugzilla_url: null
date: '2026-11-07'
is_stub: false
stub_reason: ''
---

Harshit Kumar is following up on a previous patch that added test cases for aux symbol overrun vulnerabilities in the linker's handling of PE/COFF and XCOFF64 formats. The tests cover specific scenarios related to malformed symbol table entries and ensure the linker handles these edge cases gracefully, preventing crashes or incorrect behavior. The author is seeking confirmation if the patch is still needed given existing tests.
