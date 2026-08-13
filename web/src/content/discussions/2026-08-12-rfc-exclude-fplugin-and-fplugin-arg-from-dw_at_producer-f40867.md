---
project: gcc
subsystem: rfc
patch_id: null
tags:
- gcc
- dwarf
- debugging
- reproducibility
discussion_id: CY5PR02MB899172AD2B298297BCE46F73E2DC2@CY5PR02MB8991.namprd02.prod.outlook.com
source_type: public_inbox
title: 'RFC: Should -fplugin and -fplugin-arg options be excluded from DW_AT_producer
  recording?'
headline: 'RFC: Exclude -fplugin and -fplugin-arg from DW_AT_producer'
tldr: Proposes excluding -fplugin and -fplugin-arg options from DW_AT_producer debug
  metadata to improve reproducibility.
proposer: Jaihind Yadav <jaihindy@qti.qualcomm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves reproducibility by removing host-specific paths from DW_AT_producer.
- Reduces the provenance information available in DW_AT_producer regarding plugin
  usage.
exchanges: []
primer_expert: This RFC addresses the recording of GCC command-line options in the
  DW_AT_producer DWARF attribute. Specifically, it targets the -fplugin and -fplugin-arg
  flags, which currently embed absolute paths to loaded plugins into the debug information.
  The proposal uses the `NoDWARFRecord` mechanism to exclude these options, aiming
  to enhance build reproducibility by removing host-specific path information from
  the generated object files.
primer_glossary:
- term: DW_AT_producer
  definition: A DWARF debugging information attribute that records information about
    the program and compilation environment that produced the debug information, often
    including compiler version and command-line options.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about compiled programs, enabling features like source-level debugging.
- term: Reproducibility
  definition: The ability to consistently obtain the same output (e.g., compiled binary,
    debug information) from the same source input and build environment.
- term: NoDWARFRecord
  definition: A GCC mechanism that flags compiler options to prevent them from being
    recorded in the DW_AT_producer DWARF attribute.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CY5PR02MB899172AD2B298297BCE46F73E2DC2@CY5PR02MB8991.namprd02.prod.outlook.com
bugzilla_url: null
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This RFC proposes excluding -fplugin and -fplugin-arg options from the DW_AT_producer debug metadata. Currently, these options can embed absolute, host-specific plugin paths into object files, harming reproducibility. The author suggests using the existing NoDWARFRecord mechanism to prevent this, as has been done for other path-containing options. The tradeoff is between improved reproducibility and slightly reduced debugging information provenance.
