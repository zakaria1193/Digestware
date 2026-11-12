---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- dwarf
- debugging
- weak symbols
discussion_id: CAKL4jwXZbEJMx9Sw_Mk4DQ0siuepwDW_pYEPmnX-Pnj211Gewg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] gas: Mark weak functions as external in DWARF'
headline: 'gas: Mark weak functions as external in DWARF'
tldr: Adds new test cases to verify that weak functions are correctly marked as external
  in DWARF debugging information.
proposer: Longjun Luo <luolongjuna@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the test suite to cover a specific edge case.
- Ensures more accurate debugging information for weak functions.
exchanges:
- author: Longjun Luo
  role: proposer
  position: Explains that new test cases are needed to specifically test the scenario
    where only a weak function is present, which is not covered by existing tests
    that include mixed global and local functions. The new tests verify that the DWARF
    emission correctly sets 'have_efunc' without 'have_lfunc' for weak functions.
  quote: 'The new tests contain only a weak function, verifying that out_debug_abbrev()
    sets have_efunc without setting have_lfunc. With have_efunc && !have_lfunc, the
    DWARF 3 case exercises the DWARF2_VERSION < 4 (DW_FORM_flag) path, while the DWARF
    5 case checks DW_FORM_flag_present.


    So the mixed tests cover the out_debug_info() hunk, and only the new ones fail
    without the out_debug_abbrev() hunk (DW_AT…'
- author: Jan Beulich
  role: reviewer
  position: Questions the necessity of new test cases, asking if the existing test
    cases already cover the functionality being tested by the new ones.
  quote: 'This part certainly is okay, but ...


    ... what does this new testcase test which ...


    ... this adjustment to the existing one doesn''t cover? (Same for the Dwarf5

    ones below then, obviously.)'
primer_expert: This patch addresses DWARF debugging information generation in the
  GNU Assembler (gas). Specifically, it concerns how weak symbols, which have different
  linkage characteristics than normal global or local symbols, are represented. The
  change ensures that the `DW_AT_external` attribute is correctly emitted for weak
  functions, which is crucial for debuggers to accurately represent symbol visibility
  and scope, especially in complex linking scenarios.
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about variables, functions, and types in compiled programs.
- term: Weak functions
  definition: Functions with special linkage properties that allow them to be overridden
    by other symbols of the same name. They are often used for optional features or
    optimizations.
- term: DW_AT_external
  definition: A DWARF attribute that indicates a symbol is external, meaning it is
    defined in another compilation unit or object file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKL4jwXZbEJMx9Sw_Mk4DQ0siuepwDW_pYEPmnX-Pnj211Gewg@mail.gmail.com
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This patch introduces new test cases for the GNU Assembler (gas) to ensure weak functions are properly marked as external in DWARF debugging information. The new tests specifically verify the behavior when only a weak function is present, distinguishing it from existing tests that cover mixed global and local functions. This ensures correct handling of DW_AT_external attribute generation for weak symbols.
