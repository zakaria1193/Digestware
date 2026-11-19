---
project: binutils
subsystem: binutils
patch_id: null
tags:
- aix
- bfd
- warning
- xcoff
- debugging
discussion_id: DSWPR15MB31981702EA2DB661FA1B5FA90BD67A2@DSWPR15MB319817.namprd15.prod.outlook.com
source_type: public_inbox
title: 'Re:  [PATCH v1] Fix wrong auxtype for storage class warning in AIX.'
headline: 'AIX: Fix wrong auxtype for storage class warning'
tldr: Resolves a spurious warning in BFD when processing AIX 64-bit binaries with
  `_AUX_EXCEPT` aux types.
proposer: Aditya Kamath <Aditya.Kamath1@ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Fixes a spurious warning, improving user experience during debugging.
- Adds a specific check for `_AUX_EXCEPT`, which is not strictly necessary for BFD's
  operation but resolves the false positive.
exchanges:
- author: Aditya Kamath
  role: proposer
  position: Submits a patch to fix a warning related to `_AUX_EXCEPT` aux types in
    AIX 64-bit binaries.
  quote: 'The openXL compiled binary or library in AIX emits _AUX_EXCEPT (auxtype
    0xff)

    auxillary entry for C_EXT and C_HIDEXT symbols which are functions that have

    exception tables. BFD''s _bfd_xcoff64_swap_aux_in() only accepted _AUX_FCN for

    non-last aux entries and jumped to error: for anything else triggering the spurious

    warning. The fix detects _AUX_EXCEPT first and silently skips it with break,

    since…'
- author: amodra@gmail.com
  role: reviewer
  position: Receives the patch for review.
  quote: null
primer_expert: This patch targets `bfd/coff64-rs6000.c` and specifically the `_bfd_xcoff64_swap_aux_in`
  function, which parses auxiliary entries in AIX XCOFF64 object files. The issue
  arises when symbols have `_AUX_EXCEPT` aux entries (indicating exception tables),
  which are used by compilers like openXL. The current BFD logic only handles `_AUX_FCN`
  for non-last aux entries and errors out on others, leading to a spurious warning.
  The fix adds a specific check for `_AUX_EXCEPT` to silently skip it, as BFD does
  not need to process its contents.
primer_glossary:
- term: AIX
  definition: Advanced Interactive eXecutive, a proprietary Unix operating system
    developed by IBM.
- term: BFD
  definition: Binary File Descriptor library, a component of GNU Binutils that provides
    a common interface for reading and writing various executable file formats.
- term: auxtype
  definition: Auxiliary type, a field within an XCOFF (Extended Common Object File
    Format) symbol table entry that provides additional information about the symbol.
- term: storage class
  definition: A concept in some object file formats (like XCOFF) that describes the
    storage attributes of a symbol.
- term: XCOFF
  definition: Extended Common Object File Format, a file format used by IBM for AIX
    and other systems.
- term: _AUX_EXCEPT
  definition: A specific auxiliary type in XCOFF indicating that a symbol has an associated
    exception table.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/DSWPR15MB31981702EA2DB661FA1B5FA90BD67A2@DSWPR15MB319817.namprd15.prod.outlook.com
bugzilla_url: null
date: '2026-11-18'
is_stub: false
stub_reason: ''
---

This patch addresses a warning message in BFD related to AIX 64-bit binaries: 'warning: BFD: ...: wrong auxtype 0xff for storage class 0x6b'. This warning occurs because the `_bfd_xcoff64_swap_aux_in()` function in BFD incorrectly flags `_AUX_EXCEPT` aux entries as an error when they are encountered for non-last auxiliary entries. The fix modifies the function to recognize and silently skip `_AUX_EXCEPT` entries, as their payload is not needed by BFD, thus eliminating the spurious warning.
