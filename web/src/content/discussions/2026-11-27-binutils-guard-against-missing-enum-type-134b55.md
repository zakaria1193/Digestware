---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- objdump
- dwarf
- bugfix
- security
discussion_id: awj1HajxQJns341u@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] binutils: guard against missing enum type'
headline: 'binutils: guard against missing enum type'
tldr: Fixes objdump crash on malformed DWARF input by adding NULL checks to DWARF
  processing functions.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: under_review
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds robustness to DWARF parsing by handling potentially malformed input gracefully.
- Removes assertions that might fail on valid, complex DWARF structures, potentially
  masking other issues but improving general stability.
- Slight modification to function signatures (`get_or_create_enum_constant`, `get_or_create_subrange_type`)
  to remove unused parameters.
exchanges:
- author: Alhuda Khan
  role: proposer
  position: Submitted a patch to fix a NULL-pointer dereference in `insert_element_in_list`
    when processing `DW_TAG_enumerator` in Binutils' DWARF handling, which could cause
    `objdump` to crash on malformed input.
  quote: null
- author: Alan Modra
  role: reviewer
  position: Agrees with the patch and expands it by adding a similar NULL check for
    `get_or_create_subrange_type` and removing potentially misleading assertions in
    `insert_element_in_list` to improve robustness against various DWARF structures.
  quote: 'Thanks.  There is another analogous case when calling

    get_or_create_subrange_type, so I''m going to fix that too.  Also, I

    believe there are other places where insert_element_in_list would

    assert.  For example, I see insert_element_in_list being called from

    read_and_display_attr_value case DW_FORM_string with both uvalue and

    svalue pointers NULL.  With fuzzed objects the tag might be

    DW_TAG_base_t…'
primer_expert: This discussion addresses a crash in `objdump` when parsing DWARF debug
  information. The issue arises from `insert_element_in_list` in `dwarf.c`, which
  incorrectly assumes `enum_type_list.tail` and `tab_type_list.tail` are non-NULL
  when creating new list elements. Malformed DWARF input, especially with `DW_TAG_enumerator`
  or `DW_TAG_subrange_type` DIEs, can lead to NULL pointer dereferences. Alan Modra's
  revision not only fixes the immediate bug with NULL checks but also removes assertions
  that could falsely trigger on valid, albeit complex, DWARF structures, making the
  DWARF parsing more res…
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about program variables, functions, and types.
- term: objdump
  definition: A command-line utility that displays information from object files,
    including disassembled code and DWARF debugging information.
- term: NULL-pointer dereference
  definition: An error that occurs when a program attempts to access memory through
    a pointer that does not point to a valid memory location (i.e., it is NULL).
- term: DW_TAG_enumerator
  definition: A DWARF tag representing an enumeration constant within an enumeration
    type.
- term: DW_TAG_subrange_type
  definition: A DWARF tag representing a range type, often used for array bounds.
- term: DIE
  definition: Debugging Information Entry. A fundamental structure in DWARF that describes
    a specific entity like a function, variable, or type.
- term: assertion
  definition: A statement in code that checks a condition believed to be true at that
    point; if false, the program typically terminates with an error, indicating a
    logic flaw.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/awj1HajxQJns341u@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This discussion concerns a NULL-pointer dereference vulnerability in GNU Binutils' DWARF parsing code, specifically within the `insert_element_in_list` function when processing `DW_TAG_enumerator`. Malformed DWARF data could trigger this, causing `objdump` to crash. The original patch introduced a NULL check for `enum_type_list.tail`. Reviewer Alan Modra expanded upon this, adding a similar check for `get_or_create_subrange_type` and removing assertions in `insert_element_in_list` that could fail with valid but complex DWARF structures.
