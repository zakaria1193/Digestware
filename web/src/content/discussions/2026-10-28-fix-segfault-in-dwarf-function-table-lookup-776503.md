---
project: binutils
subsystem: binutils
patch_id: null
tags:
- dwarf
- fuzzing
- crash
- bugfix
discussion_id: auJ2PxF59Bdag8fA@squeak.grove.modra.org
source_type: public_inbox
title: Fix lookup_address_in_function_table segfault
headline: Fix segfault in DWARF function table lookup
tldr: Fixes a segfault in DWARF processing when an unusual arange is encountered.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The `lookup_address_in_function_table` function in `bfd/dwarf2.c` searches
  for the best-matching function DIE for a given address within a DWARF compilation
  unit's address range list. The `best_fit_len` is initialized to a large value, and
  the first valid arange encountered sets `best_fit`. If an arange with `low=0` and
  `high=(bfd_vma)-1` is processed, `arange->high - arange->low` can equal the initial
  `best_fit_len`. If `best_fit` is still NULL at this point (meaning no previous match
  was found), the condition `arange->high - arange->low == best_fit_len` would be
  true, and the subsequent der…
primer_glossary:
- term: oss-fuzz
  definition: A free fuzzing service provided by Google that combines open-source
    fuzzing infrastructure with Google's infrastructure to help developers find bugs.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about source code variables, types, and code locations.
- term: arange
  definition: An Address Range Entry in DWARF debugging information, which defines
    a range of addresses associated with a particular compilation unit or function.
- term: compilation unit
  definition: A single source file that is compiled by the compiler. In DWARF, a compilation
    unit contains debugging information for that source file.
- term: DIE
  definition: Debug Information Entry. A structured record within DWARF data that
    describes a program entity like a function, variable, or type.
- term: NULL pointer dereference
  definition: An error that occurs when a program attempts to access memory through
    a pointer that has a NULL value.
- term: bfd_vma
  definition: Represents a virtual memory address within the BFD library, typically
    used to store addresses from object files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auJ2PxF59Bdag8fA@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This patch addresses a crash found by oss-fuzz in the DWARF debugging information processing. The fuzzer generated an unusual arange with `low=0` and `high=(bfd_vma)-1`, which resulted in `best_fit_len` being equal to the initial value. This condition, combined with `best_fit` being NULL, led to a NULL pointer dereference. The fix adds a check for `best_fit == NULL` to prevent this segfault.
