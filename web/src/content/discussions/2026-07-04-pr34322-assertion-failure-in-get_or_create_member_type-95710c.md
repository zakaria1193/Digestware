---
project: binutils
subsystem: pr34322
patch_id: null
tags:
- binutils
- dwarf
- debugging
- bugfix
discussion_id: akjmq8Rm_OBgmsq3@squeak.grove.modra.org
source_type: public_inbox
title: 'pr34322: assertion failure in get_or_create_member_type'
headline: 'pr34322: assertion failure in get_or_create_member_type'
tldr: Fixes a bug in binutils' DWARF processing that caused an assertion failure when
  encountering DW_TAG_member without a proper struct/union parent.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Silently ignoring malformed DWARF entries instead of warning or erroring out simplifies
  parsing but might hide deeper issues in toolchains generating the DWARF data.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to fix PR 34322 by adjusting DWARF parsing to handle missing
    parent types for DW_TAG_member.
  quote: "I thought about warning \"DW_TAG_member without struct/union parent\"\n\
    here but decided that doesn't help much as the warning is disconnected\nfrom output.\
    \  As it is the --map-global-vars code silently ignores\nunexpected attributes\
    \ that might be found in fuzzed files.  I'm fine\nwith that too.\n\n\tPR 34322\n\
    \t* dwarf.c (get_or_create_member_type): Return NULL on NULL parent.\n\t(insert_element_in_list):\
    \ Ign…"
primer_expert: This patch for binutils addresses a bug in the DWARF debugging information
  parser related to processing `DW_TAG_member` entries. It corrects an assertion failure
  in `get_or_create_member_type` by handling cases where a `member_parent` is NULL,
  and modifies `insert_element_in_list` to gracefully ignore `DW_TAG_member` DIEs
  that lack a proper struct or union parent. This improves robustness when parsing
  DWARF data from potentially malformed object files, particularly for targets like
  avr.
primer_glossary:
- term: DWARF
  definition: A standardized debugging data format used by compilers and debuggers
    to represent information about variables, types, functions, and source code locations
    within an executable.
- term: PR 34322
  definition: A specific bug report number within the binutils project's issue tracking
    system.
- term: DW_TAG_member
  definition: A DWARF tag indicating a member of a structure or union.
- term: DIE
  definition: Debug Information Entry. A fundamental unit within DWARF data, representing
    a symbol or type.
- term: struct/union parent
  definition: In DWARF, a `DW_TAG_member` DIE is typically a child of a `DW_TAG_structure_type`
    or `DW_TAG_union_type` DIE, establishing the context of the member.
- term: --map-global-vars
  definition: A binutils option likely related to mapping global variables, potentially
    interacting with DWARF information.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akjmq8Rm_OBgmsq3@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-04'
is_stub: false
stub_reason: ''
---

This patch addresses PR 34322 by modifying binutils' DWARF parsing logic. Specifically, it changes `get_or_create_member_type` to return NULL if the parent is NULL, and `insert_element_in_list` to ignore DW_TAG_member entries that lack a struct or union parent. This prevents an assertion failure and ensures malformed DWARF information is handled more gracefully.
