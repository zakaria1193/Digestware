---
project: binutils
subsystem: elf
patch_id: null
tags:
- binutils
- elf
- linker
- relocations
- bugfix
discussion_id: CAMe9rOpWmbqdUHmBWUbUROcNvMY8YJOUUf7CGoBU=AWysx596Q@mail.gmail.com
source_type: public_inbox
title: '[PATCH] elf: Set this_idx to -1 for invalid relocations'
headline: 'elf: Set this_idx to -1 for invalid relocations'
tldr: Fixes redundant error reporting for invalid relocation symbol indices in the
  ELF linker.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 5
technical_tradeoffs:
- Correcting the error reporting mechanism to avoid redundant messages.
- Ensuring that invalid relocation data does not lead to misinterpretation or repeated
  errors.
- Maintaining the linker's ability to halt on fatal errors.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Submits a patch to prevent redundant error reporting of invalid relocation
    symbol indices by setting `this_idx` to -1 and returning `false` on error.
  quote: 'When invalid relocation is reported by elf_link_read_relocs_from_section

    called from lang_gc_sections:


    ld: pr34448-bug_18.o: bad reloc symbol index (0xf2000005 >= 0x13) for

    offset 0x4 in section `.text.get_tls[get_tls]''


    the same error is reported again:


    ld: pr34448-bug_18.o: bad reloc symbol index (0xf2000005 >= 0x13) for

    offset 0x4 in section `.text.get_tls[get_tls]''


    from lang_check_relocs s…'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Withdraws the previous patch and announces an intention to post a different
    fix for the same issue.
  quote: I withdrew this patch.  I will post a different fix.
primer_expert: This patch addresses a bug in the ELF linker (ld) where an invalid
  relocation symbol index, detected during garbage collection of sections, triggers
  a fatal error message. The error is then reported again because `lang_gc_sections`
  doesn't halt the linker. The fix involves modifying `elf_link_read_relocs_from_section`
  to signal an invalid index by setting `this_idx` to -1, which will prevent the subsequent
  redundant error report.
primer_glossary:
- term: relocation
  definition: Information in an object file that describes how to modify parts of
    the code or data when linking, such as resolving symbol addresses.
- term: symbol index
  definition: An identifier or pointer within the symbol table of an object file,
    used to refer to a specific symbol (e.g., a function or variable).
- term: garbage collection (GC) of sections
  definition: A linker process that identifies and removes unused sections from an
    executable to reduce its size.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOpWmbqdUHmBWUbUROcNvMY8YJOUUf7CGoBU=AWysx596Q@mail.gmail.com
bugzilla_url: null
date: '2026-08-01'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the binutils ELF linker where invalid relocation symbol indices cause the linker to report the same error twice. The fix modifies `elf_link_read_relocs_from_section` to set `this_idx` to -1 for invalid relocations and return `false` if `this_idx` is negative, preventing subsequent erroneous checks.
