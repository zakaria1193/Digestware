---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- debugger
- DWARF
- LTO
- clang
discussion_id: CY8PR12MB734051E88B8DF63612A2EA8F87692@CY8PR12MB7340.namprd12.prod.outlook.com
source_type: public_inbox
title: '[PATCH] bfd: Fix addr2line for skipped DW_FORM_ref_addr CUs and DWARF5 one-file
  line tables'
headline: 'bfd: Fix addr2line for skipped DW_FORM_ref_addr CUs and DWARF5 one-file
  line tables'
tldr: Patch fixes addr2line to correctly handle DWARF debugging information from clang
  LTO objects and DWARF5 line tables.
proposer: '"Kumar N, Bhuvanendra" <Bhuvanendra.KumarN@amd.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves debugging accuracy for specific compiler and DWARF versions at the cost
  of slightly increased complexity in the addr2line code.
exchanges:
- author: Kumar N, Bhuvanendra <Bhuvanendra.KumarN@amd.com>
  role: proposer
  position: Submits a patch to addr2line to fix issues with DWARF debugging information
    from clang LTO objects and DWARF5 line tables.
  quote: null
primer_expert: The `addr2line` utility in binutils is failing to correctly map addresses
  to source code lines for certain DWARF debugging information. The first issue involves
  compilation units (CUs) in clang LTO (Link Time Optimization) objects where `DW_FORM_ref_addr`
  entries cause `stash_comp_unit` to parse ahead. This can lead to subsequent CUs
  being skipped by the sequential reader. The fix queues these skipped CUs in `unsearched_units`
  for later processing. The second issue relates to DWARF5 one-file line tables where
  the line number state machine incorrectly starts at file index 1, causing a 'bad
  fil…
primer_glossary:
- term: addr2line
  definition: A command-line utility that translates object code addresses into line
    number and function name information.
- term: bfd
  definition: The Binary File Descriptor library, used by binutils to handle various
    object file formats.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to represent
    information about source code, variables, and types.
- term: DW_FORM_ref_addr
  definition: A DWARF attribute form indicating a reference to a debugging information
    entry using an address.
- term: CU
  definition: Compilation Unit. A single translation unit (source file) compiled into
    an object file, described by a distinct DWARF debugging information entry.
- term: LTO
  definition: Link Time Optimization. A compiler optimization technique where optimization
    is performed across multiple translation units during the linking phase.
- term: DWARF5
  definition: The fifth version of the DWARF debugging data format specification.
- term: line tables
  definition: A part of DWARF debugging information that maps addresses within the
    executable code back to source file names and line numbers.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CY8PR12MB734051E88B8DF63612A2EA8F87692@CY8PR12MB7340.namprd12.prod.outlook.com
bugzilla_url: null
date: '2026-11-03'
is_stub: false
stub_reason: ''
---

This patch addresses two issues in binutils' addr2line tool when processing DWARF debugging information. First, it fixes an issue where addr2line might miss compilation units in clang LTO objects due to `DW_FORM_ref_addr` causing premature parsing. The fix queues these units for later searching. Second, it corrects handling of DWARF5 one-file line tables, ensuring correct file index reporting when the table only contains file 0. The proposed changes improve accuracy for clang LTO and DWARF5 outputs.
