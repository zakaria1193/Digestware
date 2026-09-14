---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- pe
- mips
- cleanup
- dead code
discussion_id: 20260913123323.9734-3-jon.turney@dronecode.org.uk
source_type: public_inbox
title: '[PATCH 2/4] bfd: pe: Drop MIPS pdata table entry handling from pe_print_pdata'
headline: 'bfd: pe: Drop MIPS pdata table entry handling from pe_print_pdata'
tldr: Remove MIPS-specific .pdata handling code as MIPS PE support was dropped.
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying maintenance.
- Reduces complexity by eliminating architecture-specific logic for unsupported platforms.
exchanges: []
primer_expert: The `pe_print_pdata` function in `bfd/peXXigen.c` previously contained
  logic to handle PE MIPS `.pdata` structures, which differed from other architectures.
  Since binutils version 2.31, PE MIPS support has been removed. This patch eliminates
  the MIPS-specific code, including the `PDATA_FORMAT_MIPS32` define and associated
  print formatting, as it is no longer relevant.
primer_glossary:
- term: PE MIPS
  definition: Support for the MIPS architecture within the Portable Executable (PE)
    file format.
- term: binutils 2.31
  definition: A specific version of the GNU Binutils software collection, released
    around 2018, which removed support for PE MIPS.
- term: obsolete code
  definition: Code that is no longer necessary or functional due to changes in requirements,
    architecture, or software versions.
series_id: 'binutils:bfd: pe: drop mips pdata table entry handling from pe_print_pdata'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260913123323.9734-3-jon.turney@dronecode.org.uk
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This patch removes the MIPS-specific handling logic from the `pe_print_pdata` function in `bfd/peXXigen.c`. PE MIPS support was removed from binutils in version 2.31 (2018), making this code obsolete. The change cleans up the codebase by eliminating dead code related to a no-longer-supported architecture.
