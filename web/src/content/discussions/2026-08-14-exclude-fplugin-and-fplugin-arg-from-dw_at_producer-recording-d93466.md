---
project: gcc
subsystem: gcc
patch_id: null
tags:
- dwarf
- debug info
- reproducibility
- compiler
- gcc
discussion_id: CAFiYyc03wuxRL=CuTr7jSNkMjWiqKaBLikdcjGfKzP2=nvQiCA@mail.gmail.com
source_type: public_inbox
title: 'Re: RFC: Should -fplugin and -fplugin-arg options be excluded from DW_AT_producer
  recording?'
headline: Exclude -fplugin and -fplugin-arg from DW_AT_producer recording
tldr: RFC to prevent absolute plugin paths and arguments from being embedded in DWARF
  debug info, improving build reproducibility.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improved build reproducibility vs. potentially losing detailed plugin invocation
  information in debug data.
exchanges:
- author: Jaihind Yadav
  role: proposer
  position: Noticed that absolute plugin paths are embedded in DW_AT_producer due
    to -fplugin and -fplugin-arg options, which harms reproducibility. Experimentally
    marked these options with NoDWARFRecord and observed no functional impact.
  quote: '-fplugin=<path> and -fplugin-arg-* options are currently recorded in

    DW_AT_producer when -grecord-gcc-switches is enabled.


    As a result, an absolute plugin path may become embedded in debug

    metadata.


    This introduces host-specific path information into the generated

    artifact and may negatively affect reproducibility.


    As an experiment, I modified:


    gcc/common.opt


    and marked:


    -fplugin=

    -fplugin-…'
- author: Richard Biener
  role: reviewer
  position: Acknowledged the proposal to exclude plugin options from DW_AT_producer
    recording, which aligns with existing mechanisms for handling reproducibility
    concerns.
  quote: 'The plugin is still loaded correctly, plugin arguments are still passed,

    and generated code/debug information remain unchanged. The only observed

    difference is that plugin-related command-line options are no longer

    recorded in DW_AT_producer.'
primer_expert: This RFC addresses the embedding of absolute paths for GCC plugins
  (specified via -fplugin and -fplugin-arg-*) into the DW_AT_producer DWARF attribute
  when -grecord-gcc-switches is active. The proposal leverages the existing NoDWARFRecord
  mechanism in gcc/common.opt to prevent these host-specific paths from being recorded,
  thereby enhancing the reproducibility of builds.
primer_glossary:
- term: DW_AT_producer
  definition: A DWARF debugging information attribute that stores a string identifying
    the toolchain that produced the compilation unit, including compiler version and
    command-line options.
- term: DWARF
  definition: A standardized debugging data format used by many compilers and debuggers,
    containing information about variables, types, and code structure.
- term: -grecord-gcc-switches
  definition: A GCC command-line option that instructs the compiler to record all
    command-line switches used for compilation in the DWARF debug information.
- term: NoDWARFRecord
  definition: A mechanism within GCC's option handling that specifies certain command-line
    options should not be recorded in the DW_AT_producer string.
- term: Reproducibility
  definition: The ability to reliably produce the exact same build output from the
    same source code and build environment, which is crucial for security auditing
    and debugging.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc03wuxRL=CuTr7jSNkMjWiqKaBLikdcjGfKzP2=nvQiCA@mail.gmail.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This RFC proposes excluding GCC plugin-related options (-fplugin=<path> and -fplugin-arg-*) from being recorded in the DW_AT_producer DWARF attribute when -grecord-gcc-switches is enabled. The current behavior embeds absolute host-specific paths, which negatively impacts build reproducibility. The patch modifies gcc/common.opt to mark these options with NoDWARFRecord, addressing the issue without affecting plugin functionality.
