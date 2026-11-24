---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- dwarf
- debugging
- crash
- vulnerability
discussion_id: loopr.30.udztyxirhgnm@research.digiscrypt.com
source_type: public_inbox
title: '[PATCH] binutils: guard against missing enum type'
headline: 'binutils: guard against missing enum type'
tldr: Patch guards against NULL pointer dereference in DWARF enumerator handling by
  checking if `enum_type_list.tail` is NULL before use.
proposer: Alhuda Khan <alhuda@research.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alhuda Khan <alhuda@research.digiscrypt.com>
  role: proposer
  position: Submits a patch to add a NULL check for `enum_type_list.tail` in the DWARF
    enumerator handling code to prevent a crash.
  quote: 'The code accesses enum_type_list.tail without checking whether it is NULL
    before passing it to get_or_create_enum_constant().


    Malformed DWARF input can trigger this condition and cause objdump to crash.


    The patch adds a NULL check before the function call, preventing the invalid access.'
primer_expert: This patch for binutils/dwarf.c fixes a NULL pointer dereference in
  `insert_element_in_list` when processing `DW_TAG_enumerator` DIEs. The code attempts
  to use `enum_type_list.tail` (a pointer to the tail of a linked list of enum types)
  in `get_or_create_enum_constant` without first checking if the list is empty (i.e.,
  if `tail` is NULL). A malformed DWARF input can create this scenario, leading to
  a crash in `objdump`. The fix adds a simple `if (enum_type_list.tail == NULL) break;`.
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many Unix and Unix-like systems to support
    debuggers and other tools.
- term: enumerator
  definition: In programming, an enumerator defines a set of named integer constants.
    In DWARF, `DW_TAG_enumerator` represents such constants.
- term: NULL pointer dereference
  definition: An error that occurs when a program attempts to access memory using
    a pointer that points to no valid object (a NULL pointer), often leading to a
    crash.
- term: objdump
  definition: A utility program that displays information from object files, including
    symbols and disassembled code. Part of GNU Binutils.
- term: DIE
  definition: Debugging Information Entry; a structure within DWARF data that describes
    a program entity like a variable, type, or function.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/loopr.30.udztyxirhgnm@research.digiscrypt.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

This patch addresses a NULL pointer dereference in GNU Binutils' DWARF handling code, specifically within the `insert_element_in_list` function when processing `DW_TAG_enumerator`. The issue occurs because `enum_type_list.tail` is accessed without a preceding NULL check. Malformed DWARF input can trigger this, causing `objdump` to crash. The fix adds a NULL check to prevent this invalid access, with test suite results indicating successful patching.
