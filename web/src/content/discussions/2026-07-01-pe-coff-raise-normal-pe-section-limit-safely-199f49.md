---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- binutils
- PE/COFF
- linker
- sections
- Windows
discussion_id: c30158ee-1917-47e9-b4e4-b7755f42a9ec@suse.com
source_type: public_inbox
title: 'Re: [PATCH] PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Discusses a patch to increase the PE section limit from 32767 to 65279 by using
  unsigned 16-bit integers.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increases the maximum number of sections supported in PE/COFF files, aligning with
  modern compiler capabilities.
- Ensures compatibility by preserving special section number values while adopting
  unsigned interpretation for normal sections.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Raises a concern about the implementation details of the `pe_decode_sym_section_number`
    function regarding unsigned integer handling.
  quote: null
primer_expert: This discussion centers on a binutils patch that modifies how PE/COFF
  symbol section numbers are handled. The PE/COFF format uses a 16-bit field for section
  numbers, and previously, binutils treated this as a signed integer, limiting objects
  to 32,767 sections. Modern compilers like MSVC and Clang support up to 65,279 sections
  using unsigned 16-bit integers. The patch, proposed by Oleg Tolmatcev and reviewed
  by Jan Beulich, updates binutils to correctly decode and encode these section numbers
  as unsigned values, thereby raising the supported limit. Beulich's review focuses
  on the specifics of…
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the file format used
    for executables, object code, and DLLs on 32-bit and 64-bit versions of Windows.
- term: section number
  definition: An identifier within a PE/COFF symbol table that indicates which section
    of the executable or object file the symbol belongs to.
- term: symbol table
  definition: A data structure within an object file that lists all symbols (e.g.,
    function names, variable names) and their corresponding addresses or properties.
- term: MSVC
  definition: Microsoft Visual C++, a suite of tools for software development, including
    a compiler and debugger, for Windows.
- term: Clang
  definition: A compiler front-end for C, C++, Objective-C, and Objective-C++ that
    interfaces with the LLVM optimizer and code generator.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c30158ee-1917-47e9-b4e4-b7755f42a9ec@suse.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

Jan Beulich expresses minor concerns about a patch that aims to increase the maximum number of sections in PE/COFF files from 32767 to 65279. The original patch by Oleg Tolmatcev uses unsigned 16-bit integers for section numbers, which aligns with MSVC and Clang capabilities and preserves special section identifiers. Beulich's specific concern relates to the implementation details of `pe_decode_sym_section_number` and how it handles the unsigned conversion.
