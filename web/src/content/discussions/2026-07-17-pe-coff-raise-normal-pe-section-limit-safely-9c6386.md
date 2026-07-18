---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- binutils
- PE/COFF
- sections
- Windows
- portability
discussion_id: 71e08b2d-715a-4cb4-941e-7e548c4b264c@suse.com
source_type: public_inbox
title: 'Re: [PATCH v4] PE/COFF: raise normal PE section limit safely'
headline: 'PE/COFF: raise normal PE section limit safely'
tldr: Patch to safely increase the maximum number of sections in PE/COFF files from
  32767 to 65279 is reviewed positively.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increasing the section limit improves compatibility with modern compilers but requires
  careful handling of signed/unsigned conversions to avoid breaking existing reserved
  values.
- The change benefits users creating very large executables or libraries with many
  sections.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Submits a patch to increase the PE/COFF section limit by correctly handling
    unsigned 16-bit section numbers.
  quote: 'PE/COFF stores symbol section numbers in a 16-bit field.  Binutils used

    signed 16-bit handling there, which limited normal PE objects to 32767

    sections even though MSVC and Clang already accept a larger unsigned

    range. ... Raise the normal PE section limit to 65279 ...'
- author: Alan Modra
  role: reviewer
  position: Approves the patch, stating 'This looks OK to me.'
  quote: This looks OK to me.
- author: Jan Beulich
  role: reviewer
  position: Concurs with Alan Modra's assessment and indicates the patch will be committed
    soon.
  quote: Same here. I'll get this committed soon-ish.
primer_expert: This patch addresses a limitation in `binutils`' handling of PE/COFF
  section counts. The COFF symbol table uses a 16-bit field for section numbers. Historically,
  `binutils` interpreted this as a signed integer, effectively limiting the maximum
  number of sections to 32,767. However, modern compilers like MSVC and Clang correctly
  use this field as an unsigned integer, supporting up to 65,279 sections. The patch
  modifies `bfd/coffcode.h` and `peXXigen.c` to correctly decode and encode section
  numbers as unsigned values within the valid range, while ensuring that reserved
  section numbers (undefin…
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, the file format used
    for executables, object code, DLLs, and system files on Windows operating systems.
- term: section
  definition: A logical division within an executable or object file, containing related
    data such as code, initialized data, or uninitialized data.
- term: symbol section number
  definition: A field in a PE/COFF symbol table entry that indicates which section
    the symbol belongs to.
- term: MSVC
  definition: Microsoft Visual C++, Microsoft's integrated development environment
    (IDE) for C and C++ programming languages.
- term: Clang
  definition: A C, C++, Objective-C, and Objective-C++ frontend for the LLVM compiler
    infrastructure.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: objdump
  definition: A standard Unix utility that displays information from object files,
    including symbols, sections, and disassembly.
- term: bfd
  definition: The Binary File Descriptor library, a GNU library that provides a common
    interface to various object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/71e08b2d-715a-4cb4-941e-7e548c4b264c@suse.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This discussion confirms a positive review for a patch that safely increases the maximum number of sections allowed in normal PE/COFF files. The current limit of 32,767 sections is due to binutils using a signed 16-bit integer for symbol section numbers, whereas compilers like MSVC and Clang support a larger unsigned range up to 65,279. The patch modifies `binutils` to correctly handle this larger unsigned range for normal PE symbol section numbers while preserving reserved values for special symbols. A new gas test case is also added to verify this functionality.
