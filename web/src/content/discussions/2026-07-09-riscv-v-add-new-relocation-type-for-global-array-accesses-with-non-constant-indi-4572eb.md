---
project: binutils
subsystem: riscv-v
patch_id: null
tags:
- RISC-V
- relocations
- linker
- patching
- ChangeLog
discussion_id: cd4a4dbd-af14-42ff-871a-25a3ec751d8a@suse.com
source_type: public_inbox
title: 'Re: [PATCH] RISCV-V: Add new relocation type for global array accesses with
  non-constant indices'
headline: 'RISCV-V: Add new relocation type for global array accesses with non-constant
  indices'
tldr: Comments on the patch submission regarding ChangeLog format and indentation.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Critiques the patch's submission method, noting that ChangeLog entries
    should be in the commit message, not a direct patch, and highlights inconsistent
    indentation (spaces vs. tabs).
  quote: 'Btw, as you can see from the adjacent date: ChangeLog files aren''t meant
    to be

    patched directly anymore. ChangeLog entries, if you want to have them, are now

    supposed to be part of the commit message.


    There also looks to be a problem with your mailing of patches: The entry in

    context really uses tab indentation (as it is supposed to be), yet throughout

    the entire patch there''s no single hard tab…'
primer_expert: 'This thread contains feedback on a RISC-V patch series that introduces
  new relocation types (`BFD_RELOC_RISCV_BASE_IDX_LO12_I`, `_S`, `_ADD`) to support
  global array accesses with non-constant indices. The feedback concerns meta-issues:
  the proper format for updating `ChangeLog` files (now part of commit messages) and
  correct use of tab characters for indentation within patches. The core functionality
  of the patch involves enhancing BFD''s relocation handling for RISC-V.'
primer_glossary:
- term: relocation type
  definition: A type of information embedded in an object file that tells the linker
    how to modify certain symbols or addresses when combining multiple object files
    into an executable or library. For RISC-V, specific types cater to its instruction
    set architecture.
- term: global array accesses
  definition: Accessing elements within an array that is allocated in the global or
    static storage duration of a program.
- term: non-constant indices
  definition: When an array element is accessed using an index that is not known at
    compile time, often determined at runtime.
- term: BFD
  definition: Binary File Descriptor, a library within GNU Binutils that provides
    a common interface for reading and writing various object file formats.
- term: ChangeLog
  definition: A file traditionally used to record changes made to a software project,
    often formatted as dated entries. In modern development, individual commit messages
    often serve this purpose.
- term: tab indentation
  definition: Using the tab character (\t) for aligning code or text, often preferred
    for consistency in certain coding standards.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/cd4a4dbd-af14-42ff-871a-25a3ec751d8a@suse.com
bugzilla_url: null
date: '2026-07-09'
is_stub: false
stub_reason: ''
---

Jan Beulich provides feedback on a patch adding new RISC-V relocation types, specifically addressing issues with the ChangeLog format and inconsistent indentation. He points out that ChangeLog entries should now be part of commit messages, not directly patched, and that the patch uses spaces where tabs should be used for indentation. The original patch introduced three new relocation types and updated ELF support for RISC-V to handle them.
