---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- addr2line
- dwarf
- debugging
discussion_id: 20e3fd7b-03ea-4f82-b716-a70458d36064@suse.com
source_type: public_inbox
title: 'Re: [PATCH] bfd: Fix addr2line for skipped DW_FORM_ref_addr CUs and DWARF5
  one-file line tables'
headline: 'bfd: Fix addr2line for skipped DW_FORM_ref_addr CUs and DWARF5 one-file
  line tables'
tldr: Jan Beulich provides feedback on a patch that fixes addr2line's handling of
  DWARF debugging information, suggesting minor improvements.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improved accuracy of `addr2line` in mapping addresses to source locations vs. potential
  complexity introduced in CU parsing logic.
- Correct handling of DWARF5 line tables vs. ensuring compatibility with existing
  DWARF versions.
- Test case robustness (output inclusion, documentation) vs. developer time.
exchanges:
- author: Kumar N, Bhuvanendra
  role: proposer
  position: Submitted a patch to fix `addr2line` issues with DWARF debugging information,
    specifically concerning `DW_FORM_ref_addr` and DWARF5 line tables.
  quote: 'For clang compiled objects, addr2line can miss a later compilation unit

    when an earlier CU is scanned and DW_FORM_ref_addr causes stash_comp_unit

    to parse ahead.  Those units never go through the sequential reader.

    Queue them on unsearched_units and search only that small set.


    Separately, PR 30783 starts the DWARF5 line state machine at file

    index 1.  A table that contains only file 0 then repor…'
- author: Jan Beulich
  role: reviewer
  position: Acknowledges the patch as acceptable but suggests two minor improvements
    regarding test output and documentation.
  quote: 'Okay, albeit I think I''ll ...


    - discard-pie.d doesn''t seem to include the expected output. So it would not
    turn into an XPASS automatically in case the problem goes away, right?

    - Should we, in discard-shared.d, document that the outcome is not what we want
    but rather what it is today?'
primer_expert: This patch addresses issues in the `addr2line` utility within the Binutils
  BFD library, specifically concerning the parsing of DWARF debugging information.
  The primary fix involves handling compilation units (CUs) referenced by `DW_FORM_ref_addr`
  and `DW_FORM_GNU_ref_alt` by queuing them for later processing, thus preventing
  `addr2line` from missing them. A secondary fix corrects the DWARF5 line table state
  machine initialization, ensuring correct file indexing when only file 0 is present.
  Review feedback suggests minor improvements to test case output and documentation.
primer_glossary:
- term: addr2line
  definition: A command-line utility that translates addresses into symbolic debugging
    information (filenames, function names, line numbers). It's part of the GNU Binutils.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU Binutils to provide
    a common interface for reading and writing various executable file formats (like
    ELF, COFF, a.out).
- term: DWARF
  definition: A debugging data format used by many compilers (like GCC and Clang)
    to store symbolic debugging information in executable files. This information
    allows debuggers and tools like `addr2line` to map addresses back to source code
    elements.
- term: CU
  definition: Compilation Unit. In DWARF, a CU represents a single source file that
    was compiled. It contains debugging information specific to that file.
- term: DW_FORM_ref_addr
  definition: A DWARF attribute form indicating that the attribute value is a reference
    to an address, typically another debugging information entry within the same or
    a different CU.
- term: DWARF5 line tables
  definition: A part of the DWARF debugging information format that maps addresses
    in the compiled code back to source file names and line numbers. DWARF5 is a specific
    version of this standard.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20e3fd7b-03ea-4f82-b716-a70458d36064@suse.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

Jan Beulich reviews a patch intended to fix issues in `addr2line` related to DWARF debugging information, specifically handling `DW_FORM_ref_addr` in compilation units (CUs) and DWARF5 line tables. Beulich's feedback includes two minor suggestions: to ensure the `discard-pie.d` test includes expected output for automated pass/fail detection, and to document the current behavior (rather than desired behavior) in `discard-shared.d`. The patch aims to resolve problems where `addr2line` might miss CUs or misinterpret line tables.
